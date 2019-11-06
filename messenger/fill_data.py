from user_profile.models import User, Member
from chats.models import Chat, Message, Attachment


def fill_messages():
    messages = ((1, 1, 'hi'), (1, 2, 'Got a million'), (1, 3, 'Lucky you'), (2, 2, 'MU will win for sure'), (2, 3, 'Made 100k bet'), (3, 3, 'hi, mom'))
    for chat_id, user_id, content in chat_user:
        message = Message(chat=chat_id, user=user_id, content=content)
        message.save()


def fill_users():
    info = (('Vasya Pupkin', 'pupka'),
             ('Petrov Petr', 'pet'),
             ('Ivanov Ivan', 'iwa_123'))
    for username, nickname in info:
        usr = User(username=username, nickname=nickname, avatar_path = 'C:\\urls')
        usr.save()


def fill_chats():
    info = (('MoneyMakers', True),
            ('1xbet', True),
            ('Mom', False))
    for title, is_group_chat in info:
        chat = Chat(title = title, is_group_chat = is_group_chat)
        chat.save()


def fill_members():
    members = ((1, 1), (2, 1), (3, 1), (2, 2), (3, 2), (3, 3))
    for user_id, chat_id in members:
        member = Member(chat_id =chat_id, user_id = user_id)
        member.save()


def fill_attachments():
    attachments = ((1, 'image'), (2, 'video'), (3, 'gif'))
    for message_id, type_attach in attachments:
        attachment = Attachment(message =message_id, type_attach = type_attach, url_attach = 'C:\\urls_attach')
        attachment.save()

fill_users()
fill_chats()
fill_members()
fill_messages()
fill_attachments()