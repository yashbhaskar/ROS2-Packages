from launch import LaunchDescription
from launch_ros.actions import Node
# from launch.actions import ExecuteProcess

def generate_launch_description():
    # ign_gazebo = ExecuteProcess(                                      used to open gazebo using executable file
    #     cmd = ["ign", " gazebo", " -r", " empty.sdf"],
    #     shell = True,
    #     output = "screen"
    # )
    return LaunchDescription([
        Node(
            package='simple_pkg_python',
            executable='talker',
            name='sim',
            output='screen'
        ),
        Node(
            package='simple_pkg_python',
            executable='listener',
            name='sim',
            output='screen'
        ),
        # ign_gazebo
    ])
