from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, validators, SubmitField, SelectField, IntegerField

class RegistrationForm(FlaskForm):
  username = StringField("Nimi", [validators.DataRequired(), validators.Length(min=4, max=25)])
  password = PasswordField("Salasana", [validators.DataRequired(), validators.Length(min=4, max=25)])
  submit = SubmitField("Luo tunnus")

class LoginForm(FlaskForm):
  username = StringField("Nimi", [validators.DataRequired(), validators.Length(min=4, max=25)])
  password = PasswordField("Salasana", [validators.DataRequired(), validators.Length(min=4, max=25)])
  submit = SubmitField("Kirjaudu")

class AddRoutineForm(FlaskForm):
  sets = IntegerField("Kierroksia", [validators.DataRequired(), validators.Length(min=4, max=25)])
  reps = IntegerField("Toistoja", [validators.DataRequired(), validators.Length(min=4, max=25)])
  quantity = StringField("Painot/aika", [validators.DataRequired(), validators.Length(min=4, max=25)])
  exercise = SelectField("Liike", coerce=int)
  submit = SubmitField("Tallenna")

class AddExerciseForm(FlaskForm):
  exercise = StringField("Treenin nimi", [validators.DataRequired(), validators.Length(min=4, max=25)])
  description = StringField("Treenin kuvaus", [validators.DataRequired(), validators.Length(min=4, max=25)])
  submit = SubmitField("Tallenna")

class AddPlanForm(FlaskForm):
  name = StringField("Suunnitelman nimi", [validators.DataRequired(), validators.Length(min=4, max=25)])
  duration = IntegerField("Pituus", [validators.DataRequired(), validators.Length(min=4, max=25)])
  submit = SubmitField("Tallenna")