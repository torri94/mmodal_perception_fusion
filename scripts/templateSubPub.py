#ROS Node Subscriber & Publisher template

#!/usr/bin/env python

#remove or add the library/libraries for ROS
import rospy
from std_msgs.msg import String
from sofar_multimodal.msg import *

varS=None

#define function/functions to provide the required functionality
def callback(msg):
    global varS
    varS==do_something(msg.data)

if __name__=='__main__':
    #Add here the name of the ROS. In ROS, names are unique named.
    rospy.init_node('NODE_NAME')
    #subscribe to a topic using rospy.Subscriber class
    sub=rospy.Subscriber('TOPIC_NAME', THE_TYPE_OF_THE_MESSAGE, callback)
    #publish messages to a topic using rospy.Publisher class
    pub=rospy.Publisher('TOPIC_NAME', THE_TYPE_OF_THE_MESSAGE, queue_size=1)
    rate=rospy.Rate(10)

    while not rospy.is_shutdown():
        if varS<= var2:
            varP=something()
        else:
            varP=something()

        pub.publish(varP)
        rate.sleep()