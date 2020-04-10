# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays(
    songplay_id SERIAL PRIMARY KEY,
    start_time timestamp,
    user_id int,
    level varchar, 
    song_id varchar,
    artist_id varchar,
    session_id int, 
    location varchar,
    user_agent varchar)
""")

user_table_create = ("""

    CREATE TABLE IF NOT EXISTS users(
    user_id int,
    first_name varchar, 
    last_name varchar, 
    gender varchar, 
    level varchar)
""")

song_table_create = ("""

    CREATE TABLE IF NOT EXISTS songs(
    song_id varchar,
    title varchar, 
    artist_id varchar,
    year int, 
    duration float)
""")

artist_table_create = ("""

    CREATE TABLE IF NOT EXISTS artists(
    artist_id varchar,
    name varchar,
    location varchar, 
    latitude float,
    longitude float)
""")

time_table_create = ("""

    CREATE TABLE IF NOT EXISTS time(
    start_time timestamp,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday int)

""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT into songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
values (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT into users (user_id, first_name, last_name, gender, level)
values (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""
INSERT into songs (song_id, title, artist_id, year, duration)
values (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""
INSERT into artists (artist_id, name, location, latitude, longitude)
values (%s, %s, %s, %s, %s)
""")


time_table_insert = ("""
INSERT into time (start_time, hour, day, week, month, year, weekday)
values (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS
# title, artist name, and duration of a song
song_select = ("""
SELECT s.song_id, a.artist_id FROM songs s 
INNER JOIN artists a on 
s.artist_id = a.artist_id
WHERE s.title = %s 
AND a.name = %s
AND s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]