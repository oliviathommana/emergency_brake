add_executable(emergency_brake_node src/emergency_brake_node.cpp)

ament_target_dependencies(emergency_brake_node rclcpp sensor_msgs std_msgs)

install(TARGETS
  emergency_brake_node
  DESTINATION lib/${PROJECT_NAME}
)
