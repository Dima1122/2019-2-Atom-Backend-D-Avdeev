from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def contact_list(request):
    if request.method == 'POST' or request.method == 'GET':
        return JsonResponse({'amount of contacts': 100,
                            'favourite user': 'Vasya'})
    return JsonResponse({'Error': 'Wrong method {}'.format(request.method)},status = 405)
