# 🚀 START HERE - Tri-Tier Chatbot Setup

## 📖 Welcome!

This is your **complete guide** to setting up the Tri-Tier Chatbot with Azure OpenAI.

---

## ⚡ Quick Setup (5 Minutes)

### **Step 1: Open PowerShell**
Navigate to the project:
```powershell
cd C:\GCO\GCOFeb26Chatbot
```

### **Step 2: Create Virtual Environment**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If you get an error, run this first:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### **Step 3: Install Dependencies**
```powershell
pip install -r requirements.txt
```

### **Step 4: Set Azure OpenAI Keys**

**🔑 IMPORTANT: Replace these with YOUR actual values from Azure Portal!**

```powershell
$env:AZURE_OPENAI_ENDPOINT="https://your-resource-name.openai.azure.com/"
$env:AZURE_OPENAI_KEY="your-actual-key-here"
$env:AZURE_API_VERSION="2024-02-15-preview"
$env:AZURE_DEPLOYMENT_NAME="gpt-4o-mini"
```

### **Step 5: Run the Application**
```powershell
python main.py
```

**That's it! 🎉**

---

## 🔑 Where to Find Your Azure Values

### **Azure Portal:**
1. Go to https://portal.azure.com
2. Find your **Azure OpenAI Service** resource
3. Click **"Keys and Endpoint"**
   - Copy **Endpoint** → Use as `AZURE_OPENAI_ENDPOINT`
   - Copy **Key 1** → Use as `AZURE_OPENAI_KEY`
4. Click **"Model deployments"**
   - Copy your deployment name → Use as `AZURE_DEPLOYMENT_NAME`

---

## 📚 Documentation Guide

| File | Purpose | Read When |
|------|---------|-----------|
| **WHERE_TO_SET_KEYS.md** | 🔑 Where to set Azure keys | **Start here** if confused about keys |
| **STEP_BY_STEP_SETUP.md** | 📋 Detailed step-by-step | First-time setup |
| **AZURE_SETUP_GUIDE.md** | 📖 Complete Azure guide | Need detailed instructions |
| **CHANGES_SUMMARY.md** | 📝 What was changed | Want to understand modifications |
| **QUICK_REFERENCE.md** | ⚡ Quick lookup | Need quick answers |

---

## ✅ What You Need

### **4 Environment Variables:**

| Variable | Required | Example | Where to Find |
|----------|----------|---------|---------------|
| `AZURE_OPENAI_ENDPOINT` | ✅ Yes | `https://my-resource.openai.azure.com/` | Azure Portal → Keys and Endpoint |
| `AZURE_OPENAI_KEY` | ✅ Yes | `abc123...` | Azure Portal → Keys and Endpoint |
| `AZURE_API_VERSION` | ⚠️ Optional | `2024-02-15-preview` | Use default |
| `AZURE_DEPLOYMENT_NAME` | ⚠️ Optional | `gpt-4o-mini` | Azure Portal → Model deployments |

---

## 🎯 Test Your Setup

Once running, try these queries:

### **Knowledge Base Test:**
```
User: What is the office address?
Expected: 124 High Street, London, EC1A 1BB
```

### **Database Test:**
```
User: Is the Waterproof Commuter Jacket available in XL?
Expected: Yes (3 in stock)
```

### **Price Test:**
```
User: What is the price of the Dry-Fit Running Tee?
Expected: £25.00
```

### **Fallback Test:**
```
User: What is the capital of France?
Expected: I'm sorry, I cannot answer your query at the moment.
```

---

## 🔧 What Was Changed for Azure OpenAI

### **2 Files Modified:**

1. **config.py** (Lines 16-20)
   - Changed to use Azure OpenAI environment variables

2. **services/llm_service.py** (Lines 8, 15-27)
   - Changed to use `AzureOpenAI` client

**Everything else stays the same!**

---

## 🐛 Troubleshooting

### **Problem: "AZURE_OPENAI_ENDPOINT environment variable not set"**
**Solution:** Set the environment variable:
```powershell
$env:AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/"
```

### **Problem: Virtual environment won't activate**
**Solution:** 
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

### **Problem: "Module not found: openai"**
**Solution:** Make sure `(venv)` is showing, then:
```powershell
pip install -r requirements.txt
```

### **Problem: "Invalid API key"**
**Solution:** 
- Go back to Azure Portal
- Verify you copied the correct key
- Make sure there are no extra spaces

---

## 📋 Pre-Flight Checklist

Before running, verify:

- [ ] PowerShell is open
- [ ] You're in the project directory (`C:\GCO\GCOFeb26Chatbot`)
- [ ] Virtual environment is activated (see `(venv)` in prompt)
- [ ] Dependencies are installed (`pip list` shows `openai`)
- [ ] All 4 environment variables are set (run `echo $env:AZURE_OPENAI_ENDPOINT`)
- [ ] You've replaced placeholder values with YOUR actual Azure values
- [ ] `inventory.db` file exists in the project root

---

## 🎓 Project Structure

```
C:\GCO\GCOFeb26Chatbot\
│
├── main.py                    # Entry point - run this!
├── config.py                  # Configuration (Azure keys used here)
│
├── services/
│   ├── router.py             # Routes queries through 3 tiers
│   ├── kb_service.py         # Tier 1: Knowledge Base
│   ├── inventory_service.py  # Tier 2: Database
│   └── llm_service.py        # Azure OpenAI integration (keys used here)
│
├── data/
│   └── knowledge_base.txt    # Static Q&A data
│
├── inventory.db              # SQLite database
└── test_suite.json           # Test cases
```

---

## 🎯 Next Steps After Setup

1. ✅ Test all query types (see test cases above)
2. ✅ Review `test_suite.json` for comprehensive tests
3. ✅ Read `PROJECT_STRUCTURE.md` for architecture details
4. ✅ Explore the code in `services/` folder

---

## 💡 Pro Tips

### **Use .env File for Repeated Use:**
Instead of setting variables every time, create a `.env` file:

1. Create `.env` in project root:
   ```powershell
   notepad .env
   ```

2. Add your values:
   ```env
   AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
   AZURE_OPENAI_KEY=your-key-here
   AZURE_API_VERSION=2024-02-15-preview
   AZURE_DEPLOYMENT_NAME=gpt-4o-mini
   ```

3. Save and close

The app will automatically load these values!

---

## 📞 Need More Help?

### **For Setup Issues:**
- Read: `STEP_BY_STEP_SETUP.md`
- Read: `AZURE_SETUP_GUIDE.md`

### **For Key Configuration:**
- Read: `WHERE_TO_SET_KEYS.md`

### **For Understanding Changes:**
- Read: `CHANGES_SUMMARY.md`

### **For Quick Reference:**
- Read: `QUICK_REFERENCE.md`

---

## 🎉 You're Ready!

Once you've completed the 5 steps above, you're all set!

```powershell
(venv) PS C:\GCO\GCOFeb26Chatbot> python main.py
============================================================
Welcome to TechGear UK Chatbot
============================================================
Type 'exit' to quit

User: _
```

**Happy Chatting! 🚀**

---

## 📌 Remember

- Virtual environment must be **activated** (see `(venv)`)
- Environment variables must be **set** before running
- Use **YOUR actual Azure values**, not placeholders
- Type **`exit`** to quit the chatbot

**Good luck! 🎊**
