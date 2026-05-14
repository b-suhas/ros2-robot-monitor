#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from robot_monitor_interfaces.msg import RobotStatus

class SubscriberNode(Node):
    def __init__(self):
        super().__init__("subscriber_node")
        self.robot_status_subscription = self.create_subscription(
            RobotStatus,"/robot_status",self.robot_status_callback,10 
            )
        
    def robot_status_callback(self,msg):
        self.get_logger().info(f"\n===== ROBOT STATUS =====\nBattery Level : {msg.battery_level} %\nIs Moving     : {msg.is_moving}\nMessage       : {msg.status_msg}\n========================")
    

def main(args = None):
    # inititalize the ROS client library
    rclpy.init(args=args)
    node = SubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()