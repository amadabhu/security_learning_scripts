from base64 import b64decode, b64encode

import binascii

#binary_string = binascii.unhexlify(hex_string)
def bytesxor(input1:str,input2:str) -> bytes:

    print("These are the inputs:")
    print(input1)
    print(input2)

    print("These are the inputs in byte form")
    bytes1 = bytes.fromhex(input1)
    bytes2 = bytes.fromhex(input2)
    print(bytes1)
    print(bytes2)

    print("The XOR operation happens now:")

    output_bytes = bytes(a ^ b for a,b in zip(bytes1,bytes2))

    print("Done.")
    output_hex = output_bytes.hex()

    print("Output:")
    print(output_bytes)

    print("Output in hex:")
    print(output_hex)


    return output_bytes



if __name__ == '__main__':

    bytesxor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965')

