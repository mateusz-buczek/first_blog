# first_blog
# General info
My second choice for Django training was to biuld a simple blog app. 
So far blog allows reading, adding and editing posts (deleting available from admin panel). Planned functionalities: deleting/removing posts, adding comments, managing comments. 
The visual aspect is quite barbaric, however it's supposed to work, not to be miss universe ;) 

# Technologies 
* Python 3.7.2
* Django 2.1.7 
* SQLite (Django's default DB)
* HTML
* CSS 
* Bootstrap 3.2.0 (bootstrapcdn.com) 

# Setup 
Copy this repository to your HDD or choose corresponding option in your IDE (PyCharm recommended). 
Install Django: 
```
$ pip install django 
```
Pycharm should create venv for you. If not, choose default Python based one when asked. 
If you're impatient type: 
```
$ cd mysite
```
and then (when in folder mysite): 
```
$ py manage.py runserver 
```
which will probably give you only django welcome site at 127.0.0.1:8000 because of unapplied SQL migrations (database in .gitignore). Hit ctrl+C or break.
Go ahead and do the following: 
```
$ py manage.py migrate
$ py manage.py makemigrations blog
$ py manage.py sqlmigrate blog 0001 
```
and again: 
```
$ py manage.py migrate 
```

From now on 
```
$ py manage.py runserver  
```
should run empty blog, yet without adding or editing options - you need superuser account to see and use those. Hit ctrl+C or break. Type: 
```
$ py manage.py createsuperuser 
```
and follow instructions (e-mail not required, can skip with enter) 
Now re-run server: 
```
$ py manage.py runserver
```
log in with created account at 
``` 
127.0.0.1:8000/admin 
```
You can add, delete and edit posts from admin panel, however i encourage you to try doing it from blog-level - go to 
```
127.0.0.1:8000 
```
Feel free to send feedback :) 

# Sources/Inspirations 
I tried to work as much as possible with Django documentation, altough tutorial from djangogirls.com was very helpful in creating stable skeleton, comparing my own work and finding bugs. Therefore I'm obliged to give credit and license this work under the Creative Commons Attribution-ShareAlike 4.0 International License. 
