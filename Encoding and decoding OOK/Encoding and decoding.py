def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])


s = "Hello, World!"
s_bits = string2bits(s)
s_bits_as_str = "".join(s_bits)
decoded_s = bits2string(s_bits)
print(s_bits)
print(s_bits_as_str)
print(decoded_s)

