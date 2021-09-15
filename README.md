# Tech notes plus
Replication process for Tech Notes Plus(tested on ubuntu 20.04)

# Note
### Please make sure git and python 3.8 or above is installed

### Step 1: Create a virtualenv
### Step 2: From terminal go to the folder(technoteplus)
### Step 3: Activate the virtualenv
### Step 4: Run "pip install -r requirement.txt"
### Step 5: Run "python manage.py makemigrations"
### Step 6: Run "python manage.py migrate"
### Step 7: Run "python manage.py create_user_groups"
### Step 8: Run "python manage.py create_super_user" to create a superuser "admin" with password "admin"

### Step 9 Run "python manage.py create_dummy_users" to create the following dummy users
#### 1. Whitney Tucker (username: whitney, password: whitney, email: whitney@technoteplus.com)
#### 2. Scott Hampton (username: scott, password: scott,scott@technoteplus.com)
###S tep 10 Run "python manage.py create_tags"
### Step 11 Run "python manage.py runserver"
### Step 12 go to technoeplus_vue
### Step 13 type npm install
### Step 14 type npm run serve

#For Postman
#### All the API are inside the postman json file. Please make sure to add environment variable BASE_URL and set it to http://localhost:8000
#### Please add the following two lines in get token API
#### 1.var jsonData = JSON.parse(responseBody);
#### 2.postman.setEnvironmentVariable("TOKEN", jsonData.access);

#### Please add the environment variable TOKEN as well. This configuration will set the latest token everytime and will be used throughout all API