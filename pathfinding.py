"""
1507 PATHFINDING
Will it ever work? who knows
By: Jack Skerrett
"""

import cv2
import numpy as np
import math
import csv

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
    cv2.imshow("1507 Pathfinding", img )


def CreatePath(event, x, y, flags, params):
    global first, origin, filename
    if event == cv2.EVENT_LBUTTONDOWN:
        if not first: ## Sets the origin to help with the relative points that help calculate angles
            origin = (x,y)
            first = True
            print(f"origin {origin}")
        print(x, y)
        cv2.circle(img, (x,y), 3, (0,225,0), -1) ## Place all other points 
        cv2.imshow("1507 Pathfinding", img)
        pointList.append((x ,y))
    elif event == cv2.EVENT_RBUTTONDOWN:
        for index, point in enumerate(pointList): 
            relativeList.append(((point[0] - origin[0]), -(point[1] - origin[1]))) ## Create the list of points relative to the origin
        #print(pointList[1][1] - pointList[0][1])
        for index, point in enumerate(pointList):
            if index+1 < len(pointList):
                cv2.line(img, point, pointList[index+1], (0,225,0), 2) ## Draw the lines on the image
                cv2.imshow("1507 Pathfinding", img)
                #########DISTANCE CALC###########
                dx = pointList[index+1][0] - point[0] 
                dy = pointList[index+1][1] - point[1]  
                d = math.sqrt(dx**2 + dy**2) ## Yay vector math
                distances.append(round(P2I(d),2)) ## distances in Inches that the robot can use (rounded to 2 decimal places)
                #################################
        #########ANGLE CALC##############
        for index, point in enumerate(relativeList):
            if index+1 < len(relativeList):
                dx = relativeList[index+1][0] - point[0]  ## Caluclate the angle using cool inverse trig
                dy = relativeList[index+1][1] - point[1] 
                sqrt = math.sqrt((dx**2) + (dy**2))   
                print(dx, dy, "hi")
                theta = math.acos(dx/sqrt) ## Theta in radians because python math hates me
                theta = math.degrees(theta) ## convert to degrees
                if(dy < 0): ## Math above only works from 0-pi (top half of the unit circle) so this help with any degree values that are supposed to be above 180
                    theta = 360 - theta
                angles.append(round(theta,2)) 
        ######################
        print(distances)
        print(angles) ## Print for debug
        print(relativeList)
        with open(filename+".csv", 'w', newline='') as file: ## Write all important data to CSV to be read by C++ code
            writer = csv.writer(file)
            field = ["Distance (In) ", " Direction (Deg)", " Points(x,y)"]
            writer.writerow(field) 
            for index, dist in enumerate(distances):
                writer.writerow([dist,angles[index], pointList[index]]) 
            writer.writerow([None, None, pointList[-1]]) ## There is one more point than there are distances so this accounts for that fact
            
        print(f"Your values are now in {filename}.csv")
    

def ViewPath(file):
        CreateWindow()
        i = 0
        readList = []
        with open(file+".csv") as points: 
            for row in points:
                if i == 0: ## Ignore the title row
                    i = 1
                else:
                    x = row.split(",")[2] ## This doesnt look pretty but its so you can get rid of the () and "" attatched to the numbers
                    y = row.split(",")[3]
                    x = x.replace("(", "")
                    x = x.replace( '"', "")
                    y = y.replace(")", "")
                    y = y.replace( '"', "")
                    readList.append((int(x),int(y)))
            for index, point in enumerate(readList): ## Same as the stuff above with the drawing lines and stuff
                print(point)
                cv2.circle(img, (point[0],point[1]), 3, (0,225,0), -1)
                cv2.imshow("1507 Pathfinding", img)
                if index+1 < len(readList):
                    cv2.line(img, point, readList[index+1], (0,225,0), 2)
                    cv2.imshow("1507 Pathfinding", img)

            

def main():  ## user pick betweens making a new auto or viewing an already made one
    global filename
    print("Pathfinding for 1507")
    choice = input("Would you like to place points or read from a CSV file? (P/R):" )
    if choice.upper() == 'P':
        filename = input("Name the file you would like your numbers to go to: ")
        print("Left Click To Place Points, Right Click To Finish Placing Points")
        CreateWindow()
        cv2.setMouseCallback("1507 Pathfinding", CreatePath)
    elif choice.upper() == 'R':
        file = input("What file would you like to view from? (do not add file extention): ")
        ViewPath(file)




if __name__ == "__main__":
    main()
    cv2.waitKey(0)