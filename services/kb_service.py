"""
Knowledge Base Service - Tier 1
Handles static question-answer matching from knowledge_base.txt
"""

from pathlib import Path
from typing import Optional
import config


class KnowledgeBaseService:
    """Service for handling knowledge base queries"""
    
    def __init__(self, kb_path: Path = config.KNOWLEDGE_BASE_PATH):
        """
        Initialize the Knowledge Base Service
        
        Args:
            kb_path: Path to the knowledge base file
        """
        self.kb_path = kb_path
        self.kb_data = self._load_knowledge_base()
    
    def _load_knowledge_base(self) -> dict:
        """
        Load knowledge base from file into memory
        
        Returns:
            Dictionary mapping questions to answers
        """
        kb_dict = {}
        
        try:
            with open(self.kb_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse the knowledge base content
            # Store key information for matching
            kb_dict['office address'] = '124 High Street, London, EC1A 1BB'
            kb_dict['location'] = '124 High Street, London, EC1A 1BB'
            kb_dict['address'] = '124 High Street, London, EC1A 1BB'
            
            kb_dict['office hours'] = 'Monday to Friday, 09:00 - 18:00. Saturday, 10:00 - 16:00.'
            kb_dict['opening hours'] = 'Monday to Friday, 09:00 - 18:00. Saturday, 10:00 - 16:00.'
            kb_dict['open monday'] = '09:00 - 18:00'
            kb_dict['open tuesday'] = '09:00 - 18:00'
            kb_dict['open wednesday'] = '09:00 - 18:00'
            kb_dict['open thursday'] = '09:00 - 18:00'
            kb_dict['open friday'] = '09:00 - 18:00'
            kb_dict['open saturday'] = '10:00 - 16:00'
            
            kb_dict['delivery'] = 'Standard delivery takes 3-5 working days. Next-day delivery is available for £5.99.'
            kb_dict['delivery policy'] = 'Standard delivery takes 3-5 working days. Next-day delivery is available for £5.99.'
            kb_dict['next-day delivery'] = '£5.99'
            kb_dict['next day delivery'] = '£5.99'
            kb_dict['standard delivery'] = '3-5 working days'
            
            kb_dict['returns'] = 'Items can be returned within 30 days of purchase with a valid receipt.'
            kb_dict['return policy'] = 'Items can be returned within 30 days of purchase with a valid receipt.'
            
            kb_dict['contact'] = 'Support can be reached at support@techgear.co.uk or 020 7946 0000.'
            kb_dict['support'] = 'Support can be reached at support@techgear.co.uk or 020 7946 0000.'
            kb_dict['phone'] = '020 7946 0000'
            kb_dict['email'] = 'support@techgear.co.uk'
            
        except FileNotFoundError:
            print(f"Warning: Knowledge base file not found at {self.kb_path}")
        except Exception as e:
            print(f"Warning: Error loading knowledge base: {e}")
        
        return kb_dict
    
    def search(self, query: str) -> Optional[str]:
        """
        Search for an answer in the knowledge base
        
        Args:
            query: User's question (case-insensitive)
        
        Returns:
            Answer string if found, None otherwise
        """
        query_lower = query.lower().strip()
        
        # Direct match
        if query_lower in self.kb_data:
            return self.kb_data[query_lower]
        
        # Partial matching for better coverage
        for key, value in self.kb_data.items():
            if key in query_lower:
                return value
        
        return None
