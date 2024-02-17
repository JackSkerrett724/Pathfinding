import cv2
import numpy as np
import math


#1 Pixel = .996 inches
P2I = lambda p: p*.996 ## Convert Pixels to Inches 
first = False
origin = (0,0)
pointList = []
relativeList = []
distances = []
angles = []
def CreateWindow():
    global img
    #img = np.zeros((512, 512, 1), dtype = "uint8")
    img = cv2.imread("2024Field.png")
    img = cv2.resize(img, (0,0), fx=0.25, fy=0.25) 
    #img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow("Window", img )


def CreatePath(event, x, y, flags, params):
    global first, origin
    if event == cv2.EVENT_LBUTTONDOWN:
        if not first:
            origin = (x,y)
            first = True
            print(f"origin {origin}")
        print(x, y)
        cv2.circle(img, (x,y), 3, (0,225,0), -1)
        cv2.imshow("Window", img)
        pointList.append((x ,y))
    elif event == cv2.EVENT_RBUTTONDOWN:
        for index, point in enumerate(pointList): 
            relativeList.append(((point[0] - origin[0]), -(point[1] - origin[1])))
        #print(pointList[1][1] - pointList[0][1])
        for index, point in enumerate(pointList):
            if index+1 < len(pointList):
                cv2.line(img, point, pointList[index+1], (0,225,0), 2)
                cv2.imshow("Window", img)
                #########DISTANCE CALC###########
                dx = pointList[index+1][0] - point[0] 
                dy = pointList[index+1][1] - point[1] 
                d = math.sqrt(dx**2 + dy**2)
                distances.append(P2I(d)) ## distances in Inches that the robot can use
                #################################
        #########ANGLE CALC##############
        for index, point in enumerate(relativeList):
            if index+1 < len(relativeList):
                dx = relativeList[index+1][0] - point[0] 
                dy = relativeList[index+1][1] - point[1] 
                sqrt = math.sqrt((dx**2) + (dy**2))   
                print(dx, dy, "hi")
                theta = math.acos(dx/sqrt) ## Theta in radians because python math hates me
                theta = math.degrees(theta) ## convert to degrees
                if(dy < 0):
                    theta = 360 - theta
                angles.append(theta)
        ######################
        print(distances)
        print(angles)
        print(relativeList)



def main():
    print("Pathfinding for 1507")
    print("Left Click To Place Points, Right Click To Finish Placing Points")
    CreateWindow()
    cv2.setMouseCallback("Window", CreatePath)


if __name__ == "__main__":
    main()
    cv2.waitKey(0)