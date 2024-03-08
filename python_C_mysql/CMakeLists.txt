# cmake version check
cmake_minimum_required(VERSION 3.0)

# project name
project(booklist)

find_library(MYSQL mysqlclient)

# add the executable
add_executable(${PROJECT_NAME} booklist.c)
target_include_directories(${PROJECT_NAME} PUBLIC /usr/include/mysql)
target_link_libraries(${PROJECT_NAME} ${MYSQL})

