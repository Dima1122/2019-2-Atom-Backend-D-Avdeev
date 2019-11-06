from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length = 128, blank = False, default = 'Unidentified turtle')
    status = models.CharField(max_length = 512, blank = True, default = 'Very busy')
    avatar_path = models.FilePathField(blank = False)

class Member(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    chat = models.ForeignKey('chats.Chat', on_delete = models.CASCADE)

