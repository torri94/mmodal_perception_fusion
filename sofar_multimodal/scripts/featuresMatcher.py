#!/usr/bin/env python
"""
author:    Filippo Lapide
author:	Vittoriofranco Vagge
"""

import rospy
from std_msgs.msg import *
from sofar_multimodal.msg import *

#INITIALIZATION 
reasoner_out = outputReasoner()
selector_out = selectorMatcher()
obj_list = adapter()
obj_list.id_mod = 90 #the most frightening
matcher = matcherObj()

##Function
def matcherFunction(obj_list, r_out):
    ##
    #Function to match unionObject from featureSelector module with the IDs passed by reasoner module
    for linea in r_out.lines:
        matcher.sameObj[:] = []
        matcher.correlation = linea.corr
        for ogg_reas in linea.rec:
            for ogg_lista in obj_list.adap:
                for caratteristica in ogg_lista.obj:
                    if (caratteristica.name == 'id'):
                        if ((ogg_reas[1:]) == (caratteristica.value[0])):
                            matcher.sameObj.append(ogg_lista)                           # make a list of matching objects
                            obj_list.adap.remove(ogg_lista)                             # delete the object from the list
        pub_results.publish(matcher)                                                    # pubblish output


##CALLBACK
def callbackSelector(selectorMatcher):
    ##
    # Loop to create a list of objects from selctorMatcher input
    for moduli in selectorMatcher.matcher:
        for scene in moduli.common:
            for oggetti in scene.adap:
                obj_list.adap.append(oggetti)  
    
##CALLBACK
def callbackReasoner(outputReasoner):
    reasoner_out = outputReasoner
    matcherFunction(obj_list,reasoner_out)
 
	 
if __name__ == '__main__':
	rospy.loginfo("Running...")
	rospy.init_node('featuresMatcher', anonymous=True)
	##SUBSCRIBER
	sub_pitt = rospy.Subscriber('reasoner_output', outputReasoner, callbackReasoner)
	##SUBSCRIBER
	sub_tensor = rospy.Subscriber('/featureScheduler/pubUnion', selectorMatcher, callbackSelector)
	##PUBLISHER
	pub_results = rospy.Publisher('/featureMatcher/dataPub', matcherObj, queue_size=10)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():

		rate.sleep()
