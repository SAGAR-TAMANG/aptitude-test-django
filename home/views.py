from django.shortcuts import render


# Create your views here.
def Home(request):
    return render(request, 'home.html')

def Questions(request):
    return render(request, 'questions101/questions.html')

def QuestionsTest(request):
    return render(request, 'questions101/questions_test.html')