# Step-by-Step Setup Guide

## 🎯 Complete Setup in 5 Steps

---

## Step 1️⃣: Create Virtual Environment

Open **PowerShell** and navigate to your project:

```powershell
cd C:\GCO\GCOFeb26Chatbot
```

Create the virtual environment:

```powershell
python -m venv venv
```

**What this does:** Creates a folder called `venv` with an isolated Python environment.

---

## Step 2️⃣: Activate Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

**Expected result:** You should see `(venv)` at the start of your prompt:
```
(venv) PS C:\GCO\GCOFeb26Chatbot>
```

**If you get an error about execution policy:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then try activating again.

---

## Step 3️⃣: Install Required Packages

```powershell
pip install -r requirements.txt
```

**What this installs:**
- `openai` - Azure OpenAI Python SDK
- `python-dotenv` - For loading environment variables from .env file

**Verify installation:**
```powershell
pip list
```

You should see `openai` and `python-dotenv` in the list.

---

## Step 4️⃣: Set Azure OpenAI Environment Variables

### **Option A: Using PowerShell (Quick & Easy)**

Copy and paste these commands, **replacing with your actual values:**

```powershell
# Replace these with YOUR actual Azure values!
$env:AZURE_OPENAI_ENDPOINT="https://your-resource-name.openai.azure.com/"
$env:AZURE_OPENAI_KEY="your-actual-key-from-azure-portal"
$env:AZURE_API_VERSION="2024-02-15-preview"
$env:AZURE_DEPLOYMENT_NAME="gpt-4o-mini"
```

**Verify they are set:**
```powershell
echo $env:AZURE_OPENAI_ENDPOINT
echo $env:AZURE_OPENAI_KEY
```

### **Option B: Using .env File (Recommended for Repeated Use)**

1. **Copy the template file:**
   ```powershell
   Copy-Item .env.template .env
   ```

2. **Edit the .env file:**
   ```powershell
   notepad .env
   ```

3. **Fill in your actual values:**
   ```env
   AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
   AZURE_OPENAI_KEY=your-actual-key-here
   AZURE_API_VERSION=2024-02-15-preview
   AZURE_DEPLOYMENT_NAME=gpt-4o-mini
   ```

4. **Save and close** the file

---

## Step 5️⃣: Run the Application

```powershell
python main.py
```

**Expected output:**
```
============================================================
Welcome to TechGear UK Chatbot
============================================================
Type 'exit' to quit

User: _
```

---

## 🎉 Test It Out!

Try these test queries:

### **Knowledge Base Test:**
```
User: What is the office address?
Bot: 124 High Street, London, EC1A 1BB
```

### **Database Test:**
```
User: Is the Waterproof Commuter Jacket available in XL?
Bot: Yes (3 in stock)
```

### **Price Test:**
```
User: What is the price of the Dry-Fit Running Tee?
Bot: £25.00
```

### **Fallback Test:**
```
User: What is the capital of France?
Bot: I'm sorry, I cannot answer your query at the moment.
```

---

## 📍 Where to Find Your Azure Values

### **Step-by-Step in Azure Portal:**

1. **Go to Azure Portal:**
   - Open https://portal.azure.com
   - Sign in with your account

2. **Find Your Azure OpenAI Resource:**
   - Click "All resources" or search for your OpenAI service
   - Click on your Azure OpenAI resource name

3. **Get Endpoint and Key:**
   - In the left menu, click **"Keys and Endpoint"**
   - You'll see:
     - **Endpoint:** Copy this entire URL → This is your `AZURE_OPENAI_ENDPOINT`
     - **KEY 1:** Copy this → This is your `AZURE_OPENAI_KEY`

4. **Get Deployment Name:**
   - In the left menu, click **"Model deployments"**
   - OR click **"Go to Azure OpenAI Studio"**
   - Find your deployment name (e.g., `gpt-4o-mini`) → This is your `AZURE_DEPLOYMENT_NAME`

---

## 🔍 Troubleshooting

### **Problem: "AZURE_OPENAI_ENDPOINT environment variable not set"**

**Solution:**
```powershell
# Check if variable is set
echo $env:AZURE_OPENAI_ENDPOINT

# If empty, set it:
$env:AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/"
```

### **Problem: Virtual environment not activating**

**Solution:**
```powershell
# Try this first:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate:
.\venv\Scripts\Activate.ps1
```

### **Problem: "Module not found: openai"**

**Solution:**
```powershell
# Make sure (venv) is showing in your prompt
# Then reinstall:
pip install -r requirements.txt
```

### **Problem: "Invalid API key"**

**Solution:**
- Go back to Azure Portal
- Verify you copied the correct key
- Try using KEY 2 instead of KEY 1
- Make sure there are no extra spaces

---

## 📋 Complete Command Checklist

Copy and paste this entire block (replace values in Step 4):

```powershell
# Step 1: Navigate to project
cd C:\GCO\GCOFeb26Chatbot

# Step 2: Create virtual environment
python -m venv venv

# Step 3: Activate virtual environment
.\venv\Scripts\Activate.ps1

# Step 4: Install dependencies
pip install -r requirements.txt

# Step 5: Set environment variables (REPLACE WITH YOUR VALUES!)
$env:AZURE_OPENAI_ENDPOINT="https://YOUR-RESOURCE.openai.azure.com/"
$env:AZURE_OPENAI_KEY="YOUR-KEY-HERE"
$env:AZURE_API_VERSION="2024-02-15-preview"
$env:AZURE_DEPLOYMENT_NAME="gpt-4o-mini"

# Step 6: Verify variables are set
echo $env:AZURE_OPENAI_ENDPOINT

# Step 7: Run the application
python main.py
```

---

## 🎓 Understanding the Setup

### **Why Virtual Environment?**
- Keeps project dependencies isolated
- Prevents conflicts with other Python projects
- Easy to delete and recreate if needed

### **Why Environment Variables?**
- Keeps sensitive keys out of code
- Easy to change without modifying code
- Follows security best practices

### **What Files Were Changed?**
Only 2 files were modified to support Azure OpenAI:
1. `config.py` - Reads Azure environment variables
2. `services/llm_service.py` - Uses Azure OpenAI client

---

## ✅ Success Checklist

Before running, verify:

- [ ] Virtual environment created (`venv` folder exists)
- [ ] Virtual environment activated (`(venv)` shows in prompt)
- [ ] Dependencies installed (`pip list` shows `openai`)
- [ ] `AZURE_OPENAI_ENDPOINT` is set (echo shows your endpoint)
- [ ] `AZURE_OPENAI_KEY` is set (echo shows your key)
- [ ] `AZURE_API_VERSION` is set (or using default)
- [ ] `AZURE_DEPLOYMENT_NAME` is set (or using default)
- [ ] `inventory.db` file exists in project root

---

## 🎯 Next Steps

Once setup is complete:

1. **Test all query types** (KB, DB, Fallback)
2. **Review test_suite.json** for comprehensive test cases
3. **Explore the code** in the `services/` folder
4. **Read PROJECT_STRUCTURE.md** for architecture details

---

## 📞 Need Help?

- **Full Azure Guide:** See `AZURE_SETUP_GUIDE.md`
- **Quick Reference:** See `QUICK_REFERENCE.md`
- **Architecture:** See `PROJECT_STRUCTURE.md`

---

**You're all set! Happy coding! 🚀**
