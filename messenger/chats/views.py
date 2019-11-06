from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def chat_list(request, pk=None):
    if pk is None:
        return JsonResponse({'error':'You did not enter value'},status = 404)
    if request.method == 'POST':
        return JsonResponse({'chat_id': pk, 'members': 1000})
    elif request.method == 'GET':
        return JsonResponse({'chat_id': pk, 'members': 50})
    return JsonResponse(status = 405)
