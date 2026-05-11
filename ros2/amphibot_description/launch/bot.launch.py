"""
bot.launch.py
-------------
Launches the robot_state_publisher for the Amphibious Bot.
Reads the URDF/XACRO description and publishes robot TF frames.

Usage:
    ros2 launch amphibot_description bot.launch.py
    ros2 launch amphibot_description bot.launch.py use_sim_time:=true
"""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, Command
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
import xacro


def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time')
    use_ros2_control = LaunchConfiguration('use_ros2_control')

    pkg_path = os.path.join(get_package_share_directory('amphibot_description'))
    xacro_file = os.path.join(pkg_path, 'urdf', 'amphibot.xacro')

    # Process xacro file at launch time via Command substitution
    robot_description_config = Command(['xacro ', xacro_file])

    params = {
        'robot_description': robot_description_config,
        'use_sim_time': use_sim_time,
    }

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params],
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description=(
                "Set to 'true' to subscribe to /clock and sync "
                "to simulation time published by Gazebo."
            ),
        ),
        DeclareLaunchArgument(
            'use_ros2_control',
            default_value='true',
            description="Enable ros2_control hardware interface.",
        ),
        robot_state_publisher,
    ])
