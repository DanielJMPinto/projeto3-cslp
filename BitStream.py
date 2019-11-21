class BitStream:
    def __init__(self):
        self.bit_array = None

    def read_file(self, filename):
        file = open(filename, 'rb')
        fcontent = file.read()
        self.bit_array = ''.join(format(ord(byte), '08b') for byte in str(fcontent))
        print(self.bit_array)

        #print(len(self.bit_array))

        file.close()

    def read_n_bits(self, num):
        pass

    def write_file(self, filename):
        file = open(filename, 'wb')

        str = "hello world".encode()

        file.write(str)
        file.close()


if __name__ == '__main__':

    bs = BitStream()
    bs.write_file('test_b')
    bs.read_file('test_b')