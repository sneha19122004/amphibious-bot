"""
display.launch.py
-----------------
Launches robot_state_publisher + joint_state_publisher + RViz2
for visualising the Amphibious Bot URDF model.

Usage:
    ros2 launch amphibot_description display.launch.py
    ros2 launch amphibot_description display.launch.py gui:=False
"""

import os
import xacro

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    share_dir = get_package_share_directory('amphibot_description')
    xacro_file = os.path.join(share_dir, 'urdf', 'amphibot.xacro')
    robot_description_config = xacro.process_file(xacro_file)
    robot_urdf = robot_description_config.toxml()

    rviz_config_file = os.path.join(share_dir, 'config', 'display.rviz')

    # ── Arguments ────────────────────────────────────────────────────────────
    gui_arg = DeclareLaunchArgument(
        name='gui',
        default_value='True',
        description="Launch joint_state_publisher_gui if True, else headless.",
    )
    show_gui = LaunchConfiguration('gui')

    # ── Nodes ─────────────────────────────────────────────────────────────────
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        parameters=[{'robot_description': robot_urdf}],
    )

    # Headless joint state publisher (no GUI)
    joint_state_publisher_node = Node(
        condition=UnlessCondition(show_gui),
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
    )

    # Interactive joint state publisher with sliders
    joint_state_publisher_gui_node = Node(
        condition=IfCondition(show_gui),
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_file],
        output='screen',
    )

    return LaunchDescription([
        gui_arg,
        robot_state_publisher_node,
        joint_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz_node,
    ])
