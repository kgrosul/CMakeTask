cmake_minimum_required(VERSION 3.2)

set(CMAKE_CXX_STANDARD 11)

project(TP)

execute_process(
        COMMAND python3 A/preparing.py
)
include_directories("${PROJECT_SOURCE_DIR}")


add_subdirectory("B")

set(SOURCE_FILES B/lib.cpp C/main.cpp)

add_executable(build ${SOURCE_FILES})
