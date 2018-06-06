from django.shortcuts import render
from .topics import ALLOWED_TOPICS_READ

# Create your views here.
def index(request):
    return render(request, 'sensorApp/index.html', {})

def sensor(request):
    return render(request, 'sensorApp/sensor.html', {'topics':ALLOWED_TOPICS_READ})

def drive(request):
    return render(request, 'sensorApp/drive.html', {})

def motors(request):
    return render(request, 'sensorApp/motors.html', {})