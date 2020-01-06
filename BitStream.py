
import os

class BitStream:
    def __init__(self):
        pass

    def read_n_bits(self, filename):
        bit_array=[]
        with open(filename, 'rb') as f:
            for l in range(os.path.getsize(filename)):
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


    bs = BitStream()
    ba = bs.read_n_bits('teste.txt')
    bs.write_n_bits('output',ba)
