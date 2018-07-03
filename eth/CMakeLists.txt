set(PYTHON3 "LD_LIBRARY_PATH=${CMAKE_SOURCE_DIR}/libraries/python;${CMAKE_SOURCE_DIR}/libraries/python/dist/bin/python3")

add_custom_command(
    OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/wrap/eth_.wrap.cpp
    COMMAND PYTHON3 -m cython --cplus ${CMAKE_CURRENT_SOURCE_DIR}/eth_.pyx -o ${CMAKE_CURRENT_SOURCE_DIR}/wrap/eth_.wrap.cpp
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/eth_.pyx
)

set(
    sources
    AccountManager.cpp AccountManager.h
    main.cpp
    wrap/eth_.wrap.cpp
    MinerAux.h
)

add_executable(eth ${sources})
target_link_libraries(
    eth
    PRIVATE ethereum ethashseal evm web3jsonrpc webthree devcore python3 Boost::program_options
)

target_include_directories(eth PRIVATE ../utils
        PUBLIC ${CMAKE_SOURCE_DIR}/libraries/python
        PUBLIC ${CMAKE_SOURCE_DIR}/libraries/python/Include
)


if(MINIUPNPC)
    target_compile_definitions(eth PRIVATE ETH_MINIUPNPC)
endif()

install(TARGETS eth DESTINATION bin)
