from django.shortcuts import render


def estimates(request):
    return render(request, 'estimate/index.html')
