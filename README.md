# ROS2-Packages
This repository contains two simple ROS 2 packages — one written in **C++** and another in **Python** — demonstrating basic publisher/subscriber functionality.   It serves as a reference for understanding the structure and setup of both types of ROS 2 packages.

---

## Repository Structure

### C++ Package

├── simple_pkg_cpp/
  ├── CMakeLists.txt
  ├── package.xml
  └── src/
  │ ├── pub.py                        # publisher node
  │ └── sub.py                        # subscriber node
  └── include/
  ├── scripts/                        
  │ └── simple.cpp                    # cpp script
  └── launch/                         # launch folder

### Python Package

├── simple_pkg_python/
  ├── setup.py
  ├── package.xml
  ├── simple_pkg_python/
  │ ├── init.py
  │ ├── pub.py                        # publisher node
  │ └── sub.py                        # subscriber node
  └── resource/
  │ └── simple_pkg_python
  ├── scripts/                        
  │ └── simple.py                     # python script
  └── launch/
    └── main.launch.py                # launch file

---

##  Package Overview 

### C++ ROS 2 Package Overview

The C++ ROS 2 package is a software module developed using the ament_cmake build system and the rclcpp client library.
It provides the foundation for building high-performance ROS 2 nodes written in C++.

- Concept

Each C++ ROS 2 package contains one or more nodes, which are executable units that perform specific robotic tasks (like publishing sensor data or controlling actuators).
It follows a publisher–subscriber model, where one node publishes messages to a topic and other nodes subscribe to it.
The build process uses CMake (via CMakeLists.txt) to compile the source code, link libraries, and generate ROS executables.

- Main Components

CMakeLists.txt — Specifies how to build the C++ source code, defines dependencies, and sets up installation.
package.xml — Describes the package metadata, dependencies, and version information.
src/ directory — Contains the C++ source files implementing ROS 2 nodes.

- Purpose

Demonstrates how to implement ROS 2 nodes using C++.
Shows how to use the rclcpp API to create publishers, subscribers, and timers.
Provides a structure suitable for more complex robotics applications requiring performance and real-time control.


### Python ROS 2 Package Overview

The Python ROS 2 package is built using the ament_python build system and the rclpy client library.
It focuses on ease of development, readability, and quick prototyping of ROS 2 applications.

- Concept

The Python package defines nodes in .py scripts, typically organized in a module directory.
It uses setup.py instead of CMake for installation and to register ROS 2 executables.
Python nodes can publish or subscribe to ROS 2 topics, similar to C++ nodes, but with less boilerplate and faster iteration.

- Main Components

setup.py — Acts as the build and install configuration file, defining entry points for executables.
package.xml — Lists package metadata and runtime dependencies (like rclpy and std_msgs).
simple_pkg_python/ directory — Contains the Python node implementations and module files.

- Purpose

Demonstrates how to write simple and clear ROS 2 nodes using Python.
Useful for testing, data processing, or rapid development.
Ideal for developers who prefer flexibility over performance-critical execution.

---

## ✉️ Contact

📧 Yash Bhaskar – ybbhaskar19@gmail.com
📌 GitHub: https://github.com/yashbhaskar
