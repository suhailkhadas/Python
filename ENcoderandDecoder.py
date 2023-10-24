import base64

#encoder
def encrypt_pass(password):
    encoded_bytes = base64.b64encode(password.encode())
    print(encoded_bytes)


user_pass=input("Enter the password: ")
encrypt_pass(user_pass)


#decoder
def decrypt_pass(password):
    decode_bytes=base64.b64decode(password)
    decode_data=decode_bytes.decode()
    print("decode password",decode_data)

user_pass=input("Enetr base 64 string: ")
decrypt_pass(user_pass)