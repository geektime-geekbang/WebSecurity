from django.shortcuts import render

# Create your views here.
def firsthtml(request):
    return render(request, 'index.html')