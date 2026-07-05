from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. You're at the chaiaurdjango home.")

def index(request):
    return HttpResponse("Hello, world. You're at the chaiaurdjango index.")

def contact(request):
    return HttpResponse("Hello, world. You're at the chaiaurdjango contact.")