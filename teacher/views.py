from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'teacher_templates/base.html')



def attendance(request):
    return render(request,'teacher_templates/add_attentance.html')    



def profile(request):
    return render(request,'teacher_templates/profile.html')    




def viewstudents(request):
    return render(request,'teacher_templates/viewstudent.html')    


