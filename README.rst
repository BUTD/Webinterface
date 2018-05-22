Benjamin Becker, 19.05.2018

This package is a web app created with Django and Channels to communicate 
with ROS via rosbridge server.

The following steps are necessary to run this application:

Run all following commands in individual processes.

1. ROS
1a. roscore
1b. roslaunch rosbridge_server rosbridge_websocket.launch
1c. rostopic pub -r 1 /my_topic std_msgstring "Hello!"
1d. rostopic pub -r 0.3 /my_topic std_msgstring "Hello 2!"

2. redis for the channel layer of DJANGO CHANNELS
docker run [?what container (see channels documentation)?]

3. DJANGO (run in virtualenv)
3a. python manage.py runserver
3b. python manage.py showTopicTest

4. Browser
browse to http://127.0.0.1:8000/sensorapp/sensor/

TO DO:
test server with access in local network
deployment
