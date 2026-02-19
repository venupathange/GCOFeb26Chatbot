# 🚀 Tri-Tier Chatbot Enhancements - Semantic Matching & Intelligent Classification

## ✅ What Was Enhanced

The chatbot has been upgraded from **exact string matching** to **intelligent semantic understanding** using Azure OpenAI classification.

---

## 🎯 Key Improvements

### **1. Semantic Query Classification**
- ✅ Queries are now classified by LLM into: `company_info`, `inventory`, or `unknown`
- ✅ No more rigid exact phrase matching
- ✅ Natural language understanding

### **2. Structured Company Metadata**
- ✅ Company information stored in structured dictionary
- ✅ Easy to maintain and update
- ✅ Consistent responses

### **3. Intelligent Company Response Generator**
- ✅ Understands intent behind questions
- ✅ Returns specific or general information as needed
- ✅ UK English formatting

### **4. Environment Variable Loading**
- ✅ Azure OpenAI keys now loaded from `.env` file
- ✅ No need to set environment variables in PowerShell each time
- ✅ More secure and convenient

---

## 📋 Enhanced Query Handling

### **Before (Exact Matching):**
```
User: what is the company name
Bot: I'm sorry, I cannot answer your query at the moment.
```

### **After (Semantic Matching):**
```
User: what is the company name
Bot: TechGear UK

User: tell me about techgear
Bot: TechGear UK is located at 124 High Street, London, EC1A 1BB. We are open Monday to Friday, 09:00 - 18:00. Saturday, 10:00 - 16:00. For support, contact support@techgear.co.uk or 020 7946 0000.

User: where are you located
Bot: 124 High Street, London, EC1A 1BB

User: contact details
Bot: Support can be reached at support@techgear.co.uk or 020 7946 0000.
```

---

## 🏗️ Architecture Changes

### **Enhanced Three-Tier System:**

```
User Query
    ↓
[LLM Classification]
    ↓
┌───────────────────────────────────────┐
│ Classification Result:                │
│ - company_info                        │
│ - inventory                           │
│ - unknown                             │
└───────────────────────────────────────┘
    ↓
┌─────────────────┬──────────────────┬──────────────┐
│                 │                  │              │
│ company_info    │   inventory      │   unknown    │
│      ↓          │       ↓          │      ↓       │
│  [TIER 1]       │   [TIER 2]       │  [TIER 3]    │
│  KB Service     │   Inventory DB   │  Fallback    │
│  (Semantic)     │   (Tool Call)    │              │
└─────────────────┴──────────────────┴──────────────┘
```

---

## 📝 Files Modified

### **1. config.py**
**Change:** Added `python-dotenv` loading
```python
from dotenv import load_dotenv
load_dotenv()  # Automatically loads .env file
```

### **2. services/kb_service.py** (Complete Rewrite)
**Changes:**
- ✅ Removed exact string matching
- ✅ Added structured `company_data` dictionary
- ✅ Added `_classify_company_query()` for semantic classification
- ✅ Added `_generate_company_response()` for intelligent responses
- ✅ Integrated Azure OpenAI for classification

**Key Features:**
- Classifies queries into: `company_name`, `location`, `office_hours`, `delivery_policy`, `returns`, `contact`, `general_info`
- Returns specific information for targeted queries
- Returns comprehensive summary for broad queries

### **3. services/llm_service.py** (Enhanced)
**Changes:**
- ✅ Added `classify_query()` method for high-level classification
- ✅ Improved system prompts for better classification
- ✅ Maintains existing `should_use_inventory()` for tool calling

**Key Features:**
- Two-level classification system:
  1. High-level: `company_info`, `inventory`, `unknown`
  2. Company-level: Specific company information types

### **4. services/router.py** (Enhanced)
**Changes:**
- ✅ Now uses LLM classification before routing
- ✅ Routes to KB service only for `company_info`
- ✅ Routes to inventory service only for `inventory`
- ✅ Returns fallback for `unknown`

**Key Features:**
- Intelligent routing based on query intent
- Clear separation of concerns
- Maintains three-tier architecture

---

## 🔧 Structured Company Data

Located in `services/kb_service.py`:

```python
self.company_data = {
    "company_name": "TechGear UK",
    "location": "124 High Street, London, EC1A 1BB",
    "office_hours": "Monday to Friday, 09:00 - 18:00. Saturday, 10:00 - 16:00.",
    "delivery_policy": "Standard delivery takes 3-5 working days. Next-day delivery is available for £5.99.",
    "returns": "Items can be returned within 30 days of purchase with a valid receipt.",
    "contact": "Support can be reached at support@techgear.co.uk or 020 7946 0000."
}
```

**To update company information:**
1. Open `services/kb_service.py`
2. Modify the `company_data` dictionary
3. Save the file
4. Restart the application

---

## 🎯 Query Examples

### **Company Name Queries:**
```
✅ "what is the company name"
✅ "what is techgear uk"
✅ "company name"
✅ "who are you"
→ Response: "TechGear UK"
```

### **Location Queries:**
```
✅ "where are you located"
✅ "what is the office address"
✅ "company location"
✅ "address"
→ Response: "124 High Street, London, EC1A 1BB"
```

### **Office Hours Queries:**
```
✅ "when do you open on Monday"
✅ "office timings"
✅ "opening hours"
✅ "what time do you close"
→ Response: "Monday to Friday, 09:00 - 18:00. Saturday, 10:00 - 16:00."
```

### **Contact Queries:**
```
✅ "contact details"
✅ "how do I reach you"
✅ "phone number"
✅ "email address"
→ Response: "Support can be reached at support@techgear.co.uk or 020 7946 0000."
```

### **General Company Queries:**
```
✅ "tell me about techgear"
✅ "about the company"
✅ "company data"
✅ "company information"
→ Response: "TechGear UK is located at 124 High Street, London, EC1A 1BB. 
            We are open Monday to Friday, 09:00 - 18:00. Saturday, 10:00 - 16:00. 
            For support, contact support@techgear.co.uk or 020 7946 0000."
```

### **Inventory Queries (Unchanged):**
```
✅ "Is the Waterproof Commuter Jacket available in XL?"
→ Response: "Yes (3 in stock)"

✅ "What is the price of the Dry-Fit Running Tee?"
→ Response: "£25.00"
```

### **Fallback Queries:**
```
✅ "What is the capital of France?"
✅ "Can I have a discount code?"
→ Response: "I'm sorry, I cannot answer your query at the moment."
```

---

## 🔑 Environment Variables (.env File)

### **Setup:**

1. **Edit the `.env` file** in the project root:
   ```env
   AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
   AZURE_OPENAI_KEY=your-actual-key-here
   AZURE_API_VERSION=2024-02-15-preview
   AZURE_DEPLOYMENT_NAME=gpt-4o-mini
   ```

2. **Save the file**

3. **Run the application:**
   ```powershell
   python main.py
   ```

**No need to set environment variables in PowerShell anymore!**

---

## 🚀 How to Run (Updated)

### **Step 1: Activate Virtual Environment**
```powershell
cd C:\GCO\GCOFeb26Chatbot
.\venv\Scripts\Activate.ps1
```

### **Step 2: Edit .env File**
```powershell
notepad .env
```
Add your Azure OpenAI credentials and save.

### **Step 3: Run the Application**
```powershell
python main.py
```

**That's it!** The app will automatically load credentials from `.env`.

---

## 🧪 Testing the Enhancements

### **Test Company Information:**
```
User: what is the company name
Expected: TechGear UK

User: tell me about techgear
Expected: [Full company summary]

User: where are you located
Expected: 124 High Street, London, EC1A 1BB

User: contact details
Expected: Support can be reached at support@techgear.co.uk or 020 7946 0000.

User: office timings
Expected: Monday to Friday, 09:00 - 18:00. Saturday, 10:00 - 16:00.
```

### **Test Inventory (Should Still Work):**
```
User: Is the Waterproof Commuter Jacket available in XL?
Expected: Yes (3 in stock)

User: What is the price of the Dry-Fit Running Tee?
Expected: £25.00
```

### **Test Fallback:**
```
User: What is the capital of France?
Expected: I'm sorry, I cannot answer your query at the moment.
```

---

## 🔍 How It Works

### **1. Query Classification (Router)**
```python
classification = self.llm_service.classify_query(query)
# Returns: 'company_info', 'inventory', or 'unknown'
```

### **2. Company Info Handling (KB Service)**
```python
if classification == "company_info":
    # Classify specific company info type
    kb_classification = self._classify_company_query(query)
    # Returns: 'company_name', 'location', 'office_hours', etc.
    
    # Generate appropriate response
    response = self._generate_company_response(kb_classification, query)
```

### **3. Inventory Handling (Inventory Service)**
```python
elif classification == "inventory":
    # Use tool calling to extract parameters
    function_call = self.llm_service.should_use_inventory(query)
    
    # Query database with extracted parameters
    response = self.inventory_service.get_inventory(
        item_name=item_name,
        size=size,
        intent=intent
    )
```

### **4. Fallback**
```python
# If classification is 'unknown' or no valid response
return config.FALLBACK_MESSAGE
```

---

## ✅ What Stays the Same

- ✅ Three-tier architecture maintained
- ✅ Inventory queries work exactly as before
- ✅ Fallback behavior unchanged
- ✅ CLI interface unchanged
- ✅ Database structure unchanged
- ✅ Project structure unchanged
- ✅ UK English formatting maintained
- ✅ GBP currency formatting maintained

---

## 🎓 Benefits

### **1. Better User Experience**
- Natural language understanding
- Handles variations in phrasing
- More flexible query handling

### **2. Easier Maintenance**
- Structured company data
- Easy to update information
- Clear separation of concerns

### **3. Scalability**
- Easy to add new company information fields
- Easy to extend classification categories
- Modular design

### **4. Security**
- Credentials in `.env` file (not in code)
- `.env` file ignored by Git
- Environment-based configuration

---

## 📊 Comparison

| Feature | Before | After |
|---------|--------|-------|
| **Matching** | Exact string matching | Semantic LLM classification |
| **Company Queries** | Very limited | Broad and flexible |
| **Data Structure** | Hardcoded key-value pairs | Structured metadata |
| **Response Generation** | Static lookup | Intelligent generation |
| **Environment Setup** | PowerShell commands | `.env` file |
| **Flexibility** | Low | High |
| **Maintainability** | Difficult | Easy |

---

## 🔧 Troubleshooting

### **Issue: "Classification not working"**
**Solution:** Ensure `.env` file has correct Azure OpenAI credentials

### **Issue: "Company queries return fallback"**
**Solution:** Check that Azure OpenAI endpoint is accessible

### **Issue: "Environment variables not loading"**
**Solution:** Ensure `python-dotenv` is installed: `pip install python-dotenv`

---

## 📝 Summary

### **Enhanced Features:**
✅ Semantic query classification using Azure OpenAI  
✅ Structured company metadata dictionary  
✅ Intelligent company response generation  
✅ Broad query support (company name, about, location, etc.)  
✅ `.env` file support for credentials  
✅ Maintains three-tier architecture  
✅ Inventory queries unchanged  
✅ Fallback behavior unchanged  

### **Files Modified:**
- `config.py` - Added dotenv loading
- `services/kb_service.py` - Complete rewrite with semantic matching
- `services/llm_service.py` - Added classification method
- `services/router.py` - Enhanced with classification-based routing

### **New Files:**
- `.env` - Environment variables (add your credentials here)

---

**The chatbot is now more intelligent and user-friendly! 🎉**
