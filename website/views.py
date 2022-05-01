from cgi import test
from concurrent.futures.process import _python_exit
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse,HttpResponseRedirect
import os
from numpy import full

def sendForm(formType,fullName, email,phone,bus,service,message):
    send_mail(formType + ' SUBMISSION',
                'Name: ' + fullName + '\nEmail: ' + email +
                '\nPhone: '+ phone + '\nFirm: ' + bus + 
                '\nService: ' + service + '\n\nTESTIMONIAL: \n' + 
                message,email,['mostellerwb@gmail.com'])

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'index.html', {})

def error404(request):
    return render(request, '404.html', {})

def order(request):
    return render(request, 'order.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})

def services(request):
    return render(request, 'services.html', {})

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
        
        try: 
            #send email
            sendForm("TESTIMONIAL",request.POST['fullName'], request.POST['email'],
                request.POST['phone'], request.POST['business'],
                request.POST['service'], request.POST['message'])
        except:
            return HttpResponse('Message failed to send')

        firstName = request.POST['fullName'].split()
        return HttpResponseRedirect('/thanks.html?name=' + firstName[0] + '&type=testimonial')

    return render(request, 'testimonials.html', {'testimonials' : test, "message" : message01})

def contact(request):
    if request.method == "POST":
        try: 
            #send email
            sendForm("CONTACT", request.POST['fullName'], request.POST['email'],
                request.POST['phone'], request.POST['business'],
                '', request.POST['message'])
        except:
            return HttpResponse('Message failed to send')

        firstName = request.POST['fullName'].split()
        return HttpResponseRedirect('/thanks.html?name=' + firstName[0] + '&type="Contact Us"')

    else:
        return render(request, 'contact.html', {})

def payment(request):
    if request.method == "POST":
        #try: 
            #send email
        send_mail('PAYMENT SUBMISSION',
                "Invoice #: " + request.POST['invoice'] + "\nPayment Amount: " + request.POST['amount'] +
                "\nEmail: "+request.POST['email'] + "\n\nDescription:\n " + request.POST['desc']
                ,request.POST['email'],['mostellerwb@gmail.com'])
        #except:
        #    return HttpResponse('Message failed to send')
        return HttpResponseRedirect('/thanks.html?name=' + "tUJirE/s3-9JMCL" + '&type=Payment')

    else:
        return render(request, 'payment.html', {})

def thanks(request):
    name = ""
    type = "contact"

    name = request.GET['name']
    type = request.GET['type']

    return render(request, "thanks.html", { 'name' : name, 'type' : type })
