find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate
python manage.py create_user_groups
python manage.py create_super_user
python manage.py create_dummy_users
python manage.py create_tags