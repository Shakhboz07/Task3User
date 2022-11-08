from django.shortcuts import redirect, render

from apps.models import User

# Create your views here.


def index_page(request):
    users = User.objects.all()
    context = {
        "users": users
    }
    return render(request, 'apps/index.html', context)
