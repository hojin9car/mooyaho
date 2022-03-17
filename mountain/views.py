from django.shortcuts import render
from .models import Mountain
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'mountain/main.html')


# @login_required()
def mountains(request):
    # user = request.user.is_authenticated
    all_mountain = Mountain.objects.all()
    return render(request, 'mountain/all_mountain.html', {'mountains': all_mountain})


def mountains_detail(request, id):
    my_mountain = Mountain.objects.get(id=id)
    return render(request, 'mountain/mountains_detail.html', {'mountain_info': my_mountain})
