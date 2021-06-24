from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def send_message(request):
    
    template = 'contact/contact.html'
    
    if request.method == 'POST': 
        contact_form = ContactForm(request.POST)
        send_mail()

    
    else:
        contact_form = ContactForm()
    
    context = {
        'contact_form': contact_form
    }


    return render(request, template, context)

def success(request):
    pass 
