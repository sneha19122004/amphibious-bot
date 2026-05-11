# 🤖 ROS2-Based Screw Propelled Autonomous Amphibious Robot

<p align="center">
  <img src="docs/images/robot_preview.png" alt="Amphibious Robot" width="600"/>
</p>

> **Mini Project Report** — B.Tech in Robotics and Automation  
> Adi Shankara Institute of Engineering and Technology, Kalady  
> APJ Abdul Kalam Technological University | December 2024

---

## 👥 Team

| Name | Roll No |
|------|---------|
| Akshay Raj B | ASI22RA010 |
| Nandana Sunil | ASI22RA038 |
| Sneha Alphonso Francis | ASI22RA041 |
| Swaroop S | ASI22RA047 |

**Guide:** Mr. Sreedeep Krishnan, Associate Professor, Dept. of Robotics and Automation

---

## 📌 Project Overview

This project introduces a **ROS2-based Screw Propelled Amphibious Robot** capable of navigating both terrestrial and aquatic environments autonomously. The robot uses a unique helical screw-wheel mechanism that allows seamless transition between land, water, mud, and sand — without any mechanical reconfiguration.

### Key Features
- 🌊 Dual-terrain locomotion (land + water) using screw-propelled wheels
- 🧠 Autonomous navigation via **ROS2 + SLAM**
- 📡 Real-time sensing with **LiDAR** and **ZED 2i Stereo Camera**
- 📱 Bluetooth-based manual override via smartphone
- 🖥️ Gazebo simulation support
- ⚡ Powered by **Raspberry Pi 4B** + **Arduino Uno**

---

## 🏗️ Repository Structure

```
amphibious_bot/
├── arduino/
│   ├── motor_control/
│   │   └── motor_control.ino       # Bluetooth motor control (HC-05)
│   └── bluetooth_passthrough/
│       └── bluetooth_passthrough.ino  # BT serial passthrough sketch
├── ros2/
│   └── amphibot_description/
│       ├── launch/
│       │   ├── bot.launch.py
│       │   ├── display.launch.py
│       │   ├── gazebo.launch.py
│       │   └── launch_sim.launch.py
│       ├── urdf/
│       │   └── amphibot.gazebo     # Gazebo plugin config (XACRO)
│       ├── config/
│       │   └── display.rviz        # RViz config placeholder
│       └── world/
│           └── custom_environment.world  # Gazebo world placeholder
├── docs/
│   └── Amphi_report.pdf            # Full project report
└── README.md
```

---

## ⚙️ Hardware Components

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

## 🔩 Locomotion Modes

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

## 📐 Mathematical Model (Kinematics)

With the chassis frame `xc Oc yc` and helix angle = 45°:

**Forward kinematics (velocity):**
```
[Vx]       [  1      1   ] [W1]
[Vy] = R/2 [  1      1   ] [W2]
[Wz]       [-1/(l1+l2)  1/(l1+l2)]
```

**Inverse kinematics (wheel speeds):**
```
[W1]   1  [  1   1  -(l1+l2) ] [Vx]
[W2] = - [ -1   1   (l1+l2)  ] [Vy]
       R                        [Wz]
```

Where:
- `R` = screw radius
- `W1, W2` = angular velocity of screws 1 and 2
- `l1, l2` = distances between screw axis and body center

---

## 🚀 Getting Started

### Prerequisites
- ROS2 (Humble or later)
- Gazebo
- `robot_state_publisher`, `joint_state_publisher`, `gazebo_ros` packages
- Arduino IDE (for hardware upload)

### ROS2 Setup

```bash
# Clone the repository
git clone https://github.com/<your-username>/amphibious_bot.git
cd amphibious_bot

# Copy the ROS2 package to your workspace
cp -r ros2/amphibot_description ~/ros2_ws/src/

# Build
cd ~/ros2_ws
colcon build
source install/setup.bash
```

### Launch Gazebo Simulation

```bash
# Full simulation with custom world
ros2 launch amphibot_description launch_sim.launch.py

# Visualize in RViz only
ros2 launch amphibot_description display.launch.py

# Gazebo only
ros2 launch amphibot_description gazebo.launch.py
```

### Arduino Upload

1. Open `arduino/motor_control/motor_control.ino` in Arduino IDE
2. Connect Arduino Uno via USB
3. Select **Board: Arduino Uno** and correct COM port
4. Upload the sketch
5. Pair HC-05 with your smartphone (default PIN: `1234`)
6. Use any **Bluetooth RC Controller** app and send commands: `F` / `B` / `L` / `R` / `S`

---

## 📱 Bluetooth Control Commands

| Command | Action |
|---------|--------|
| `F` | Move Forward |
| `B` | Move Backward |
| `L` | Turn Left |
| `R` | Turn Right |
| `S` | Stop |

---

## 🎯 Applications

- 🆘 **Flood rescue & disaster response** — navigates debris, mud, and flooded zones
- 🏗️ **Dam & infrastructure inspection** — 3D mapping of walls and underwater tunnels
- 🌿 **Environmental monitoring** — wetlands, water quality, invasive species detection
- 🪖 **Defense & surveillance** — river/swamp patrol with stealth capabilities
- 🌾 **Aquaculture & agriculture** — field irrigation canals and offshore modules

---

## 🏆 Funding & Achievements

- Funded by **Kerala Technological University** via **Research Seed Money (RSM)**
- Review paper submitted to **IEEE** conference:  
  *"Revolutionary Screw-Propelled Amphibious Robots for Environmental and Disaster Management"*

---

## 📄 License

This project is submitted as an academic mini-project under APJ Abdul Kalam Technological University. All rights reserved by the authors.

---

## 🙏 Acknowledgements

We thank **God Almighty**, our guide **Mr. Sreedeep Krishnan**, project coordinators **Dr. Athira** and **Mr. Sreedeep Krishnan**, Principal **Dr. M S Murali**, and HOD **Dr. Vinila M L** for their invaluable support.
