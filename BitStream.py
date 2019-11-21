import math

class BitStream:
    def __init__(self):
        self.bit_array = None

    def read_file(self, filename):
        file = open(filename, 'rb')
        fcontent = file.read().decode('cp1252')
        self.bit_array = ''.join(format(ord(byte), '08b') for byte in str(fcontent))

        #print(len(self.bit_array))

        file.close()

    def read_n_bits(self, num):
        print(self.bit_array[0:num])

    def write_bits_to_file(self, filename):
        file = open(filename, 'wb')
        num_bytes = math.ceil(len(self.bit_array) / 8)
        bytes = int(self.bit_array, 2).to_bytes(num_bytes, byteorder='big', signed=True)
        print(bytes)

        file.write(bytes)


    def write_file(self, filename):
        file = open(filename, 'wb')

        str = "hello world".encode()

        file.write(str)
        file.close()


if __name__ == '__main__':

    bs = BitStream()
    #bs.write_file('test_b')
    bs.read_file('metade.pbm')
    bs.read_n_bits(30)
    bs.write_bits_to_file('test_c')