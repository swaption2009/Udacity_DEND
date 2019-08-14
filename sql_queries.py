# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("CREATE TABLE IF NOT EXISTS songplays (start_time BIGINT NOT NULL, \
                                                                user_id INTEGER NOT NULL, \
                                                                level VARCHAR(20) NOT NULL, \
                                                                song_id VARCHAR(20), \
                                                                artist_id VARCHAR(20),\
                                                                session_id INT, \
                                                                location VARCHAR, \
                                                                user_agent VARCHAR);")

user_table_create = ("CREATE TABLE IF NOT EXISTS users (user_id INTEGER NOT NULL PRIMARY KEY, \
                                                        first_name VARCHAR(20) NOT NULL, \
                                                        last_name VARCHAR(20) NOT NULL,\
                                                        gender VARCHAR(20) NOT NULL, \
                                                        level VARCHAR(20) NOT NULL);")

song_table_create = ("CREATE TABLE IF NOT EXISTS songs (song_id VARCHAR(20) NOT NULL PRIMARY KEY, \
                                                        title VARCHAR NOT NULL, \
                                                        artist_id VARCHAR(20) NOT NULL, \
                                                        year INTEGER, \
                                                        duration FLOAT);")

artist_table_create = ("CREATE TABLE IF NOT EXISTS artists (artist_id VARCHAR(20) NOT NULL PRIMARY KEY, \
                                                            artist_name VARCHAR NOT NULL, \
                                                            artist_location VARCHAR, \
                                                            artist_latitude FLOAT, \
                                                            artist_longitude FLOAT);")

time_table_create = ("CREATE TABLE IF NOT EXISTS time (timestamp INTEGER NOT NULL PRIMARY KEY, \
                                                       hour INTEGER NOT NULL, \
                                                       day INTEGER NOT NULL, \
                                                       weekofyear INTEGER NOT NULL, \
                                                       month INTEGER NOT NULL, \
                                                       year INTEGER NOT NULL, \
                                                       isoweekday INTEGER NOT NULL);")

# INSERT RECORDS

songplay_table_insert = ("INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, \
                          location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);")

user_table_insert = ("INSERT INTO users (user_id, first_name, last_name, gender, level) \
                      VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO NOTHING;")

song_table_insert = ("INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES(%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO NOTHING;")

artist_table_insert = ("INSERT INTO artists (artist_id, artist_name, artist_location, artist_latitude, artist_longitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING;")


time_table_insert = ("INSERT INTO time (timestamp, hour, day, weekofyear, month, year, isoweekday) VALUES (%s, %s, %s, %s, %s, %s, %s);")

# FIND SONGS

song_select = ("SELECT s.song_id, a.artist_id \
                FROM artists as a \
                JOIN songs AS s ON a.artist_id = s.artist_id \
                WHERE s.title=(%s) AND a.artist_name=(%s) AND s.duration=(%s)")


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]