# ROS2-Packages

This repository contains simple ROS 2 packages implemented in both Python and C++. It demonstrates the structural, build, and performance differences between ROS 2 Python and C++ packages, helping beginners understand when to use each for robotics application development.

---

## C++ Package Structure

```
├── simple_pkg_cpp/
  ├── CMakeLists.txt                 # Builds C++ source files, links ROS 2 libraries, and creates runnable ROS2 nodes
  ├── package.xml
  ├── scripts/                       # Scripts
  │ └── simple.cpp
  ├── include/
  │ └── simple_pkg_cpp/
  ├── src/                           # Nodes
  │ ├── pub.cpp                      # Publisher Node
  │ └── sub.cpp                      # Subscriber Node
  └── launch                         # Launch Files
```

## Python Package Structure

```
├── simple_pkg_python/
  ├── setup.py                      # Registers Python scripts as ROS 2 nodes and handles installation
  ├── setup.cfg
  ├── package.xml
  ├── scripts/                      # Scripts
  ├── simple_pkg_python/            # Nodes
  | ├── __init__.py
  | ├── pub.py                      # Publisher Node
  | ├── sub.py                      # Subscriber Node
  │ └── parameter_handling.py       # Parameter Handling Concept
  ├── launch/                       # Launch Files
  │ └── main.launch.py
  ├── resource/                           
  │ └── simple_pkg_python
  └── bag_files                     # Bag File
```

---

## 🚀 Packages Overview

### 🔹 ROS 2 C++ Package
- Written using `rclcpp`
- Better runtime performance
- Ideal for:
  - Real-time systems
  - Performance-critical nodes
  - Low-level robot control

### 🔹 ROS 2 Python Package
- Written using `rclpy`
- Faster to develop and easier to read
- Ideal for:
  - Prototyping
  - Scripting
  - High-level logic

---

## 🧠 Key Differences

| Feature            | Python (`rclpy`) | C++ (`rclcpp`) |
|--------------------|-----------------|---------------|
| Development Speed  | Fast            | Moderate      |
| Performance        | Moderate        | High          |
| Ease of Learning   | Easy            | Moderate      |
| Real-time Support  | Limited         | Better        |
| Use Case           | Prototyping     | Production    |

---

## 🔑 Key Features

- Simple and minimal ROS 2 Python (`rclpy`) package  
- Simple and minimal ROS 2 C++ (`rclcpp`) package  
- Side-by-side comparison of Python vs C++ ROS 2 nodes  
- Clear package structure for both build systems  
- Easy-to-run examples for quick understanding  
- Beginner-friendly and well-documented code  

## 🎯 Learning Objectives

- Understand the structural differences between ROS 2 Python and C++ packages  
- Learn how ROS 2 nodes are implemented using `rclpy` and `rclcpp`  
- Understand the purpose of `setup.py` and `CMakeLists.txt`  
- Learn when to choose Python vs C++ for robotics applications  
- Build and run ROS 2 packages using `colcon`  
- Gain confidence in creating custom ROS 2 packages  

---

## ✉️ Contact

📧 Yash Bhaskar – ybbhaskar19@gmail.com

📌 GitHub: https://github.com/yashbhaskar
