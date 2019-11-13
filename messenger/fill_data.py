from user_profile.models import User, Member
from chats.models import Chat, Message, Attachment


def fill_messages():
    messages = ((1, 1, 'hi'), 
                (1, 2, 'Got a million'), 
                (1, 3, 'Lucky you'), 
                (2, 2, 'MU will win for sure'), 
                (2, 3, 'Made 100k bet'), 
                (3, 3, 'hi, mom'))
    for chat_id, user_id, msg in messages:
        user = User.objects.get(id=user_id)
        chat = Chat.objects.get(id=chat_id)
        message = Message.objects.create(chat=chat, user=user, content=msg)


def fill_users():
    info = (('Vasya Pupkin', 'pupka'),
             ('Petrov Petr', 'pet'),
             ('Ivanov Ivan', 'iwa_123'))
    for username, nickname in info:
        usr = User(username=username, nickname=nickname, avatar_path='C:\\urls')
        usr.save()


def fill_chats():
    info = (('MoneyMakers', True),
            ('1xbet', True),
            ('Mom', False))
    for title, is_group_chat in info:
        chat = Chat(title=title, is_group_chat=is_group_chat, icon='C:\\icons')
        chat.save()


def fill_members():
    members = ((1, 1), (2, 1), (3, 1), (2, 2), (3, 2), (3, 3))
    for user_id, chat_id in members:
        user = User.objects.get(id=user_id)
        chat = Chat.objects.get(id=chat_id)
        member = Member.objects.create(user=user, chat=chat)


def fill_attachments():
    attachments = ((1, 'image'), 
                   (2, 'video'), 
                   (3, 'gif'))
    for message_id, type_attach in attachments:
        message = Message.objects.get(id=message_id)
        attachment = Attachment.objects.create(message=message, type_attach=type_attach, url_attach='C:\\urls_attach')

fill_users()
fill_chats()
fill_members()
fill_messages()
fill_attachments()