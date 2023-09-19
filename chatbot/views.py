from django.http import JsonResponse
from django.shortcuts import render
import openai

openai.api_key = ""

def generate_response(text):
    response = openai.Completion.create(
        prompt=text,
        engine='text-davinci-003',
        max_tokens=100,  # max words
        temperature=0.7,  # creativity
        n=3,  # diverse answers
        stop=None,  # on what word ends
        timeout=15,  # max time to wait
    )
    if response and response.choices:
        return response.choices[0].text.strip()
    else:
        return None

def get_openai_response(request):
    user_message = request.GET.get('user_message', '')  # Get user's message from the request

    # Call your OpenAI script here to generate a response
    message = user_message  # Use the user's message as input

    prompt = f"As a soccer expert, can you explain {message} from a soccer standpoint?. Start with sentence, \"As a football expert\""
    response = generate_response(prompt + message)

    return JsonResponse({'response': response})

def index(request):
    return render(request, 'chatbot/index.html')
