# Tri-Tier Chatbot - Project Structure

## Overview
Production-style Python console chatbot with three-tier architecture for TechGear UK.

## Architecture

### Tier 1: Knowledge Base Service
- **File:** `services/kb_service.py`
- **Purpose:** Handles static Q&A from `data/knowledge_base.txt`
- **Features:**
  - Case-insensitive matching
  - No LLM usage (direct lookup)
  - Pre-loaded into memory for fast access

### Tier 2: Inventory Service + LLM Service
- **Files:** 
  - `services/inventory_service.py` - Database operations
  - `services/llm_service.py` - OpenAI function calling
- **Purpose:** Handles product inventory queries via SQLite
- **Features:**
  - OpenAI GPT-4o-mini with function/tool calling
  - Parameterised SQL queries (SQL injection safe)
  - Extracts: item_name, size (optional), intent (stock/price)
  - Returns formatted responses with GBP currency

### Tier 3: Fallback
- **Trigger:** When no KB match and no valid DB query
- **Response:** "I'm sorry, I cannot answer your query at the moment."

## File Structure

```
tri_tier_chatbot/
│
├── main.py                     # Entry point - CLI loop
├── config.py                   # Configuration (paths, API settings)
├── requirements.txt            # Python dependencies
│
├── services/
│   ├── __init__.py            # Package initializer
│   ├── router.py              # Main routing logic (3-tier)
│   ├── kb_service.py          # Knowledge base handler
│   ├── inventory_service.py   # SQLite database handler
│   └── llm_service.py         # OpenAI integration
│
├── data/
│   ├── knowledge_base.txt     # Static Q&A data
│   └── (inventory.db symlink) # Points to root inventory.db
│
└── inventory.db               # SQLite database (root level)
```

## Key Design Decisions

### 1. Service-Based Architecture
- Clean separation of concerns
- Each service has a single responsibility
- Easy to test and maintain

### 2. Router Pattern
- Single entry point for all queries
- Sequential tier checking (KB → DB → Fallback)
- Centralized error handling

### 3. Function Calling Implementation
- OpenAI tool/function calling for parameter extraction
- Automatic intent detection (stock vs price)
- Handles optional parameters (size)

### 4. Database Safety
- Parameterised queries (no string concatenation)
- Connection management per query
- Graceful error handling

### 5. UK Localisation
- All prices in GBP (£)
- UK English spelling
- Proper currency formatting (£XX.XX)

## Data Flow

```
User Input
    ↓
Router (router.py)
    ↓
[Tier 1] KB Service → Match? → Return Answer
    ↓ (No match)
[Tier 2] LLM Service → Function Call? → Inventory Service → Return Result
    ↓ (No function call or no result)
[Tier 3] Return Fallback Message
```

## Function Schema

```json
{
  "name": "get_inventory",
  "parameters": {
    "item_name": "string (required)",
    "size": "string (optional) - S|M|L|XL",
    "intent": "string (optional) - stock|price"
  }
}
```

## Response Formats

### Stock Queries:
- In stock: "Yes (X in stock)"
- Out of stock: "0 / Out of stock"

### Price Queries:
- Format: "£XX.XX"

### Knowledge Base:
- Direct answer from KB

### Fallback:
- "I'm sorry, I cannot answer your query at the moment."

## Error Handling

1. **Missing API Key:** Raises ValueError on initialization
2. **Missing Database:** Raises Exception with clear message
3. **Invalid Query:** Returns fallback message
4. **LLM Errors:** Caught and logged, proceeds to fallback
5. **DB Errors:** Caught and returns error message

## Testing

Reference `test_suite.json` for comprehensive test cases covering:
- KB queries (IDs 1-3)
- DB queries (IDs 4-7)
- Fallback queries (IDs 8-10)

## Configuration

All settings in `config.py`:
- `OPENAI_MODEL`: "gpt-4o-mini"
- `INVENTORY_DB_PATH`: "./inventory.db" (relative)
- `KNOWLEDGE_BASE_PATH`: "data/knowledge_base.txt"
- `FALLBACK_MESSAGE`: Standard error message

## Dependencies

- `openai>=1.12.0` - OpenAI Python SDK
- `sqlite3` - Built-in Python module
- `pathlib` - Built-in Python module

## Production Considerations

✅ Clean code structure
✅ Type hints for better IDE support
✅ Comprehensive docstrings
✅ Error handling at all levels
✅ No hardcoded paths
✅ Environment variable for API key
✅ Parameterised SQL queries
✅ Modular and testable design
