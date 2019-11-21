#!/usr/bin/env python

import rospy, math, random
from std_msgs.msg import String

def dummyTalker():
    pub = rospy.Publisher('correlationTables', String, queue_size=10)
    corr = [["10", "24" , 0], ["11", "23" , 1],["11", "22" , 0], ["10", "23" , 0],
            ["10", "22" , 1],["11", "24" , 1]]
    rospy.init_node('dummyTalker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    corr_msg1 = ""
    while not rospy.is_shutdown():
        for i in range (len(corr)):
            corr[i][2] = abs(corr[i][2] - random.uniform(0,0.4))
        for i in range (len(corr)):
            for j in range(len(corr[i])):
                corr_msg1 += " " + str(corr[i][j])
        hello_msg1 = corr_msg1
        rospy.loginfo(hello_msg1 + "\n")
        pub.publish(hello_msg1)
        rate.sleep()

if __name__ == '__main__':
    try:
        dummyTalker()
    except rospy.ROSInterruptException:
        pass