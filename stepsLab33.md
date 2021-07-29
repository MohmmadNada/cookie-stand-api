## link with new repo 
1. create new repo 
2. run `git remote set-url origin <link>`
3. add commit and push 
## setup
1. run `poetry add djangorestframework_simplejwt`
2. Open docker-compose , change all 8000 to be 8002
3. Open settings.py , Add to REST_FRAMEWORK JWTAuthentication 
4. Open urls.py in project => import views from jwt => add path for token and refresh
5. run `poetry export -f requirements.txt -o requirements.txt`
6. run `docker-compose up --build`
## Get token
1. Go to postman site or desktop app 
2. add `http://localhost:8002/api/token/` as **post** for secuirty **not get **
   1. go to body then form  add  username and password then send
   2. open new tab , add link to show data `http://localhost:8002/api/v2/players`
      1. Authentication=> chose Bearer token and add your`s 
   3. open new tab ,**POST** add link to show data `http://localhost:8002/api/token/refresh/`=> body =>form => add key 'refresh' and your refresh token
3. open settings.py => REST_FRAMEWORK = >  DEFAULT_AUTHENTICATION_CLASSES add BasicAuthentication and SessionAuthentication
   1. for ability to use username and password to show data



## production mode wsgi :
1. Open docker-compose => change command to `gunicorn <projectnme>.wsgi:application --bind 0.0.0.0:8002 --workers 4`
2. run `poetry add gunicorn`
3. run `poetry export -f requirements.txt -o requirements.txt`
4. run `docker-compose up --build`
### setup CSS
Warning You will run into styling issues when you switch over to Gunicorn.
    * On Django side you’ll need to properly handle static files using Whitenoise
1. Open settings.py => STATIC_URL add:
   1. import os
   2. add STATIC_DIR 
   3. add STATIC_ROOT
   4. add STATICFILES_DIRS
2. add `'whitenoise.middleware.WhiteNoiseMiddleware',` to MIDDLEWARE
3. add `'whitenoise.runserver_nostatic',` to INSTALLED_APPS
4. run `poetry add whitenoise`
5. run `poetry export -f requirements.txt -o requirements.txt`
6. run `docker-compose up --build`
7. run `docker-compose run web python manage.py migrate`
8. run http://localhost:8000/
