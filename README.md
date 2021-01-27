Introduction

A startup called Sparkify want to analyze their user activity and songs data from their new music streaming app. They want to understand the user song listening behaviour. The aim is to create a database schema using postgres and ETL pipeline so that this song play analysis can be done

Project Description

In this project, we have to create a datamodel with Postgres and build ETL pipeline using Python. The datamodel will constitute the facts and dimensions. These facts and dimensions will be populated by files located in two local directories using Python and SQL.

Database Schema Design:

![Image of Sparkify Data Model](https://github.com/MahimaKukreja/Udacity_Sparkify/blob/main/Sparkify_App_Data%20Model.PNG)

Fact Table- SongPlays gives information about the songs that are played by the user in a particular session. It picks the data from log data

Dimension Tables- The dimensions include users, songs, artists and time table. 

a. The Users dimension gives information about users in the app

b. The songs dimension gives information about songs in music database

c. The artists dimension provides information about all the artists in music database

d. The time dimension include timestamps of records

ETL design:

ETL pipeline includes reading and parsing of Json files and storing the parsed data into the corresponding tables columns with proper format

Table creation script:

sql_queries.py is a script for dropping and creating the tables in the database SparkifyDB. The script - Create_tables.py imports functions (create_table_queries and drop_table_queries) written in sql_queries.py. 

In order to create tables and make connections to the databaase (sparkifydb), run ´python create_tables.py´ in a terminal


ETL Script
An ETL script (etl.py) automatically loops through the logs and songs directories, reads every file, transforms the data using Pandas, and insert them on the star-schema according to the tables defined.
 
