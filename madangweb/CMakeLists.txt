cmake_minimum_required(VERSION 3.10)
project(MyWtProject)

set(CMAKE_CXX_STANDARD 14)

find_package(Wt REQUIRED)
find_library(MYSQLCPPCONN_LIBRARY mysqlcppconn HINTS /usr/lib)

include_directories(/usr/include/mysql)

add_executable(MyWtProject web.cpp)
target_link_libraries(MyWtProject Wt::Wt Wt::HTTP Wt::Dbo Wt::DboSqlite3 ${MYSQLCPPCONN_LIBRARY})