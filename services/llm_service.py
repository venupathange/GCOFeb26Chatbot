"""
LLM Service - Azure OpenAI Integration
Handles function/tool calling for inventory queries
"""

import json
from typing import Optional, Dict, Any
from openai import AzureOpenAI
import config


class LLMService:
    """Service for handling Azure OpenAI LLM interactions with function calling"""
    
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
