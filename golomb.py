import os
import math

class Golomb():
    def __init__(self, m):
        self.m = m
        self.code = []
        
                
    def golomb_encode(self, value):
        with open(self.filename, 'rb') as f:
            for l in range(os.path.getsize(self.filename)):
                byte = ord(value)
                quot = byte // self.m
                rest = byte % self.m
                
                for i in range(int(math.log2(self.m))):
                    self.code.append((rest >> i) & 1)
                
                self.code = self.code + ([1] * quot + [0])
                

        
    def golomb_decode(self):
        size_resto=int(math.log2(self.m))
        resto_bi=''
        quociente=0
        with open("output_golomb.txt", 'w') as f:
            for l in self.code:
                
                if len(resto_bi) == size_resto:
                    resto=int(resto_bi[::-1], 2)

                    if l == 0:
                        byte = self.m * quociente + resto
                        f.write(chr(byte))
                        resto_bi=''
                        quociente=0
                        
                    else:
                        quociente += 1

                else:
                    resto_bi=resto_bi+str(l)
