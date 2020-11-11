from app import app
from flask import render_template, request, redirect
import plan, users, exercise

@app.route("/")
def index():
	list = plan.get_list()
	return render_template("index.html", count=len(list), plan=list)

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username,password):
            return redirect("/plan")
        else:
            return render_template("error.html",message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["get","post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Rekisteröinti ei onnistunut")

@app.route("/newplan")
def new():
    list = exercise.get_list()
    return render_template("addplan.html", exercises=list)

@app.route("/addplan", methods=["post"])
def addplan():
    name = request.form["name"]
    duration = request.form["duration"]
    if plan.new_plan(name, duration):
        return redirect("/plan")
    else:
        return render_template("error.html",message="Suunnitelman luominen ei onnistunut")

@app.route('/plan')
def show():
    list = plan.get_list()
    return render_template("plan.html", plans=list)