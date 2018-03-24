file(GLOB sources "*.cpp")
file(GLOB headers "*.h")

find_package(Boost REQUIRED filesystem system thread)

add_library(devcore ${sources} ${headers})

add_dependencies(devcore BuildInfo.h)

include_directories (${CMAKE_SOURCE_DIR}/libraries/ethereum)

# Needed to prevent including system-level boost headers:
target_include_directories(devcore SYSTEM PUBLIC ${Boost_INCLUDE_DIR} PRIVATE ../utils)

target_link_libraries(devcore ${Boost_LIBRARIES} Threads::Threads)

find_package(LevelDB)
target_include_directories(devcore SYSTEM PUBLIC ${LEVELDB_INCLUDE_DIRS})
target_link_libraries(devcore ${LEVELDB_LIBRARIES})
