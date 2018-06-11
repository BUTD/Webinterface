from django.shortcuts import render
from butd.topics import ALLOWED_TOPICS_READ

# Create your views here.
def index(request):
    return render(request, 'butd/index.html', {})

def sensor(request):
    return render(request, 'butd/sensor.html', {'topics':ALLOWED_TOPICS_READ})

def drive(request):
    return render(request, 'butd/drive.html', {})

def motors(request):
    return render(request, 'butd/motors.html', {})

def test(request):
    return render(request, 'butd/base.html', {})