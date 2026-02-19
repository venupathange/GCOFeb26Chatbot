# 🔑 WHERE TO SET YOUR AZURE OPENAI KEYS

## Quick Answer: 3 Options

You need to set **4 environment variables**. Choose ONE method:

---

## ✅ OPTION 1: PowerShell Commands (Easiest)

**Copy and paste these commands** (replace with your actual values):

```powershell
$env:AZURE_OPENAI_ENDPOINT="https://your-resource-name.openai.azure.com/"
$env:AZURE_OPENAI_KEY="your-actual-key-from-azure-portal"
$env:AZURE_API_VERSION="2024-02-15-preview"
$env:AZURE_DEPLOYMENT_NAME="gpt-4o-mini"
```

**Note:** These are temporary and only last for the current PowerShell session.

---

## ✅ OPTION 2: .env File (Recommended)

### Step 1: Create .env file
```powershell
# In project root directory
notepad .env
```

### Step 2: Add these lines (with your actual values):
```env
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_KEY=your-actual-key-from-azure-portal
AZURE_API_VERSION=2024-02-15-preview
AZURE_DEPLOYMENT_NAME=gpt-4o-mini
```

### Step 3: Save and close

**Note:** The app will automatically load these when it starts.

---

## ✅ OPTION 3: Windows System Environment Variables (Permanent)

### Step 1: Open Environment Variables
- Press `Win + X`
- Click "System"
- Click "Advanced system settings"
- Click "Environment Variables" button

### Step 2: Add New Variables
Click "New" under "User variables" and add each:

| Variable Name | Variable Value (example) |
|--------------|--------------------------|
| `AZURE_OPENAI_ENDPOINT` | `https://your-resource.openai.azure.com/` |
| `AZURE_OPENAI_KEY` | `abc123def456...` |
| `AZURE_API_VERSION` | `2024-02-15-preview` |
| `AZURE_DEPLOYMENT_NAME` | `gpt-4o-mini` |

### Step 3: Restart Terminal
Close and reopen PowerShell for changes to take effect.

---

## 📍 How to Find Your Azure Values

### Get AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_KEY:

1. **Go to Azure Portal:** https://portal.azure.com
2. **Find your Azure OpenAI resource** (search for it)
3. **Click "Keys and Endpoint"** in the left menu
4. **Copy the values:**
   - **Endpoint** → This is your `AZURE_OPENAI_ENDPOINT`
   - **KEY 1** → This is your `AZURE_OPENAI_KEY`

### Get AZURE_DEPLOYMENT_NAME:

1. **In the same Azure OpenAI resource**
2. **Click "Model deployments"** in the left menu
3. **Or click "Go to Azure OpenAI Studio"**
4. **Find your deployment name** (e.g., `gpt-4o-mini`, `gpt-35-turbo`)
5. **Copy the deployment name** → This is your `AZURE_DEPLOYMENT_NAME`

### AZURE_API_VERSION:

- Use `2024-02-15-preview` (this is the default)
- Or check Azure docs for the latest version

---

## 🎯 Complete Setup Commands

**Copy this entire block** (replace values in the $env lines):

```powershell
# Navigate to project
cd C:\GCO\GCOFeb26Chatbot

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Set environment variables (REPLACE WITH YOUR ACTUAL VALUES!)
$env:AZURE_OPENAI_ENDPOINT="https://YOUR-RESOURCE-NAME.openai.azure.com/"
$env:AZURE_OPENAI_KEY="YOUR-ACTUAL-KEY-HERE"
$env:AZURE_API_VERSION="2024-02-15-preview"
$env:AZURE_DEPLOYMENT_NAME="gpt-4o-mini"

# Verify variables are set
Write-Host "Endpoint: $env:AZURE_OPENAI_ENDPOINT"
Write-Host "Key is set: $($env:AZURE_OPENAI_KEY -ne $null)"
Write-Host "API Version: $env:AZURE_API_VERSION"
Write-Host "Deployment: $env:AZURE_DEPLOYMENT_NAME"

# Run the application
python main.py
```

---

## ✅ Verify Your Setup

**Check if variables are set:**

```powershell
echo $env:AZURE_OPENAI_ENDPOINT
echo $env:AZURE_OPENAI_KEY
echo $env:AZURE_API_VERSION
echo $env:AZURE_DEPLOYMENT_NAME
```

**Each command should show your value, not empty!**

---

## 🚨 Common Mistakes

### ❌ WRONG:
```powershell
# Don't include quotes in the actual values
$env:AZURE_OPENAI_ENDPOINT="https://my-resource.openai.azure.com/"
# Then copying: "https://my-resource.openai.azure.com/" (with quotes)
```

### ✅ CORRECT:
```powershell
# The quotes are only for PowerShell syntax
$env:AZURE_OPENAI_ENDPOINT="https://my-resource.openai.azure.com/"
# The actual value stored is: https://my-resource.openai.azure.com/ (no quotes)
```

### ❌ WRONG:
```powershell
# Missing the trailing slash
$env:AZURE_OPENAI_ENDPOINT="https://my-resource.openai.azure.com"
```

### ✅ CORRECT:
```powershell
# Include the trailing slash
$env:AZURE_OPENAI_ENDPOINT="https://my-resource.openai.azure.com/"
```

---

## 📋 Checklist Before Running

- [ ] Virtual environment created (`venv` folder exists)
- [ ] Virtual environment activated (see `(venv)` in prompt)
- [ ] Dependencies installed (`pip list` shows `openai`)
- [ ] `AZURE_OPENAI_ENDPOINT` is set (run `echo $env:AZURE_OPENAI_ENDPOINT`)
- [ ] `AZURE_OPENAI_KEY` is set (run `echo $env:AZURE_OPENAI_KEY`)
- [ ] `AZURE_API_VERSION` is set (or using default)
- [ ] `AZURE_DEPLOYMENT_NAME` is set (or using default)
- [ ] Values are YOUR actual values from Azure Portal (not placeholders!)

---

## 🎉 Ready to Run!

Once all variables are set:

```powershell
python main.py
```

You should see:
```
============================================================
Welcome to TechGear UK Chatbot
============================================================
Type 'exit' to quit

User: _
```

---

## 📚 Need More Help?

- **Step-by-step guide:** `STEP_BY_STEP_SETUP.md`
- **Full Azure guide:** `AZURE_SETUP_GUIDE.md`
- **What changed:** `CHANGES_SUMMARY.md`
- **Quick reference:** `QUICK_REFERENCE.md`

---

## 🎯 Summary

**You need to set 4 variables:**

1. ✅ `AZURE_OPENAI_ENDPOINT` - Your endpoint URL from Azure Portal
2. ✅ `AZURE_OPENAI_KEY` - Your API key from Azure Portal
3. ✅ `AZURE_API_VERSION` - Use `2024-02-15-preview`
4. ✅ `AZURE_DEPLOYMENT_NAME` - Your deployment name (e.g., `gpt-4o-mini`)

**Easiest method:** Copy the PowerShell commands at the top of this file!

**That's it! 🚀**
