#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from robot_monitor_interfaces.msg import RobotStatus

class PublisherNode(Node):
    def __init__(self):
        super().__init__("publisher_node")
        self.robot_status_publisher = self.create_publisher(
            RobotStatus,"/robot_status",10
        )
        self.timer = self.create_timer(1.0,self.publish_robot_status)

    def publish_robot_status(self):
        msg = RobotStatus()
        msg.battery_level = 75.0
        msg.is_moving = True
        msg.status_msg = "Robot moving"
        self.robot_status_publisher.publish(msg)


def main(args = None):
    # inititalize the ROS client library
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()