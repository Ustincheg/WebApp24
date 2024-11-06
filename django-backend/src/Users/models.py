from django.db import models
from django.contrib.auth.models import User
import uuid
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)


class EmailToken(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	token = models.UUIDField(default= uuid.uuid4() ,unique= True)
	created_at = models.DateTimeField(auto_now_add=True)