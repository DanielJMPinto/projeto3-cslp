import cv2
import sys
import numpy
from Frame import Frame
from golomb import Golomb
from BitStream import BitStream

class Video():
    def __init__(self, video_name):
        self.filename = video_name
        with open(self.filename, "rb") as header:
            self.header = (header.readline()).decode("utf-8")
            
        header_info = self.header.split(" ")
        for info in header_info:
            if info[0] == "W":
                self.width = int(info[1:])
            elif info[0] == "H":
                self.height = int(info[1:])
            elif info[0] == "F":
                fps=info.split(":")
                self.framerate = int(fps[0][1:])

        self.frame = Frame(self.width, self.height)
    
    def player(self):
        cap = cv2.VideoCapture(self.filename)
        i=1
        while (cap.isOpened()):
            ret, frame = cap.read()
            if i==1:
                #print(frame)
                i=0
            if ret == True:
                cv2.imshow('OpenCV based Video Player', frame)
                if cv2.waitKey(int(1000 / self.framerate)) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()
        cv2.destroyAllWindows()

    def encode_video(self,compressed_name):
        counter = 0
        golomb = Golomb(4)
        bitstream = BitStream
    
        with open(self.filename, "rb") as video:
            with open(compressed_name, "wb") as compressed_file:
                
                for line in video:
                    # passar as primeiras duas linhas pois sao parte do header
                    if counter >=2:
                        self.frame.setYUV(video)
                        compressed_frame=self.frame.encode_frame()
                        
                        y = compressed_frame[0]
                        u = compressed_frame[1]
                        v = compressed_frame[2]

                        for arr in y:
                            for value in arr:
                                pass

                        for arr in u:
                            for value in arr:
                                pass

                        for arr in v:
                            for value in arr:
                                pass

                    compressed_file.write(line)
                    
                    counter+=1
            

                    
        print(counter)

            


if __name__ == '__main__':
    video=Video(sys.argv[1])
    video.player()
    #video.encode_video("ducks_take_off2_444_720p50")