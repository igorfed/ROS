#!/usr/bin/env python3
import rospy
import numpy as np 
from std_msgs.msg import Float32 
from hello_ros1.msg import Signal 

class SignalGenerator(object):
    def __init__(self):
        # Creating publisher for the signal 
        self.signal_pub = rospy.Publisher ("signal", 
                                           Float32, 
                                           queue_size =10)
    def generate_and_publish_signal(self):
        # Generating and publishing sine signal
        # dependemnt on curebt system time 
        seconds = rospy.get_time()
        new_signal_value = Signal()
        new_signal_value.header.stamp = rospy.Time.now()
        new_signal_value = np.sin(seconds) + 0.2 * np.random.randn()
        self.signal_pub.publish(new_signal_value)
    def launch_signal_generator(self):
        #Initializeing node with the signal generator name 
        rospy.init_node("signal_generator")
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.generate_and_publish_signal()
            # Using sleep to keep the desired rate
            rate.sleep()
if __name__ == "__main__":
    try:
        new_generator = SignalGenerator()
        new_generator.launch_signal_generator()
    except rospy.ROSInterruptException:
        rospy.logger("CTRL+C was pressed")        