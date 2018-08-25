set(
    sources
    AccountManager.cpp AccountManager.h
    main.cpp
    MinerAux.cpp MinerAux.h
)

add_executable(aleth ${sources})
target_link_libraries(
    aleth
    PRIVATE ethereum ethashseal evm web3jsonrpc webthree devcore Boost::program_options python3
)

target_include_directories(aleth PRIVATE ../utils
    PRIVATE ${CMAKE_SOURCE_DIR}/externals/python/Include
    PRIVATE ${CMAKE_SOURCE_DIR}/externals/python
)

if(MINIUPNPC)
    target_compile_definitions(aleth PRIVATE ETH_MINIUPNPC)
endif()

install(TARGETS aleth DESTINATION bin)
