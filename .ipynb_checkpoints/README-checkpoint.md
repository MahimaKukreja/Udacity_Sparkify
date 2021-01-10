Introduction

A startup called Sparkify want to analyze their user activity and songs data from their new music streaming app. They want to understand the user song listening behaviour. The aim is to create a database schema using postgres and ETL pipeline so that this song play analysis can be done

Project Description

In this project, we have to create a datamodel with Postgres and build ETL pipeline using Python. The datamodel will constitute the facts and dimensions. These facts and dimensions will be populated by files located in two local directories using Python and SQL.

Database Schema Design:

Fact Table-

songplays records from log data 

Dimension Tables-

users in the app

songs in music database

artists in music database

timestamps of records

ETL design:

ETL pipeline includes reading and parsing of Json files and storing the parsed data into the corresponding tables columns with proper format

