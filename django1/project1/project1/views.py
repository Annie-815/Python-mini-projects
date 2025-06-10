#from django.http import HttpResponse
from django.shortcuts import render,redirect

def homepage(request):
    #return HttpResponse("Ann Karanja's Portfolio")
    return render(request, 'homepage.html')

def about(request):
    #return HttpResponse("I am a python developer")
    return render(request, 'about.html')
def contacts(request):
    return render(request, 'contactme.html')
def hireme(request):
    if request.method == "POST":        
        return redirect('homepage.html') 
    return render(request, 'hireme.html')
def skills(request):
    return render(request, 'skills.html')

