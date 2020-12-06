cmake_minimum_required(VERSION 3.2)
set(CMAKE_CXX_STANDARD 11)
project(CMakeTask)

set(EXECUTABLE_OUTPUT_PATH ${CMAKE_SOURCE_DIR}/bin)
set(LIBRARY_OUTPUT_PATH ${CMAKE_SOURCE_DIR}/lib)

execute_process(
        COMMAND python3 ${PROJECT_SOURCE_DIR}/A/preparing.py ${PROJECT_SOURCE_DIR}/A/index.h
)
include_directories("${PROJECT_SOURCE_DIR}")

add_subdirectory("B")
add_subdirectory("A")

set(SOURCE_FILES B/lib.cpp C/main.cpp)

add_executable(build ${SOURCE_FILES})
