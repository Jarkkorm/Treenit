CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT);
CREATE TABLE plan (id SERIAL PRIMARY KEY, name TEXT, duration TEXT, user_id INTEGER REFERENCES user); 
CREATE TABLE exercise_plan (id SERIAL PRIMARY KEY, exercise_id INTEGER REFERENCES exercise, plan_id INTEGER REFERENCES plan, reps INTEGER, sets INTEGER, quantity TEXT);
CREATE TABLE exercise (id SERIAL PRIMARY KEY, name TEXT, description TEXT);
CREATE TABLE history ( user_id INTEGER REFERENCES users, order INTEGER, reps INTEGER, sets INTEGER, quantity TEXT, name TEXT, description TEXT);