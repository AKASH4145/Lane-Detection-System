import cv2
import numpy as np

def region_of_interest(edges):
    height, width = edges.shape
    mask = np.zeros_like(edges)
    polygon = np.array([[
    (0, height),
    (width, height),
    (width*0.75, height*0.55),
    (width*0.25, height*0.55)
  ]], np.int32)
    cv2.fillPoly(mask, polygon, 255)

    masked = cv2.bitwise_and(edges, mask)
    return masked

def make_coordinates(frame, line_parameters):
    slope, intercept = line_parameters

    y1 = frame.shape[0]
    y2 = int(y1 * 0.6)

    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)

    return np.array([x1, y1, x2, y2])

def lane_detection(frame):
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_blur=cv2.GaussianBlur(gray,(5,5),0)
    edges=cv2.Canny(gray_blur,30,100)
    cv2.namedWindow("Edges",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Edges",600,400)
    cv2.imshow("Edges", edges)
    roi=region_of_interest(edges)

    lines = cv2.HoughLinesP(roi,2,np.pi/180,50,minLineLength=40,maxLineGap=100)

    left_fit = []
    right_fit = []

    if lines is not None:
     for line in lines:
        x1, y1, x2, y2 = line[0]

        if x2 == x1:
            continue

        slope = (y2 - y1) / (x2 - x1)
        intercept = y1 - slope * x1

        if abs(slope) < 0.5:
            continue

        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))


    if len(left_fit) > 0:
     left_lane = np.mean(left_fit, axis=0)
     left_line = make_coordinates(frame, left_lane)
     cv2.line(frame,(left_line[0],left_line[1]),(left_line[2],left_line[3]),(0,255,0),5)

    if len(right_fit) > 0:
     right_lane = np.mean(right_fit, axis=0)
     right_line = make_coordinates(frame, right_lane)
     cv2.line(frame,(right_line[0],right_line[1]),(right_line[2],right_line[3]),(0,255,0),5)  

    if len(left_fit) > 0 and len(right_fit) > 0:

     points = np.array([
        [left_line[0], left_line[1]],
        [left_line[2], left_line[3]],
        [right_line[2], right_line[3]],
        [right_line[0], right_line[1]]
    ])

     lane_overlay = np.zeros_like(frame)
     cv2.fillPoly(lane_overlay, [points], (0,255,0))
     frame = cv2.addWeighted(frame, 1, lane_overlay, 0.3, 0)

    cv2.namedWindow("Region of interest",cv2.WINDOW_NORMAL)
    cv2.namedWindow("Detected lane",cv2.WINDOW_NORMAL)   
    cv2.resizeWindow("Region of interest",600,400)
    cv2.resizeWindow("Detected lane",600,400)
    cv2.imshow( "Region of interest",roi)
    cv2.imshow("Detected lane",frame)
    

    


if __name__=='__main__':
    cap=cv2.VideoCapture(r"C:\Users\akash\Desktop\OpenCV Projects\Lane Detection\Sample Videos\dashcam.mp4")
    while True:
     ret , frame=cap.read()
     if ret:
        lane_detection(frame)
        if cv2.waitKey(1)==13:
            break
    cap.release()
    cv2.destroyAllWindows    