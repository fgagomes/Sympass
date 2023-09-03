import base64

# These functions should be modified with real encryption
# For now, they will encode and decode using base64 just to make file not easily readable
# Since the file is stored locally, it should suffice for my level of knowledge


def encrypt(data):
    key = "adminFelipe"
    data_bytes = data.encode()
    key_bytes = key.encode()

    encrypted_data = bytearray()

    for i in range(len(data_bytes)):
        encrypted_byte = data_bytes[i] ^ key_bytes[i % len(key_bytes)]
        encrypted_data.append(encrypted_byte)

    encoded_data = base64.b64encode(encrypted_data).decode()
    return encoded_data


def decrypt(encrypted_data):
    key = "adminFelipe"
    decoded_data = base64.b64decode(encrypted_data)
    decrypted_data = bytearray()

    key_bytes = key.encode()

    for i in range(len(decoded_data)):
        decrypted_byte = decoded_data[i] ^ key_bytes[i % len(key_bytes)]
        decrypted_data.append(decrypted_byte)

    return decrypted_data.decode()
