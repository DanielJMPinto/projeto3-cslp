from BitStream import BitStream

stream = BitStream('test')

stream.read_n_bits(16)

print(stream.bit_array)
