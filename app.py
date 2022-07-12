




from plumber import write_emails
from flask import Flask, render_template, request
import pdfplumber

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/results", methods = ["POST"])
def result():
    pdf_file = request.files["file"]
    emails = write_emails(pdf_file)
    return render_template('result.html', emails = emails)


if __name__ == '__main__':
    app.run(debug=True , host='0.0.0.0', port= 3000)  