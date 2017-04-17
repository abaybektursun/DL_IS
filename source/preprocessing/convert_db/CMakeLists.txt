cmake_minimum_required (VERSION 2.6)
project (convert_db)

include_directories("/usr/local/caffe/.build_release/src")
include_directories("/usr/local/caffe/include")
include_directories("/usr/local/cuda/include")
add_executable(convert main.cpp)


