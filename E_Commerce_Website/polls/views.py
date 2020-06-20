from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User

def home(request):

    context={}
    me = User.objects.get(username="Rounak")
    #if we want to pick up attribute of a model we use . (period), but
    #if we want to pick up their corresponding methods we use __
    # questions = Questions.objects.all().filter(created_by__is_staff=True)
    questions = Questions.objects.all() # returns array
    context['title'] = 'polls'
    context['questions'] = questions
    # print(dir(request))
    print(request.user)
    # print(dir(request.user))

    return render(request, 'polls/poll/index.html', context)


def details(request, id=None):

    context={}
    if request.method == 'POST':

        print(request.POST)
        print(request.POST['fname'])
        answer = Answer()
        answer.user = request.user
        answer.choice = Choices.objects.get(id=request.POST['fname'])
        answer.save()

        context['answer'] = answer
        return render(request, 'polls/poll/entry.html', context)
    
    else:

        context['detail']= Questions.objects.get(id=id)
        return render(request, 'polls/poll/details.html', context)


# def entry(request, id=None):

#     if request.method == 'POST':

#         answer = Answer()
#         answer.user = request.user
#         answer.choice = Choices.objects.get(id=id)
#         answer.save()
    
#     context = {}
#     context['answer'] = answer

#     return render(request, 'polls/entry.html', context)