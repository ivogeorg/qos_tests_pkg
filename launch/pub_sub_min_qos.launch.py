from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument("reliability", default_value="reliable"),
        LogInfo(msg=LaunchConfiguration("reliability")),
        Node (
            package='qos_tests_pkg',
            executable='sub_custom_min_qos_node',
            output='screen',
            emulate_tty=True,
        ),
        Node (
            package='qos_tests_pkg',
            executable='pub_custom_min_qos_node',
            output='screen',
            emulate_tty=True,
            arguments=[
                "-reliability",
                LaunchConfiguration("reliability")]
        ),
    ])