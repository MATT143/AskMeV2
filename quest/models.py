from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import uuid

# Create your models here.

class Post(models.Model):
    CATEGORY_CHOICES = (
        ('sap', 'SAP'),
        ('java', 'JAVA'),
        ('python', 'PYTHON'),
        ('testing', 'TESTING'),

    )
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title=models.CharField(max_length=200)
    content=models.TextField()
    category=models.CharField(max_length=100,choices=CATEGORY_CHOICES,default='python')
    date_posted=models.DateTimeField(default=timezone.now())
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=50,default='POSTED')
    solution=models.TextField(blank=True)
    last_modified=models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('profile')

# class SolutionCallBack(models.Model):
#     cust_id=models.CharField(max_length=100)
#     solution=models.TextField()
#     category=models.CharField(max_length=30)
#     title=models.CharField(max_length=200)
#     creation_date=models.DateTimeField(default=timezone.now())





