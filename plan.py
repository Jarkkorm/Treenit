from db import db
import users, exercise

def get_list():
	user_id = users.user_id()
	sql = "SELECT P.name, P.duration FROM plan P, users U " \
		"WHERE P.user_id=U.id AND U.id=:user_id"
	result = db.session.execute(sql, {"user_id":user_id})
	return result.fetchall()

def new_plan(name, duration):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO plan (name, duration, user_id) VALUES (:name, :duration, :user_id)"
    db.session.execute(sql, {"name":name, "duration":duration, "user_id":user_id})
    db.session.commit()
    return True