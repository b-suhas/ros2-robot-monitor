# ROS2 Robot Monitor

![ROS2](https://img.shields.io/badge/ROS2-Humble-blue?style=flat-square&logo=ros)
![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)
![Build](https://img.shields.io/badge/build-colcon-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square)

A two-package ROS2 workspace demonstrating **custom message interface design** and **OOP-based publisher/subscriber architecture** for real-time robot state monitoring.

---

##  Overview

This project implements a minimal but architecturally complete ROS2 system that publishes and subscribes to a custom `RobotStatus` message type. Rather than relying on standard `std_msgs`, it defines a typed message interface in a dedicated `ament_cmake` package — a pattern used in production ROS2 systems.

The publisher broadcasts robot telemetry (battery level, motion state, status string) at 1 Hz. The subscriber receives and displays it with formatted terminal output. Node communication is visualized via `rqt_graph`.

---

##  Features

- **Custom ROS2 message interface** — `RobotStatus.msg` with typed fields (`float32`, `bool`, `string`)
- **OOP node architecture** — both publisher and subscriber implemented as Python classes inheriting from `rclpy.node.Node`
- **Two-package workspace structure** — interfaces package (`ament_cmake`) cleanly separated from logic package (`ament_python`)
- **1 Hz telemetry publishing** — timer-driven publisher using `create_timer()`
- **Formatted subscriber output** — structured terminal logging via `get_logger().info()`
- **Node graph visualization** — full pub/sub flow visible in `rqt_graph`

---

##  Tech Stack

| Component         | Technology                          |
|-------------------|-------------------------------------|
| Framework         | ROS2 Humble                         |
| Language          | Python 3.10                         |
| Build System      | `colcon` + `ament_cmake` / `ament_python` |
| Interface IDL     | ROS2 IDL (`.msg` file)              |
| Visualization     | `rqt_graph`                         |
| Middleware        | DDS (ROS2 default)                  |

---

##  Architecture

```
/publisher_node  ──►  /robot_status  ──►  /subscriber_node
  (publishes)         (RobotStatus.msg)      (subscribes)
```

### Message Definition

```
# robot_monitor_interfaces/msg/RobotStatus.msg

float32  battery_level    # Battery percentage (0.0 – 100.0)
bool     is_moving        # True if robot is currently in motion
string   status_msg       # Human-readable status string
```

### Data Flow

```
PublisherNode
  └── create_timer(1.0 sec)
        └── publish_robot_status()
              └── RobotStatus msg → /robot_status topic
                                          └── SubscriberNode
                                                └── robot_status_callback()
                                                      └── get_logger().info()
```

---

##  Folder Structure

```
ros2-robot-monitor/
│
├── robot_monitor/                    # ament_python package — node logic
│   ├── robot_monitor/
│   │   ├── __init__.py
│   │   ├── publisher_node.py         # PublisherNode class (1 Hz telemetry publisher)
│   │   └── subscriber_node.py        # SubscriberNode class (formatted status display)
│   ├── resource/
│   │   └── robot_monitor
│   ├── test/
│   │   ├── test_copyright.py
│   │   ├── test_flake8.py
│   │   └── test_pep257.py
│   ├── package.xml
│   ├── setup.cfg
│   └── setup.py
│
├── robot_monitor_interfaces/         # ament_cmake package — custom message definition
│   ├── msg/
│   │   └── RobotStatus.msg           # Custom message: battery_level, is_moving, status_msg
│   ├── CMakeLists.txt
│   └── package.xml
│
└── .gitignore
```

---

##  Prerequisites

- Ubuntu 22.04 (recommended)
- [ROS2 Humble](https://docs.ros.org/en/humble/Installation.html) installed and sourced
- `colcon` build tool

Verify your setup:
```bash
ros2 --version
colcon version-check
```

---

##  Installation

```bash
# 1. Clone the repository
git clone https://github.com/b-suhas/ros2-robot-monitor.git

# 2. Navigate into the workspace
cd ros2-robot-monitor

# 3. Build both packages
colcon build

# 4. Source the workspace
source install/setup.bash
```

> You must run `source install/setup.bash` in **every new terminal** before running nodes.

---

##  Running the Project

Open **three separate terminals**. Source the workspace in each one.

**Terminal 1 — Start the publisher:**
```bash
source install/setup.bash
ros2 run robot_monitor publisher_node
```

**Terminal 2 — Start the subscriber:**
```bash
source install/setup.bash
ros2 run robot_monitor subscriber_node
```

**Terminal 3 — Visualize the node graph (optional):**
```bash
source install/setup.bash
rqt_graph
```

---

##  Example Output

```
[INFO] [subscriber_node]:
===== ROBOT STATUS =====
Battery Level : 75.0 %
Is Moving     : True
Message       : Robot moving
========================
```

---

##  Key ROS2 Concepts Demonstrated

| Concept | Where used |
|---|---|
| Custom message interface (`.msg`) | `robot_monitor_interfaces/msg/RobotStatus.msg` |
| Two-package workspace | `ament_cmake` + `ament_python` packages |
| OOP node pattern | `PublisherNode`, `SubscriberNode` inherit from `rclpy.node.Node` |
| Timer-driven publishing | `create_timer(1.0, callback)` in publisher |
| Topic pub/sub | `/robot_status` topic with queue size 10 |
| Node graph visualization | `rqt_graph` |

---

##  Roadmap

- [ ] turtlesim geometric path controller (spiral + figure-8)
- [ ] Real-time keyboard teleop interface
- [ ] ROS2 launch file for single-command startup
- [ ] Dynamic battery simulation (declining level over time)
- [ ] Gazebo simulation integration
- [ ] OpenCV + ROS2 vision pipeline

---

## 👤 Author

**B Suhas**
- GitHub: [@b-suhas](https://github.com/b-suhas)
- LinkedIn: [B Suhas](https://www.linkedin.com/in/b-suhas)

---
