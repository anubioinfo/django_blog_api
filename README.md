This is a Simple Blog Application where we can create and list the blogs. In order to run this application we need to run the following commands:

# make migrations
python3 manage.py makemigrations

# migrate the tables
python3 manage.py migrate

# run the server
python3 manage.py runserver

# After successfully executing the above command we can run the server using below URL:
http://127.0.0.1:8000/blogs

# We can access the swagger using the below link:
http://127.0.0.1:8000/swagger/

This way we can execute the Django blog application
