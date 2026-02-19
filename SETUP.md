# Tri-Tier Chatbot Setup Instructions

## Prerequisites
- Python 3.10 or higher
- OpenAI API key

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Set up your OpenAI API key as an environment variable:

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="your_openai_api_key_here"
```

**Windows (Command Prompt):**
```cmd
set OPENAI_API_KEY=your_openai_api_key_here
```

**Linux/Mac:**
```bash
export OPENAI_API_KEY="your_openai_api_key_here"
```

3. Ensure the database exists:
```bash
sqlite3 inventory.db < inventory_setup.sql
```

## Running the Application

```bash
python main.py
```

## Usage

- Type your questions at the `User:` prompt
- Type `exit` to quit the application

## Project Structure

```
tri_tier_chatbot/
│
├── main.py                 # Main entry point
├── config.py               # Configuration settings
│
├── services/
│   ├── router.py           # Query routing logic
│   ├── kb_service.py       # Knowledge base service (Tier 1)
│   ├── inventory_service.py # Database service (Tier 2)
│   └── llm_service.py      # OpenAI integration
│
├── data/
│   ├── knowledge_base.txt  # Static Q&A data
│   └── inventory.db        # SQLite database
│
└── requirements.txt        # Python dependencies
```

## Test Queries

### Knowledge Base (Tier 1):
- "What is the office address?"
- "When do you open on Monday?"
- "How much is next-day delivery?"

### Database (Tier 2):
- "Is the Waterproof Commuter Jacket available in XL?"
- "Do you have the Waterproof Commuter Jacket in size M?"
- "How many Tech-Knit Hoodies in size M?"
- "What is the price of the Dry-Fit Running Tee?"

### Fallback (Tier 3):
- "What is the capital of France?"
- "Can I have a discount code?"
