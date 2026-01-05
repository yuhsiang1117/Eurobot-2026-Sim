import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

def generate_launch_description():

    #####################################
    # Path settings

    # Declared the world path
    # Ref: https://github.com/ROBOTIS-GIT/turtlebot3_simulations/tree/98a27b20952b11047f454d7ec751f8c742862713/turtlebot3_gazebo/worlds/turtlebot3_world.world
    world_path = PathJoinSubstitution([
        FindPackageShare("sim_desp"), 
        "worlds", "Eurobot2026.world"
    ])

    # Gazebo launch file path
    # Ref: https://github.com/ros-simulation/gazebo_ros_pkgs/blob/0f4818cd5d594f044a65e5beaf4a8b296ed00bc6/gazebo_ros/launch/gazebo.launch.py
    gazebo_path = PathJoinSubstitution([
        FindPackageShare("gazebo_ros"), 
        "launch", "gazebo.launch.py"
    ])


    #####################################
    # Add launch description
    
    # Launch Gazebo with the given world file
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gazebo_path),
        launch_arguments={'world': world_path}.items()
    )

    #####################################
    # Other nodes

    # RViz
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz',
        output='screen',
    )

    #####################################
    # Launch description
    return LaunchDescription([
        gazebo, rviz
    ])