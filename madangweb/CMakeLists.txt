# cmake_minimum_required(VERSION 3.10)
# project(MyWtProject)

# set(CMAKE_CXX_STANDARD 14)

# find_package(Wt REQUIRED)
# find_library(MYSQLCPPCONN_LIBRARY mysqlcppconn HINTS /usr/lib)

# include_directories(/usr/include/mysql)

# add_executable(MyWtProject web.cpp)
# target_link_libraries(MyWtProject Wt::Wt Wt::HTTP Wt::Dbo Wt::DboSqlite3 ${MYSQLCPPCONN_LIBRARY})


# CMake 최소 버전
cmake_minimum_required(VERSION 3.5)

# 프로젝트 이름 및 버전
project(web4 VERSION 1.0)

# C++ 표준 설정
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Poco 라이브러리 찾기
find_package(Poco REQUIRED COMPONENTS Foundation Net Util)
find_library(MYSQLCPPCONN_LIBRARY mysqlcppconn HINTS /usr/lib)
include_directories(/usr/include/mysql)
# 소스 파일 추가
add_executable(web4 web4.cpp)

# Poco 라이브러리 링크
target_link_libraries(web4 Poco::Foundation Poco::Net Poco::Util ${MYSQLCPPCONN_LIBRARY})