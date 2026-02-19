# Quick Start Guide - Tri-Tier Chatbot

## Installation (3 steps)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set OpenAI API Key
```powershell
# PowerShell (Windows)
$env:OPENAI_API_KEY="sk-your-key-here"
```

### 3. Run the Application
```bash
python main.py
```

## Usage

```
User: What is the office address?
Bot: 124 High Street, London, EC1A 1BB

User: Is the Waterproof Commuter Jacket available in XL?
Bot: Yes (3 in stock)

User: What is the price of the Dry-Fit Running Tee?
Bot: £25.00

User: exit
```

## Test Cases (from test_suite.json)

### Knowledge Base Queries:
1. "What is the office address?" → 124 High Street, EC1A 1BB
2. "When do you open on Monday?" → 09:00 - 18:00
3. "How much is next-day delivery?" → £5.99

### Database Queries:
4. "Is the Waterproof Commuter Jacket available in XL?" → Yes (3 in stock)
5. "Do you have the Waterproof Commuter Jacket in size M?" → 0 / Out of stock
6. "How many Tech-Knit Hoodies in size M?" → 10
7. "What is the price of the Dry-Fit Running Tee?" → £25.00

### Fallback Queries:
8. "What is the capital of France?" → I'm sorry, I cannot answer your query at the moment.
9. "Can I have a discount code?" → I'm sorry, I cannot answer your query at the moment.
10. "Who is the Prime Minister?" → I'm sorry, I cannot answer your query at the moment.

## Troubleshooting

**Error: "OPENAI_API_KEY environment variable not set"**
- Solution: Set the environment variable before running

**Error: "Database error"**
- Solution: Regenerate database: `sqlite3 inventory.db < inventory_setup.sql`

**Error: "Knowledge base file not found"**
- Solution: Ensure `data/knowledge_base.txt` exists

## Architecture Summary

```
Query → Router → [KB Service] → Found? → Return
                      ↓ Not Found
                 [LLM Service] → Function Call?
                      ↓ Yes
                 [Inventory Service] → Query DB → Return
                      ↓ No/Error
                 [Fallback] → Return default message
```

## Files You Need

✅ `main.py` - Entry point
✅ `config.py` - Configuration
✅ `services/router.py` - Main logic
✅ `services/kb_service.py` - Knowledge base
✅ `services/inventory_service.py` - Database
✅ `services/llm_service.py` - OpenAI
✅ `data/knowledge_base.txt` - Static data
✅ `inventory.db` - SQLite database
✅ `requirements.txt` - Dependencies

## That's It!

The chatbot is production-ready with:
- Clean modular architecture
- Proper error handling
- OpenAI function calling
- SQLite integration
- UK English & GBP formatting
