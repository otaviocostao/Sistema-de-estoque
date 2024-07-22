from django.shortcuts import render

# Create your views here.
def inicioview(request):
    
    return render(request, "estoque/home.html", )