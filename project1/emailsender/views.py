from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
def index(request):
    if request.method == "POST":
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        email = request.POST.get('email')
        print(sub,msg,email)
        send_mail(
            sub,msg,'sharonlilly2003@gmail.com',
            [email]
        )
        return HttpResponse('Email send that!')
    return render(request, 'emailsender/form.html')    
