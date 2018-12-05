from flask import Flask,render_template,request,json

app = Flask(__name__)

@app.route("/")
def hello():
   message = "Welcome to Doyenne"
   return render_template("index.html", message=message)




@app.route('/confirmation', methods=["GET", "POST"])
def confirmation():
   data = {}

   data["users"] = []
   data["users"].append({
       "name": request.args.get('email'),
       "address": request.args.get('firstname'),
       "phone": request.args.get('lastname')
   })
   with open("users.json", "w") as write_file:
       json.dump(data, write_file)
   return render_template('/confirmation.html')


app.run(debug=True)

