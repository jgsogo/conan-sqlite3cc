PROJECT(sqlite3cc)
cmake_minimum_required(VERSION 2.8)

include(../conanbuildinfo.cmake)
conan_basic_setup()

# The library itself
file(GLOB HEADERS ${CMAKE_SOURCE_DIR}/include/*.h)
file(GLOB SOURCES ${CMAKE_SOURCE_DIR}/src/*.cc)

include_directories(${CMAKE_SOURCE_DIR}/include ${CONAN_INCLUDE_DIRS})
add_library(sqlite3cc STATIC ${SOURCES})
target_link_libraries(sqlite3cc ${CONAN_LIBS})

install(FILES ${HEADERS} DESTINATION include)
install(TARGETS sqlite3cc LIBRARY DESTINATION lib ARCHIVE DESTINATION lib)

# Tests
add_executable(test_main ${CMAKE_SOURCE_DIR}/test/test-main.cc)
target_link_libraries(test_main sqlite3cc ${CONAN_LIBS})

