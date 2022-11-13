cmake_minimum_required(VERSION 3.17)
project(Chess VERSION 5.5)


add_executable(chess main.cpp)


add_subdirectory("${PROJECT_SOURCE_DIR}/thc-chess-library" EXCLUDE_FROM_ALL)
include_directories(${THC_CHESS_INCLUDE})
target_link_libraries(chess thc_chess_static) # or thc_chess for dynamic linking
