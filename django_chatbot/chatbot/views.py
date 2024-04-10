from django.shortcuts import render
from django.http import JsonResponse
import openai


openai_api_key='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'
openai.api_key=openai_api_key


def ask_openai(message):
    response=openai.Completion.create(
        model="gpt-3.5",
        prompt=message,
        max_tokens=150,
        n=1,
        stop=None,
        temperatur=0.7,

    )
    print(response)
    #answer= response.choice[0].text.strip()
    #return answer

# Create your views here.
def chatbot(request):
    if request.method=='POST':
        message=request.POST.get('message')
        response=ask_openai(message)
        return JsonResponse({'message':message,'response':response})
    return render(request,'chatbot.html')

