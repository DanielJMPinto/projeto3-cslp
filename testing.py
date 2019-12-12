from BitStream import BitStream

stream = BitStream('test')

stream.read_n_bits(48)

print(stream.bit_array)

stream.write_n_bits('out', 47)
