# Quickstart

### Create Virtualenv

```
virtualenv -p python3 env

cd env

source env/bin/activate
```

### Install requirements

```
pip install -r requirements.txt
```

### Configure and Run 

```
cd backend/

./manage.py makemigrations

./manage.py migrate

./manage.py createsuperuser

./manage.py loaddata users.json

./manage.py runserver
```

### EndPoints

**Auth**
> Type: POST | Url: localhost:8000/api-token-auth/ | Return Type: Json | Return Data:  {token: xxx} 

** Post User **
> Type: POST | Header required: {Authorization: JWT < token >}| Url: http://localhost:8000/users/ | Data : { "first_name": "xxx", "last_name": "xxx", "academic_level": 1, "address": "xxx", "city": 1, "country": 1 }| Return Type: Json | Return Data:  [{ "first_name": "xxx", "last_name": "xxx", "academic_level": 1, "address": "xxx", "city": 1, "country": 1 } ]

**Get User List**
> Type: GET | Header required: {Authorization: JWT < token >}| Url: http://localhost:8000/users/ | Return Type: Json | Return Data:  [{ "first_name": "xxx", "last_name": "xxx" } ]

