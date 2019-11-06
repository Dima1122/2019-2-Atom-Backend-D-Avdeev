from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def chat(request, pk=None):
    if pk is None:
        return JsonResponse({'message': 'You should enter chat page id'}, status = 404)
    if request.method == 'POST' or request.method == 'GET':
        return JsonResponse({'chat page id': pk, 'Number of messages': 1000,
            'name': 'Vasya', 'time':'last at 21:00'})
    return JsonResponse({'Error': 'Wrong method {}'.format(request.method)},status = 405)
