from flask import Flask, render_template, request
from jsonreading import extract_json

app = Flask(__name__)

@app.route("/")
def hello():
    message = "Hi!"
    return render_template("hello.html", message=message)

@app.route("/data/<user_number>")
def data(user_number):
    raw_data = extract_json()
    users = raw_data ["users"]
    current_user = users[int(user_number)]
    # return str(current_user)
    name = str(current_user['name'])
    address = str(current_user['address'])
    phone = str(current_user['phone'])
    return render_template("userprofile.html", name=name, address=address, phone=phone)




app.run(debug=True)

