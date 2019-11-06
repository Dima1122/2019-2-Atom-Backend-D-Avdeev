from django.db import models
import datetime
from user_profile.models import User

class Chat(models.Model):
    title = models.CharField(max_length = 128, blank = False)
    is_group_chat = models.BooleanField(default = False)
    last_message = models.DateTimeField(default=datetime.date.today)

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.CharField(max_length = 512, blank = False)
    added_at = models.DateTimeField(default = datetime.date.today)

class Attachment(models.Model):
    message = models.ForeignKey(Message, on_delete = models.CASCADE)
    type_attach = models.CharField(max_length = 16, choices = (('image','image'),('video','video'),('gif','gif'),('voice_record','voice_record')))
    url_attach = models.FilePathField(blank = True) 
