





from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/results", methods = ["POST"])
def result():
    pdf_file = request.files["file"]
    
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True , host='0.0.0.0', port= 3000)  