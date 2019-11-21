#!/usr/bin/env python
"""
author:    Filippo Lapide
author:	Vittoriofranco Vagge
"""
import rospy
from std_msgs.msg import *
from sofar_multimodal.msg import *

#INITIALIZATION
copy_buf = commonFeature()											
commonObj = commonFeature()
union_objs = selectorMatcher()
compare = commonFeature()
output = selectorMatcher()
common_feature = []
name_common = []

##Function
def comparison(buffer):
	global common_feature, name_common
	##
	# The function that compare common features from objects by N different perception modules
	name_common_mem = []
	output.matcher[:] = []
	union_objs.matcher[:] = []
	if(len(buffer.common)>1):
		"""Loop to create the union objects struct to publish to FeatureMatcher module"""
		for k in range(0,len(buffer.common)):
			for j in range(k+1,len(buffer.common)):
				commonObj.common[:] = []
				commonObj.common.append(buffer.common[k])
				commonObj.common.append(buffer.common[j])
				union_objs.matcher.append(commonObj)
		pub_union.publish(union_objs)										#PUBLISHER UNION DATA

		"""Loop to create the intersection objects struct to publish to tableMatcher module"""
		for k in range(0,len(buffer.common)):
			for j in range(k+1,len(buffer.common)):
				for oggetto in range(0,len(buffer.common[k].adap)):
					if not (buffer.common[k].adap):
						return
					"""Loop to compare all features from different perption modules and find the common"""
					for feature in range(0, len(buffer.common[k].adap[oggetto].obj)):
						if not (buffer.common[j].adap):
							return
						for feature_2 in range(0, len(buffer.common[j].adap[0].obj)):
							try:
								if(buffer.common[k].adap[oggetto].obj[feature].name ==  buffer.common[j].adap[0].obj[feature_2].name):
									common_feature.append(feature)
							except IndexError:
								print("OutOfIndex")

					"""Loop to delete common feature of objects from scene read by K perception module""" 
					for feature in range(len(buffer.common[k].adap[oggetto].obj)-1,-1,-1):
						if common_feature:
							if(feature==common_feature[-1]):
								name_common.append(buffer.common[k].adap[oggetto].obj[feature].name)
								common_feature.pop()
							else:
								del(buffer.common[k].adap[oggetto].obj[feature])
						else:
							del(buffer.common[k].adap[oggetto].obj[feature])
					name_common_mem = list(name_common)
					name_common[:]=[]

				"""Loop to delete common feature of objects from scene read by J perception module"""
				for oggetto in range(0,len(buffer.common[j].adap)):
					name_temp = list(name_common_mem)
					for feature in range(len(buffer.common[j].adap[oggetto].obj)-1,-1,-1):
						if name_temp:
							if(buffer.common[j].adap[oggetto].obj[feature].name == name_temp[0]):
								del(name_temp[0])
							else:
								del(buffer.common[j].adap[oggetto].obj[feature])
						else:
							del(buffer.common[j].adap[oggetto].obj[feature])
	
				compare.common[:] = []
				compare.common.append(buffer.common[k])
				compare.common.append(buffer.common[j])
				output.matcher.append(compare)				

		if not (output.matcher[0].common[0].adap):
			return
		elif not (output.matcher[0].common[0].adap[0]):
			return
		pub_intersect.publish(output)										#PUBLISHER INTERSECTION DATA

##Function
def checkNewValue(value, buffer):
	##
	# Function to checks if there are any older values from the same perception module to replace
	for k in range(0,len(buffer.common)):
		if(value.id_mod == buffer.common[k].id_mod):
			buffer.common[k] = value
			return
	buffer.common.append(value)
	
##

#CALLBACKS
"""If you have more perception modules, add here the proper callback"""
# def callbackNewModule(adapter):
# 	checkNewValue(adapter, copy_buf)
##CALLBACK
def callbackPitt(adapter):
	checkNewValue(adapter, copy_buf)
##CALLBACK
def callbackTensor(adapter):
	checkNewValue(adapter,copy_buf)

	
if __name__ == '__main__':
	rospy.loginfo("Running...")
	rospy.init_node('selectorMatcher', anonymous=True)
	##SUBSCRIBER
	sub_pitt = rospy.Subscriber('outputAdapterPitt', adapter, callbackPitt)
	##SUBSCRIBER
	sub_tensor = rospy.Subscriber('outputAdapterTensor', adapter, callbackTensor)
	##PUBLISHER
	pub_intersect = rospy.Publisher('/featureScheduler/pubIntersection', selectorMatcher, queue_size=10)
	##PUBLISHER
	pub_union = rospy.Publisher('/featureScheduler/pubUnion', selectorMatcher, queue_size=10)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		comparison(copy_buf)

		rate.sleep()
