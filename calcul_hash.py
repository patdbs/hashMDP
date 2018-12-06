# python3
from hashlib import md5,sha1

lemdp="monmotdepassesecret"

def hash_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()

def hash_sha1(s, encoding='utf-8'):
    return sha1(s.encode(encoding)).hexdigest()


print("Hash non sécurisé du mot de passe (MD5)")
print(hash_md5(lemdp, encoding='utf-8'))

print("Hash sécurisé du mot de passe (SHA1)")
print(hash_sha1(lemdp, encoding='utf-8'))


