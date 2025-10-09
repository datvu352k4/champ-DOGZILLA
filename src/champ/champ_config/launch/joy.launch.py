import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution

def generate_launch_description():
    teleop_pkg = get_package_share_directory('teleop_twist_joy')
    champ_pkg = get_package_share_directory('champ_config')

    config_arg = DeclareLaunchArgument(
        'config_filepath',
        default_value=os.path.join(champ_pkg, 'config', 'xbox', 'robot.config.yaml')
    )
    joy_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(teleop_pkg, 'launch', 'teleop-launch.py')
        ),
        launch_arguments={
            'config_filepath': LaunchConfiguration('config_filepath'),
        }.items()
    )

    return LaunchDescription([
        config_arg,
        joy_launch
    ])
