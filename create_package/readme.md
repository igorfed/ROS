    $ docker stop r1_noetic_from_file

    $ docker rm r1_noetic_from_fil

    $ ./run_docker.bash

    $ mkdir -p ~/catkin_ws/src 

    $ cd ~/catkin_ws/

    $ catkin_make

    $ source ~/catkin_ws/devel/setup.bash

    $ env | grep ROS

    $ ls -la 

    $ cd src/

    $ catkin create_pkg hello_ros rospy std_msgs

    $ cd hello_ros/