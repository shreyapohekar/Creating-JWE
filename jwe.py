from jwcrypto import jwk, jwe
from jwcrypto.common import json_encode
import python_jwt as jwt, jwcrypto.jwk as jwk, datetime
from Crypto.PublicKey import RSA


key = RSA.importKey(open("public.pem","rb"))
pk = key.exportKey()
print(pk)
pub_key = jwk.JWK.from_pem(pk)
eprot = {"alg":"RSA-OAEP","enc":"A192GCM"}
stringPayload = '{"user":"admin"}'
E = jwe.JWE(stringPayload, json_encode(eprot))
E.add_recipient(pub_key)
encrypted_token = E.serialize(compact=True)
print(encrypted_token)
