from __future__ import print_function
import sys
import cv2
import numpy as np

video = cv2.VideoCapture("com_3.mp4")
image = cv2.imread("img2.jpg")

filename = "out2.mp4"
codec = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
framerate = 60
resolution = (1920, 1080)
VideoOutPut = cv2.VideoWriter(filename, codec, framerate, resolution)

def nothing(): 
  pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",300,300)

cv2.createTrackbar("L - H", "Trackbars", 0,179, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0,255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0,255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 179,179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255,255, nothing)
cv2.createTrackbar("U - v", "Trackbars", 255,255, nothing)

while(video.isOpened()):
    ret, frame = video.read()

    if not ret:
      break
    image = cv2.resize(image, (resolution))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_green = np.array([32, 94, 132])
    u_green = np.array([179, 255, 255])

    mask = cv2.inRange(hsv, l_green, u_green)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    f = frame-res
    final_video=np.where(f==0, image, f)

    VideoOutPut.write(final_video)
    cv2.imshow("Writing To A Video", final_video)
    k = cv2.waitKey(1)
    if k == ord('q'):
      break
    if k == 27:
      break
cv2.destroyAllWindows()
VideoOutPut.release()
video.release()