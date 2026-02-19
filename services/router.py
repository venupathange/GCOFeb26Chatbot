"""
Router Service - Enhanced Query Routing Logic
Routes queries through the three-tier system with intelligent classification
"""

from services.kb_service import KnowledgeBaseService
from services.inventory_service import InventoryService
from services.llm_service import LLMService
import config


class ChatbotRouter:
    """Main router for handling query routing through three tiers with semantic classification"""
    
    def __init__(self):
        """Initialize all service components"""
        self.kb_service = KnowledgeBaseService()
        self.inventory_service = InventoryService()
        self.llm_service = LLMService()
    
    def route_query(self, query: str) -> str:
        """
        Route a user query through the enhanced three-tier system
        
        Enhanced Routing Logic:
        1. Classify query using LLM (company_info, inventory, or unknown)
        2. Route to appropriate tier based on classification
        3. Fall back if no valid response
        
        Tier 1: Knowledge Base (company information with semantic matching)
        Tier 2: Database (inventory via function calling)
        Tier 3: Fallback message
        
        Args:
            query: User's question
        
        Returns:
            Response string
        """
        try:
            # STEP 1: Classify the query using LLM
            # This determines which tier should handle the query
            classification = self.llm_service.classify_query(query)
            
            # STEP 2: Route based on classification
            
            # TIER 1: Company Information (Knowledge Base)
            if classification == "company_info":
                # Use semantic KB service to handle company-related queries
                kb_answer = self.kb_service.search(query)
                if kb_answer:
                    return kb_answer
            
            # TIER 2: Inventory Information (Database with Tool Calling)
            elif classification == "inventory":
                # Use LLM function calling to extract inventory parameters
                function_call = self.llm_service.should_use_inventory(query)
                
                if function_call and function_call.get("function") == "get_inventory":
                    # Extract arguments from function call
                    args = function_call.get("arguments", {})
                    item_name = args.get("item_name")
                    size = args.get("size")
                    intent = args.get("intent")
                    
                    # Query inventory database with extracted parameters
                    if item_name:
                        response = self.inventory_service.get_inventory(
                            item_name=item_name,
                            size=size,
                            intent=intent
                        )
                        
                        # Only return if it's not the fallback message
                        if response != config.FALLBACK_MESSAGE:
                            return response
        
        except Exception as e:
            print(f"Router Error: {e}")
        
        # TIER 3: Fallback
        # If classification is 'unknown' or no valid response from other tiers
        return config.FALLBACK_MESSAGE
