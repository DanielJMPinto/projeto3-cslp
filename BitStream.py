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
                    print(bit_to_store)
                    if bit_to_store:
                        self.bit_array.append(1)
                    else:
                        self.bit_array.append(0)
                    bits_read += 1
                else:
                    return True

    def write_n_bits(self, filename, n):
        dest = open(filename, 'wb')

        for i in range(n):
            bit_to_write = self.bit_array[i]



        pass

    def read_file(self, filename):
        file = open(filename, 'rb')
        bit_count = 0
        #fcontent = file.read().decode('latin1')
        #self.bit_array = ''.join(format(ord(byte), '08b') for byte in str(fcontent))


        file.close()

    def write_bits_to_file(self, filename):
        file = open(filename, 'wb')
        num_bytes = math.ceil(len(self.bit_array) / 8)
        '''
        for i in range(0, num_bytes*8, 8):
            print(int(self.bit_array[i:i+8], 2))
            byte = int(self.bit_array[i:i+8], 2).to_bytes(1, byteorder='big', signed=True)
            file.write(byte)
        '''

        bytes = int(self.bit_array, 2).to_bytes(num_bytes, byteorder='big', signed=True)

        file.write(bytes)