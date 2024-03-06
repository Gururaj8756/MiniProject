from django.shortcuts import render
from django.contrib.auth import authenticate, login
from hi.models import User,QuestionsTable
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
def create_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        password=request.POST['password']
        email = request.POST['email']
        dob=request.POST['dob']
        age = int(request.POST['age'])
        new_user = User(name=name,username=username,password=make_password(password),email=email,dob=dob,age=age)
        new_user.save()
        return render(request, 'success.html')
    return render(request, 'user_form.html')

def welcome(request):
    return render(request,'hi.html')

def hi(request):
    return render(request,'success.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') # email
        password = request.POST.get('password')       
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        
        if user is not None and user.check_password(password):
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('success.html')  
        
        error_message = "Invalid credentials. Please try again."
    else:
        error_message = ""
    return render(request, 'login.html', {'error_message': error_message})

from django.http import JsonResponse
from .models import QuestionsTable  

def my_question(request):
    
    questions = QuestionsTable.objects.all()
    
   
    data = {
        'questions': [
            {
                'QId': question.QId,
                'Questions': question.Question,
                'Option1': question.Option1,
                'Option2': question.Option2,
                'Option3': question.Option3,
                'Option4': question.Option4,
            }
            for question in questions
        ]
    }

   
    return JsonResponse(data)

