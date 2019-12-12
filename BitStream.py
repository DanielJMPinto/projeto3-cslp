import math
import os

class BitStream:
    def __init__(self, filename):
        self.filename = filename
        self.bit_array = []
        self.bits_read = 0
        self.file_size = os.path.getsize(filename)

    def read_n_bits(self, n):
        bits_read = 0
        filecontent = open(self.filename, 'rb')

        for bytecount in range(self.file_size):
            cur_byte = ord(filecontent.read(1))

            for i in range(0, 8):
                if bits_read < n:
                    bit_to_store = (cur_byte & (1 << (7 - i)))
                    if bit_to_store:
                        self.bit_array.append(1)
                    else:
                        self.bit_array.append(0)
                    bits_read += 1
                else:
                    return True

    def write_n_bits(self, filename, n):
        dest = open(filename, 'wb')

        nbytes = math.ceil(n / 8)
        print(nbytes)
        bits_written = 0

        for i in range(nbytes):
            counter = 0
            built_byte = 0
            while counter < 8:
                bit_to_write = self.bit_array[bits_written]
                built_byte = built_byte | (bit_to_write << (7 - counter))
                counter += 1
                bits_written += 1

                if bits_written == n:
                    print(built_byte)
                    dest.write(built_byte.to_bytes(1, "little"))
                    break
            if bits_written == n:
                break
            else:
                print(built_byte)
                dest.write(built_byte.to_bytes(1, "little"))