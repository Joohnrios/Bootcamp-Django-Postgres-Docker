from django.shortcuts import render

# Create your views here.

def sacForm(request):
    return render(request, 'sac/form.html')