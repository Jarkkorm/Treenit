from app import app
from db import db
from flask import render_template, url_for, request, redirect, flash
from forms import RegistrationForm, LoginForm, AddExerciseForm, AddRoutineForm, AddToHistoryForm, AddPlanForm, DeletePlanForm
import plan, users, exercise, routine, forms, plan, history

@app.route('/', methods=["GET","POST"])
def index():
    if users.user_id():
        return redirect('/plan')
    form = LoginForm(request.form)
    if form.validate_on_submit():
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/plan")
        else:
            flash("Väärä käyttäjätunnus tai salasana")
            return render_template("login.html", form=form)
    return render_template("login.html", form = form)

@app.route('/logout')
def logout():
    users.logout()
    return redirect("/")

@app.route('/register', methods=["GET","POST"])
def register():
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username,password):
            return redirect("/")
        else:
            flash("Käyttäjänimi on varattu")
            return render_template("register.html", form=form)
    return render_template("register.html", form=form)

@app.route('/addplan', methods=["GET","POST"])
def addplan():
    form = AddPlanForm(request.form)
    if form.validate_on_submit():
        name = request.form["name"]
        duration = request.form["duration"]
        if plan.new_plan(name, duration):
            return redirect("/plan")
        else:
            return render_template("error.html",message="Suunnitelman luominen ei onnistunut")
    return render_template("addplan.html", form=form)

@app.route('/addexercise', methods=["GET","POST"])
def addexercise():
    form = AddExerciseForm(request.form)
    if form.validate_on_submit():
        name = request.form["name"]
        description = request.form["description"]
        if exercise.new_exercise(name, description):
            return redirect("/newexercise")
        else:
            return render_template("error.html",message="Harjoitteen luominen ei onnistunut")
    return render_template("addexercise.html", exercises=list, form=form)

@app.route('/addroutine/<int:id>', methods=["GET","POST"])
def addroutine(id):
    planid=id
    exercise_list = exercise.get_list()
    exercises = [(i.id, i.name) for i in exercise_list]
    form = AddRoutineForm(request.form)
    form.exercise.choices = exercises
    if form.validate_on_submit():
        reps = request.form["reps"]
        sets = request.form["sets"]
        quantity = request.form["quantity"]
        selectedExercise = request.form["exercise"]
        if routine.new_routine(selectedExercise, id, sets, reps, quantity):
            return redirect('/plan')
        else:
            return render_template("error.html", message="Harjoitteen luominen ei onnistunut")
    return render_template("addroutine.html", id = id, form = form )

@app.route('/plan')
def show():
    list = plan.get_list()
    return render_template("plans.html", plans=list)

@app.route('/plan/<int:id>', methods=["GET","POST"])
def showplan(id):
    form = AddToHistoryForm(request.form)
    title = plan.get_title(id)
    routines = routine.get_routines(id)
    if form.validate_on_submit():
        routine.save_routine(routines)
    return render_template("plan.html", title=title, routines = routines, id = id, form = form )

@app.route('/exercises', methods=["GET","POST"])
def showexercises():
    form = AddExerciseForm(request.form)
    exercises = exercise.get_list()
    if form.validate_on_submit():
        name = request.form["name"]
        description = request.form["description"]
        if exercise.new_exercise(name, description):
            return redirect('/exercises')
        else:
            return render_template("error.html",message="Liikkeen luominen ei onnistunut")
    return render_template("exercises.html", form=form, exercises=exercises)

@app.route('/history')
def gethistory():
    histories = history.get_history()
    return render_template("history.html", histories=histories)
