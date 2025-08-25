from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = "secureocr"
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        flash("No file uploaded")
        return redirect(url_for("index"))
    file = request.files["file"]
    if file.filename == "":
        flash("No selected file")
        return redirect(url_for("index"))
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    # Dummy OCR result (replace with Azure OCR API call)
    data = [f"OCR extracted text from {file.filename}"]
    return render_template("result.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
