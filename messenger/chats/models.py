from django.db import models
from django.utils import timezone
from user_profile.models import User

class Chat(models.Model):
    title = models.CharField(max_length = 128, blank = False)
    is_group_chat = models.BooleanField(default = False)
    icon = models.FilePathField(blank = True)


    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.CharField(max_length = 512, blank = False)
    added_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Attachment(models.Model):
    choices = (('image','image'),
               ('video','video'),
               ('gif','gif'),
               ('voice_record','voice_record'))
    message = models.ForeignKey(Message, on_delete = models.CASCADE)
    type_attach = models.CharField(max_length = 16, choices = choices)
    url_attach = models.FilePathField(blank = True)


    class Meta:
        verbose_name = 'Приложение'
        verbose_name_plural = 'Приложения'
