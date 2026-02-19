# 🔑 .env File Setup Guide

## ✅ What Changed

**Before:** You had to set environment variables in PowerShell every time  
**Now:** Set them once in a `.env` file and forget about it!

---

## 🚀 Quick Setup (3 Steps)

### **Step 1: Locate the .env File**
The `.env` file is in your project root:
```
C:\GCO\GCOFeb26Chatbot\.env
```

### **Step 2: Edit the .env File**
```powershell
notepad .env
```

### **Step 3: Add Your Azure OpenAI Credentials**
Replace the placeholder values with your actual credentials:

```env
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_KEY=your-actual-key-here
AZURE_API_VERSION=2024-02-15-preview
AZURE_DEPLOYMENT_NAME=gpt-4o-mini
```

**Save and close the file.**

---

## 📍 Finding Your Azure Values

### **Azure Portal:**
1. Go to https://portal.azure.com
2. Navigate to your **Azure OpenAI Service** resource
3. Click **"Keys and Endpoint"**
   - Copy **Endpoint** → Use as `AZURE_OPENAI_ENDPOINT`
   - Copy **Key 1** → Use as `AZURE_OPENAI_KEY`
4. Click **"Model deployments"**
   - Copy your deployment name → Use as `AZURE_DEPLOYMENT_NAME`

---

## ✅ Example .env File

```env
# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT=https://my-openai-resource.openai.azure.com/
AZURE_OPENAI_KEY=abc123def456ghi789jkl012mno345pqr678stu901vwx234yz
AZURE_API_VERSION=2024-02-15-preview
AZURE_DEPLOYMENT_NAME=gpt-4o-mini
```

---

## 🚀 Running the Application

### **No More PowerShell Commands!**

**Before:**
```powershell
# Had to run these every time
$env:AZURE_OPENAI_ENDPOINT="..."
$env:AZURE_OPENAI_KEY="..."
$env:AZURE_API_VERSION="..."
$env:AZURE_DEPLOYMENT_NAME="..."
python main.py
```

**Now:**
```powershell
# Just run the app - credentials load automatically!
python main.py
```

---

## 🔒 Security

### **✅ The .env File is Safe**
- ✅ Automatically ignored by Git (won't be committed)
- ✅ Stays on your local machine only
- ✅ Easy to update without touching code

### **❌ Don't:**
- ❌ Commit `.env` to Git
- ❌ Share `.env` file with others
- ❌ Include `.env` in documentation

---

## 🧪 Verify Setup

### **Check if .env is loaded:**
```powershell
# Run the application
python main.py
```

**If credentials are correct:**
```
============================================================
Welcome to TechGear UK Chatbot
============================================================
Type 'exit' to quit

User: _
```

**If credentials are missing or wrong:**
```
Error initializing chatbot: AZURE_OPENAI_ENDPOINT environment variable not set
```

---

## 🐛 Troubleshooting

### **Problem: "AZURE_OPENAI_ENDPOINT environment variable not set"**
**Solution:**
1. Check that `.env` file exists in project root
2. Check that `.env` has correct values (no placeholder text)
3. Check that `python-dotenv` is installed: `pip install python-dotenv`

### **Problem: "Invalid API key"**
**Solution:**
1. Go back to Azure Portal
2. Verify you copied the correct key
3. Make sure there are no extra spaces in `.env`

### **Problem: ".env file not found"**
**Solution:**
1. Create it manually:
   ```powershell
   notepad .env
   ```
2. Add your credentials and save

---

## 📋 Complete Setup Checklist

- [ ] `.env` file exists in `C:\GCO\GCOFeb26Chatbot\`
- [ ] `AZURE_OPENAI_ENDPOINT` is set (with trailing `/`)
- [ ] `AZURE_OPENAI_KEY` is set (your actual key, not placeholder)
- [ ] `AZURE_API_VERSION` is set (use `2024-02-15-preview`)
- [ ] `AZURE_DEPLOYMENT_NAME` is set (your deployment name)
- [ ] No placeholder text like "your-resource-name" remains
- [ ] File is saved
- [ ] `python-dotenv` is installed

---

## 🎯 Quick Commands

### **Edit .env:**
```powershell
notepad .env
```

### **Check if python-dotenv is installed:**
```powershell
pip list | findstr dotenv
```

### **Install python-dotenv if missing:**
```powershell
pip install python-dotenv
```

### **Run the application:**
```powershell
python main.py
```

---

## 📝 .env File Format

**Important Rules:**
1. ✅ One variable per line
2. ✅ Format: `VARIABLE_NAME=value`
3. ✅ No spaces around `=`
4. ✅ No quotes needed (optional)
5. ✅ Comments start with `#`

**Good:**
```env
AZURE_OPENAI_ENDPOINT=https://my-resource.openai.azure.com/
AZURE_OPENAI_KEY=abc123
```

**Bad:**
```env
AZURE_OPENAI_ENDPOINT = "https://my-resource.openai.azure.com/"  # Spaces around =
AZURE_OPENAI_KEY = abc123  # Spaces around =
```

---

## ✨ Benefits

### **Convenience:**
- ✅ Set once, use forever
- ✅ No need to remember commands
- ✅ Automatic loading on startup

### **Security:**
- ✅ Not committed to Git
- ✅ Local to your machine
- ✅ Easy to update

### **Simplicity:**
- ✅ Just edit one file
- ✅ Clear and organized
- ✅ No PowerShell commands needed

---

## 🎓 How It Works

### **1. Application Starts**
```python
# config.py
from dotenv import load_dotenv
load_dotenv()  # Reads .env file
```

### **2. Variables Loaded**
```python
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
```

### **3. Services Use Variables**
```python
# services/llm_service.py
self.client = AzureOpenAI(
    azure_endpoint=config.AZURE_OPENAI_ENDPOINT,
    api_key=config.AZURE_OPENAI_KEY,
    api_version=config.AZURE_API_VERSION
)
```

---

## 📚 Related Documentation

- **Full Setup Guide:** `START_HERE.md`
- **Azure Setup:** `AZURE_SETUP_GUIDE.md`
- **Enhancements:** `ENHANCEMENTS_GUIDE.md`

---

## 🎉 Summary

**Old Way:**
```powershell
$env:AZURE_OPENAI_ENDPOINT="..."
$env:AZURE_OPENAI_KEY="..."
$env:AZURE_API_VERSION="..."
$env:AZURE_DEPLOYMENT_NAME="..."
python main.py
```

**New Way:**
```powershell
# Edit .env once
notepad .env

# Then just run
python main.py
```

**Much easier! 🚀**
