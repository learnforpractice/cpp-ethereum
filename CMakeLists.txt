# Aleth: Ethereum C++ client, tools and libraries.
# Copyright 2018 Aleth Autors.
# Licensed under the GNU General Public License, Version 3. See the LICENSE file.

cmake_minimum_required(VERSION 3.5.1)

project(cpp-ethereum)
set(PROJECT_VERSION 1.4.0.dev0)

if (NOT EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/evmjit/.git)
    message(FATAL_ERROR "Git submodules not initialized, execute:\n  git submodule update --init")
endif()

cable_set_build_type(DEFAULT RelWithDebInfo CONFIGURATION_TYPES Debug;Release;RelWithDebInfo)

cable_add_buildinfo_library(PROJECT_NAME aleth)

set(CMAKE_SKIP_INSTALL_ALL_DEPENDENCY On)

include(EthCcache)
include(EthOptions)
include(EthCompilerSettings)
include(EthExecutableHelper)
include(EthDependencies)
include(EthUtils)

#set(Boost_USE_STATIC_LIBS ON)
#set(Boost_USE_MULTITHREADED ON)
#hunter_add_package(Boost COMPONENTS program_options filesystem system thread context fiber log)
#find_package(Boost CONFIG REQUIRED program_options filesystem system thread context fiber log)

hunter_add_package(jsoncpp)
find_package(jsoncpp CONFIG REQUIRED)

hunter_add_package(Snappy)
find_package(Snappy CONFIG REQUIRED)

hunter_add_package(cryptopp)
find_package(cryptopp CONFIG REQUIRED)

hunter_add_package(libjson-rpc-cpp)
find_package(libjson-rpc-cpp CONFIG REQUIRED)

hunter_add_package(libscrypt)
find_package(libscrypt CONFIG REQUIRED)

hunter_add_package(ethash)
find_package(ethash CONFIG REQUIRED)

include(ProjectSecp256k1)
#include(ProjectLibFF)

find_package(Threads)

if(MINIUPNPC)
    find_package(Miniupnpc 1.8.2013 REQUIRED)
endif()

set(UTILS_INCLUDE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/utils")

configure_project()

if(TESTS)
    # Import binaryen library before hera to make it available also to testeth.
    include(hera/cmake/ProjectBinaryen.cmake)
endif()

add_subdirectory(evmc)

if (HERA)
    add_subdirectory(hera)
endif()

#Global include path for all libs.
include_directories("${CMAKE_CURRENT_SOURCE_DIR}")

option(ALETH_INTERPRETER_SHARED "Build aleth-interpreter as a shared library" OFF)
add_subdirectory(libaleth-interpreter)

add_subdirectory(libdevcore)
add_subdirectory(libdevcrypto)
add_subdirectory(libp2p)

add_subdirectory(libethcore)
add_subdirectory(libevm)

add_subdirectory(libethereum)
add_subdirectory(libethashseal)

#add_subdirectory(libwebthree)
#add_subdirectory(libweb3jsonrpc)

if (EVMJIT)
    add_subdirectory(evmjit)
endif()

add_subdirectory(aleth)

if (TOOLS)
    add_subdirectory(aleth-key)
    add_subdirectory(aleth-vm)
    add_subdirectory(rlp)
endif()

if (TESTS)
#    enable_testing()
#    add_subdirectory(test)
endif()


install(FILES ${PROJECT_BINARY_DIR}/aleth/buildinfo.json DESTINATION ${CMAKE_INSTALL_DATADIR}/aleth)


if(WIN32)
    set(CPACK_GENERATOR ZIP)
else()
    set(CPACK_GENERATOR TGZ)
endif()
set(CPACK_PACKAGE_FILE_NAME ${PROJECT_NAME})
set(CPACK_PACKAGE_CHECKSUM SHA256)
set(CPACK_INCLUDE_TOPLEVEL_DIRECTORY FALSE)
include(CPack)
