# -*- coding: utf-8 -*-
import hashlib, binascii, os
class Hash(object):
    def hash_info(password):
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        passwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                    salt, 100000)
        passwdhash = binascii.hexlify(passwdhash)
        return (salt + passwdhash).decode('ascii')

    def verify_two_hash(original_hash, info_no_hash):
        salt = original_hash[:64]
        original_hash = original_hash[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      info_no_hash.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == original_hash
