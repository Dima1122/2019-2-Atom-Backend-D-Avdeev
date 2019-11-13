from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django import forms
from .models import Chat
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from user_profile.models import User, Member

class NewChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('title', 'is_group_chat',)
    
    def clean(self):
        super(NewChatForm, self).clean()
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        chat = Chat.objects.all().filter(title__iexact=title).first()
        if chat is not None:
            self.add_error('title', "Sorry, but this chat does not exist")
        return cleaned_data


class MembersForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('user',)


@csrf_exempt
def create_chat(request):
    if request.method == 'POST':
        form = NewChatForm(request.POST)
        form2 = MembersForm(request.POST)
        if form.is_valid() and form2.is_valid():
            current_chat = form.save()
            member = form2.save(commit=False)
            user = User.objects.get(username = member.user)
            member = Member.objects.create(chat = current_chat, user = user)
    form = NewChatForm()
    form2 = MembersForm()
    return render_to_response('new_chat.html', {'form': form, 'form2': form2},)


@csrf_exempt
def list_chats(request, pk=None):
    if request.method == 'GET':
        if pk is None:
            return JsonResponse({'msg': 'please, specify user nickname'}, status=404)
        user = User.objects.all().filter(nickname__iexact=pk).first()
        if user is None:
            return JsonResponse({'response': 'user not found'}, status = 400)
        membership = Member.objects.all().filter(user=user.id)
        chats = []
        for member in membership:
            chats.append(member.chat)
        response = dict()
        for chat in chats:
            response['chat#{}'.format(chat.title)] = {
                'user': user.username,
                'is_group': chat.is_group_chat,
            }
        return JsonResponse(response)
    return JsonResponse({'Error': 'Wrong method {}'.format(request.method)}, status=405)
