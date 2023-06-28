cmake_minimum_required(VERSION 3.25)

#Defines the project
project(HelloWorld VERSION 0.0.0)

#Makes .dll instead of .exe
option(BUILD_SHARED_LIBS "Build using shared libraries" ON)

#Defines C++ version
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED True)

#Defines output location
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/obj)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/obj)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/obj)

#Finds and includes pybind dependencies
set(Python_EXECUTABLE "/c/Python310/python")
find_package(Python COMPONENTS Interpreter REQUIRED)
execute_process(COMMAND ${Python_EXECUTABLE} -m pybind11 --includes OUTPUT_VARIABLE PY_INCL)
string(REGEX REPLACE "-I" "" PY_INCL ${PY_INCL})
string(REGEX REPLACE "\n" "" PY_INCL ${PY_INCL})
string(REGEX REPLACE "C\:" "/c" PY_INCL ${PY_INCL})
separate_arguments(PY_INCL)
include_directories(${PY_INCL})

#Finds source files
file(GLOB SRC_FILES ${PROJECT_SOURCE_DIR}/src/*.cpp)

#Declares .dll
add_library(HelloWorld ${SRC_FILES})

#Renames library to follow pybind standards
set_target_properties(HelloWorld PROPERTIES SUFFIX ".pyd")
set_target_properties(HelloWorld PROPERTIES PREFIX "lib")

#Adds compiler options
add_compile_options(-Wall -O3 -march=native -MMD -MP -DMS_WIN64 -D_hypot=hypot)

#Adds linking options
target_link_libraries(HelloWorld -DMS_WIN64 -D_hypot=hypot)
target_link_libraries(HelloWorld -L/c/Python310/ -lpython310)

#install(DIRECTORY ${PROJECT_SOURCE_DIR}/obj/ DESTINATION ${PROJECT_SOURCE_DIR}/HelloWorld/ FILES_MATCHING PATTERN "libHelloWorld.*")
install(TARGETS HelloWorld
		DESTINATION ${PROJECT_SOURCE_DIR}/HelloWorld)