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
obj_out = obj()
matcher = matcherObj()
matcherOut = matcher_out()

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
                            ogg_lista.obj.remove(caratteristica)                        # remove ID feature
                            matcher.sameObj.append(ogg_lista)                           # make a list of matching objects
                            obj_list.adap.remove(ogg_lista)                             # delete the object from the list
        if(len(matcher.sameObj)>1):
            obj_out.obj[:] = []
            for oggetto_1 in matcher.sameObj:
                if (matcher.sameObj.index(oggetto_1)+1 < len(matcher.sameObj)):
                    for caratteristica_1 in matcher.sameObj[matcher.sameObj.index(oggetto_1)].obj:
                        for caratteristica_2 in matcher.sameObj[matcher.sameObj.index(oggetto_1)+1].obj:
                            if caratteristica_1.name == caratteristica_2.name:
                                for k in range(0, len(caratteristica_1.value)):
                                    new_value = str((float(caratteristica_1.value[k])+float(caratteristica_2.value[k]))/2)
                                    caratteristica_2.value[k] = new_value
                                caratteristica_1.name = "done"
                            if caratteristica_2 not in obj_out.obj:
                                obj_out.obj.append(caratteristica_2)
                        if(caratteristica_1.name != "done"):
                            obj_out.obj.append(caratteristica_1)
            matcherOut.obj[:] = obj_out.obj[:]
            matcherOut.correlation = matcher.correlation
            pub_results.publish(matcherOut)                                             # publish output
        else:
            if matcher.sameObj:
                matcherOut.obj[:] = matcher.sameObj[0].obj[:]
                matcherOut.correlation = matcher.correlation
                pub_results.publish(matcherOut)                                         # publish output

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
	pub_results = rospy.Publisher('/featureMatcher/dataPub', matcher_out, queue_size=10)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():

		rate.sleep()
