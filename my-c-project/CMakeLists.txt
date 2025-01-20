cmake_minimum_required(VERSION 3.10)
project(my-c-project)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 11)

enable_testing()
find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})

find_package(SDL2 REQUIRED)
find_package(PkgConfig REQUIRED)
pkg_check_modules(SDL2_TTF REQUIRED SDL2_ttf)
include_directories(${SDL2_INCLUDE_DIRS} ${SDL2_TTF_INCLUDE_DIRS} include)

add_executable(my-c-project src/main.c src/utils.c src/tetris.c)
set_target_properties(my-c-project PROPERTIES LINKER_LANGUAGE C)
target_link_libraries(my-c-project ${SDL2_LIBRARIES} ${SDL2_TTF_LIBRARIES})

add_executable(test-my-c-project tests/test_main.cpp src/utils.c src/tetris.c)
set_target_properties(test-my-c-project PROPERTIES LINKER_LANGUAGE CXX)
target_link_libraries(test-my-c-project
    ${GTEST_LIBRARIES}
    ${SDL2_LIBRARIES}
    ${SDL2_TTF_LIBRARIES}
    pthread
)

add_test(NAME test-my-c-project COMMAND ${CMAKE_BINARY_DIR}/test-my-c-project)
