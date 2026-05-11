cmake_minimum_required(VERSION 3.8)
project(amphibot_description)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)

# Install launch files
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

# Install URDF / XACRO files
install(
  DIRECTORY urdf
  DESTINATION share/${PROJECT_NAME}
)

# Install RViz config
install(
  DIRECTORY config
  DESTINATION share/${PROJECT_NAME}
)

# Install Gazebo world files
install(
  DIRECTORY world
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
