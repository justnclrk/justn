from django.shortcuts import render
from django.contrib.auth.models import User


def home(request):
    user = User.objects.get(username='justin')
    context = {
        'user': user
    }
    return render(request, 'justn/index.html', context)