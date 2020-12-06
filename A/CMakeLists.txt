cmake_minimum_required(VERSION 3.0)

project(aLib)

add_library(aLib SHARED index.h)
set_target_properties(aLib PROPERTIES LINKER_LANGUAGE CXX)