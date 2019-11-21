	# data.matcher represents all the possible comparisons between perceptive modules
	# data.matcher[i].common represents i-th comparison between two different perceptive modules. 
	# data.matcher[i].common[0].adap. Each one of the two adapters contains n objects (perceived by modules on the scene)
	# data.matcher[i].common[0].adap[l].obj[j]. It is the l-th object perceived characterized by the j-th feature
	# data.matcher[i].common[0].adap[l].obj[j].value. They are the values of the j-th feature				
	
	

	# function implementing euclidean distances between 2d coordinates				
def	get_dist_2d(mod_perc_comp1,mod_perc_comp2,table,alfa_2d,j):
	
	for l in range(0,len(mod_perc_comp1.adap)):
		
		object_mod1=mod_perc_comp1.adap[l]
		feature_object_mod1= object_mod1.obj[j]
		
		for k in range(0,len(mod_perc_comp2.adap)):
			
			object_mod2=mod_perc_comp2.adap[k]
			feature_object_mod2 = object_mod2.obj[j]
			
			deltaX = float(feature_object_mod1 .value[0]) - float(feature_object_mod2.value[0])						
			deltaY = float(feature_object_mod1 .value[1]) - float(feature_object_mod2.value[1])
			
			table[l][k] = table[l][k] + alfa_2d*pow((pow(deltaX,2)+ pow(deltaY,2)),0.5)
	
	# function implementing euclidean distances between 3d coordinates
def get_dist_3d(mod_perc_comp1,mod_perc_comp2,table,beta_3d,j):
	
	for l in range(0,len(mod_perc_comp1.adap)):
		
		object_mod1=mod_perc_comp1.adap[l]
		feature_object_mod1 = object_mod1.obj[j]
		
		for k in range(0,len(mod_perc_comp2.adap)):
			
			object_mod2=mod_perc_comp2.adap[k]
			feature_object_mod2 = object_mod2.obj[j]
			
			deltaX = float(feature_object_mod1 .value[0]) - float(feature_object_mod2.value[0])							
			deltaY = float(feature_object_mod1 .value[1]) - float(feature_object_mod2.value[1])
			try:
				deltaZ = float(feature_object_mod1 .value[2]) - float(feature_object_mod2.value[2])
			except IndexError:
				print("OutOfIndex")
			
			table[l][k] = table[l][k] + beta_3d*pow((pow(deltaX,2)+ pow(deltaY,2)+pow(deltaZ,2)),0.5)
	
	# function converting colour name into RGB values. Then computing euclidean distances between RGB channels
def get_colour_name(mod_perc_comp1,mod_perc_comp2,table,gamma_color_rgb,j):			
	
	for l in range(0,len(mod_perc_comp1.adap)):
		
		object_mod1=mod_perc_comp1.adap[l]
		feature_object_mod1= object_mod1.obj[j]
		
		for k in range(0,len(mod_perc_comp2.adap)):
			
			object_mod2=mod_perc_comp2.adap[k]
			feature_object_mod2 = object_mod2.obj[j]
			
			color1 = color_dictionary.get(feature_object_mod1 .value[0],-1)
			color2 = color_dictionary.get(feature_object_mod2.value[0],-1)
			
			delta_color_R = gamma_color_rgb*(color1[0] - color2[0])
			delta_color_G = gamma_color_rgb*(color1[1] - color2[1])
			delta_color_B = gamma_color_rgb*(color1[2] - color2[2])
			
			table[l][k] = table[l][k] + pow((pow(delta_color_R,2) + pow(delta_color_G,2) + pow(delta_color_B,2)),0.5)
	
	# function computing euclidean distances between RGB channels
def get_RGB(mod_perc_comp1,mod_perc_comp2,table,gamma_color_rgb,j):	
	
	for l in range(0,len(mod_perc_comp1.adap)):		
		
		object_mod1=mod_perc_comp1.adap[l]
		feature_object_mod1= object_mod1.obj[j]
		
		for k in range(0,len(mod_perc_comp2.adap)):
			
			object_mod2=mod_perc_comp2.adap[k]
			feature_object_mod2 = object_mod2.obj[j]
			
			delta_color_R = gamma_color_rgb*(float(feature_object_mod1 .value[0]) - float(feature_object_mod2.value[0]))						
			delta_color_G = gamma_color_rgb*(float(feature_object_mod1 .value[1]) - float(feature_object_mod2.value[1]))
			delta_color_B = gamma_color_rgb*(float(feature_object_mod1 .value[2]) - float(feature_object_mod2.value[2]))
			
			table[l][k] = table[l][k] + pow((pow(delta_color_R,2)+ pow(delta_color_G,2)+pow(delta_color_B,2)),0.5)
	
def get_HSV(mod_perc_comp1,mod_perc_comp2,table,delta_hue,j):
	
	for l in range(0,len(mod_perc_comp1.adap)):
		
		object_mod1=mod_perc_comp1.adap[l]
		feature_object_mod1= object_mod1.obj[j]
		
		for k in range(0,len(mod_perc_comp2.adap)):
			
			object_mod2=mod_perc_comp2.adap[k]
			feature_object_mod2 = object_mod2.obj[j]
			
			delta_color_H = delta_hue*(float(feature_object_mod1 .value[0]) - float(feature_object_mod2.value[0]))							
			delta_color_S = delta_hue*(float(feature_object_mod1 .value[1]) - float(feature_object_mod2.value[1]))
			delta_color_V = delta_hue*(float(feature_object_mod1 .value[2]) - float(feature_object_mod2.value[2]))
			
			table[l][k] = table[l][k] + pow((pow(delta_color_H,2)+ pow(delta_color_S,2)+pow(delta_color_V,2)),0.5)
