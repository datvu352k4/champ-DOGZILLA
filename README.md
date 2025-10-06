**1. Installation**

1.1 Clone and install all dependencies:
<code>sudo apt install -y python3-rosdep
rosdep update<code>

<code>cd <your_ws>/src
git clone --recursive https://github.com/chvmp/champ -b ros2
git clone https://github.com/chvmp/champ_teleop -b ros2
cd ..
rosdep install --from-paths src --ignore-src -r -y<code>

1.2 Build your workspace:
<code>cd <your_ws>
colcon build
. <your_ws>/install/setup.bash<code>

**2.Run Rviz and Gazebo simulation**
<code>ros2 launch champ_config gazebo.launch.py<code>
<code>ros2 run teleop_twist_keyboard teleop_twist_keyboard<code>
<code>rviz2<code>
