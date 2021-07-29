## Setup 

### new file 
1. copy the files from lab 33 to new directory
2. check if it work fine by run `docker-compose up `
3. the files remote with repo lab 33 => delete it 
   1. show repo linked `git remote -v` 
   2. delete => `git remote rm [origin]`
### link with new repo 
4. create new repo and link it  
   1. `git remote add origin https://github.com/user/repo.git`
   2. `git remote -v`
### install backges and check  
5. add backges
   1. `poetry add django-environ` for variable 
   2. run `poetry add psycopg2-binary` for cloud database
6. export run `poetry export -f requirements.txt -o requirements.txt`
7. remove .venv folder that have all backges 
8. `poetry install` 
9. `docker-compose up` its work fine !!
10. `export run `poetry export -f requirements.txt -o requirements.txt`
### Variable section
1. touch .env inside project file **not in root** add this content [sample](https://github.com/codefellows/python-401-api-quickstart/blob/main/project/.env.sample)
2. touch .gitignore and add .env to it
3. Open project => settings.py 
   1. import **environ** 
   2. env = environ.Env(
    DEBUG = (bool, False)
)environ.Env.read_env()

    3. update settings.py to use values in .env
       1.  `SECRET_KEY = env.str('SECRET_KEY')`
       2.  `DEBUG = env.bool('DEBUG')`
       3.  ALLOWED_HOSTS = tuple(env.list('ALLOWED_HOSTS'))

    4. `export run `poetry export -f requirements.txt -o requirements.txt`
    5. `docker compose up --build` 
### before database
1. signin => username: mohammad => password: mohammad123456789
2. Let`s go to Postman
3. add http://localhost:8005/api/token/ => get access and refresh token
4. add http://localhost:8005/api/v2/players as get with access key and select Auth =>Bearer 
5. every thing Good ? Go a heaad
### Setup DataBase using elephantsql
1. Sign up => with gethub is better => 
2. Create new Instance => add name  : playersdb => Select region=>create 
3. add the data locally:
   1.  Open .env add from site (name, user,host and passwoed)
   2.  Open settings => databases => link the defult with env 
4. `docker-compose run web python manage.py migrate`
5. Connecting Done :)
6. `docker-compose up` => new data , no users no data 
7. Let`s add new user and data
   1. `docker-compose run web python manage.py createsuperuser`
   2. run `docker-compose up` and login => add new data
   3. from elephantsql site click on BROWSER and check the users and data  

### production mode
after what we did in previous lab (gunicorn ) let`s continue on it
1. Open .gitignore and add all content from [here](https://github.com/LTUC/blogpostsapid4/blob/master/.gitignore)
2. run `heroku apps:create playerapi34`
3. run `git remote -v` should show repo nd heroku 
4. in root add file heroku.yml 
5. copy and past from [here](https://github.com/LTUC/blogpostsapid4/blob/master/heroku.yml) change the project name 
6. run `heroku stack:set container`
7. docker-compose run web python manage.py gunicorn projectname.wsgi 
8. run poetry shell => gunicorn projectname.wsgi =>run server and add data 
