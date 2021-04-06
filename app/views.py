from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def password_generate(request):
    stringss = list('abcdefghiklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        stringss.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYX'))

    if request.GET.get('special'):
        stringss.extend(list('@#$%^&*()[]\/|!'))

    if request.GET.get('number'):
        stringss.extend(list('1234567890'))

    length = int(request.GET.get('length'))

    passwordss = ''

    for x in range(length):
        passwordss += random.choice(stringss)

    return render(request, 'app/password_generated.html', {'passwordss' : passwordss})