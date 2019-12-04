import sys
from unary_coding import inverted_unary
from minimal_binary_coding import minimal_binary_coding

class Golomb():
    def __init__(self, file, b):
        self.file = file
        self.b = b

    def read_file(self):
        f = open(self.file, 'rb')
        fcontent = f.read().decode('cp1252')
        bit_array = ''.join(format(ord(byte), '08b') for byte in str(fcontent))

        bi=int(bit_array)
        #print(bi)

        f.close()
        self.golomb_encode(12662531652349)

    def golomb_encode(self, bits):
        print(inverted_unary(bits // self.b)+minimal_binary_coding(bits % self.b, self.b))

        
    def golomb_decode(self):
        pass

if __name__ == '__main__':
    b=120000000
    gol = Golomb('teste.txt', b)
    
    gol.read_file()