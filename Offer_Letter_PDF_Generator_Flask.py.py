# Required modules:
# pip install flask reportlab

from flask import Flask, request, send_file, render_template_string
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO
from datetime import datetime

app = Flask(__name__)

# Simple HTML form for input
HTML_FORM = '''
<!DOCTYPE html>
<html>
<head>
    <title>Offer Letter Generator</title>
</head>
<body>
    <h2>Internship Offer Letter Generator</h2>
    <form method="POST" action="/generate">
        Name: <input type="text" name="name" required><br><br>
        College: <input type="text" name="college" required><br><br>
        Domain: <input type="text" name="domain" required><br><br>
        Duration (in weeks): <input type="text" name="duration" required><br><br>
        Start Date: <input type="date" name="start_date" required><br><br>
        <button type="submit">Generate PDF</button>
    </form>
</body>
</html>
'''

@app.route("/", methods=["GET"])
def index():
    return render_template_string(HTML_FORM)

@app.route("/generate", methods=["POST"])
def generate_pdf():
    name = request.form["name"]
    college = request.form["college"]
    domain = request.form["domain"]
    duration = request.form["duration"]
    start_date = request.form["start_date"]
    issue_date = datetime.today().strftime("%Y-%m-%d")

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Header
    p.setFont("Helvetica-Bold", 16)
    p.drawString(180, 800, "Internship Offer Letter")

    # Content
    p.setFont("Helvetica", 12)
    text_lines = [
        f"Date of Issue: {issue_date}",
        "",
        f"Dear {name},",
        "",
        f"We are pleased to offer you an internship in the domain of '{domain}' at Micro Information Technology Services (MITS).",
        f"You will be representing your college '{college}' for this internship program.",
        f"The duration of the internship is {duration} weeks, starting from {start_date}.",
        "",
        "You are expected to follow the guidelines provided and contribute sincerely.",
        "We hope this internship will enhance your skills and industry exposure.",
        "",
        "Best wishes for your internship journey.",
        "",
        "Sincerely,",
        "MITS Internship Team"
    ]

    y = 750
    for line in text_lines:
        p.drawString(70, y, line)
        y -= 20

    p.showPage()
    p.save()
    buffer.seek(0)

    return send_file(buffer, as_attachment=True,
                     download_name=f"Offer_Letter_{name.replace(' ', '_')}.pdf",
                     mimetype='application/pdf')

if __name__ == "__main__":
    app.run(debug=True)
