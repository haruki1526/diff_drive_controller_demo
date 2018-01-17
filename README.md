# ros_demo
ロボットシステム学課題2

# 概要
シミュレータ上の2輪の台車をDUALSHOCK4の左のジョイスティックで操作できます。

# 実演
https://www.youtube.com/watch?v=51kOU_XzJ6A

# 必要なもの
* DUALSHOCK4
* PC(Ubuntu 16.04 LTS)
* ROS kinetic
* GAZEBO 7.0

# 使用方法

joyパッケージがインストールされていなければ以下のコマンドでインストールします  
`sudo apt-get install ros-kinetic-joy`

DUALSHOCK4をOSに認識させておきます

以下のコマンドを入力します  
`roslaunch robosys_gazebo robosys.launch`

gazeboが起動し操作できるようになります 

左スティックを倒した方向に走ります

