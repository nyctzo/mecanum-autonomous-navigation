#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from tf2_msgs.msg import TFMessage


class TFOdomBridge(Node):

    def __init__(self):
        super().__init__("tf_odom_bridge")

        self.subscription = self.create_subscription(
            TFMessage,
            "/mecanum_drive_controller/tf_odometry",
            self.callback,
            10,
        )

        self.publisher = self.create_publisher(
            TFMessage,
            "/tf",
            10,
        )

        self.get_logger().info("TF odom bridge started.")

    def callback(self, msg):
        self.get_logger().info("Received TF")
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = TFOdomBridge()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
