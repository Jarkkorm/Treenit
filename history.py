from db import db
from datetime import datetime
import users

def get_history():
	user_id = users.user_id()
	sql = "SELECT H.date, L.name AS planname, E.name, P.reps, P.sets, P.quantity FROM history H, users U, exercise_plan P, exercise E , plan L " \
		"WHERE H.exercise_plan_id = P.id AND L.user_id = U.id AND P.exercise_id = E.id AND P.plan_id = L.id AND U.id=:user_id"
	result = db.session.execute(sql, {"user_id":user_id})
	return result.fetchall()