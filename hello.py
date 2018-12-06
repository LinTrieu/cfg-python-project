from flask import Flask,render_template,request,json
from jsonreading import extract_json

app = Flask(__name__)

@app.route("/")
def hello():
   message = "Hi!"
   return render_template("hello.html", message=message)




@app.route('/confirmation')
def confirmation():
    with open("users.json", "r") as outfile:
        raw_data = json.load(outfile)
        print(raw_data)
    new_user = {
       "email": request.args.get('email'),
       "first_name": request.args.get('firstname'),
       "surname": request.args.get('lastname')
    }
    print(new_user)

    with open("users.json", "w+") as outfile:
        raw_data['users'].append(new_user)

        json.dump(raw_data, outfile,indent=4)
    return render_template('confirmation.html')

@app.route("/userprofile/<user_number>")
def data(user_number):
    raw_data = extract_json()
    users = raw_data ["users"]
    current_user = users[int(user_number)]
    # return str(current_user)
    email= str(current_user['email'])
    first_name = str(current_user['firstname'])
    surname = str(current_user['surname'])
    return render_template("userprofile.html", email=email, first_name=first_name, surname=surname)

app.run(debug=True)

