#!/usr/bin/env python

import numpy as n
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
from sofar_multimodal.msg import adapter
from sofar_multimodal.msg import feature
from sofar_multimodal.msg import obj
from sofar_multimodal.msg import commonFeature
from sofar_multimodal.msg import selectorMatcher
from sofar_multimodal.msg import corr
from sofar_multimodal.msg import correlationTable

# import functions fromcorrelation_functions.py
from correlation_functions import get_dist_2d
from correlation_functions import get_dist_3d
from correlation_functions import get_colour_name
from correlation_functions import get_RGB
from correlation_functions import get_HSV

def callback(data):	
	
	# RGB values related to a color name
	color_dictionary = {'black':[(0,0,0)],
						'blue':[0,0,255],
						'brown': [128,0,0],
						'green': [0,255,0],
						'grey': [128,128,128],
						'magenta': [255,0,255],
						'orange': [255,165,0],
						'purple': [128,0,128],
						'red': [255,0,0],
						'white': [255,255,255],
						'yellow': [255,255,0]}
						
	alfa_2d = 0.5 # weight of 2D coordinates in the correlation function
	beta_3d = 0.5
	gamma_color_rgb = 1/255
	delta_hue = 1/360
	delta_sat = 1/100
	delta_value = 1/100
	w = 20
	
	for i in range(0,len(data.matcher)):
			
			mod_perc_comp1 =data.matcher[i].common[0] # compared  perceptive module 1
			mod_perc_comp2 =data.matcher[i].common[1] # compared  perceptive module 2
			
			table = Float32MultiArray()
			table = n.zeros((len(mod_perc_comp1.adap),len(mod_perc_comp2.adap)))
			
			id_perc1= mod_perc_comp1.id_mod
			id_perc2= mod_perc_comp2.id_mod			
			
			id_tot1=list()
			id_tot2=list()
			
			for j in range(0,len(mod_perc_comp1.adap[0].obj)):				
				if mod_perc_comp1.adap[0].obj[j].name == 'id':
					for l in range(0,len(mod_perc_comp1.adap)):					
						strings = str(id_perc1)+str(mod_perc_comp1.adap[l].obj[j].value)[2:-2]
						id_tot1.append(strings)
											
					for k in range(0,len(mod_perc_comp2.adap)):					
						id_tot2.append(str(id_perc2)+str(mod_perc_comp2.adap[k].obj[j].value)[2:-2])					
				
				if mod_perc_comp1.adap[0].obj[j].name == 'pose_2d':
					
					get_dist_2d(mod_perc_comp1,mod_perc_comp2,table,alfa_2d,j)				
				
				if (mod_perc_comp1.adap[0].obj[j].name == 'pose_3d'):
					get_dist_3d(mod_perc_comp1,mod_perc_comp2,table,beta_3d,j)
				
				if (mod_perc_comp1.adap[0].obj[j].name == 'color_name'):
					get_colour_name(mod_perc_comp1,mod_perc_comp2,table,gamma_color_rgb,j)
				
				if (mod_perc_comp1.adap[0].obj[j].name == 'color_rgb'):
					get_RGB(mod_perc_comp1,mod_perc_comp2,table,gamma_color_rgb,j)				
							
				if (mod_perc_comp1.adap[0].obj[j].name == 'colour_hsv'):
					get_HSV(mod_perc_comp1,mod_perc_comp2,table,delta_hue,j)
					
			table = - table/w
			table_corr = n.tanh(table)+1
			unpackaging(id_tot1,id_tot2,table_corr)
			

def unpackaging(id_tot1,id_tot2,table_corr):	
	table_corr_unpack = correlationTable()
	for i in range(0,len(id_tot1)):
		for j in range(0,len(id_tot2)):
			single_corr = corr()
			single_corr.first_percepted_object = id_tot1[i]
			single_corr.second_percepted_object = id_tot2[j]
			single_corr.correlation = table_corr[i][j]
			table_corr_unpack.table.append(single_corr)
	
	pub=rospy.Publisher('correlationTables',correlationTable, queue_size=1)
	rate=rospy.Rate(20)
	pub.publish(table_corr_unpack)
	
	# print(id_tot1)		 
	# print(id_tot2)
	# print(table_corr)
	# print(table_corr_unpack)
		
				


def listener():
    
    rospy.init_node('table', anonymous=True)
    rospy.Subscriber('/featureScheduler/pubIntersection', selectorMatcher, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
	listener()

  



