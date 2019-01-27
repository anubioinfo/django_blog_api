from django.db import models
from django.contrib.auth.models import User


'''
Blogs model with title, content, author field
'''
class Blogs(models.Model):
    title = models.CharField(max_length=1500, null=True, default='Test Blog')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


'''
Comment model with content, author field
'''
class Comments(models.Model):
    content = models.CharField(max_length=1500, null=True, default='Test Comment')
    authors = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)