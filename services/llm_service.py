"""
LLM Service - Azure OpenAI Integration
Handles query classification and function/tool calling for inventory queries
"""

import json
from typing import Optional, Dict, Any
from openai import AzureOpenAI
import config


class LLMService:
    """Service for handling Azure OpenAI LLM interactions with classification and function calling"""
    
    def __init__(self):
        """Initialize the LLM Service with Azure OpenAI client"""
        if not config.AZURE_OPENAI_ENDPOINT:
            raise ValueError("AZURE_OPENAI_ENDPOINT environment variable not set")
        if not config.AZURE_OPENAI_KEY:
            raise ValueError("AZURE_OPENAI_KEY environment variable not set")
        
        self.client = AzureOpenAI(
            azure_endpoint=config.AZURE_OPENAI_ENDPOINT,
            api_key=config.AZURE_OPENAI_KEY,
            api_version=config.AZURE_API_VERSION
        )
        self.model = config.AZURE_DEPLOYMENT_NAME
        
        # Define the inventory tool/function schema
        self.tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_inventory",
                    "description": "Query the product inventory database for stock levels or pricing information. Use this for questions about product availability, stock counts, sizes, or prices.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "item_name": {
                                "type": "string",
                                "description": "The name of the product (e.g., 'Waterproof Commuter Jacket', 'Tech-Knit Hoodie', 'Dry-Fit Running Tee')"
                            },
                            "size": {
                                "type": "string",
                                "description": "The size of the product (e.g., 'S', 'M', 'L', 'XL'). Optional.",
                                "enum": ["S", "M", "L", "XL"]
                            },
                            "intent": {
                                "type": "string",
                                "description": "The intent of the query: 'stock' for availability/stock count, 'price' for pricing information",
                                "enum": ["stock", "price"]
                            }
                        },
                        "required": ["item_name"]
                    }
                }
            }
        ]
    
    def classify_query(self, query: str) -> str:
        """
        Classify user query into one of three categories:
        - company_info: Questions about TechGear UK company details
        - inventory: Questions about product stock, availability, or prices
        - unknown: Everything else
        
        Args:
            query: User's question
        
        Returns:
            Classification string: 'company_info', 'inventory', or 'unknown'
        """
        try:
            # System prompt for high-level query classification
            system_prompt = """You are a query classifier for TechGear UK, a clothing retailer.
Classify each user query into EXACTLY ONE category:

1. "company_info" - Questions about:
   - Company name, identity, or what TechGear UK is
   - Location, address, where they are located
   - Office hours, opening times, when they're open
   - Contact details, phone, email
   - Delivery policy, shipping information
   - Return policy, refunds
   - General company information

2. "inventory" - Questions about:
   - Product availability, stock levels
   - Specific items (jackets, hoodies, tees)
   - Product sizes (S, M, L, XL)
   - Product prices
   - "Do you have...", "Is X available...", "How many..."

3. "unknown" - Everything else:
   - General knowledge questions
   - Unrelated topics
   - Requests outside company/inventory scope

Respond with ONLY ONE WORD: company_info, inventory, or unknown"""

            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ]
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0,
                max_tokens=10
            )
            
            classification = response.choices[0].message.content.strip().lower()
            
            # Validate classification
            if classification in ['company_info', 'inventory', 'unknown']:
                return classification
            
            # Default to unknown if invalid response
            return 'unknown'
        
        except Exception as e:
            print(f"LLM Classification Error: {e}")
            return 'unknown'
    
    def should_use_inventory(self, query: str) -> Optional[Dict[str, Any]]:
        """
        Determine if query requires inventory lookup and extract parameters
        
        Args:
            query: User's question
        
        Returns:
            Dictionary with function call details if inventory lookup needed, None otherwise
        """
        try:
            # Create messages for the LLM
            messages = [
                {
                    "role": "system",
                    "content": "You are a helpful assistant for TechGear UK, a clothing retailer. "
                               "Use the get_inventory function to answer questions about product availability, "
                               "stock levels, sizes, and prices. Only use the function for inventory-related queries."
                },
                {
                    "role": "user",
                    "content": query
                }
            ]
            
            # Call OpenAI with function calling
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=self.tools,
                tool_choice="auto"
            )
            
            # Check if the model wants to call a function
            message = response.choices[0].message
            
            if message.tool_calls:
                tool_call = message.tool_calls[0]
                function_name = tool_call.function.name
                
                if function_name == "get_inventory":
                    # Parse function arguments
                    function_args = json.loads(tool_call.function.arguments)
                    return {
                        "function": function_name,
                        "arguments": function_args
                    }
            
            return None
        
        except Exception as e:
            print(f"LLM Service Error: {e}")
            return None
