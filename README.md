# inCollege
For the inCollege app from team Michigan

*We're using postgresql

Create database type:
CREATE DATABASE incollege;

Create table for users type:
CREATE TABLE auth (id SERIAL PRIMARY KEY, username VARCHAR(50) NOT NULL, password VARCHAR(50) NOT NULL);


*To set up your python 3 environment with the necessary libraries you'll need to install the packages in the requirements.txt
just look up 'psycopg2 install [inset your os]'