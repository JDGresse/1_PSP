from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def individuals(request):
    return render(request, 'individuals.html')

def couples(request):
    return render(request, 'couples.html')

def what_to_expect(request):
    return render(request, 'what_to_expect.html')

def contact(request):
    return render(request, 'contact.html')