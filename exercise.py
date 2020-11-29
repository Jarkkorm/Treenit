from db import db
import users

def get_list():
	user_id = users.user_id()
	sql = "SELECT E.id, E.name FROM exercise E"
	result = db.session.execute(sql)
	return result.fetchall()

def new_exercise(name, description):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO exercise (name, description) VALUES (:name, :description)"
    db.session.execute(sql, {"name":name, "description":description})
    db.session.commit()
    return True