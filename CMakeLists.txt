cmake_minimum_required(VERSION 3.10)
project(Image_Processing)

set(CMAKE_CXX_STANDARD 11)
find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(3d_Disparity 3d_Disparity.cpp)
add_executable(First_program First_program.cpp)

target_link_libraries(3d_Disparity ${OpenCV_LIBS})
target_link_libraries(First_program ${OpenCV_LIBS})