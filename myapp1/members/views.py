from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from . models import Q_A
from . models import Regform
from django.urls import reverse


def members(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

def register(request):
    template=loader.get_template('registrationform.html')
    return HttpResponse(template.render())

def registerdb(request):
    fn=request.GET.get("fname")
    ln=request.GET.get("lname")
    g=request.GET.get("gender")
    d=request.GET.get("dob")
    pn=request.GET.get("mobile")
    e=request.GET.get("email")
    un=request.GET.get("su_name")
    ps=request.GET.get("su_pass")
    details=Regform(fname=fn,lname=ln,gender=g,dob=d,phone=pn,email=e,uname=un,passcode=ps)
    details.save()
    template=loader.get_template('login.html')
    return redirect('login')
    


def login(request):
    template=loader.get_template('login.html')
    return HttpResponse(template.render())

def logindb(request):
    un=request.GET.get("uname")
    pa=request.GET.get("pass")
    check = Regform.objects.filter(uname=un,passcode=pa).values()
    if check:
        return redirect(reverse('record'))
        
    else:
        template=loader.get_template('login.html')
        context = {'result':'Incorrect password,try again',}
        return HttpResponse(template.render(context,request))
    
        
def record(request):
    score=0
    if "score" in request.GET:
        score=int(request.GET["score"])
    if "submit2" in request.GET:
        result=loader.get_template('result.html')
        con = {'myresult':result,'score':score,}
        return HttpResponse(result.render(con,request))
    else:
        template=loader.get_template('question1.html')
        a=0
        if "id_text" in request.GET:
            a=int(request.GET.get("id_text",1))       
        if "op" in request.GET:
            check=request.GET["op"]
            correct=Q_A.objects.filter(id=a).values_list('answer',flat=True).first()
            if check==correct:
                score+=1
        a+=1   
        elements = Q_A.objects.filter(id=a).values()         
        context = {'myelements':elements,'score':score,}
        return HttpResponse(template.render(context,request))
print('hi')    


    