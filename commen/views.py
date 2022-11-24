from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'commen_templates/home.html')



def school(request):
    return render(request,'commen_templates/schoollogin.html')    



def teacher(request):
    return render(request,'commen_templates/teacherlogin.html')    




def student(request):
    return render(request,'commen_templates/studentlogin.html')    



def sumathi(request):
    return render(request,'commen_templates/sumathi.html')    

