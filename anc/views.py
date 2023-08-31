from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from anc.models import Students
from .forms import Std_form
from .forms import LogCredent as lcr

def home(request):
    return render(request, 'anc/home.html')

def students_list(request):
    students = Students.objects.all().values()
    std_dict = {
        'students' : students,
    }
    template = loader.get_template('anc/students_list.html')
    return HttpResponse(template.render(std_dict, request))

def update(request, id):
    student = Students.objects.all().get(id = id)
    
    std = {
        'student' : student,
    }
    
    if request.method == 'POST':
        student.delete()
        stdForm = Std_form(request.POST)
        if stdForm.is_valid():
            stdForm.save()
            return redirect('/anc')

    # template = loader.get_template('anc/update.html')
    # return HttpResponse(template.render(std,request))

    return render(request, 'anc/update.html', {'student':student})

def create(request):
    stdform = Std_form()
    if request.method == 'POST':
        stdForm = Std_form(request.POST)
        if stdForm.is_valid():
            stdForm.save()
            return redirect('/anc')

    return render(request, 'anc/create.html', {'stdform':stdform})

def delete(request, id):
    student = Students.objects.all().get(id=id)
    student.delete()
    return redirect('/anc')

def login(request):
    return render(request, 'anc/login.html' )

def signup(request):
    return render(request, 'anc/signup.html' )

def testlogin(request):
    logform = lcr()
    stds = Students.objects.all().values('roll_no')
    rollist = []
    for x in stds:
        for y in x.values():
            rollist.append(y)

    if request.method == "POST":
        lform = lcr(request.POST)
        if lform.is_valid():
            roll = lform.cleaned_data['username']
            pwd = lform.cleaned_data['password']

            for z in rollist:
                if roll == str(z):
                    uname = Students.objects.filter(roll_no = z).values('name')
                    paswd = Students.objects.filter(roll_no = z).values('password')

                    for p in paswd:
                        if pwd == p['password']:

                            return render(request, 'anc/sucess.html', {'rol':roll, 'uname':uname, 'paswd':paswd})
                        else : 
                            return render(request, 'anc/testlogin.html', {'logform':logform, 'stds':rollist, 'pwderror':'wrong password! Retry'})
               
    return render(request, 'anc/testlogin.html', {'logform':logform, 'stds':rollist})