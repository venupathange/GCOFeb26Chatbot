# Quick Reference - Azure OpenAI Keys Location

## 🔑 Where to Set Your Azure OpenAI Keys

### **Environment Variables Required:**

| Variable Name | Description | Example Value |
|--------------|-------------|---------------|
| `AZURE_OPENAI_ENDPOINT` | Your Azure OpenAI endpoint URL | `https://your-resource.openai.azure.com/` |
| `AZURE_OPENAI_KEY` | Your Azure OpenAI API key | `abc123...xyz` |
| `AZURE_API_VERSION` | API version (optional) | `2024-02-15-preview` |
| `AZURE_DEPLOYMENT_NAME` | Your model deployment name | `gpt-4o-mini` |

---

## 📂 Files Modified for Azure OpenAI

### **1. config.py** (Lines 15-18)
**Location:** `C:\GCO\GCOFeb26Chatbot\config.py`

```python
# Azure OpenAI settings
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION", "2024-02-15-preview")
AZURE_DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME", "gpt-4o-mini")
```

### **2. services/llm_service.py** (Lines 8, 15-24)
**Location:** `C:\GCO\GCOFeb26Chatbot\services\llm_service.py`

```python
from openai import AzureOpenAI  # Line 8 - Changed import

# Lines 15-24 - Updated initialization
def __init__(self):
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

## 🚀 Three Ways to Set Environment Variables

### **Method 1: PowerShell (Temporary)**
```powershell
$env:AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/"
$env:AZURE_OPENAI_KEY="your-key-here"
$env:AZURE_API_VERSION="2024-02-15-preview"
$env:AZURE_DEPLOYMENT_NAME="gpt-4o-mini"
```

### **Method 2: .env File (Recommended)**
1. Copy `.env.template` to `.env`
2. Fill in your actual values
3. The app will auto-load them

### **Method 3: Windows System Variables (Permanent)**
1. Win + X → System → Advanced → Environment Variables
2. Add each variable under "User variables"
3. Restart terminal

---

## 🏃 Quick Start Commands

```powershell
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
.\venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set environment variables (use your actual values!)
$env:AZURE_OPENAI_ENDPOINT="https://YOUR-RESOURCE.openai.azure.com/"
$env:AZURE_OPENAI_KEY="YOUR-KEY-HERE"
$env:AZURE_API_VERSION="2024-02-15-preview"
$env:AZURE_DEPLOYMENT_NAME="gpt-4o-mini"

# 5. Run the app
python main.py
```

---

## 📍 Finding Your Azure Values

### **Azure Portal:**
1. Go to https://portal.azure.com
2. Navigate to your **Azure OpenAI Service**
3. Click **"Keys and Endpoint"**
   - Copy **Endpoint** → Use as `AZURE_OPENAI_ENDPOINT`
   - Copy **Key 1** or **Key 2** → Use as `AZURE_OPENAI_KEY`
4. Go to **"Model deployments"** or Azure OpenAI Studio
   - Find your deployment name → Use as `AZURE_DEPLOYMENT_NAME`

---

## ✅ Verify Setup

```powershell
# Check if variables are set
echo $env:AZURE_OPENAI_ENDPOINT
echo $env:AZURE_OPENAI_KEY
echo $env:AZURE_API_VERSION
echo $env:AZURE_DEPLOYMENT_NAME

# Check if virtual environment is active (should see (venv))
# Check if packages are installed
pip list | findstr openai
```

---

## 📚 Related Files

- **Full Setup Guide:** `AZURE_SETUP_GUIDE.md`
- **Environment Template:** `.env.template`
- **Configuration:** `config.py`
- **LLM Service:** `services/llm_service.py`
- **Requirements:** `requirements.txt`

---

## 🎯 Summary

**Two files were modified:**
1. ✅ `config.py` - Changed to use Azure OpenAI environment variables
2. ✅ `services/llm_service.py` - Changed to use `AzureOpenAI` client

**You need to set:**
1. ✅ `AZURE_OPENAI_ENDPOINT`
2. ✅ `AZURE_OPENAI_KEY`
3. ✅ `AZURE_API_VERSION` (optional, has default)
4. ✅ `AZURE_DEPLOYMENT_NAME` (optional, has default)

**Then run:**
```powershell
python main.py
```

That's it! 🎉
