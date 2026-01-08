cmake_minimum_required(VERSION 3.8)
project(simple_pkg_cpp)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)			# Add rclcpp
find_package(std_msgs REQUIRED)			# Add std_msgs
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

# Make Node Executable
add_executable(talker src/pub.cpp)
ament_target_dependencies(talker rclcpp std_msgs)
add_executable(listener src/sub.cpp)
ament_target_dependencies(listener rclcpp std_msgs)

# Executables for Nodes
install(TARGETS
  talker
  listener
  DESTINATION lib/${PROJECT_NAME})
  
# Executables for directories
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}
)

# Executables for scripts
install(PROGRAMS
  scripts/simple.cpp
  
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
