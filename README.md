# Inventory-Update-Form
Simple form application based on django.
# Setup and running
Clone the repo and cd to the folder
```
$ git clone https://github.com/dggs123/flashpoint
$ cd Inventory-Update-Form
```
Install and setup pip and Virtualenv. This may take sometime depending on your internet speed.
```
$ sudo apt-get install python-pip
$ pip install virtualenv
```
Commands to run server
```
$ virtualenv .
$ pip install -r requirements.txt
# This may take few minutes, go get some coffee until then

$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
Now the website should be available on localhost:8000
# ScreenShots
