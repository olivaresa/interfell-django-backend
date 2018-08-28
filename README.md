==Quickstart

virtualenv -p python3 env

cd env

source env/bin/activate
 
pip install -r requirements.txt

cd backend/

./manage.py makemigrations

./manage.py migrate

./manage.py createsuperuser

./manage.py loaddata users.json