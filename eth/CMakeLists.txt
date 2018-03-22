add_custom_command(
    OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/wrap/eth_.wrap.cpp
    COMMAND cython --cplus ${CMAKE_CURRENT_SOURCE_DIR}/eth_.pyx -o ${CMAKE_CURRENT_SOURCE_DIR}/wrap/eth_.wrap.cpp
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/eth_.pyx
)


set(
    sources
    AccountManager.cpp AccountManager.h
    main.cpp
    wrap/eth_.wrap.cpp
    MinerAux.h
)

find_package(openssl REQUIRED)

add_executable(eth ${sources})
target_link_libraries(
    eth 
    PUBLIC intl
    PUBLIC ${CMAKE_SOURCE_DIR}/libraries/python/libpython3.6m.a
    PUBLIC ${OPENSSL_CRYPTO_LIBRARY} ${OPENSSL_SSL_LIBRARY}
    PRIVATE ethereum ethashseal evm web3jsonrpc webthree devcore 
)

target_include_directories(eth PRIVATE ../utils
                                 PUBLIC ${CMAKE_SOURCE_DIR}/libraries/python/dist/include/python3.6m
)

install(TARGETS eth DESTINATION bin)
