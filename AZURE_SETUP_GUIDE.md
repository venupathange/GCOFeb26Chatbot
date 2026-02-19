# Azure OpenAI Setup Guide - Tri-Tier Chatbot

## 📋 Prerequisites

- Python 3.10 or higher
- Azure OpenAI Service access
- Your Azure OpenAI credentials

---

## 🔧 Step 1: Create Virtual Environment

### **Windows (PowerShell)**

```powershell
# Navigate to project directory
cd C:\GCO\GCOFeb26Chatbot

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# If you get execution policy error, run this first:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### **Windows (Command Prompt)**

```cmd
# Navigate to project directory
cd C:\GCO\GCOFeb26Chatbot

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate.bat
```

### **Linux/Mac**

```bash
# Navigate to project directory
cd /path/to/GCOFeb26Chatbot

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### **Verify Virtual Environment is Active**

You should see `(venv)` at the beginning of your command prompt:

```
(venv) PS C:\GCO\GCOFeb26Chatbot>
```

---

## 📦 Step 2: Install Dependencies

```powershell
# Make sure virtual environment is activated
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🔑 Step 3: Configure Azure OpenAI Environment Variables

You need to set these **4 environment variables**:

1. **AZURE_OPENAI_ENDPOINT** - Your Azure OpenAI endpoint URL
2. **AZURE_OPENAI_KEY** - Your Azure OpenAI API key
3. **AZURE_API_VERSION** - API version (default: 2024-02-15-preview)
4. **AZURE_DEPLOYMENT_NAME** - Your deployment name (model name)

---

### **Option A: Set Environment Variables (Temporary - Current Session)**

#### **Windows PowerShell:**

```powershell
# Set Azure OpenAI credentials
$env:AZURE_OPENAI_ENDPOINT="https://your-resource-name.openai.azure.com/"
$env:AZURE_OPENAI_KEY="your-azure-openai-key-here"
$env:AZURE_API_VERSION="2024-02-15-preview"
$env:AZURE_DEPLOYMENT_NAME="gpt-4o-mini"

# Verify they are set
echo $env:AZURE_OPENAI_ENDPOINT
echo $env:AZURE_OPENAI_KEY
echo $env:AZURE_API_VERSION
echo $env:AZURE_DEPLOYMENT_NAME
```

#### **Windows Command Prompt:**

```cmd
set AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
set AZURE_OPENAI_KEY=your-azure-openai-key-here
set AZURE_API_VERSION=2024-02-15-preview
set AZURE_DEPLOYMENT_NAME=gpt-4o-mini
```

#### **Linux/Mac:**

```bash
export AZURE_OPENAI_ENDPOINT="https://your-resource-name.openai.azure.com/"
export AZURE_OPENAI_KEY="your-azure-openai-key-here"
export AZURE_API_VERSION="2024-02-15-preview"
export AZURE_DEPLOYMENT_NAME="gpt-4o-mini"
```

---

### **Option B: Create .env File (Recommended for Development)**

1. Create a file named `.env` in the project root:

```powershell
# Create .env file
New-Item -Path .env -ItemType File
```

2. Add your credentials to `.env`:

```env
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_KEY=your-azure-openai-key-here
AZURE_API_VERSION=2024-02-15-preview
AZURE_DEPLOYMENT_NAME=gpt-4o-mini
```

3. Install python-dotenv:

```powershell
pip install python-dotenv
```

4. Update `config.py` to load from .env (see instructions below)

---

### **Option C: Set System Environment Variables (Permanent - Windows)**

1. **Open System Properties:**
   - Press `Win + X` → Select "System"
   - Click "Advanced system settings"
   - Click "Environment Variables"

2. **Add New Variables:**
   - Click "New" under "User variables"
   - Add each variable:
     - Variable name: `AZURE_OPENAI_ENDPOINT`
     - Variable value: `https://your-resource-name.openai.azure.com/`
   - Repeat for all 4 variables

3. **Restart your terminal** for changes to take effect

---

## 📝 Step 4: Update config.py (If Using .env File)

If you chose Option B (.env file), update `config.py`:

```python
"""
Configuration settings for Tri-Tier Chatbot
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Base directory
BASE_DIR = Path(__file__).parent

# Data paths
DATA_DIR = BASE_DIR / "data"
KNOWLEDGE_BASE_PATH = DATA_DIR / "knowledge_base.txt"
INVENTORY_DB_PATH = "./inventory.db"

# Azure OpenAI settings
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION", "2024-02-15-preview")
AZURE_DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME", "gpt-4o-mini")

# Fallback message
FALLBACK_MESSAGE = "I'm sorry, I cannot answer your query at the moment."

# Database table name
DB_TABLE_NAME = "product_inventory"
```

---

## 🚀 Step 5: Run the Application

```powershell
# Make sure virtual environment is activated (you should see (venv))
# Make sure environment variables are set
python main.py
```

---

## ✅ Verification Checklist

Before running, verify:

- [ ] Virtual environment is activated `(venv)` appears in prompt
- [ ] Dependencies installed: `pip list | findstr openai`
- [ ] Environment variables set:
  ```powershell
  echo $env:AZURE_OPENAI_ENDPOINT
  echo $env:AZURE_OPENAI_KEY
  echo $env:AZURE_API_VERSION
  echo $env:AZURE_DEPLOYMENT_NAME
  ```
- [ ] All values are correct (no placeholder text)
- [ ] Database exists: `inventory.db` in root folder

---

## 🔍 Where Azure OpenAI Keys Are Used

### **1. config.py** (Lines 15-18)
```python
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION", "2024-02-15-preview")
AZURE_DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME", "gpt-4o-mini")
```

### **2. services/llm_service.py** (Lines 15-24)
```python
def __init__(self):
    """Initialize the LLM Service with Azure OpenAI client"""
    if not config.AZURE_OPENAI_ENDPOINT:
        raise ValueError("AZURE_OPENAI_ENDPOINT environment variable not set")
    if not config.AZURE_OPENAI_KEY:
        raise ValueError("AZURE_OPENAI_KEY environment variable not set")
    
    self.client = AzureOpenAI(
        azure_endpoint=config.AZURE_OPENAI_ENDPOINT,
        api_key=config.AZURE_OPENAI_KEY,
        api_version=config.AZURE_API_VERSION
    )
    self.model = config.AZURE_DEPLOYMENT_NAME
```

---

## 🎯 Quick Start (Copy-Paste Ready)

```powershell
# 1. Navigate to project
cd C:\GCO\GCOFeb26Chatbot

# 2. Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Set environment variables (REPLACE WITH YOUR VALUES!)
$env:AZURE_OPENAI_ENDPOINT="https://YOUR-RESOURCE.openai.azure.com/"
$env:AZURE_OPENAI_KEY="YOUR-KEY-HERE"
$env:AZURE_API_VERSION="2024-02-15-preview"
$env:AZURE_DEPLOYMENT_NAME="gpt-4o-mini"

# 5. Run the application
python main.py
```

---

## 🐛 Troubleshooting

### **Error: "AZURE_OPENAI_ENDPOINT environment variable not set"**
- **Solution:** Set the environment variable before running
- **Check:** `echo $env:AZURE_OPENAI_ENDPOINT` should show your endpoint

### **Error: "Execution policy" (PowerShell)**
- **Solution:** Run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### **Error: "Module not found: openai"**
- **Solution:** Make sure virtual environment is activated and run `pip install -r requirements.txt`

### **Error: "Invalid API key"**
- **Solution:** Verify your `AZURE_OPENAI_KEY` is correct
- **Check:** Go to Azure Portal → Your OpenAI Resource → Keys and Endpoint

### **Virtual environment not activating**
- **PowerShell:** Use `.\venv\Scripts\Activate.ps1`
- **CMD:** Use `venv\Scripts\activate.bat`
- **Check:** You should see `(venv)` in your prompt

---

## 📊 Finding Your Azure OpenAI Values

### **Azure Portal Steps:**

1. Go to [Azure Portal](https://portal.azure.com)
2. Navigate to your **Azure OpenAI Service** resource
3. Click **"Keys and Endpoint"** in the left menu

You'll find:
- **Endpoint:** `https://your-resource-name.openai.azure.com/`
- **Key 1 or Key 2:** Use either key as `AZURE_OPENAI_KEY`

4. Click **"Model deployments"** or go to Azure OpenAI Studio
5. Find your deployment name (e.g., `gpt-4o-mini`, `gpt-35-turbo`)

---

## 🔒 Security Best Practices

✅ **DO:**
- Use `.env` file for local development
- Add `.env` to `.gitignore`
- Use system environment variables for production
- Rotate keys regularly

❌ **DON'T:**
- Commit `.env` file to Git
- Share keys in code or documentation
- Hardcode credentials in source files

---

## 📝 Example .env File Template

Create `.env` in project root:

```env
# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_KEY=1234567890abcdef1234567890abcdef
AZURE_API_VERSION=2024-02-15-preview
AZURE_DEPLOYMENT_NAME=gpt-4o-mini
```

---

## ✨ You're Ready!

Once setup is complete:

```powershell
(venv) PS C:\GCO\GCOFeb26Chatbot> python main.py
============================================================
Welcome to TechGear UK Chatbot
============================================================
Type 'exit' to quit

User: What is the office address?
Bot: 124 High Street, London, EC1A 1BB

User: Is the Waterproof Commuter Jacket available in XL?
Bot: Yes (3 in stock)

User: exit
```

**Happy Chatting! 🎉**
