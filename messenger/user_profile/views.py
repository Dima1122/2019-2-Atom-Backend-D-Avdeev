from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def user_info(request, pk=None):
    if pk is None:
        return JsonResponse({'msg': 'enter user id'},status = 404)
    if request.method == 'POST' or request.method == 'GET':
        return JsonResponse({'id': 123456, 'NickName': 'Vasya',
                            'Status': 'Unknown'})
    return JsonResponse({'Error': 'Wrong method {}'.format(request.method)}, status = 405)
