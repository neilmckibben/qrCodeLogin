import hashlib


#Hashes email and returns a nice hash
def generate_hash(email):
    hash_object = hashlib.sha256(email.encode())
    hex_dig = hash_object.hexdigest()
    print(hex_dig)


if __name__ == '__main__':
    generate_hash("hah")
