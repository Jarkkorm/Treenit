from db import db
from datetime import datetime
import users

def new_routine(exercise, plan, sets, reps, quantity):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO exercise_plan (exercise_id, plan_id, reps, sets, quantity) VALUES (:exercise_id, :plan_id, :reps, :sets, :quantity)"
    db.session.execute(sql, {"exercise_id":exercise, "plan_id":plan, "reps":reps, "sets":sets, "quantity":quantity})
    db.session.commit()
    return True

def get_routines(id):
    sql = "SELECT E.id, E.reps, E.sets, E.quantity, X.name FROM exercise_plan E, exercise X WHERE E.exercise_id = X.id AND plan_id = :id"
    result = db.session.execute(sql, {"id":id})
    routines = result.fetchall()
    return routines

def save_routine(routines):
    user_id = users.user_id()
    for routine in routines:
        sql = "INSERT INTO history (date, exercise_plan_id) VALUES (:date, :exercise_plan_id)"
        db.session.execute(sql, {"date":datetime.utcnow(), "exercise_plan_id":routine.id})
        db.session.commit()
    return True