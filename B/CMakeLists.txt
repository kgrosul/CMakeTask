cmake_minimum_required(VERSION 3.2)

project(lib)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_EXE lib.cpp)

add_library(lib.h SHARED lib.cpp)