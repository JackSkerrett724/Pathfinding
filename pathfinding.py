import cv2
import numpy as np

def CreateWindow():
    global img
    img = np.zeros((512, 512, 1), dtype = "uint8")
    cv2.imshow("Window", img)

def CreatePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        cv2.circle(img, (x,y), 1, (225,225,0), -1)
        cv2.imshow("Window", img)

def main():
    print("Pathfinding for 1507")
    CreateWindow()
    print("continue")
    cv2.setMouseCallback("Window", CreatePoints)


if __name__ == "__main__":
    main()
    cv2.waitKey(0)