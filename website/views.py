from concurrent.futures.process import _python_exit
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def error404(request):
    return render(request, '404.html', {})

def contact(request):
    if request.method == "POST":
        fullName = request.POST['fullName']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        firstName = fullName.split()

        #send email
        send_mail('WEBSITE CONTACT SECTION','Name: ' + fullName + '\nEmail: ' + email +'\nPhone: '+ phone + '\n\n' + message,email,['mostellerwb@gmail.com'])
        return render(request, 'contact.html', { 'name' : firstName[0] })

    else:
        return render(request, 'contact.html', {})
