/**********************************************************************
 * Copyright (c) 2014 Pieter Wuille                                   *
 * Distributed under the MIT software license, see the accompanying   *
 * file COPYING or http://www.opensource.org/licenses/mit-license.php.*
 **********************************************************************/

#ifndef _SECP256K1_HASH_
#define _SECP256K1_HASH_

#include <stddef.h>
#include <stdint.h>

#ifndef CURVE_B
#define CURVE_B                        eth_CURVE_B
#endif
#ifndef secp256k1_context_clone
#define secp256k1_context_clone        eth_secp256k1_context_clone
#endif
#ifndef secp256k1_context_create
#define secp256k1_context_create       eth_secp256k1_context_create
#endif
#ifndef secp256k1_context_destroy
#define secp256k1_context_destroy      eth_secp256k1_context_destroy
#endif
#ifndef secp256k1_context_randomize
#define secp256k1_context_randomize    eth_secp256k1_context_randomize
#endif
#ifndef secp256k1_context_set_error_callback
#define secp256k1_context_set_error_callback eth_secp256k1_context_set_error_callback
#endif
#ifndef secp256k1_context_set_illegal_callback
#define secp256k1_context_set_illegal_callback eth_secp256k1_context_set_illegal_callback
#endif
#ifndef secp256k1_ec_privkey_tweak_add
#define secp256k1_ec_privkey_tweak_add eth_secp256k1_ec_privkey_tweak_add
#endif
#ifndef secp256k1_ec_privkey_tweak_mul
#define secp256k1_ec_privkey_tweak_mul eth_secp256k1_ec_privkey_tweak_mul
#endif
#ifndef secp256k1_ec_pubkey_combine
#define secp256k1_ec_pubkey_combine    eth_secp256k1_ec_pubkey_combine
#endif
#ifndef secp256k1_ec_pubkey_create
#define secp256k1_ec_pubkey_create     eth_secp256k1_ec_pubkey_create
#endif
#ifndef secp256k1_ec_pubkey_parse
#define secp256k1_ec_pubkey_parse      eth_secp256k1_ec_pubkey_parse
#endif
#ifndef secp256k1_ec_pubkey_serialize
#define secp256k1_ec_pubkey_serialize  eth_secp256k1_ec_pubkey_serialize
#endif
#ifndef secp256k1_ec_pubkey_tweak_add
#define secp256k1_ec_pubkey_tweak_add  eth_secp256k1_ec_pubkey_tweak_add
#endif
#ifndef secp256k1_ec_pubkey_tweak_mul
#define secp256k1_ec_pubkey_tweak_mul  eth_secp256k1_ec_pubkey_tweak_mul
#endif
#ifndef secp256k1_ec_seckey_verify
#define secp256k1_ec_seckey_verify     eth_secp256k1_ec_seckey_verify
#endif
#ifndef secp256k1_ecdh
#define secp256k1_ecdh                 eth_secp256k1_ecdh
#endif
#ifndef secp256k1_ecdh_raw
#define secp256k1_ecdh_raw             eth_secp256k1_ecdh_raw
#endif
#ifndef secp256k1_ecdsa_recover
#define secp256k1_ecdsa_recover        eth_secp256k1_ecdsa_recover
#endif
#ifndef secp256k1_ecdsa_recoverable_signature_convert
#define secp256k1_ecdsa_recoverable_signature_convert eth_secp256k1_ecdsa_recoverable_signature_convert
#endif
#ifndef secp256k1_ecdsa_recoverable_signature_parse_compact
#define secp256k1_ecdsa_recoverable_signature_parse_compact eth_secp256k1_ecdsa_recoverable_signature_parse_compact
#endif
#ifndef secp256k1_ecdsa_recoverable_signature_serialize_compact
#define secp256k1_ecdsa_recoverable_signature_serialize_compact eth_secp256k1_ecdsa_recoverable_signature_serialize_compact
#endif
#ifndef secp256k1_ecdsa_sign
#define secp256k1_ecdsa_sign           eth_secp256k1_ecdsa_sign
#endif
#ifndef secp256k1_ecdsa_sign_recoverable
#define secp256k1_ecdsa_sign_recoverable eth_secp256k1_ecdsa_sign_recoverable
#endif
#ifndef secp256k1_ecdsa_signature_normalize
#define secp256k1_ecdsa_signature_normalize eth_secp256k1_ecdsa_signature_normalize
#endif
#ifndef secp256k1_ecdsa_signature_parse_compact
#define secp256k1_ecdsa_signature_parse_compact eth_secp256k1_ecdsa_signature_parse_compact
#endif
#ifndef secp256k1_ecdsa_signature_parse_der
#define secp256k1_ecdsa_signature_parse_der eth_secp256k1_ecdsa_signature_parse_der
#endif
#ifndef secp256k1_ecdsa_signature_serialize_compact
#define secp256k1_ecdsa_signature_serialize_compact eth_secp256k1_ecdsa_signature_serialize_compact
#endif
#ifndef secp256k1_ecdsa_signature_serialize_der
#define secp256k1_ecdsa_signature_serialize_der eth_secp256k1_ecdsa_signature_serialize_der
#endif
#ifndef secp256k1_ecdsa_verify
#define secp256k1_ecdsa_verify         eth_secp256k1_ecdsa_verify
#endif
#ifndef secp256k1_hmac_sha256_finalize
#define secp256k1_hmac_sha256_finalize eth_secp256k1_hmac_sha256_finalize
#endif
#ifndef secp256k1_hmac_sha256_initialize
#define secp256k1_hmac_sha256_initialize eth_secp256k1_hmac_sha256_initialize
#endif
#ifndef secp256k1_hmac_sha256_write
#define secp256k1_hmac_sha256_write    eth_secp256k1_hmac_sha256_write
#endif
#ifndef secp256k1_nonce_function_default
#define secp256k1_nonce_function_default eth_secp256k1_nonce_function_default
#endif
#ifndef secp256k1_nonce_function_rfc6979
#define secp256k1_nonce_function_rfc6979 eth_secp256k1_nonce_function_rfc6979
#endif
#ifndef secp256k1_rfc6979_hmac_sha256_finalize
#define secp256k1_rfc6979_hmac_sha256_finalize eth_secp256k1_rfc6979_hmac_sha256_finalize
#endif
#ifndef secp256k1_rfc6979_hmac_sha256_generate
#define secp256k1_rfc6979_hmac_sha256_generate eth_secp256k1_rfc6979_hmac_sha256_generate
#endif
#ifndef secp256k1_rfc6979_hmac_sha256_initialize
#define secp256k1_rfc6979_hmac_sha256_initialize eth_secp256k1_rfc6979_hmac_sha256_initialize
#endif
#ifndef secp256k1_sha256_finalize
#define secp256k1_sha256_finalize      eth_secp256k1_sha256_finalize
#endif
#ifndef secp256k1_sha256_initialize
#define secp256k1_sha256_initialize    eth_secp256k1_sha256_initialize
#endif
#ifndef secp256k1_sha256_writ
#define secp256k1_sha256_writ          eth_secp256k1_sha256_writ
#endif


# ifdef __cplusplus
extern "C" {
# endif

typedef struct {
    uint32_t s[8];
    uint32_t buf[16]; /* In big endian */
    size_t bytes;
} secp256k1_sha256_t;

void secp256k1_sha256_initialize(secp256k1_sha256_t *hash);
void secp256k1_sha256_write(secp256k1_sha256_t *hash, const unsigned char *data, size_t size);
void secp256k1_sha256_finalize(secp256k1_sha256_t *hash, unsigned char *out32);

typedef struct {
    secp256k1_sha256_t inner, outer;
} secp256k1_hmac_sha256_t;

void secp256k1_hmac_sha256_initialize(secp256k1_hmac_sha256_t *hash, const unsigned char *key, size_t size);
void secp256k1_hmac_sha256_write(secp256k1_hmac_sha256_t *hash, const unsigned char *data, size_t size);
void secp256k1_hmac_sha256_finalize(secp256k1_hmac_sha256_t *hash, unsigned char *out32);

typedef struct {
    unsigned char v[32];
    unsigned char k[32];
    int retry;
} secp256k1_rfc6979_hmac_sha256_t;

void secp256k1_rfc6979_hmac_sha256_initialize(secp256k1_rfc6979_hmac_sha256_t *rng, const unsigned char *key, size_t keylen);
void secp256k1_rfc6979_hmac_sha256_generate(secp256k1_rfc6979_hmac_sha256_t *rng, unsigned char *out, size_t outlen);
void secp256k1_rfc6979_hmac_sha256_finalize(secp256k1_rfc6979_hmac_sha256_t *rng);

# ifdef __cplusplus
}
# endif

#endif
