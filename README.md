# 📝 Offer Letter PDF Generator (Flask + Python)

This project is a web-based application that generates personalized internship offer letters as PDF files, on-the-fly, using user input submitted via a form.

## 🚀 Features

- 📄 On-the-fly PDF generation (no server-side saving)
- 🧾 Collects input: Name, College, Domain, Duration, Start Date
- ⚙️ Built using Python Flask
- 🖨️ PDF generated using ReportLab
- 📥 Instantly downloads PDF via browser

## 🛠 Technologies Used

- Python 3
- Flask (for web server and form handling)
- ReportLab (for PDF generation)
- HTML Form (rendered using Flask)
- BytesIO (for memory buffer)

## 🎯 Use Case

Ideal for:
- Internship portals
- Certificate/Offer Letter auto-generation
- Backend microservices needing dynamic document generation

## 💡 How It Works

1. User fills the form at `/` route
2. Flask sends data to `/generate` route via POST
3. ReportLab dynamically creates the PDF in memory
4. Flask returns the PDF as a downloadable response

## ▶️ Getting Started

### 1. Install dependencies

```bash
pip install flask reportlab
```

### 2. Run the server

```bash
python Offer_Letter_PDF_Generator_Flask.py
```

### 3. Open in browser

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 📁 Files

- `Offer_Letter_PDF_Generator_Flask.py` - Main Flask app
- `Mukesh_Offer_Letter_Generator_Project.pptx` - Presentation for project submission

---

✅ Developed by **Mukesh** as part of the Micro IT Internship program.
