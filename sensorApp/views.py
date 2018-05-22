from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'sensorApp/index.html', {})

def sensor(request):
    return render(request, 'sensorApp/sensor.html', {})