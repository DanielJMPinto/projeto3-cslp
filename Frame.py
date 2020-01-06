import numpy

class Frame():
    def __init__(self, width, height):
        self.width=width
        self.height=height
        self.Y = None
        self.U = None
        self.V = None
        

    def predictor(self, a, b, c):
        if c >= max(a,b):
            return min(a,b)

        elif c <= min(a,b):
            return max(a,b)

        else:
            return a+b-c


    def encode_frame(self):
        encode_y = numpy.zeros(self.Y.shape)
        encode_u = numpy.zeros(self.U.shape)
        encode_v = numpy.zeros(self.V.shape)

        for h in range(self.height):
            for w in range(self.width):
                if w-1 >= 0 and h-1 >= 0:
                    predictor_y = self.predictor(int(self.Y[h, w-1]), int(self.Y[h-1, w]), int(self.Y[h-1, w-1]))
                    predictor_u = self.predictor(int(self.U[h, w-1]), int(self.U[h-1, w]), int(self.U[h-1, w-1]))
                    predictor_v = self.predictor(int(self.V[h, w-1]), int(self.V[h-1, w]), int(self.V[h-1, w-1]))
                else:
                    predictor_y = 0
                    predictor_u = 0
                    predictor_v = 0

                encode_y[h, w] = int(self.Y[h, w]) - predictor_y
                encode_u[h, w] = int(self.U[h, w]) - predictor_u
                encode_v[h, w] = int(self.V[h, w]) - predictor_v

        self.Y = encode_y
        self.U = encode_u
        self.V = encode_v

        return (self.Y, self.V, self.U)

    
    def setYUV(self, video):
        self.Y = numpy.fromfile(video, dtype=numpy.uint8, count=self.width * self.height).reshape((self.height, self.width))
        self.U = numpy.fromfile(video, dtype=numpy.uint8, count=self.width * self.height).reshape((self.height, self.width))
        self.V = numpy.fromfile(video, dtype=numpy.uint8, count=self.width * self.height).reshape((self.height, self.width))
        
