# BIMLinkBot
Using ROS and QR code tracking with a Turtlebot 2 to detect and map QR codes in 3D space.

__Workflow:__
Use SLAM to map the space and run AMCL to navigate the robot. As QR codes' are detected by the camera, markers will be published at the QR codes positions.


## Requirements: 
* [Turtlebot 2](http://wiki.ros.org/Robots/TurtleBot)
* [ROS Melodic](http://wiki.ros.org/melodic/Installation/Ubuntu) (Ubuntu 18.04)
* Camera ([Orbbec Astra](http://wiki.ros.org/astra_camera)  used here)
* [visp_auto_tracker](http://wiki.ros.org/visp_auto_tracker)
* [slam_gmapping](http://wiki.ros.org/gmapping)
* [Lidar](http://wiki.ros.org/rplidar_ros)

## Getting Started:
* catkin_make the packages mentioned in the Requirements section
* use gmapping to SLAM the space
* with AMCL running, run the vispMarker.py script
* navigate space, as the camera detects the QR codes, the markers will be published (note: you may need to turn on the marker visibility after the first is detected - it may not appear as a topic until the first detection is made. If this is the case, kill and rerun the python script after turning on the marker topic visibility)

## Future Improvements:
* The ultimate goal of this project would include developing an interface with a database accessible upon scanning the QR codes. This would provide a new workflow for site issue management and coordination, giving stakeholders the ability to communicate and track issues and bind them to 3D coordinates accessible in other BIM software.
* The markers in the current code do not use the proper frame when set. As such, they don't properly populate in RViz and seem to move around with the robot.

## References: 
* [ROS Markers](http://wiki.ros.org/rviz/DisplayTypes/Marker)
* [Check Sheets](https://en.wikipedia.org/wiki/Check_sheet) & [Punch Lists](https://en.wikipedia.org/wiki/Punch_list) description for those unaware

Credits: Based on IAAC publishing guidelines:
BIMLinkBot is a project of IaaC, Institute for Advanced Architecture of Catalonia. developed at Master in Robotics and Advanced Construction in 2019-2020 by:

Students: Alfred Bowles, Amy Yeo Jeong Kim, Chris Booth, Robert Michael Blackburn, Tomas Quijano

Faculty: Carlos Rizzo, Vincent Huyghe

