# JetBot LUIS Command Parser ROS Node
ROS node to translate intents from the Azure Language Understanding Intelligent Service (LUIS) to motor commands for the NVIDIA JetBot. This node works alongside the Azure LUIS ROS node and NVIDIA JetBot ROS node to create an end-to-end, cross-device demo for using voice commands to control the robot. In the demo, this node and the LUIS ROS node run on a Windows PC, while the JetBot ROS node runs on the Jetson Nano inside the NVIDIA JetBot.

## Setup Instructions (Windows)
First, follow setup instructions for the ROS LUIS node here: https://github.com/ms-iot/ros_msft_luis#building-on-windows. This includes installing ROS Melodic and setting up a catkin workspace if you have not already done so.  
  
Then, navigate to the src folder and clone this repo:
```
cd c:\ws\luis_ws\src
git clone https://github.com/gitri-ms/jetbot_luis_cmd_parser
cd ..
catkin_make
devel\setup.bat
```
