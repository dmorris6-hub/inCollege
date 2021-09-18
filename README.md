# inCollege
For the inCollege app from team Michigan

*We're using postgresql

Create database type:
CREATE DATABASE incollege;

Create table for users type:
CREATE TABLE auth (id SERIAL PRIMARY KEY, username VARCHAR(50) NOT NULL, password VARCHAR(50) NOT NULL);