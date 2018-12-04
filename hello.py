from flask import Flask,render_template,request,json

app = Flask(__name__)

@app.route("/")
def hello():
   message = "Hi!"
   return render_template("hello.html", message=message)




@app.route('/confirmation')
def confirmation():
   data = {}

   data["users"] = []
   data["users"].append({
       "name": request.args.get('email'),
       "address": request.args.get('firstname'),
       "phone": request.args.get('lastname')
   })
   with open("users.json", "w") as outfile:
       json.dump(data, outfile)
   return render_template('confirmation.html')


app.run(debug=True)

