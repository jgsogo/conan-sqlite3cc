
project(ConanPackageTest)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package("SQLite3cc")

IF(SQLITE3CC_FOUND)
    add_executable(test main.cpp)
    include_directories(${CONAN_INCLUDE_DIRS})
    target_link_libraries(test PUBLIC ${CONAN_LIBS})
ELSE()
    message(FATAL_ERROR "SQLite3cc not found")
ENDIF()
