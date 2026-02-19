"""
Inventory Service - Tier 2
Handles database queries for product inventory
"""

import sqlite3
from typing import Optional, Dict, Any
import config


class InventoryService:
    """Service for handling inventory database queries"""
    
    def __init__(self, db_path: str = config.INVENTORY_DB_PATH):
        """
        Initialize the Inventory Service
        
        Args:
            db_path: Path to the SQLite database
        """
        self.db_path = db_path
        self._verify_database()
    
    def _verify_database(self):
        """Verify that the database exists and is accessible"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{config.DB_TABLE_NAME}'")
            result = cursor.fetchone()
            conn.close()
            
            if not result:
                raise Exception(f"Table '{config.DB_TABLE_NAME}' not found in database")
        except sqlite3.Error as e:
            raise Exception(f"Database error: {e}")
    
    def get_inventory(self, item_name: str, size: Optional[str] = None, intent: Optional[str] = None) -> str:
        """
        Query inventory database for product information
        
        Args:
            item_name: Name of the product (required)
            size: Size of the product (optional)
            intent: Query intent - "stock" or "price" (optional)
        
        Returns:
            Formatted response string
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Build parameterised query
            if size:
                query = f"""
                    SELECT item_name, size, stock_count, price_gbp 
                    FROM {config.DB_TABLE_NAME} 
                    WHERE LOWER(item_name) = LOWER(?) AND LOWER(size) = LOWER(?)
                """
                params = (item_name, size)
            else:
                query = f"""
                    SELECT item_name, size, stock_count, price_gbp 
                    FROM {config.DB_TABLE_NAME} 
                    WHERE LOWER(item_name) = LOWER(?)
                """
                params = (item_name,)
            
            cursor.execute(query, params)
            results = cursor.fetchall()
            conn.close()
            
            if not results:
                return config.FALLBACK_MESSAGE
            
            # Handle intent-based responses
            if intent == "price":
                # Return price information
                price = results[0][3]
                return f"£{price:.2f}"
            
            # Handle stock queries
            if size:
                # Specific size requested
                stock_count = results[0][2]
                if stock_count > 0:
                    return f"Yes ({stock_count} in stock)"
                else:
                    return "0 / Out of stock"
            else:
                # No size specified - return aggregate or first match
                if len(results) == 1:
                    stock_count = results[0][2]
                    if stock_count > 0:
                        return f"Yes ({stock_count} in stock)"
                    else:
                        return "0 / Out of stock"
                else:
                    # Multiple sizes available - return summary
                    total_stock = sum(row[2] for row in results)
                    if total_stock > 0:
                        return f"Yes ({total_stock} in stock across all sizes)"
                    else:
                        return "0 / Out of stock"
        
        except sqlite3.Error as e:
            return f"Database error: {e}"
        except Exception as e:
            return f"Error: {e}"
