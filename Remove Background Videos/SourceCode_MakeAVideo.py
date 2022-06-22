from AddVideoBackground import l_green, u_green, mask, res, image
import cv2
import numpy as np

def main():
    windowname = "Writing To A Video"
    cv2.namedWindow(windowname)
    cap = cv2.VideoCapture("com.mp4")
    filename = "out.mp4"
    codec = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    framerate = 30
    resolution = (1920, 1080)
    VideoOutPut = cv2.VideoWriter(filename, codec, framerate, resolution)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    while ret:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (1920, 1080))
        f = frame-res
        green_screen = np.where(f==0, image, f)
        VideoOutPut.write(green_screen)
        cv2.imshow(windowname, green_screen)
        if cv2.waitKey(1) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
    VideoOutPut.release()

if __name__ == "__main__":
    main()