import hashlib
import qrcode

#Hashes email and returns a nice hash
def generate_hash(email):
    hash_object = hashlib.sha256(email.encode())
    hex_dig = hash_object.hexdigest()
    print(hex_dig)
    return hex_dig


def generate_qr_code(hash_value):
    img = qrcode.make(hash_value)
    img.save('test')

if __name__ == '__main__':
    hash = generate_hash("hah")
    generate_qr_code(hash)
