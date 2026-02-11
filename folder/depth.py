import cv2
from pal.products.qcar import QCarRealSense

myCam =QCarRealSense (mode = 'RGB , Depth')

try:
    while True:
        myCam.read_RGB()
        cv2.imshow('my RGB', myCam.imageBufferRGB)

        myCam.read_depth()
        cv2.imshow('my depth', myCam.imageBufferDepthPX)

        if cv2.waitKey(1) & 0xFF ==ord('q'):
            print("stoppoing")
            break
except KeyboardInterrupt:
    print("Exit")

cv2.destroyAllWindows()
