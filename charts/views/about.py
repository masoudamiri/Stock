from django.shortcuts import render

def about_view(request):
    return render(request, 'charts/about.html')