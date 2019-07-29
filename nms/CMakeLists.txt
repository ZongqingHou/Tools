project(nms)
add_definitions(-std=c++11)
cmake_minimum_required(VERSION 2.8)
aux_source_directory(. SRC_LIST)

INCLUDE_DIRECTORIES("/home/hdd/Git/NumCpp/include")
INCLUDE_DIRECTORIES("/home/hdd/lib/boost_1_70_0")

add_executable(${PROJECT_NAME} ${SRC_LIST})
