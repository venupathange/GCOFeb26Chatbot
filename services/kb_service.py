"""
Knowledge Base Service - Tier 1 (Enhanced with Semantic Matching)
Handles company information queries using structured metadata and intelligent matching
"""

from typing import Optional, Dict, Any
from openai import AzureOpenAI
import config


class KnowledgeBaseService:
    """Service for handling knowledge base queries with semantic understanding"""
    
    def __init__(self):
        """Initialize the Knowledge Base Service with structured company data"""
        
        # Structured company metadata
        self.company_data = {
            "company_name": "TechGear UK",
            "location": "124 High Street, London, EC1A 1BB",
            "office_hours": "Monday to Friday, 09:00 - 18:00. Saturday, 10:00 - 16:00.",
            "delivery_policy": "Standard delivery takes 3-5 working days. Next-day delivery is available for £5.99.",
            "returns": "Items can be returned within 30 days of purchase with a valid receipt.",
            "contact": "Support can be reached at support@techgear.co.uk or 020 7946 0000."
        }
        
        # Initialize Azure OpenAI client for semantic classification
        if config.AZURE_OPENAI_ENDPOINT and config.AZURE_OPENAI_KEY:
            self.client = AzureOpenAI(
                azure_endpoint=config.AZURE_OPENAI_ENDPOINT,
                api_key=config.AZURE_OPENAI_KEY,
                api_version=config.AZURE_API_VERSION
            )
            self.model = config.AZURE_DEPLOYMENT_NAME
        else:
            self.client = None
            self.model = None
    
    def _classify_company_query(self, query: str) -> Optional[str]:
        """
        Use LLM to classify what type of company information is being requested
        
        Args:
            query: User's question
        
        Returns:
            Classification: 'company_name', 'location', 'office_hours', 'delivery_policy', 
                           'returns', 'contact', 'general_info', or None
        """
        if not self.client:
            return None
        
        try:
            # System prompt for classification
            system_prompt = """You are a query classifier for TechGear UK company information.
Classify the user query into ONE of these categories:
- company_name: asking about company name, what is the company, company identity
- location: asking about address, location, where located, where are you
- office_hours: asking about opening hours, timings, when open, office hours
- delivery_policy: asking about delivery, shipping, how long delivery takes
- returns: asking about return policy, refunds, returning items
- contact: asking about contact details, phone, email, how to reach
- general_info: broad questions like "about the company", "company data", "tell me about techgear"
- not_company: not asking about company information

Respond with ONLY the category name, nothing else."""

            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ]
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0,
                max_tokens=20
            )
            
            classification = response.choices[0].message.content.strip().lower()
            
            # Return classification if it's a valid company info type
            if classification in ['company_name', 'location', 'office_hours', 'delivery_policy', 
                                 'returns', 'contact', 'general_info']:
                return classification
            
            return None
        
        except Exception as e:
            print(f"KB Classification Error: {e}")
            return None
    
    def _generate_company_response(self, classification: str, query: str) -> str:
        """
        Generate appropriate company information response based on classification
        
        Args:
            classification: Type of information requested
            query: Original user query
        
        Returns:
            Formatted response string
        """
        # Direct field responses
        if classification == "company_name":
            return self.company_data["company_name"]
        
        elif classification == "location":
            return self.company_data["location"]
        
        elif classification == "office_hours":
            return self.company_data["office_hours"]
        
        elif classification == "delivery_policy":
            return self.company_data["delivery_policy"]
        
        elif classification == "returns":
            return self.company_data["returns"]
        
        elif classification == "contact":
            return self.company_data["contact"]
        
        elif classification == "general_info":
            # Generate comprehensive company summary for broad queries
            return (
                f"{self.company_data['company_name']} is located at {self.company_data['location']}. "
                f"We are open {self.company_data['office_hours']} "
                f"For support, contact {self.company_data['contact'].replace('Support can be reached at ', '')}"
            )
        
        return None
    
    def search(self, query: str) -> Optional[str]:
        """
        Search for company information using semantic classification
        
        Args:
            query: User's question
        
        Returns:
            Answer string if company info found, None otherwise
        """
        # Step 1: Classify the query using LLM
        classification = self._classify_company_query(query)
        
        # Step 2: If classified as company info, generate appropriate response
        if classification:
            response = self._generate_company_response(classification, query)
            if response:
                return response
        
        # Step 3: If no classification or response, return None (will proceed to next tier)
        return None
