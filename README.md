1. Installation
1.1 Clone and install all dependencies:
sudo apt install -y python3-rosdep
rosdep update

cd <your_ws>/src
git clone --recursive https://github.com/chvmp/champ -b ros2
git clone https://github.com/chvmp/champ_teleop -b ros2
cd ..
rosdep install --from-paths src --ignore-src -r -y

1.2 Build your workspace:
cd <your_ws>
colcon build
. <your_ws>/install/setup.bash

2.Run Rviz and Gazebo simulation
ros2 launch champ_config gazebo.launch.py 
ros2 run teleop_twist_keyboard teleop_twist_keyboard
rviz2
