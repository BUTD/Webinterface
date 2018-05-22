#!/bin/bash
roscore &
roslaunch rosbridge_server rosbridge_websocket.launch &
rostopic pub -r 1 /my_topic std_msgstring "Hello!" &
docker start adoring snyder
python manage.py runserver &
python manage.py showTopicTest &
