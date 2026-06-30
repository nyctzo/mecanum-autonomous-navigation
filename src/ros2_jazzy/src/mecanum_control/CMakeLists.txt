cmake_minimum_required(VERSION 3.8)
project(mecanum_control)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_msgs REQUIRED)
add_executable(mecanum_control_node
  src/mecanum_control_node.cpp
)

ament_target_dependencies(
  mecanum_control_node
  rclcpp
  geometry_msgs
  std_msgs
)

install(TARGETS
  mecanum_control_node
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
