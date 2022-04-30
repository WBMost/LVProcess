from cgi import test
from concurrent.futures.process import _python_exit
from django.shortcuts import render
from django.core.mail import send_mail
import os

from numpy import full

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def error404(request):
    return render(request, '404.html', {})

def order(request):
    return render(request, 'order.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})

def testimonials(request):
    test = {}
    firstName = None
    message01 = None

    #manages reading and passing testimonials to page
    try:
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir,'testimonials.txt')
        tests = open(file_path, 'r')
        data = tests.read()
        tests = data.split(';')
        for t in tests:
            dic = t.split('WRITTEN-BY')
            test[dic[0]] = dic[1]
    except:
        message01 = "Oops..."

    #sets up if a testimonial was posted
    if request.method == "POST":
        fullName = request.POST['fullName']
        email = request.POST['email']
        phone = request.POST['phone']
        bus = request.POST['business']
        service = request.POST['service']
        message = request.POST['message']
        firstName = fullName.split()


        #send email
        send_mail('TESTIMONIAL SUBMISSION','Name: ' + fullName + '\nEmail: ' + email +'\nPhone: '+ phone + '\nBusiness: ' + bus + '\nService: ' + service + '\n\nTESTIMONIAL: \n' + message,email,['mostellerwb@gmail.com'])
        #lazy but effective coding
        return render(request, 'testimonials.html', {'testimonials' : test, "message" : message01, "name" : firstName[0]})

    return render(request, 'testimonials.html', {'testimonials' : test, "message" : message01})
    


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
