#!/usr/bin/env python3

# Import necessary libraries
import rclpy
from rclpy.node import Node
from robot_monitor_interfaces.msg import RobotStatus

# Define the PublisherNode class
class PublisherNode(Node):

    # Initialize the node and create a publisher
    def __init__(self):
        # Call the constructor of the parent class
        super().__init__("publisher_node")
        # Create a publisher for the RobotStatus message type
        self.robot_status_publisher = self.create_publisher(
            RobotStatus,"/robot_status",10
        )
        # Create a timer to publish robot status every second
        self.timer = self.create_timer(1.0,self.publish_robot_status)

    # Define the method to publish robot status
    def publish_robot_status(self):
        # Create a RobotStatus message and populate it with data
        msg = RobotStatus()
        msg.battery_level = 75.0
        msg.is_moving = True
        msg.status_msg = "Robot moving"
        # Publish the message to the topic
        self.robot_status_publisher.publish(msg)

# Define the main function to run the node
def main(args = None):
    # inititalize the ROS client library
    rclpy.init(args=args)

    # create the publisher node
    node = PublisherNode()

    # Keeping the node alive to publish messages
    rclpy.spin(node)

    # Shutdown the ROS client library
    rclpy.shutdown()
