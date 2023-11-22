import cv2
import numpy as np
import math

#263 pixels = 224 inches
#1 Pixel = .85 inches
P2I = lambda p: p*.85 ## Convert Pixels to Inches
pointList = []
distances = []
def CreateWindow():
    global img
    #img = np.zeros((512, 512, 1), dtype = "uint8")
    img = cv2.imread("2023Field.png")
    img = cv2.resize(img, (768, 372)) 
    img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow("Window", img )

def CreatePath(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        cv2.circle(img, (x,y), 3, (0,225,0), -1)
        cv2.imshow("Window", img)
        pointList.append((x,y))
    elif event == cv2.EVENT_RBUTTONDOWN:
        #print(pointList[1][1] - pointList[0][1])
        for index, point in enumerate(pointList):
            if index+1 < len(pointList):
                cv2.line(img, point, pointList[index+1], (0,225,0), 2)
                cv2.imshow("Window", img)
                dx = pointList[index+1][0] - point[0] 
                dy = pointList[index+1][1] - point[1] 
                d = math.sqrt(dx**2 + dy**2)
                distances.append(P2I(d))
        print(distances)



def main():
    print("Pathfinding for 1507")
    print("Left Click To Place Points, Right Click To Finish Placing Points")
    CreateWindow()
    cv2.setMouseCallback("Window", CreatePath)


if __name__ == "__main__":
    main()
    cv2.waitKey(0)