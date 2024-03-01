# original code https://www.youtube.com/watch?v=YKX4E9Vh-ug&t=4427s
import rospy
import numpy as np 
from std_msg.msg import Float32 
from collection import deque

class SignalFilter(object):
    def __init__(self):
        # Creating subscriber for the signal and publisher for the filtered one 
        self.signal_pub = rospy.Publisher ("signal", 
                                           Float32, 
                                           queue_size =10)
        # Buffer to store last 5 signal values
        self.signal_pub = rospy.Publisher("filtered signal", Float32,
                                          )
        # Buffer to store last 5 signal values
        self.signal_window = deque([], 5)
        
    def signal_callback (self, signal):
        # Logging received data
        rospy.loginfo("I've got {}".format(signal.data))
        # filtering signal with the moving average and
        # publishing filtered signal
        self.signal_window.append(signal.data)
        filtered_signal = sum (self.signal_window)/len(self.signal_window)
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
        