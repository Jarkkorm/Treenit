from app import app
from db import db
from flask import render_template, url_for, request, redirect
from forms import RegistrationForm, LoginForm, AddExerciseForm
import plan, users, exercise, routine, forms

@app.route('/', methods=["GET","POST"])
def index():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/plan")
        else:
            return render_template("error.html",message="Väärä tunnus tai salasana")
    return render_template("login.html", form = form)

@app.route('/logout')
def logout():
    users.logout()
    return redirect("/")

@app.route('/register', methods=["GET","POST"])
def register():
    form = RegistrationForm(request.form)
    if form.validate():
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username,password):
            return redirect("/login")
        else:
            return render_template("error.html",message="Rekisteröinti ei onnistunut")
    return render_template('register.html', form=form)

@app.route('/addplan', methods=["GET","POST"])
def addplan():
    form = AddPlanForm(request.form)
    if form.validate():
        name = request.form["name"]
        duration = request.form["duration"]
        planid = plan.new_plan(name, duration)
        if planid > -1:
            return redirect("/plan")
        else:
            return render_template("error.html",message="Suunnitelman luominen ei onnistunut")
    return render_template("addplan.html", form=form)

@app.route('/newexercise', methods=["GET","POST"])
def addexercise():
    form = AddExerciseForm(request.form)
    if form.validate():
        name = request.form["name"]
        description = request.form["description"]
        if exercise.new_exercise(name, description):
            return redirect("/newexercise")
        else:
            return render_template("error.html",message="Harjoitteen luominen ei onnistunut")
    return render_template("addexercise.html", exercises=list, form=form)

@app.route('/plan')
def show():
    list = plan.get_list()
    return render_template("plans.html", plans=list)

@app.route('/plan/<int:id>',methods=["GET","POST"])
def showplan(id):
    title = plan.get_title(id)
    routines = routine.get_routines(id)
    exercise_list = exercise.get_list()
    exercises = [(i.id, i.name) for i in exercise_list]
    form = AddRoutineForm(request.form)
    form.exercise.choices = exercises
    if form.validate_on_submit():
        reps = request.form["reps"]
        sets = request.form["sets"]
        quantity = request.form["quantity"]
        selectedExercise = request.form["exercise"]
        routine.new_routine(selectedExercise, id, sets, reps, quantity)

    return render_template("plan.html", title=title, routines = routines, exercises = exercises, id = id, form = form, )