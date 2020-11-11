from db import db
import users

def get_list():
	sql = "SELECT E.description FROM excercise_plan E, users U " \
		"WHERE E.user_id=U.id "
	result = db.session.execute(sql)
	return result.fetchall()

def new_plan(description):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO excercise_plan (description, user_id) VALUES (:description, :user_id)"
    db.session.execute(sql, {"description":description, "user_id":user_id})
    db.session.commit()
    return True