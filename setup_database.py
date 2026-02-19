"""
Database Setup Script
Initializes the inventory database using inventory_setup.sql
"""

import sqlite3
import os
from pathlib import Path


def setup_database():
    """Initialize the inventory database from SQL file"""
    
    # File paths
    db_path = Path("inventory.db")
    sql_file = Path("inventory_setup.sql")
    
    # Check if SQL file exists
    if not sql_file.exists():
        print(f"❌ Error: {sql_file} not found!")
        return False
    
    try:
        # Read SQL file
        with open(sql_file, 'r', encoding='utf-8') as f:
            sql_script = f.read()
        
        # Connect to database (creates it if doesn't exist)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Execute SQL script
        cursor.executescript(sql_script)
        conn.commit()
        
        # Verify data was inserted
        cursor.execute("SELECT COUNT(*) FROM product_inventory")
        count = cursor.fetchone()[0]
        
        conn.close()
        
        print("✅ Database setup successful!")
        print(f"📊 Created: {db_path}")
        print(f"📦 Loaded {count} products")
        
        # Display sample data
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT item_name, size, stock_count, price_gbp FROM product_inventory LIMIT 3")
        
        print("\n📋 Sample Data:")
        print("-" * 70)
        print(f"{'Item Name':<35} {'Size':<6} {'Stock':<8} {'Price'}")
        print("-" * 70)
        
        for row in cursor.fetchall():
            item_name, size, stock, price = row
            print(f"{item_name:<35} {size:<6} {stock:<8} £{price:.2f}")
        
        print("-" * 70)
        conn.close()
        
        return True
        
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


if __name__ == "__main__":
    print("=" * 70)
    print("🔧 Inventory Database Setup")
    print("=" * 70)
    print()
    
    success = setup_database()
    
    if success:
        print("\n✨ Database is ready to use!")
        print("💡 Run 'python main.py' to start the chatbot")
    else:
        print("\n❌ Database setup failed!")
        print("💡 Please check the error messages above")
