"""
launch_sim.launch.py
--------------------
Full simulation launcher for the Amphibious Bot.
Brings up:
  1. robot_state_publisher  (via bot.launch.py)
  2. Gazebo with a custom world
  3. Robot spawner (delayed 5 s to wait for Gazebo to initialise)

Usage:
    ros2 launch amphibot_description launch_sim.launch.py
"""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():

    package_name = 'amphibot_description'

    # ── 1. robot_state_publisher ──────────────────────────────────────────────
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory(package_name),
                'launch',
                'bot.launch.py',
            )
        ]),
    )

    # ── 2. Gazebo with custom world ───────────────────────────────────────────
    world_file = os.path.join(
        get_package_share_directory(package_name),
        'world',
        'custom_environment.world',
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('gazebo_ros'),
                'launch',
                'gazebo.launch.py',
            )
        ]),
        launch_arguments={'world': world_file}.items(),
    )

    # ── 3. Spawn entity (delayed to allow Gazebo to start) ────────────────────
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'my_bot',
        ],
        output='screen',
    )

    # Delay spawn by 5 seconds so Gazebo is ready
    delayed_spawn = TimerAction(period=5.0, actions=[spawn_entity])

    return LaunchDescription([
        rsp,
        gazebo,
        delayed_spawn,
    ])
