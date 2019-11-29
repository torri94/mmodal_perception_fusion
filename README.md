# A Software Architecture for Multimodal Semantic Perception Fusion

## Objective of the Project
The project proposes an implementation of architecture to fuse geometric features computed from point clouds and Convolution Neural Network (CNN) classifications, based on images.

## The System’s Architecture

### Overall Architecture
Architecture fuses geometric features computed from N-perception modules.
This implementation uses two perception modules, point clouds (PITT) and Convolution Neural Network (CNN - TensorFlow).
Between a Perception module and Feature selector module, there is an Adapter to implement a standard message for each perception module.
Then, Feature Selector receives all the information acquired by the sensors and produces two outputs. An intersection of data that identifies any common features between the objects from different perception modules and an union data containing all information from the sensors.
Correlation Table Manager takes union data and __........__
Reasoner takes in input the output of Correlation Table Manager and generates an index of correlation for objects recognized from different perception modules __..........__
Finally the Feature Selector join the data from Reasoner and Feature Selector module by searching for objects' IDs and assorting all features coming from different perceptive modules. Then, it returns an output message for each object recognized comprehensive with all information collected by the various sensors.


<p align="center"> 
<img src="https://github.com/EmaroLab/mmodal_perception_fusion/blob/master/imgs/Schermata%202019-11-14%20alle%2014.55.55.png">
</p>

#### Messages
##### Feature.msg

```
string types
string name
string[] value
```
##### Obj.msg

```
feature[] obj
```
##### Adapter.msg

```
uint32 id_mod
obj[] adap
```
##### CommonFeature.msg

```
adapter[] common
```
##### FeatureMatcher.msg

```
commonFeature[] matcher
```
##### Corr.msg

```
string first_percepted_object
string second_percepted_object
float32 correlation
```
##### CorrelationTable.msg

```
corr[] table
```
##### Record.msg

```
string[] rec
float32 corr
```
##### OutputReasoner.msg

```
record[] lines
```
##### MatcherObj.msg

```
obj[] sameObj
float32 correlation
```
##### Matcher_out.msg

```
feature[] obj
float32 correlation
```
#### Messages Rappresentation

<p align="center"> 
<img src="https://github.com/EmaroLab/mmodal_perception_fusion/blob/master/imgs/Schermata%202019-11-14%20alle%2016.39.25.png">
</p>

### Description of the Modules
#### PITT Perception module
It describes all the modules within the architecture, i.e, (i) the inputs, (ii) the internal working, and (iii) the outputs.
* __Input__: 
* __Output__:
* __Publisher__: [__O1__]

#### Tensorflow Perception module
It describes all the modules within the architecture, i.e, (i) the inputs, (ii) the internal working, and (iii) the outputs.
* __Input__: 
* __Output__:
* __Publisher__: [__O2__]

#### Adapter module
It's a module between a perception module and Feature selector module and makes a standard message for each perception module.  We provide an adapter for the Pitt module and another for the Tensorflow module. 
To add another perception module, it needs to implement a different adapter.
* __Input__: a type of message of a perception module
* __Output__: an adapter.msg
* __Publisher__: /outputAdapterPitt | /outputAdapterTensor

#### Features Selector module
It receives all the information acquired by the sensors, storing them inside a buffer.
It produces two outputs: the first one transmits the information saved in the buffer to the "Feature Matcher" and the other output transmits to the "Correlation Table Manager" module.
For the second output, the module identifies any common features between the objects recognized by the sensors (for example, shape or color).
* __Input__: an adapter.msg
* __Output__: a selectorMatcher.msg
* __Publisher__: /featureScheduler/pubIntersection [__F__]| /featureScheduler/pubUnion [__R__]

#### Features Matcher module
In this module, the data received from the Reasoner and the Feature Selector are joined.
From the Reasoner, this module receives the objects' IDs detected by different perception modules plus the degree of correlation (a number that indicates the reliability of the analysis obtained).
From Feature Selector, Feature Matcher receives all data of objects detected.
The Features Matcher finds the information by searching for objects' IDs and assorting all features coming from different perceptive modules. Then, it returns an output message for each object recognized comprehensive with all information collected by the various sensors.
* __Input__: a selectorMatcher.msg | outputReasoner.msg
* __Output__: a matcher_out.msg
* __Publisher__: /featureMatcher/dataPub [__P__]

#### Table matcher module
It describes all the modules within the architecture, i.e, (i) the inputs, (ii) the internal working, and (iii) the outputs.
* __Input__: 
* __Output__:
* __Publisher__: [__T__]

#### Reasoner module
It describes all the modules within the architecture, i.e, (i) the inputs, (ii) the internal working, and (iii) the outputs.
* __Input__: 
* __Output__:
* __Publisher__: [__U__]

## Implementation

### Prerequisites
On the machine must be installed RoS with rospy and python.

### Installation
```
cd catkin_ws/src/
catkin_create_pkg sofar_multimodal std_msgs rospy roscpp
catkin_make
 . ~/catkin_ws/devel/setup.bash
cd sofar_multimodal
git clone https://github.com/EmaroLab/mmodal_perception_fusion.git .
catkin_make
```
### How to run the project

```
cd sofar_multimodal
roscore &
source devel/setupe.bash
rosrun sofar_multimodal talkerPitt &
rosrun sofar_multimodal talkerTensor &
rosrun sofar_multimodal adapterPitt &
rosrun sofar_multimodal adapterTensor &
rosrun sofar_multimodal featureScheduler.py &
rosrun sofar_multimodal tableMatcher.py &
rosrun sofar_multimodal reasonerMain.py &
rosrun sofar_multimodal featuresMatcher.py &
```
To monitor the output:
```
rostpic echo /featureMatcher/dataPub
```

## Results

<p align="center"> 
<img src="https://github.com/EmaroLab/mmodal_perception_fusion/blob/master/imgs/VirtualBox_EmaroBox_1_29_11_2019_16_32_49.png?raw=true">
</p>

### Video
[![Watch the video](https://github.com/EmaroLab/mmodal_perception_fusion/blob/master/imgs/VirtualBox_EmaroBox_1_21_11_2019_11_53_42.png)](https://www.youtube.com/embed/JwPSA9yZG2A)

## Recommendations
To add a perception module, you will need to add an Adapter module between perception module and feature selector module.
Then, add a subscriber and its callback in featureScheduler.py by following the [commented example](https://github.com/EmaroLab/mmodal_perception_fusion/blob/a56460ff915c84362d3897307453054a5fdfaa02/scripts/featureScheduler.py#L104-L105) into the script.

In [docs](https://github.com/EmaroLab/mmodal_perception_fusion/blob/master/docs/) directory there is the doxygen documentation in html or latex format.


## Authors
* Filippo Lapide

* Vittoriofranco Vagge

* Maicol Polvere
* Daniele Torrigino
* Francesco Giovinazzo

* Nicolò Baldassarre
* Andrea Rusconi
* Matteo Panzera

* Francesco Bruno
* Ariel Gjaci
