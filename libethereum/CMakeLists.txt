file(GLOB sources "*.cpp" "*.h")

add_library(ethereum ${sources})

message(STATUS, "++++++libethereum++++++++""${JSONCPP_LIBRARY}")

target_include_directories(ethereum PRIVATE ../utils)
target_link_libraries(ethereum PUBLIC evm ethcore p2p devcrypto devcore PRIVATE jsoncpp_lib_static Snappy::snappy)
