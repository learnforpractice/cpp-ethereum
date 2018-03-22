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

add_library(python3.6m STATIC IMPORTED)
set_property(TARGET python3.6m PROPERTY IMPORTED_LOCATION $ENV{PYTHON_LIB})

#add_library( ssl SHARED IMPORTED )
#set_property( TARGET ssl PROPERTY IMPORTED_LOCATION /usr/local/Cellar/openssl/1.0.2l/lib/libssl.dylib )

#add_library( crypto SHARED IMPORTED )
#set_property( TARGET crypto PROPERTY IMPORTED_LOCATION /usr/local/Cellar/openssl/1.0.2l/lib/libcrypto.dylib )

find_package(openssl REQUIRED)

add_executable(eth ${sources})
target_link_libraries(
    eth 
    PUBLIC intl
    PUBLIC $ENV{PYTHON_LIB}
    PUBLIC ${OPENSSL_CRYPTO_LIBRARY} ${OPENSSL_SSL_LIBRARY}
    PRIVATE ethereum ethashseal evm web3jsonrpc webthree devcore 
)

target_include_directories(eth PRIVATE ../utils
                                  PUBLIC $ENV{PYTHON_INC}
                                  PUBLIC $ENV{PYTHON_INC}/..
)

install(TARGETS eth DESTINATION bin)
