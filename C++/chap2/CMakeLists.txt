cmake_minimum_required(VERSION 3.10)
project(chapter2)
set(CMAKE_CXX_STANDARD 14)
set(EXECUTABLES
    ex2-1-simpleC++
    ex2-2-coutSample
    ex2-3-KeyInput
    ex2-4-ReadC-String
    ex2-5-password
    ex2-6-getline
    ex2-7-string
    widthHeight
    getString
    test)

foreach(EXECUTABLE ${EXECUTABLES})
    add_executable(${EXECUTABLE} ${EXECUTABLE}.cpp)
endforeach()

# add_executable(ex2-1-simpleC++ ex2-1-simpleC++.cpp)
# add_executable(ex2-2-coutSample ex2-2-coutSample.cpp)
# add_executable(ex2-3KeyInput ex2-3KeyInput.cpp)
# add_executable(widthHeight widthHeight.cpp)
# add_executable(getString getString.cpp)

