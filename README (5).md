# ROS2-Based Screw Propelled Autonomous Amphibious Robot

> **Mini Project Report** — B.Tech in Robotics and Automation  
> Adi Shankara Institute of Engineering and Technology, Kalady  
> APJ Abdul Kalam Technological University | December 2024

---

## Team

| Name | Roll No |
|------|---------|
| Akshay Raj B | ASI22RA010 |
| Nandana Sunil | ASI22RA038 |
| Sneha Alphonso Francis | ASI22RA041 |
| Swaroop S | ASI22RA047 |

**Guide:** Mr. Sreedeep Krishnan, Associate Professor, Dept. of Robotics and Automation

---

## Project Overview

This project introduces a **ROS2-based Screw Propelled Amphibious Robot** capable of navigating both terrestrial and aquatic environments autonomously. The robot uses a unique helical screw-wheel mechanism that allows seamless transition between land, water, mud, and sand — without any mechanical reconfiguration.

### Key Features
- Dual-terrain locomotion (land + water) using screw-propelled wheels
- Autonomous navigation via **ROS2 + SLAM**
- Real-time sensing with **LiDAR** and **ZED 2i Stereo Camera**
- Bluetooth-based manual override via smartphone
- Gazebo simulation support
- Powered by **Raspberry Pi 4B** + **Arduino Uno**

---

## 3D CAD Design

<p align="center">
<a href="https://github.com/sneha19122004/amphibious-bot/blob/master/CAD-assembly">
<img src="https://github.com/sneha19122004/amphibious-bot/blob/master/CAD-assembly" alt="3D CAD Assembly of Amphibious Robot" width="700"/>
</a>
</p>

> Full CAD assembly files → [`/CAD-assembly`](https://github.com/sneha19122004/amphibious-bot/blob/master/CAD-assembly)

The robot chassis is designed in a cuboidal form using acrylic sheets and 3D-printed components. The screw wheels feature a helical pitch optimised at a **30° helix angle** for maximum propulsion efficiency, with a blade height to drum diameter ratio of **0.125** and drum length to drum diameter ratio of **6**.

---

## Circuit Diagram

<p align="center">
<a href="https://github.com/sneha19122004/amphibious-bot/blob/master/circuit-diagram">
<img src="https://github.com/sneha19122004/amphibious-bot/blob/master/circuit-diagram" alt="Circuit Diagram" width="700"/>
</a>
</p>

> Full circuit diagram → [`/circuit-diagram`](https://github.com/sneha19122004/amphibious-bot/blob/master/circuit-diagram)

The electronics stack connects a **Raspberry Pi 4B** (autonomous navigation) and **Arduino Uno** (motor control) through serial communication. An **HC-05 Bluetooth module** relays smartphone commands to the Arduino, which drives the left and right screw motors via an **L298N motor driver**, all powered by an **11.1V 8000mAh LiPo battery**.

---

## Gazebo Simulation

<p align="center">
<a href="https://github.com/sneha19122004/amphibious-bot/blob/master/gazebo-simulation.mp4">
<img src="https://img.shields.io/badge/%20Watch%20Simulation-Gazebo%20ROS2-blue?style=for-the-badge&logo=ros" alt="Watch Gazebo Simulation"/>
</a>
</p>

> Download / view simulation video → [`gazebo-simulation.mp4`](https://github.com/sneha19122004/amphibious-bot/blob/master/gazebo-simulation.mp4)

The robot URDF model is spawned in a custom Gazebo world using the `launch_sim.launch.py` file. The differential drive plugin publishes odometry on `/odom` and subscribes to velocity commands on `/cmd_vel`, enabling ROS2 Nav2-compatible autonomous navigation testing in simulation before real-world deployment.

---

## Final Working Robot

<p align="center">
<a href="https://github.com/sneha19122004/amphibious-bot/blob/master/working-video">
<img src="https://img.shields.io/badge/%20Watch%20Demo-Physical%20Robot-green?style=for-the-badge" alt="Watch Working Robot Demo"/>
</a>
</p>

> Download / view working demo → [`/working-video`](https://github.com/sneha19122004/amphibious-bot/blob/master/working-video)

The physical prototype demonstrates Bluetooth-controlled locomotion on land using the screw-propelled wheel mechanism. The robot is manually driven via the HC-05 module and an Android Bluetooth RC Controller app, with commands `F` / `B` / `L` / `R` / `S` controlling direction.

---

## Repository Structure

```
amphibious_bot/
arduino/
motor_control/
motor_control.ino          # Bluetooth motor control (HC-05)
bluetooth_passthrough/
bluetooth_passthrough.ino  # BT serial passthrough sketch
ros2/
amphibot_description/
launch/
bot.launch.py
display.launch.py
gazebo.launch.py
launch_sim.launch.py
urdf/
amphibot.gazebo        # Gazebo plugin config (XACRO)
config/
display.rviz           # RViz config
world/
custom_environment.world
CAD-assembly                       # 3D design files
circuit-diagram                    # Electronics schematic
gazebo-simulation.mp4              # Simulation recording
working-video                      # Physical robot demo
docs/
Amphi_report.pdf               # Full project report
README.md
```

---

## Hardware Components

| Component | Specification |
|-----------|--------------|
| Main Controller | Raspberry Pi 4B (4GB RAM, 32GB SD) |
| Microcontroller | Arduino Uno |
| Camera | ZED 2i Stereo Camera (4K, 120° FOV, IP-66) |
| Ranging Sensor | LiDAR |
| Motors | Waveshare L-shaped motors (8.5 Nm stall torque @ 3.5A) |
| Motor Driver | L298N / L293N |
| Bluetooth Module | HC-05 |
| Battery | LiPo 11.1V, 8000mAh |
| Chassis | Acrylic sheets + 3D-printed components |

---

## Locomotion Modes

### 1. Screw Propulsion Mode
Used for deformable terrains — water, mud, clay, sand.
- Wheels rotate in **opposite directions**
- Helical threads displace fluid/granular media backward to generate thrust
- PID controller manages speed and torque for stability

### 2. Crab Crawl Mode
Used for rigid/uneven surfaces — rocky terrain.
- Wheels rotate in the **same direction** for lateral movement
- Screws enhance sideways grip and traction

---

## Mathematical Model (Kinematics)

With the chassis frame `xc Oc yc` and helix angle = 45°:

**Forward kinematics (velocity):**
```
[Vx]       [  1         1      ] [W1]
[Vy] = R/2 [  1         1      ] [W2]
[Wz]       [-1/(l1+l2)  1/(l1+l2)]
```

**Inverse kinematics (wheel speeds):**
```
[W1]   1  [  1   1  -(l1+l2) ] [Vx]
[W2] = -  [ -1   1   (l1+l2) ] [Vy]
R                        [Wz]
```

Where `R` = screw radius, `W1/W2` = angular velocities, `l1/l2` = distances from screw axis to body center.

---

## Getting Started

### Prerequisites
- ROS2 (Humble or later)
- Gazebo
- `robot_state_publisher`, `joint_state_publisher`, `gazebo_ros` packages
- Arduino IDE (for hardware upload)

### ROS2 Setup

```bash
git clone https://github.com/sneha19122004/amphibious-bot.git
cd amphibious-bot
cp -r ros2/amphibot_description ~/ros2_ws/src/
cd ~/ros2_ws
colcon build
source install/setup.bash
```

### Launch Gazebo Simulation

```bash
ros2 launch amphibot_description launch_sim.launch.py   # full sim
ros2 launch amphibot_description display.launch.py      # RViz only
ros2 launch amphibot_description gazebo.launch.py       # Gazebo only
```

### Arduino Upload

1. Open `arduino/motor_control/motor_control.ino` in Arduino IDE
2. Connect Arduino Uno, select **Board: Arduino Uno** and correct COM port
3. Upload the sketch
4. Pair HC-05 with your phone (default PIN: `1234`)
5. Use a Bluetooth RC Controller app and send: `F` / `B` / `L` / `R` / `S`

---

## Bluetooth Control Commands

| Command | Action |
|---------|--------|
| `F` | Move Forward |
| `B` | Move Backward |
| `L` | Turn Left |
| `R` | Turn Right |
| `S` | Stop |

---

## Applications

- **Flood rescue & disaster response** — navigates debris, mud, and flooded zones
- **Dam & infrastructure inspection** — 3D mapping of walls and underwater tunnels
- **Environmental monitoring** — wetlands, water quality, invasive species detection
- **Defense & surveillance** — river/swamp patrol with stealth capabilities
- **Aquaculture & agriculture** — field irrigation canals and offshore modules

---

## Funding & Achievements

- Funded by **Kerala Technological University** via **Research Seed Money (RSM)**
- Review paper submitted to **IEEE** conference:  
*"Revolutionary Screw-Propelled Amphibious Robots for Environmental and Disaster Management"*

---

## License

This project is submitted as an academic mini-project under APJ Abdul Kalam Technological University. All rights reserved by the authors.

---

## Acknowledgements

We thank our guide **Mr. Sreedeep Krishnan**, project coordinators **Dr. Athira** and **Mr. Sreedeep Krishnan**, Principal **Dr. M S Murali**, and HOD **Dr. Vinila M L** for their invaluable support.
