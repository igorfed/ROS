#!/usr/bin/env python3
import rospy
import numpy as np 
from std_msgs.msg import Float32 
from collection import deque
from hello_ros1.msg import Signal 
class SignalFilter(object):
    def __init__(self):
        # Creating subscriber for the signal and publisher for the filtered one 
        self.signal_sub = rospy.Subscriber ("signal", 
                                           Signal, 
                                           self.signal_callback)
        self.signal_pub = rospy.Publisher("filtered_signal", 
                                          Signal,
                                          queue_size=10)
        # Buffer to store last 5 signal values
        self.signal_window = deque([], 5)
    def signal_callback (self, signal):
        # Logging received data
        rospy.loginfo("I've got {}".format(signal))
        # filtering signal with the moving average and
        # publishing filtered signal
        self.signal_window.append(signal.data)
        filtered_signal = Signal()
        # timestamp
        filtered_signal.header.stamp = rospy.Time.now()
        filtered_signal.signal = sum (self.signal_window)/len(self.signal_window)
        self.signal_pub.publish(filtered_signal)
if __name__ == '__main__':
    try:
        # Initializing node with the "signal_filter" name
        rospy.init_node("signal_filter")
        new_filter = SignalFilter()
        # Giing control to ROS
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.logger('Ctrl+C was pressed')
        