# gcc booklist.cpp -o main2 -I /usr/include/cppconn -lmysqlcppconn -lstdc++
# g++ booklist.cpp -o main2 -I /usr/include/cppconn -lmysqlcppconn
# gcc -o main booklist.c -I/usr/include/mysql -lmysqlclient -L/usr/lib

# gcc -o booklist2 booklist2.c -lodbc

# booklist.cpp 를 컴파일 하기위 한 cmakelists.txt 를 만들어줘

# cmake_minimum_required(VERSION 3.10)
# project(BookList)

# set(CMAKE_CXX_STANDARD 14)

# find
# include_directories(/usr/include/mysql)

# add_executable(${PROJECT_NAME} booklist.cpp)
# target_link_libraries(${PROJECT_NAME} mysqlcppconn)

# add_executable(${PROJECT_NAME}2 booklist.c)
# target_link_libraries(${PROJECT_NAME}2 mysqlclient)


cmake_minimum_required(VERSION 3.10)
project(booklist)

set(CMAKE_CXX_STANDARD 14)

find_library(MYSQLCPPCONN_LIBRARY mysqlcppconn HINTS /usr/lib)

include_directories(/usr/include/mysql)

add_executable(${PROJECT_NAME} booklist.cpp)
target_link_libraries(${PROJECT_NAME} ${MYSQLCPPCONN_LIBRARY})
