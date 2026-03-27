from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Simple home page
@app.route("/")
def home():
    return render_template("index.html")

# Example form submission
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    return f"Hello, {name}! Your form was submitted successfully."

if __name__ == "__main__":
    app.run(debug=True)