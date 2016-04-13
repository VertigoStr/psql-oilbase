# psql-oilbase

psql-oilbase is a simple site that was made on django 1.8 with PostgreSQL.

# Install
- Install [PostgreSQL](http://www.postgresql.org/download/)
- Install [Python](https://www.python.org/downloads/)
- Create virual enviroment: 
    - python -m venv myvenv
- Install Django: 
    - run virtual enviroment
    - pip install django==1.8
- Install psycopg2:
    - pip install psycopg2
    
# Prepare to run
- Create a database in PostgreSQL
- Make migrations: 
    - python manage.py migrate
- Load content of the site from dump: 
    - python manage.py loaddata db.json
    
# Run
- python manage.py runserver
