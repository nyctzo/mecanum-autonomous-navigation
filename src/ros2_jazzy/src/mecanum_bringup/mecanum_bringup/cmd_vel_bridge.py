#!/usr/bin/env python3

import rclpy

from rclpy.node import Node

from geometry_msgs.msg import Twist
from geometry_msgs.msg import TwistStamped


class CmdVelBridge(Node):

    def __init__(self):
        super().__init__("cmd_vel_bridge")

        self.sub = self.create_subscription(
            Twist,
            "/cmd_vel",
            self.cmd_callback,
            10,
        )

        self.pub = self.create_publisher(
            TwistStamped,
            "/mecanum_drive_controller/reference",
            10,
        )

        self.get_logger().info("cmd_vel bridge started")

    def cmd_callback(self, msg):

        stamped = TwistStamped()

        stamped.header.stamp = self.get_clock().now().to_msg()
        stamped.header.frame_id = "base_link"

        stamped.twist = msg

        self.pub.publish(stamped)


def main(args=None):

    rclpy.init(args=args)

    node = CmdVelBridge()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()

