from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	username = models.CharField(max_length=32, unique=True)
	email = models.EmailField(unique=True)
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

class EmailToken(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	token = models.UUIDField(default= uuid.uuid4() ,unique= True)
	created_at = models.DateTimeField(auto_now_add=True)