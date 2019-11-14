class BitStream:

    def read_file(self, filename):
        file = open(filename, 'rb')
        while True:
            var = file.read(1)
            if len(var) == 0:
                break
            bits = format(ord(var.decode()), 'b')
            nbits = len(bits)

            if nbits < 8:
                for i in range(0,8-nbits):
                    bits = '0' + bits
            print(bits)
        file.close()

    def return_bit_pos(self, filename, pos):
        file = open(filename, 'rb')

        byte = file.read(1)

        bits = format(ord(byte.decode('ascii')),'b')

        print(bits[pos])
        file.close()

    def write_file(self, filename):
        file = open(filename, 'wb')

        str = "hello world".encode()

        file.write(str)
        file.close()


if __name__ == '__main__':

    bs = BitStream()
    bs.write_file('test_b')
    bs.read_file('metade.pbm')
    bs.return_bit_pos('test_b', 2)