
# 📊 TenderIQ

AI-powered system for automated government tender evaluation.

TenderIQ helps streamline tender scrutiny by:

- Extracting eligibility criteria from tender documents
- Parsing bidder submissions (PDFs, scanned documents, images, text)
- Matching bidder data against tender requirements
- Producing explainable and auditable evaluation decisions

---

# 🚀 Features

✅ Eligibility criteria extraction from tender documents  
✅ OCR support for scanned PDFs and images  
✅ AI + rule-based bidder evaluation  
✅ Explainable criterion-wise decision making  
✅ Confidence-aware fallback handling  
✅ Streamlit frontend + FastAPI backend  
✅ Risk summary and evidence generation  

---

# 🧾 Tech Stack

- **Frontend:** Streamlit
- **Backend:** FastAPI
- **OCR:** Tesseract OCR
- **PDF Parsing:** PyMuPDF
- **Language:** Python 3.10+

---

# ⚙️ Prerequisites

## ✅ Python

Install Python version **3.10 or above**

Verify installation:

```bash
python --version
````

---

## ✅ Tesseract OCR

TenderIQ uses Tesseract for OCR on scanned documents and images.

### Windows Installation

Download and install Tesseract OCR  
(UB Mannheim build recommended)

After installation, add Tesseract to your system PATH.

Example path:

```text
C:\Program Files\Tesseract-OCR
```

Verify installation:

```bash
tesseract --version
```

---

# 📦 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Yamini-29/TenderIQ/
cd TenderIQ
```

---

## 2️⃣ Install Dependencies

If `requirements.txt` exists:

```bash
pip install -r requirements.txt
```

If not, install manually:

```bash
pip install fastapi uvicorn streamlit requests pillow pytesseract pymupdf
```

---

# 🚀 Running the Application

## 1️⃣ Start the Backend (FastAPI)

Run:

```bash
uvicorn main:app --reload
```

Backend will start at:

```text
http://127.0.0.1:8000
```

---

## 2️⃣ Start the Frontend (Streamlit)

Open a **new terminal** and run:

```bash
streamlit run ui.py
```

Frontend will start at:

```text
http://localhost:8501
```

---

# 🌐 Access the Application

Open the following URL in your browser:

```text
http://localhost:8501
```

---

# 🧪 How to Use

## Upload Documents

Upload:

- Tender document  
    (PDF / Image / Text)
    
- Bidder document  
    (PDF / Image / Text)
    

---

## Run Evaluation

Click:

```text
🚀 Evaluate
```

---

# 📊 Output Includes

The system generates:

- 🏁 Overall Result
    
    - Eligible
        
    - Not Eligible
        
    - Needs Review
        
- 📋 Extracted Eligibility Criteria
    
- 📊 Criterion-wise Evaluation
    
- 🔍 Supporting Evidence
    
    - Extracted values
        
    - Required values
        
    - Reasoning
        
- ⚠️ Risk Summary
    

---

# 🧠 System Workflow

```text
Tender Document
       ↓
Criteria Extraction
       ↓
Bidder Document Parsing
       ↓
OCR + AI Extraction
       ↓
Rule-Based Matching
       ↓
Explainable Evaluation
       ↓
Final Eligibility Decision
```

---

# ⚠️ Common Issues

## ❌ Backend Not Responding

Ensure FastAPI backend is running:

```bash
uvicorn main:app --reload
```

---

## ❌ OCR Not Working

Verify Tesseract installation:

```bash
tesseract --version
```

Also ensure Tesseract is added to PATH.

---

## ❌ Empty or Incorrect Extraction

Try:

- Higher resolution scans
    
- Clearer images
    
- Better quality PDFs
    

---

# 📁 Supported File Types

TenderIQ supports:

✅ PDFs  
✅ Scanned documents  
✅ Images  
✅ Plain text files

---

# 🔒 Reliability Features

TenderIQ includes:

- Confidence-aware extraction
    
- Explainable reasoning
    
- Evidence-backed decisions
    
- Human-review fallback for uncertain cases
    

---

# 🏁 Final Checklist

Before running the application:

-  Backend running
    
-  Frontend running
    
-  Tesseract installed
    
-  Tesseract added to PATH
    
-  Test documents ready
    
