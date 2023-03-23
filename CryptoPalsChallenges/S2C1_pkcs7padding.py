import math
def pkcspadding(text,block_size):
    """
    Pad yellow submarine, set 2 challenge 9
    """
    no_of_blocks = math.ceil(len(text) / float(block_size))
    pad_value = int(no_of_blocks * block_size - len(text))
    char_pad = bytes([pad_value])*pad_value
    print(text+char_pad)

    #
    #if pad_value == 0:
    #    return text + chr(block_size) * block_size
    #else:
    #    return text + chr(pad_value) * pad_value
    #

if __name__ == '__main__':
    pkcspadding(b'Yellow Submarine', 20)
