from db import db
import users

def get_list():
	user_id = users.user_id()
	sql = "SELECT E.name FROM exercise E"
	result = db.session.execute(sql)
	return result.fetchall()