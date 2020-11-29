from db import db
import users, exercise

def get_list():
	user_id = users.user_id()
	sql = "SELECT P.id, P.name, P.duration FROM plan P, users U " \
		"WHERE P.user_id=U.id AND U.id=:user_id"
	result = db.session.execute(sql, {"user_id":user_id})
	return result.fetchall()

def new_plan(name, duration):
    user_id = users.user_id()
    if user_id == 0:
        return -1
    sql = "INSERT INTO plan (name, duration, user_id) VALUES (:name, :duration, :user_id) RETURNING id"
    result = db.session.execute(sql, {"name":name, "duration":duration, "user_id":user_id})
    plan_id = result.fetchone()[0]
    db.session.commit()
    return plan_id

def get_title(id):
    sql = "SELECT name FROM plan WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    title = result.fetchone()[0]
    return title