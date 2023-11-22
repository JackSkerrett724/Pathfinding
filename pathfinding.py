import cv2
import numpy as np

def CreateWindow():
    img = np.zeros((512, 512, 1), dtype = "uint8")
    cv2.imshow("Window", img)
    cv2.waitKey(0)

def main():
    print("Pathfinding for 1507")
    CreateWindow()


if __name__ == "__main__":
    main()