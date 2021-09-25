# inCollege
For the inCollege app from team Michigan

*To use inCollege run
python inCollege.py

*We're using postgresql
Create database type:
CREATE DATABASE incollege;

Create table for users type:
CREATE TABLE auth (id SERIAL PRIMARY KEY, username VARCHAR(50) NOT NULL, password VARCHAR(50) NOT NULL, first_name VARCHAR(50) NOT NULL, last_name VARCHAR(50) NOT NULL);
CREATE TABLE jobs (id SERIAL PRIMARY KEY, title VARCHAR(50) NOT NULL, description VARCHAR(255) NOT NULL, employer VARCHAR(50) NOT NULL, location VARCHAR(50) NOT NULL, salary REAL);



*To set up your python 3 environment with the necessary libraries you'll need to install the packages in the requirements.txt
just look up 'psycopg2 install [inset your os]'