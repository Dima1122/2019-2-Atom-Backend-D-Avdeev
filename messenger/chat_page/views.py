from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.shortcuts import render, render_to_response
from django.utils import timezone
from django.db.models import Max
from user_profile.models import User, Member
from chats.models import Message, Chat 

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('user',)


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('title',)
    
    def clean(self):
        super(ChatForm, self).clean()
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        chat = Chat.objects.all().filter(title__iexact=title).first()
        if chat is None:
            self.add_error('title', "Sorry, but this chat does not exist")
        return cleaned_data

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('content',)


@csrf_exempt
def chat(request, pk=None):
    if pk is None:
        return JsonResponse({'message': 'You should enter chat page id'}, status = 404)
    if request.method == 'POST' or request.method == 'GET':
        return JsonResponse({'chat page id': pk, 'Number of messages': 1000,
            'name': 'Vasya', 'time':'last at 21:00'})
    return JsonResponse({'Error': 'Wrong method {}'.format(request.method)},status = 405)

@csrf_exempt
def send_message(request):
    form = MemberForm()
    form2 = ChatForm()
    form3 = MessageForm()
    if request.method == 'POST':
        form = MemberForm(request.POST)
        form2 = ChatForm(request.POST)
        form3 = MessageForm(request.POST)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            _user = form.save(commit=False)
            _chat = form2.save(commit=False)
            _message = form3.save(commit=False)
            user = User.objects.get(username=_user.user)
            chat = Chat.objects.get(title=_chat.title)
            message = Message.objects.create(chat=chat, user=user, content=_message.content)
            member = Member.objects.filter(user__username=_user.user, chat__title__iexact=_chat.title).first()
            if member is None:
                member = Member.objects.create(user=user,chat=chat)
            return JsonResponse({'Status': 'Successfully sent'})
    return render_to_response('new_message.html', {'form': form, 'form2': form2, 'form3': form3},)




@csrf_exempt
def get_message(request):
    form = ChatForm()
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            messages = Message.objects.filter(chat__title__iexact=chat.title)
            response = dict()
            i = 0
            for message in messages:
                i+=1
                response.update({i:{
                'message': message.content,
                'added_at': message.added_at,
                }})
            return JsonResponse(response)
    return render_to_response('get_message.html', {'form': form},)


@csrf_exempt
def read_chat(request):
    form = MemberForm
    form2 = ChatForm()
    if request.method == 'POST':
        form = MemberForm(request.POST)
        form2 = ChatForm(request.POST)
        if form.is_valid() and form2.is_valid():
            _chat = form2.save(commit=False)
            _user = form.save(commit=False)
            member = Member.objects.filter(chat__title__iexact=_chat.title, user__username=_user.user).first()
            if member is None:
                return JsonResponse({'Status': 'Sorry, but you are not a member of this group'})
            msgs = Message.objects.filter(chat__title__iexact=_chat.title)
            max_date = msgs.aggregate(Max('added_at'))
            msg = Message.objects.filter(added_at=max_date['added_at__max']).first()
            member.last_read_msg = timezone.now()
            member.save()
            return JsonResponse({'Chat {}'.format(_chat.title): {'chat message': msg.content, 'added at': msg.added_at}})
    return render_to_response('read_chat.html', {'form': form, 'form2': form2 },)    
