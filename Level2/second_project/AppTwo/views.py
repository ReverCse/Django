from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.

def index(request):
    return HttpResponse("<em>My Second App!</em>")

    return render(request, 'first_app/index.html', context = my_dict)


def help(request):
    help_dict = {'help_insert': "This is my help page"}
    return render(request, 'second_app/index.html', context = help_dict)


def users(request):
    user_list = User.objects.order_by("first_name")
    user_dict = {"users":user_list}
    #will know to look in templates
    return render(request, "second_app/users.html", context = user_dict)
