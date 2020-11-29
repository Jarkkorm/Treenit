from app import app
from db import db
from flask import render_template, url_for, request, redirect
import plan, users, exercise, routine

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/login', methods=["GET","POST"])
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

@app.route('/logout')
def logout():
    users.logout()
    return redirect("/")

@app.route('/register', methods=["get","post"])
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

@app.route('/newplan')
def newplan():
    return render_template("addplan.html")

@app.route('/newexercise')
def newexercise():
    list = exercise.get_list()
    return render_template("addexercise.html", exercises=list)

@app.route('/addplan', methods=["post"])
def addplan():
    name = request.form["name"]
    duration = request.form["duration"]
    planid = plan.new_plan(name, duration)
    if planid > -1:
        return redirect("/plan")
    else:
        return render_template("error.html",message="Suunnitelman luominen ei onnistunut")

@app.route('/addexercise', methods=["post"])
def addexercise():
    name = request.form["name"]
    description = request.form["description"]
    if exercise.new_exercise(name, description):
        return redirect("/newexercise")
    else:
        return render_template("error.html",message="Harjoitteen luominen ei onnistunut")

@app.route('/plan')
def show():
    list = plan.get_list()
    return render_template("plans.html", plans=list)

@app.route('/plan/<int:id>',methods=["GET","POST"])
def showplan(id):
    if request.method == "POST":
        reps = request.form["reps"]
        sets = request.form["sets"]
        quantity = request.form["quantity"]
        exercise_id = request.form["exercise"]
        routine.new_routine(exercise_id, id, sets, reps, quantity)
    title = plan.get_title(id)
    routines = routine.get_routines(id)
    exercises = exercise.get_list()
    return render_template("plan.html", title=title, routines = routines, exercises = exercises, id = id)