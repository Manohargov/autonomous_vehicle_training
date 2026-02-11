from pal.products.qcar import QCarRealSense
import cv2

myCam = QCarRealSense(mode="RGB, Depth")
try:
    while True:
        myCam.read_RGB()
        cv2.imshow("My RGB", myCam.imageBufferRGB)

        if cv2.waitKey(1) & 0xFF ==ord('q'):
            print("stopping")
            break


except KeyboardInterrupt:
    print("exit")
    
cv2.destroyAllWindows()
