import numpy as np
import sys
import cv2 as cv

def main(img):
    if img is None:
        sys.exit("Could not read image.")

    # Show image
    cv.imshow("Display window", img)
    # Display image indefinitely here
    # To exit, press "k" on the keyboard
    k = cv.waitKey(0)

    if k == ord("s"):
        cv.imwrite("temp.png", img)
    return


if __name__ == "__main__":
    image = cv.imread("qrcodes/1.jpg", 0)
    main(image)
