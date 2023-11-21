# chatbot/views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .chatbot_logic import get_chatbot_response

@csrf_exempt
def chatbot_view(request):
    print("여기까지옴")
    if request.method == 'POST':
        try:
            user_input = request.POST.get('user_input')
            if user_input is None or user_input.strip() == '':
                raise ValueError('유효하지 않은 입력')

            response = get_chatbot_response(user_input)
            if response is None or response.strip() == '':
                raise ValueError('챗봇 응답이 비어 있음')

            return JsonResponse({'response': response})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'userpage/userpage.html')
