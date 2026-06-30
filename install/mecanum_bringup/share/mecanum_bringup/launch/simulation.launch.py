from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

import os


def generate_launch_description():

    description_pkg = get_package_share_directory(
        "my_robot_description"
    )

    bringup_pkg = get_package_share_directory(
        "mecanum_bringup"
    )

    gazebo_launch = os.path.join(
        description_pkg,
        "launch",
        "gazebo_robot.launch.py",
    )

    controllers_launch = os.path.join(
        bringup_pkg,
        "launch",
        "controllers.launch.py",
    )

    set_gz_plugin_path = SetEnvironmentVariable(
        name="GZ_SIM_SYSTEM_PLUGIN_PATH",
        value="/opt/ros/jazzy/lib",
    )

    cmd_vel_bridge = Node(
        package="mecanum_bringup",
        executable="cmd_vel_bridge",
        name="cmd_vel_bridge",
        output="screen",
    )

    tf_odom_bridge = Node(
        package="mecanum_bringup",
        executable="tf_odom_bridge",
        name="tf_odom_bridge",
        output="screen",
    )

    return LaunchDescription([

        set_gz_plugin_path,

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                gazebo_launch
            )
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                controllers_launch
            )
        ),

        cmd_vel_bridge,

        tf_odom_bridge,

    ])
