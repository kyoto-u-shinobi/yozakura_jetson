#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import rospy
from yozakura_msgs.msg import ArmState, YozakuraCommand
from std_msgs.msg import Float32MultiArray, Int16MultiArray

# remap-able names
DEFAULT_NODE_NAME = 'command_distributor'
DEFAULT_PUB_ARM_COMMAND_TOPIC_NAME = "arm_command"
DEFAULT_PUB_MOTOR_COMMAND_TOPIC_NAME = "motor_command"
DEFAULT_SUB_COMMAND_TOPIC_NAME = 'yozakura_command'

class CommandDistributor(object):
    def __init__(self):
        self._pub_arm_command = rospy.Publisher(DEFAULT_PUB_ARM_COMMAND_TOPIC_NAME, Int16MultiArray, queue_size=10)
        self._arm_command = Int16MultiArray()

        self._pub_motor_command = rospy.Publisher(DEFAULT_PUB_MOTOR_COMMAND_TOPIC_NAME, Float32MultiArray, queue_size=10)
        self._motor_command = Float32MultiArray()

        self.is_active = False

    def activate(self):
        rospy.Subscriber(DEFAULT_SUB_COMMAND_TOPIC_NAME, YozakuraCommand, self.command_callback)

        self.is_active = True

    def command_callback(self, command):
        self._arm_command.data = [-int(command.arm_vel.base_yaw), -int(command.arm_vel.base_pitch), -int(command.arm_vel.base_pitch), int(command.arm_vel.elbow_pitch), int(command.arm_vel.wrist_yaw), command.arm_vel.home_command]
        self._motor_command.data = [command.wheel_right_vel, command.wheel_left_vel, command.wheel_right_vel, command.wheel_left_vel]

    def publish_data(self):
        if not self.is_active:
            self.activate()
        self._pub_arm_command.publish(self._arm_command)
        self._pub_motor_command.publish(self._motor_command)

# ------------------------------
if __name__ == '__main__':
    rospy.init_node(DEFAULT_NODE_NAME, anonymous=True)
    rate_mgr = rospy.Rate(30)
    
    command_distributor = CommandDistributor()
    command_distributor.activate()

    while not rospy.is_shutdown():
        command_distributor.publish_data()
        rate_mgr.sleep()
#        rospy.spin()
