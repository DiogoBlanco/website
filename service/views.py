from django.shortcuts import render


def services(request):
    return render(request, 'service/index.html')
