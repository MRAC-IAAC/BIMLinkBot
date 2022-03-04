#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool
from std_msgs.msg import Int8
from geometry_msgs.msg import TransformStamped
from geometry_msgs.msg import PointStamped
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Point
from nav_msgs.msg import Odometry
from std_msgs.msg import Empty
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
import tf
from tf.transformations import euler_from_quaternion
from math import degrees
import random
import math
import pdb

markerCounter = 0
markerArray = []
coordArray = []

def callback_button(data):
    #get the status published by the visp tracker, get the QR position if the state is between 2-5
    if data.data > 1:
        sub = rospy.wait_for_message('object_position',PoseStamped)
        create_marker(sub)

def callback_odom(data):
    print("test")

def create_marker(data):
    
    global markerArray

    global markerCounter

    global coordArray

    #get QR code positions 
    robotMarker = Marker()
    robotMarker.pose.position.x = data.pose.pose.position.x
    robotMarker.pose.position.y = data.pose.pose.position.y
    robotMarker.pose.position.z = data.pose.pose.position.z
    robotMarker.pose.orientation.x = data.pose.pose.orientation.x
    robotMarker.pose.orientation.y = data.pose.pose.orientation.y
    robotMarker.pose.orientation.z = data.pose.pose.orientation.z
    robotMarker.pose.orientation.w = 1
    robotMarker.header.frame_id = "map"
    robotMarker.header.stamp = rospy.Time.now()
    robotMarker.ns = "robot"
    robotMarker.type = 0 # arrow
    robotMarker.action = 0
    robotMarker.scale.x = 0.5
    robotMarker.scale.y = 0.1
    robotMarker.scale.z = 0.1
    robotMarker.color.r = 0.0
    robotMarker.color.g = 1.0
    robotMarker.color.b = 0.0
    robotMarker.color.a = 1.0
    robotMarker.lifetime = rospy.Duration(0)
    robotMarker.id = random.getrandbits(16)

    cx = robotMarker.pose.position.x 
    cy = robotMarker.pose.position.y 
    cz = robotMarker.pose.position.z
    coords = (cx, cy, cz)

    distArray = []
    
    #add new marker if distance is far enough from previously created markers
    if markerCounter > 0:
        print(markerCounter)
        print(len(markerArray))
        for c in coordArray:
            mx = c[0]
            my = c[1]
            mz = c[2]
            print(my)

            x = robotMarker.pose.position.x
            y = robotMarker.pose.position.y
            z = robotMarker.pose.position.z
            print(x)
            d = math.sqrt(math.pow(mx - x, 2) + math.pow(my - y, 2) + math.pow(mz - z, 2)* 1.0)
            distArray.append(d)
            print(distArray)
            minDist = min(distArray)
            print("Minimum Distance: "+ str(minDist))
        if (minDist > 0.5):
            markerCounter += 1
            markerPub.publish(robotMarker)
            print (coords)
            coordArray.append(coords)
            print(coordArray)
            markerArray.append(robotMarker)
            print ("There are "+str(len(markerArray))+" markers")
            print(str(d))
            print(len(distArray))
            return
                
    else:
        markerCounter += 1
        coordArray.append(coords)
        markerArray.append(robotMarker)
        markerPub.publish(robotMarker)
        print ("There is "+str(len(markerArray))+" marker")
        rate.sleep()
        return

if __name__ == '__main__':
    rospy.init_node('tf',anonymous = True)
    rate = rospy.Rate(1) # 10hz
    #Starts script on user input
    print("Type y and press enter")
    try:
        while not rospy.is_shutdown():
            toggle = raw_input()
            print("I'm printing")
            #for visp tracker
            rospy.Subscriber('status',Int8, callback_button)
            markerPub = rospy.Publisher('robotMarker', Marker, queue_size=10)
            rospy.spin()
            rate.sleep()
    except rospy.ROSInterruptException:
        pass
    