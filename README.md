

Lesson 2 : Data Modelling with Postgres
-

**Project Description**

In this project, you'll apply what you've learned on data modeling with Postgres
and build an ETL pipeline using Python. To complete the project,
you will need to define fact and dimension tables for a star schema for a particular analytic focus,
and write an ETL pipeline that transfers data from files in two local directories into these tables
in Postgres using Python and SQL.

**Song dataset**

The first dataset  is a subset of real data from the Million Song Dataset.
Each file is in JSON format and contains metadata about a song and the artist of that song.
The files are partitioned by the first three letters

**Log dataset**

The second dataset consists of log files in JSON format generated by the event simulator
based on the songs in the dataset above.
These simulate activity logs from a music streaming app based on specified configurations.

**Star schema**

- Fact table : song plays
- Dimension Table: time, users, artists, songs.

![Star schema](https://github.com/Mustufain/Udacity-Data-Engineering/blob/master/Lesson2_Data_Modelling/Postgres_Data_Modelling/images/Untitled%20Diagram.png)

Instructions
-
- Setup your local postgres instance **CREATE ROLE student WITH LOGIN PASSWORD 'student';**
- Alter role **ALTER ROLE student CREATEDB;**
- Create database **CREATE DATABASE studentdb;**

- Create a new virtual environment **pyenv virtualenv 3.6.2 virtual-env**
- Activate virtual environment **pyenv activate virtual-env**
- Install requirements **pip install -r Lesson2_Data_Modelling/Postgres_Data_Modelling/requirements.txt**
- Create tables **python Lesson2_Data_Modelling/Postgres_Data_Modelling/create_tables.py**
- Run ETL pipeline **python Lesson2_Data_Modelling/Postgres_Data_Modelling/etl.py**
