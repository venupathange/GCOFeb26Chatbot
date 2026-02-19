"""
Configuration settings for Tri-Tier Chatbot
"""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent

# Data paths
DATA_DIR = BASE_DIR / "data"
KNOWLEDGE_BASE_PATH = DATA_DIR / "knowledge_base.txt"
INVENTORY_DB_PATH = "./inventory.db"  # Relative path as per requirements

# Azure OpenAI settings
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION", "2024-02-15-preview")
AZURE_DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME", "gpt-4o-mini")

# Fallback message
FALLBACK_MESSAGE = "I'm sorry, I cannot answer your query at the moment."

# Database table name
DB_TABLE_NAME = "product_inventory"
