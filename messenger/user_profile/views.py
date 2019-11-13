from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user_profile.models import User
import re


@csrf_exempt
def user_info(request, pk=None):
    if request.method == 'GET':
        if pk is None:
            return JsonResponse({'message': 'please, specify username'}, status = 404)
        else:
            user = User.objects.all().filter(nickname__iexact=pk).first()
            if user is None:
                return JsonResponse({'response': 'user not found'}, status = 400)
            else:    
                return JsonResponse({'response': user.__str__()})
    return JsonResponse({'test': 'Wrong method {}'.format(request.method)}, status=405)
