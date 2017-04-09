# Jigsaw Puzzle Game
Jigsaw puzzle based on django/python.

# Setup and running
Clone the repo and cd to the folder
```
$ git clone https://github.com/dggs123/jig-Saw
$ cd jig-Saw
```
Install and setup pip and Virtualenv. This may take sometime depending on your internet speed.
```
$ sudo apt-get install python-pip
$ pip install virtualenv
```
Commands to run server
```
$ virtualenv .
$ source bin/activate
$ pip install -r requirements.txt
# This may take few minutes, go get some coffee until then

$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
Now the website should be available on 127.0.0.1:8000
# ScreenShots
<p align="center">
<img src="https://firebasestorage.googleapis.com/v0/b/project-228499762619542864.appspot.com/o/Internship%20Screen%20Shots%2Fscreen1.png?alt=media&token=82174957-c41f-405d-8148-f42ef1d9e2c7" width="500"/>
</p>
<p align="center">
<img src="https://firebasestorage.googleapis.com/v0/b/project-228499762619542864.appspot.com/o/Internship%20Screen%20Shots%2Fscreen11.png?alt=media&token=b3f0a1a3-5f22-4eaa-80de-af0ef6167cc8" width="500"/>
</p>
<p align="center">
<img src="https://firebasestorage.googleapis.com/v0/b/project-228499762619542864.appspot.com/o/Internship%20Screen%20Shots%2Fscreen12.png?alt=media&token=8d7b39c7-2764-4fb5-b05a-32611018cde9" width="500"/>
</p>
