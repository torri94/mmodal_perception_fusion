"""
THIS FILE CONTAINS ALL THE METHODS USED FOR COMPUTING THE DISTANCE BETWEEN DIFFERENT FEATURE VALUES. AT THE CURRENT STATE  
IT CONTAINS 5 METHODS

- get_dist_2d: 		FUNCTION IMPLEMENTING EUCLIDEAN DISTANCE BETWEEN 2D COORDINATES

- get_dist_3d: 		FUNCTION IMPLEMENTING EUCLIDEAN DISTANCE BETWEEN 3D COORDINATES

- get_colour_name:  FUNCTION CONVERTING COLOUR NAME INTO RGB VALUES. THEN COMPUTING EUCLIDEAN DISTANCES BETWEEN RGB CHANNELS

- get_RGB:		    FUNCTION COMPUTING EUCLIDEAN DISTANCES BETWEEN RGB CHANNELS

- get_HSV:			FUNCTION COMPUTING EUCLIDEAN DISTANCES BETWEEN HSV CHANNELS

ADD OTHER POSSIBLE METHODS. DO NOT FORGET TO IMPORT WHERE NECESSARY THE DEFINED FUNCTION IN A SCRIPT

BESIDES HERE WE HAVE USED THE EUCLIDEAN DISTANCE FOR ALL THE METHODS BUT IT IS POSSIBLE TO DEFINE OTHER TYPES OF DISTANCE FUNCTIONS		
"""

def euclidean_distance(delta):
	
	temp = 0
	
	for l in range(0,len(delta)):
		temp = temp + pow(delta[l],2)
	
	distance = pow(temp,0.5)
	
	#print(distance)
	return distance
	

# 	FUNCTION IMPLEMENTING EUCLIDEAN DISTANCE BETWEEN 2D COORDINATES
			
def	get_dist_2d(mod_perc_comp1,mod_perc_comp2,table,alfa_2d,j):
	
	# n1 = number of objects perceived from the compared  perceptive module 1
	# n2 = number of objects perceived from the compared  perceptive module 2
	
	n1 = len(mod_perc_comp1.adap)
	n2 = len(mod_perc_comp2.adap)

	
	for l in range(0,n1): 
		
		object_mod1 = mod_perc_comp1.adap[l] 		# l-th object from perceptive module one
		feature_object_mod1 = object_mod1.obj[j] 	# j-th feature (obj[j]) of the l-th object. In this case obj[j]="pose_2d".
		
		for k in range(0,n2): 
			
			delta = list()			
						
			object_mod2=mod_perc_comp2.adap[k] 			# k-th object from perceptive module two. 
			feature_object_mod2 = object_mod2.obj[j] 	# j-th feature (obj[j]) of the k-th object. In this case obj[j]="pose_2d".
			
			deltaX = float(feature_object_mod1.value[0]) - float(feature_object_mod2.value[0])		# distance of x coordinates				
			deltaY = float(feature_object_mod1.value[1]) - float(feature_object_mod2.value[1]) 		# distance of y coordinates	

			delta.append(deltaX)
			delta.append(deltaY)
			
			#print(delta)
			
			distance = euclidean_distance(delta)		
			
			# updating the table at the position [l][k] with the performed euclidean distance
			table[l][k] = table[l][k] + alfa_2d*distance 
			
			#print(table)
			#print(' ')
#----------------------------------------------------------------------------------------------------------------------------------			
			
#	FUNCTION IMPLEMENTING EUCLIDEAN DISTANCE BETWEEN 3D COORDINATES	
	
def get_dist_3d(mod_perc_comp1,mod_perc_comp2,table,beta_3d,j):
	
	# n1 = number of objects perceived from the compared  perceptive module 1
	# n2 = number of objects perceived from the compared  perceptive module 2
	
	n1 = len(mod_perc_comp1.adap)
	n2 = len(mod_perc_comp2.adap)
	
	for l in range(0,n1): 
		
		object_mod1=mod_perc_comp1.adap[l] 			# l-th object from perceptive module one		
		feature_object_mod1 = object_mod1.obj[j] 	# j-th feature (obj[j]) of the l-th object. In this case obj[j]="pose_3d".
		
		for k in range(0,n2):  
			
			delta = list()
			
			object_mod2=mod_perc_comp2.adap[k] 			# k-th object from perceptive module two
			feature_object_mod2 = object_mod2.obj[j] 	# j-th feature (obj[j]) of the k-th object. In this case obj[j]="pose_3d".
			
			deltaX = float(feature_object_mod1 .value[0]) - float(feature_object_mod2.value[0])		# distance of x coordinates						
			deltaY = float(feature_object_mod1 .value[1]) - float(feature_object_mod2.value[1]) 	# distance of y coordinates	
			deltaZ = float(feature_object_mod1 .value[2]) - float(feature_object_mod2.value[2]) 	# distance of z coordinates	
			
			delta.append(deltaX)
			delta.append(deltaY)
			delta.append(deltaZ)
			
			distance = euclidean_distance(delta)
			
			# updating the table at the position [l][k] with the performed euclidean distance
			table[l][k] = table[l][k] + beta_3d*distance
			
#----------------------------------------------------------------------------------------------------------------------------------		

# FUNCTION CONVERTING COLOUR NAME INTO RGB VALUES. THEN COMPUTING EUCLIDEAN DISTANCES BETWEEN RGB CHANNELS
	
def get_colour_name(mod_perc_comp1,mod_perc_comp2,table,gamma_color_rgb,j):			
	
	# n1 = number of objects perceived from the compared  perceptive module 1
	# n2 = number of objects perceived from the compared  perceptive module 2
	
	# RGB values related to a color name. creation of a dictionary
	color_dictionary = {'black':[0,0,0],
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
	
	n1 = len(mod_perc_comp1.adap)
	n2 = len(mod_perc_comp2.adap)
	#print(table)	
	# When a colour is not recognized the table is not modified. 
		# copy function used to store the original matrix
	
	
	for l in range(0,n1):  
		
		object_mod1=mod_perc_comp1.adap[l]		# l-th object from perceptive module one
		feature_object_mod1= object_mod1.obj[j]	# j-th feature (obj[j]) of the l-th object. In this case obj[j]="color_name".
		
		#color1 = color_dictionary.get(feature_object_mod1.value[0],-1)
		#print(color1)
		#print(feature_object_mod1)
		#print(' ')
		
		for k in range(0,n2):	
			
			#print(table)
			#print(original_table)
			
			object_mod2=mod_perc_comp2.adap[k]			# k-th object from perceptive module two
			feature_object_mod2 = object_mod2.obj[j]	# j-th feature (obj[j]) of the k-th object. In this case obj[j]="color_name".
			
			#print(feature_object_mod2)
			
			delta = list()
			
			
			# get the RGB values for a given colour name. colour1 from perceptive module one
			color1 = color_dictionary.get(feature_object_mod1 .value[0],-1) 			
			# get the RGB values for a given colour name. colour2 from perceptive module two
			color2 = color_dictionary.get(feature_object_mod2.value[0],-1)
			
			if (color1 == -1 or color2 ==-1):
				print("ATTENTION: THE COLOUR '" + feature_object_mod1 .value[0] + "' NOT RECOGNIZED")			
				#print(table)			
				return -1
			
			# weighted distance of red values of two objects of two different perceptive module
			delta_color_R = gamma_color_rgb*(color1[0] - color2[0]) 			
			# weighted distance of green values of two objects of two different perceptive module
			delta_color_G = gamma_color_rgb*(color1[1] - color2[1])			
			# weighted distance of blue values of two objects of two different perceptive module
			delta_color_B = gamma_color_rgb*(color1[2] - color2[2])
			
			delta.append(delta_color_R)
			delta.append(delta_color_G)
			delta.append(delta_color_B)
			
			distance = euclidean_distance(delta)
			
			# updating the table at the position [l][k] with the performed euclidean distance
			table[l][k] = table[l][k] + distance
	
	#print(table)
	#print(' ')
#----------------------------------------------------------------------------------------------------------------------------------	

# FUNCTION COMPUTING EUCLIDEAN DISTANCES BETWEEN RGB CHANNELS

def get_RGB(mod_perc_comp1,mod_perc_comp2,table,gamma_color_rgb,j):	
	
	# n1 = number of objects perceived from the compared  perceptive module 1
	# n2 = number of objects perceived from the compared  perceptive module 2
	
	n1 = len(mod_perc_comp1.adap)
	n2 = len(mod_perc_comp2.adap)	
	
	for l in range(0,n1):		 
		
		object_mod1=mod_perc_comp1.adap[l]			# l-th object from perceptive module one
		feature_object_mod1= object_mod1.obj[j]		# j-th feature (obj[j]) of the l-th object. In this case obj[j]="color_rgb".
		
		for k in range(0,n2):	
			
			object_mod2=mod_perc_comp2.adap[k]			# k-th object from perceptive module two
			feature_object_mod2 = object_mod2.obj[j] 	# j-th feature (obj[j]) of the k-th object. In this case obj[j]="color_rgb".
			
			delta = list()
			
			# weighted distance of red values of two objects of two different perceptive module
			delta_color_R = gamma_color_rgb*(float(feature_object_mod1 .value[0]) - float(feature_object_mod2.value[0]))						
			# weighted distance of green values of two objects of two different perceptive module
			delta_color_G = gamma_color_rgb*(float(feature_object_mod1 .value[1]) - float(feature_object_mod2.value[1]))
			# weighted distance of blue values of two objects of two different perceptive module
			delta_color_B = gamma_color_rgb*(float(feature_object_mod1 .value[2]) - float(feature_object_mod2.value[2]))
			
			delta.append(delta_color_R)
			delta.append(delta_color_G)
			delta.append(delta_color_B)
			
			distance = euclidean_distance(delta)
			
			# updating the table at the position [l][k] with the performed euclidean distance
			table[l][k] = table[l][k] + distance
			
	#print(table)
	#print(' ')		
#----------------------------------------------------------------------------------------------------------------------------------	

# FUNCTION COMPUTING EUCLIDEAN DISTANCES BETWEEN HSV CHANNELS

def get_HSV(mod_perc_comp1,mod_perc_comp2,table,delta_hue,delta_sat,delta_value,j):
	
	# n1 = number of objects perceived from the compared  perceptive module 1
	# n2 = number of objects perceived from the compared  perceptive module 2
	
	n1 = len(mod_perc_comp1.adap)
	n2 = len(mod_perc_comp2.adap)
	
	for l in range(0,n1):  
		
		object_mod1=mod_perc_comp1.adap[l]		 # l-th object from perceptive module one
		feature_object_mod1= object_mod1.obj[j]	 # j-th feature (obj[j]) of the l-th object. In this case obj[j]="color_hsv".
		
		for k in range(0,n2):	
			
			object_mod2=mod_perc_comp2.adap[k]			# k-th object from perceptive module two
			feature_object_mod2 = object_mod2.obj[j] 	# j-th feature (obj[j]) of the k-th object. In this case obj[j]="color_hsv".
			
			delta = list()
			
			# weighted distance of hue values of two objects of two different perceptive module
			delta_color_H = delta_hue*(float(feature_object_mod1 .value[0]) - float(feature_object_mod2.value[0]))							
			# weighted distance of saturation values of two objects of two different perceptive module
			delta_color_S = delta_sat*(float(feature_object_mod1 .value[1]) - float(feature_object_mod2.value[1]))
			# weighted distance of value values of two objects of two different perceptive module
			delta_color_V = delta_value*(float(feature_object_mod1 .value[2]) - float(feature_object_mod2.value[2]))
			
			delta.append(delta_color_H)
			delta.append(delta_color_S)
			delta.append(delta_color_V)
			
			distance = euclidean_distance(delta)
			
			# updating the table at the position [l][k] with the performed euclidean distance
			table[l][k] = table[l][k] + distance
