from base64 import b64decode, b64encode

def conv_2_base_64 ():

    input_str = input("Type the hex value:")

    b64_encoded = b64encode(bytes.fromhex(input_str)).decode()

    print(b64_encoded)

    return b64_encoded


if __name__ == '__main__':
    conv_2_base_64()