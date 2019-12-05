import os
import math

class Golomb():
    def __init__(self, m, filename):
        self.m = m
        self.filename = filename
        self.code = []
        
                
    def golomb_encode(self):
        with open(self.filename, 'rb') as f:
            for l in range(os.path.getsize(self.filename)):
                byte = ord(f.read(1))
                quot = byte // self.m
                rest = byte % self.m
                
                for i in range(int(math.log2(self.m))):
                    self.code.append((rest >> i) & 1)
                
                self.code = self.code + ([1] * quot + [0])
                

        
    def golomb_decode(self):
        size_resto=int(math.log2(self.m))
        resto_bi=''
        quociente=0

        for l in self.code:
            
            if len(resto_bi) == size_resto:
                resto=int(resto_bi[::-1], 2)

                if l == 0:
                    byte = self.m * quociente + resto
                    
                    resto_bi=''
                    quociente=0
                    
                else:
                    quociente += 1

            else:
                resto_bi=resto_bi+str(l)


if __name__ == '__main__':
    gol = Golomb(16, 'teste.txt')
    
    gol.golomb_encode()
    gol.golomb_decode()