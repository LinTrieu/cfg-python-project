from flask import Flask, render_template, request
from jsonreading import extract_json

app = Flask(__name__)

@app.route("/")
def hello():
    message = "Welcome to Doyenne"
    return render_template("index.html", message=message)

@app.route("/data")
def data():
    raw_data = extract_json()
    current_user = str(raw_data ["users"][0])
    return render_template("userprofile.html", current_user=current_user)

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result)

app.run(debug=True)
