from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b'uma mensagem qualquer')

print(token)

mensagem = f.decrypt(token)

print(mensagem)