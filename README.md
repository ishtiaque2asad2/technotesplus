# Tech notes plus
Replication process for Tech Notes Plus(tested on ubuntu 20.04)

#Note
### Please make sure git and python 3.8 or above is installed

###Step 1: Create a virtualenv
###Step 2: From terminal go to the folder(technoteplus)
###Step 3: Activate the virtualenv
###Step 4: Run "pip install -r requirement.txt"
###Step 5: Run "python manage.py makemigrations"
###Step 6: Run "python manage.py migrate"
###Step 7: Run "python manage.py create_user_groups"
###Step 8: Run "python manage.py create_super_user" to create a superuser "admin" with password "admin"

###Step 9 Run "python manage.py create_dummy_users" to create the following dummy users
####1. Whitney Tucker (username: whitney, password: whitney, email: whitney@technoteplus.com)
####2. Scott Hampton (username: scott, password: scott,scott@technoteplus.com)
###Step 10 Run "python manage.py create_tags"
###Step 11 Run "python manage.py runserver"