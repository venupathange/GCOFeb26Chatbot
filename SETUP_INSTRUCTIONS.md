# 🚀 Setup Instructions - Tri-Tier Chatbot

## ✅ Complete Setup Guide

Follow these steps in order to set up and run the chatbot.

---

## 📋 Step-by-Step Setup

### **Step 1: Activate Virtual Environment**

```powershell
cd C:\GCO\GCOFeb26Chatbot
.\venv\Scripts\Activate.ps1
```

You should see `(venv)` at the start of your prompt.

---

### **Step 2: Configure Azure OpenAI Credentials**

Edit the `.env` file (create it if it doesn't exist):

```powershell
notepad .env
```

Add your Azure OpenAI credentials:

```env
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_KEY=your-azure-openai-key-here
AZURE_API_VERSION=2024-02-15-preview
AZURE_DEPLOYMENT_NAME=gpt-4o-mini
```

**Save and close the file.**

---

### **Step 3: Initialize Database**

Run the database setup script:

```powershell
python setup_database.py
```

**Expected Output:**
```
======================================================================
🔧 Inventory Database Setup
======================================================================

✅ Database setup successful!
📊 Created: inventory.db
📦 Loaded 8 products

📋 Sample Data:
----------------------------------------------------------------------
Item Name                           Size   Stock    Price
----------------------------------------------------------------------
Waterproof Commuter Jacket          S      5        £85.00
Waterproof Commuter Jacket          M      0        £85.00
Waterproof Commuter Jacket          L      12       £85.00
----------------------------------------------------------------------

✨ Database is ready to use!
💡 Run 'python main.py' to start the chatbot
```

---

### **Step 4: Run Tests (Optional but Recommended)**

Test the chatbot with automated test suite:

```powershell
python run_tests.py
```

**Expected Output:**
```
🔧 Initializing chatbot...
✅ Chatbot initialized

================================================================================
🧪 Running Test Suite
================================================================================

Test #1 [KB]
  Q: What is the office address?
  ✅ PASSED
  A: 124 High Street, London, EC1A 1BB

Test #2 [KB]
  Q: When do you open on Monday?
  ✅ PASSED
  A: Monday to Friday, 09:00 - 18:00. Saturday, 10:00 - 16:00.

... (more tests)

================================================================================
📊 Test Results Summary
================================================================================
Total Tests:  10
✅ Passed:    10
❌ Failed:    0
Success Rate: 100.0%
================================================================================

🎉 All tests passed!
```

---

### **Step 5: Run the Chatbot**

Start the chatbot:

```powershell
python main.py
```

**Expected Output:**
```
============================================================
Welcome to TechGear UK Chatbot
============================================================
Type 'exit' to quit

User: _
```

---

## 💬 Try These Queries

### **Company Information:**
```
User: what is the company name
User: tell me about techgear
User: where are you located
User: contact details
User: office timings
```

### **Inventory:**
```
User: Is the Waterproof Commuter Jacket available in XL?
User: What is the price of the Dry-Fit Running Tee?
User: Do you have Tech-Knit Hoodie in size M?
```

### **Fallback:**
```
User: What is the capital of France?
```

---

## 🐛 Troubleshooting

### **Issue: "AZURE_OPENAI_ENDPOINT environment variable not set"**

**Solution:**
1. Check that `.env` file exists in `C:\GCO\GCOFeb26Chatbot\`
2. Verify `.env` contains your actual Azure credentials (not placeholder text)
3. Restart the application

---

### **Issue: "Database not found"**

**Solution:**
```powershell
python setup_database.py
```

---

### **Issue: Tests failing**

**Solution:**
1. Ensure `.env` has correct Azure OpenAI credentials
2. Ensure database is initialized: `python setup_database.py`
3. Check Azure OpenAI endpoint is accessible
4. Verify deployment name matches your Azure setup

---

## 📊 What Each File Does

| File | Purpose |
|------|---------|
| `inventory_setup.sql` | SQL schema and data for inventory database |
| `test_suite.json` | 10 test cases for automated testing |
| `setup_database.py` | Script to initialize database from SQL file |
| `run_tests.py` | Script to run automated tests |
| `main.py` | Main chatbot application |

---

## ✅ Verification Checklist

Before running the chatbot, verify:

- [ ] Virtual environment is activated (`(venv)` in prompt)
- [ ] `.env` file exists with Azure OpenAI credentials
- [ ] Database initialized (`inventory.db` exists)
- [ ] Tests pass (optional: run `python run_tests.py`)
- [ ] Ready to run: `python main.py`

---

## 🎯 Quick Commands

```powershell
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Setup database
python setup_database.py

# Run tests
python run_tests.py

# Run chatbot
python main.py
```

---

## 📝 Summary

**Files Utilized:**
1. ✅ `inventory_setup.sql` → Used by `setup_database.py` to create database
2. ✅ `test_suite.json` → Used by `run_tests.py` to run automated tests
3. ✅ `inventory.db` → Created by setup script, used by chatbot

**Scripts Created:**
1. ✅ `setup_database.py` → Initializes database
2. ✅ `run_tests.py` → Runs automated tests

**Everything is now properly utilized and documented!** 🎉
