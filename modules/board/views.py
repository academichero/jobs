from django.shortcuts import render
from django.http import HttpResponse
from .forms import JobForm
from .models import Job


def home(request):
    '''
        Home page of our board
        It show a list of Positions in IFPB or other companies
    '''
    user = request.user
    jobs = Job.objects.all()

    return render(request, 'home.html', locals())
