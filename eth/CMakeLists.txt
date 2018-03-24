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

hunter_add_package(OpenSSL)
find_package(OpenSSL "1.0.2" REQUIRED)

message("++++++++eth+++++++++++++${OPENSSL_CRYPTO_LIBRARY}")

add_executable(eth ${sources})
target_link_libraries(
    eth 
    PUBLIC intl
    PUBLIC ${ETHEREUM_DIR}/../libraries/python/libpython3.6m.a
    PUBLIC ${OPENSSL_CRYPTO_LIBRARY} ${OPENSSL_SSL_LIBRARY} ${OPENSSL_LIBRARIES}
    PRIVATE ethereum ethashseal evm web3jsonrpc webthree devcore Boost::program_options
)

target_include_directories(eth PRIVATE ../utils
                                 PUBLIC ${ETHEREUM_DIR}/../libraries/python/dist/include/python3.6m
)

if(MINIUPNPC)
    target_compile_definitions(eth PRIVATE ETH_MINIUPNPC)
endif()

install(TARGETS eth DESTINATION bin)
