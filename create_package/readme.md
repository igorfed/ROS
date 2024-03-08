    $ docker stop ros

    $ docker rm ros

    $ ./run_docker_.bash

    $ mkdir -p ~/catkin_ws/src 

    $ cd ~/catkin_ws/

    $ catkin_make

    $ source ~/catkin_ws/devel/setup.bash

    $ env | grep ROS

    $ ls -la 

    $ cd src/

    $ catkin_create_pkg hello_ros rospy std_msgs

    $ cd hello_ros/src

    $ cd ~/catkin_ws

    $ catkin_make
    
    $ source ./devel/setup.bash

    $ chmod +x src/hello_ros/src/signal_generator_node.py signal_filter.py                     

    $ roscore &

    $ rosrun hello_ros signal_generator.py  %its working
lunch new console
    $ docker exec -it ros bash 

    $ source /opt/ros/noetic/setup.bash

    $ rostopic list 

    $ rostopic signal
        specific type message msgs/Float32 
        published by signal Generator
        Subscriver: None - noone read this topic
    $ rostopic echo /signal

    $ rqt_graph
        plagin Introspection 
        plagin Visualisation plot choose /signal topic Enter  

    $ docker exec -it ros bash 

    $ rostopic echo /signal


run signal gemerator 
run signal_filter 
$ catkin_make
  $ source ./devel/setup.bash





