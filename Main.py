from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


salt = b'\xf9a\x9b\x93.\xa5}\x91#\xe0"$\xa4\x8cH\\\xc7\x07:U\xa6\xe9\x06\xa9E\xa0\xe4Emf\x81\xee'
password= "mypassword"

key = PBKDF2(password, salt, dkLen=32)

message = input('Digite uma mensagem para ser criptografada: ')
bytes = message.encode("UTF-8")

cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(bytes, AES.block_size ))

with open('encrypted.bin', 'wb') as f:
    f.write(cipher.iv)
    f.write(ciphered_data)

decrypt = input('Descriptografar? (Y/N): ')
if decrypt != 'y' or decrypt == 'Y':
    print("Adeus!")

else:
    with open('encrypted.bin', 'rb') as f:
            iv = f.read(16)
            decrypt_data = f.read()

            cipher = AES.new(key, AES.MODE_CBC, iv=iv )
            original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
            print(original)