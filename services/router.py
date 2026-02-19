"""
Router Service - Main Query Routing Logic
Routes queries through the three-tier system
"""

from services.kb_service import KnowledgeBaseService
from services.inventory_service import InventoryService
from services.llm_service import LLMService
import config


class ChatbotRouter:
    """Main router for handling query routing through three tiers"""
    
    def __init__(self):
        """Initialize all service components"""
        self.kb_service = KnowledgeBaseService()
        self.inventory_service = InventoryService()
        self.llm_service = LLMService()
    
    def route_query(self, query: str) -> str:
        """
        Route a user query through the three-tier system
        
        Tier 1: Knowledge Base (static answers)
        Tier 2: Database (inventory via function calling)
        Tier 3: Fallback message
        
        Args:
            query: User's question
        
        Returns:
            Response string
        """
        # TIER 1: Check Knowledge Base first
        kb_answer = self.kb_service.search(query)
        if kb_answer:
            return kb_answer
        
        # TIER 2: Check if query requires inventory lookup via LLM
        try:
            function_call = self.llm_service.should_use_inventory(query)
            
            if function_call and function_call.get("function") == "get_inventory":
                # Extract arguments
                args = function_call.get("arguments", {})
                item_name = args.get("item_name")
                size = args.get("size")
                intent = args.get("intent")
                
                # Query inventory database
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
        return config.FALLBACK_MESSAGE
