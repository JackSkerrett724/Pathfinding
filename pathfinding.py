import cv2
import numpy as np

pointList = []
def CreateWindow():
    global img
    #img = np.zeros((512, 512, 1), dtype = "uint8")
    img = cv2.imread("2023Field.png")
    print('Image Width is',img.shape[1])
    print('Image Height is',img.shape[0])
    img = cv2.resize(img, None, fx=.1, fy=.1)
    print('Image Width is',img.shape[1])
    print('Image Height is',img.shape[0])
    cv2.imshow("Window", img )

def CreatePath(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        cv2.circle(img, (x,y), 1, (225,225,0), -1)
        cv2.imshow("Window", img)
        pointList.append((x,y))
    elif event == cv2.EVENT_RBUTTONDOWN:
        for index, point in enumerate(pointList):
            if index+1 < len(pointList):
                cv2.line(img, point, pointList[index+1], (225,225,0), 1)
                cv2.imshow("Window", img)
        for i in range(5):
            cv2.rectangle(img, (pointList[0][0]-i, pointList[0][1]-i), (pointList[0][0]+i, pointList[0][1]+i), (225, 0, 0), -1)
            cv2.imshow("Window", img)
        



def main():
    print("Pathfinding for 1507")
    print("Left Click To Place Points, Right Click To Finish Placing Points")
    CreateWindow()
    cv2.setMouseCallback("Window", CreatePath)


if __name__ == "__main__":
    main()
    cv2.waitKey(0)