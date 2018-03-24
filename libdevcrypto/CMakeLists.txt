file(GLOB SOURCES "*.cpp")
file(GLOB HEADERS "*.h")

add_library(devcrypto ${SOURCES} ${HEADERS})

target_include_directories(devcrypto PRIVATE ${UTILS_INCLUDE_DIR})
target_link_libraries(devcrypto PUBLIC devcore secp256k1eth PRIVATE libff::ff cryptopp-static libscrypt::scrypt)

