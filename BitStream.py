import os

class BitStream:
    def __init__(self, filename):
        self.filename = filename

    def read_n_bits(self, no_bits):
        bit_array=[]
        with open(self.filename, 'rb') as f:
            for l in range(os.path.getsize(self.filename)):
                byte=ord(f.read(1))
                
                for i in range (8):

                    print(byte)
                    bit_array.append((byte >> i) & 1)
                    
            
        print(bit_array)
        return bit_array
        


    def write_n_bits(self, filename, ba):
        with open(filename, 'wb') as f:
            bitstream=0
            for i in range(len(ba)):
                bit = ba[i]
                bitstream |= int(bit) << (7 - i % 8)
                if i % 8 == 0 and i != 0:
                    f.write(bitstream.to_bytes(1,"little"))
                    bitstream = 0


        f.close()


if __name__ == '__main__':

    bs = BitStream('teste.txt')
    ba = bs.read_n_bits(16)
    bs.write_n_bits('output',ba)