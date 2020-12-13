CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT);
CREATE TABLE plan (id SERIAL PRIMARY KEY, name TEXT, duration TEXT, user_id INTEGER REFERENCES user, visible INTEGER); 
CREATE TABLE exercise_plan (id SERIAL PRIMARY KEY, exercise_id INTEGER REFERENCES exercise, plan_id INTEGER REFERENCES plan, reps INTEGER, sets INTEGER, quantity TEXT);
CREATE TABLE exercise (id SERIAL PRIMARY KEY, name TEXT, description TEXT);
CREATE TABLE history (date DATETIME, exercise_plan_id INTEGER REFERENCES exercise_plan);