from django.shortcuts import render


def home(request):
    context = {
        'username': request.user.first_name
    }
    return render(request, 'home/index.html', context)
