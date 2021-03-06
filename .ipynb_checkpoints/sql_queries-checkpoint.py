# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE if not exists songplays (songplay_id serial, start_time timestamp, user_id int, level text,\
song_id text, artist_id text, session_id int, location text, user_agent text)""")

user_table_create = ("""CREATE TABLE if not exists  users (user_id int, first_name text, last_name text,gender text,level text)""")

song_table_create = ("""CREATE TABLE if not exists  songs (song_id text, title text, artist_id text, year int,duration numeric)""")

artist_table_create = ("""CREATE TABLE if not exists  artists (artist_id text, name text, location text, latitude numeric,\
longitude numeric)""")

time_table_create = ("""CREATE TABLE if not exists  time (start_time timestamp, hour int, day int, week int, month int,\
year int, weekday int)""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays(songplay_id, start_time, user_id, level, song_id, artist_id, session_id,location, user_agent) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name,gender,level)\
values(%s,%s,%s,%s,%s)""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) values(%s,%s,%s,%s,%s)""")

artist_table_insert = ("""INSERT INTO artists (artist_id,name,location, latitude,longitude) values(%s,%s,%s,%s,%s)""")


time_table_insert = ("""INSERT INTO time (start_time, hour , day , week , month , year , weekday) values(%s,%s,%s,%s,%s,%s,%s)""")

# FIND SONGS

song_select = ("""
               SELECT songs.song_id, songs.artist_id FROM songs
               JOIN artists ON artists.artist_id=songs.artist_id
               WHERE (songs.title=%s AND artists.name=%s AND songs.duration=%s);
               """)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]