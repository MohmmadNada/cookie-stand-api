## Overview
Let’s move our site closer to production grade by adding Permissions and Postgresql Database.
1. create demo link it in today directory 
2. run docker   and run `docker-compose up` and check the browser 
3. in case you face There isnt anything to compare when you make PR solve it by :: 
   1. git checkout [secondaryBRANCH]   
   2. git branch main [secondaryBRANCH] -f   
   3. git checkout main   
   4. git push origin main -f
## postgres part

note: docker-compose -up d => run the server and make the terminal not busy 
1. project => open setting => in database section Modify the defult
   1. engine must be postgres 
   2. add NAME ,USER, PASSWORD = postgres
   3. add 'HOST': 'db' and 'PORT': 5432,  > HOST MUST BE (the same in docker compse file)
2. Open docker-compose.yml file add new service the same name HOST in settings, add :
   1. image
   2. environment : with POSTGRES_DB, POSTGRES_USER and POSTGRES_PASSWORD

3. add psycopg2 `poetry add psycopg2` then
   1. psycopg2 is link postgres with python

>if you need to see error => do down then up without -d

4. export `poetry export -f requirements.txt -o requirements.txt` 
5. `docker-compose up --build`
> when we add poetry => export => --build 
6. `docker-compose run web python manage.py migrate`
6. reset the docker down to and up
7. `docker-compose run web python manage.py createsuperuser`
8. check now `docker-compose up`
## permission part
1. Go to project settings file => REST_FRAMEWORK => DEFAULT_PERMISSION_CLASSES => change AllowAny 
   * [check this link ](https://www.django-rest-framework.org/api-guide/permissions/)
2. docker-compose up check the api data , should now show, => go to admin and log in => check the data now , should be shown 
3. add user from admin and check Staff status box , until now any user admin can see and edit the data '
4. Go to app => add permissions.py => import and add class => go and check who can modify the object
5. add premissions in the app view =>import class from  permissions file
6. add it to page required => detail view =>  add permission_classes as tuple
