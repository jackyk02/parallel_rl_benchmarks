
cmake_minimum_required(VERSION 3.19)
project(pong_lf LANGUAGES C)

if(CMAKE_BUILD_TYPE STREQUAL "Test")
  set(CMAKE_BUILD_TYPE "Debug")
  if(CMAKE_C_COMPILER_ID STREQUAL "GNU")
    find_program(LCOV_BIN lcov)
    if(LCOV_BIN MATCHES "lcov$")
      set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} --coverage -fprofile-arcs -ftest-coverage")
    else()
      message("Not producing code coverage information since lcov was not found")
    endif()
  else()
    message("Not producing code coverage information since the selected compiler is no gcc")
  endif()
endif()
# Require C11
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

# Require C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(DEFAULT_BUILD_TYPE Release)
if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
    set(CMAKE_BUILD_TYPE ${DEFAULT_BUILD_TYPE} CACHE STRING "Choose the type of build." FORCE)
endif()

# do not print install messages
set(CMAKE_INSTALL_MESSAGE NEVER)


set(CMAKE_POSITION_INDEPENDENT_CODE ON)
add_compile_definitions(_PYTHON_TARGET_ENABLED)
add_subdirectory(core)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR})
set(LF_MAIN_TARGET LinguaFrancapong_lf)
find_package(Python 3.9.0...<3.11.0 REQUIRED COMPONENTS Interpreter Development)
Python_add_library(
    ${LF_MAIN_TARGET}
    MODULE
    lib/schedule.c
    lib/python_action.c
    lib/python_port.c
    lib/python_tag.c
    lib/python_time.c
    lib/pythontarget.c
    _pong_lf_main.c
    _clientreactor.c
    _serverreactor.c
    __lf_gendelay_0.c
    pong_lf.c
)
if (MSVC)
    set_target_properties(${LF_MAIN_TARGET} PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR})
    set_target_properties(${LF_MAIN_TARGET} PROPERTIES LIBRARY_OUTPUT_DIRECTORY_DEBUG ${CMAKE_SOURCE_DIR})
    set_target_properties(${LF_MAIN_TARGET} PROPERTIES LIBRARY_OUTPUT_DIRECTORY_RELEASE ${CMAKE_SOURCE_DIR})
    set_target_properties(${LF_MAIN_TARGET} PROPERTIES LIBRARY_OUTPUT_DIRECTORY_MINSIZEREL ${CMAKE_SOURCE_DIR})
    set_target_properties(${LF_MAIN_TARGET} PROPERTIES LIBRARY_OUTPUT_DIRECTORY_RELWITHDEBINFO ${CMAKE_SOURCE_DIR})
endif (MSVC)
set_target_properties(${LF_MAIN_TARGET} PROPERTIES PREFIX "")
include_directories(${Python_INCLUDE_DIRS})
target_link_libraries(${LF_MAIN_TARGET} PRIVATE ${Python_LIBRARIES})
target_compile_definitions(${LF_MAIN_TARGET} PUBLIC MODULE_NAME=LinguaFrancapong_lf)
find_library(MATH_LIBRARY m)
if(MATH_LIBRARY)
  target_link_libraries(${LF_MAIN_TARGET} PUBLIC ${MATH_LIBRARY})
endif()
target_link_libraries(${LF_MAIN_TARGET} PRIVATE core)
target_include_directories(${LF_MAIN_TARGET} PUBLIC .)
target_include_directories(${LF_MAIN_TARGET} PUBLIC include/)
target_include_directories(${LF_MAIN_TARGET} PUBLIC include/api)
target_include_directories(${LF_MAIN_TARGET} PUBLIC include/core)
target_include_directories(${LF_MAIN_TARGET} PUBLIC include/core/platform)
target_include_directories(${LF_MAIN_TARGET} PUBLIC include/core/modal_models)
target_include_directories(${LF_MAIN_TARGET} PUBLIC include/core/utils)
# Find threads and link to it
find_package(Threads REQUIRED)
target_link_libraries(${LF_MAIN_TARGET} PRIVATE Threads::Threads)

# Set the number of workers to enable threading/tracing
target_compile_definitions(${LF_MAIN_TARGET} PUBLIC NUMBER_OF_WORKERS=0)

# Set flag to indicate a multi-threaded runtime
target_compile_definitions( ${LF_MAIN_TARGET} PUBLIC LF_THREADED=1)

set(CMAKE_C_COMPILER gcc)


  if(WIN32)
    file(GENERATE OUTPUT pong_lf.bat CONTENT
      "@echo off
      ${Python_EXECUTABLE} /mnt/c/Users/jacky/Desktop/simple_multi/src-gen/pong_lf/pong_lf.py %*"
    )
    install(PROGRAMS ${CMAKE_CURRENT_BINARY_DIR}/pong_lf.bat DESTINATION ${CMAKE_INSTALL_BINDIR})
  else()
    file(GENERATE OUTPUT pong_lf CONTENT
        "#!/bin/sh\n\
        ${Python_EXECUTABLE} /mnt/c/Users/jacky/Desktop/simple_multi/src-gen/pong_lf/pong_lf.py \"$@\""
    )
    install(PROGRAMS ${CMAKE_CURRENT_BINARY_DIR}/pong_lf DESTINATION ${CMAKE_INSTALL_BINDIR})
  endif()




