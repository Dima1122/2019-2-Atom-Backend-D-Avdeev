from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length = 128, blank = False, unique = True)
    status = models.CharField(max_length = 512, blank = True, default = 'Very busy')
    avatar_path = models.FilePathField(blank = False)


    class Meta:
        verbose_name = 'Юзер'
        verbose_name_plural = 'Юзеры'

class Member(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    chat = models.ForeignKey('chats.Chat', on_delete = models.CASCADE)
    last_read_msg = models.DateTimeField(default=timezone.now)


    class Meta:
        verbose_name = 'Мембер'
        verbose_name_plural = 'Мемберы'


