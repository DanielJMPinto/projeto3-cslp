import cv2
import sys


def main(args):
    filename = args[1]
    framerate = int(args[2])

    cap = cv2.VideoCapture(filename)

    while (cap.isOpened()):
        ret, frame = cap.read()

        if ret == True:

            cv2.imshow('OpenCV based Video Player', frame)

            if cv2.waitKey(int(1000 / framerate)) & 0xFF == ord('q'):
                break

        else:
            break

    cap.release()

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv)