from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .forms import ContactForm

def home(request):
    return render(request,'blog/home.html')

def about(request):
    return render(request,'blog/about.html')

'''def response_redirect(request):
    return redirect('success')
'''
def success(request):
    return HttpResponse(request,'blog/success.html')

def contactform(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('blog/success')
    else:
        form = ContactForm()

    return render(request,'blog/contactus.html',{'form': form})

