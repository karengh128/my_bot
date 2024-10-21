from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        # First instance of the talker node
        Node(
            package='demo_nodes_cpp',
            executable='talker',
            name='talker_node_1',
            output='screen'
        ),
        
        # Second instance of the talker node
        Node(
            package='demo_nodes_cpp',
            executable='talker',
            name='talker_node_2',
            output='screen'
        ),
    ])
