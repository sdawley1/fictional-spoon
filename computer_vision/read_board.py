import cv2 as cv
import imutils
import matplotlib.pyplot as plt


def read_board(image, template, method):
    """
    Reference (OpenCV-Python docs)
    https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html

    Params
    ------
    img (image) =
    temp (template) =
    meth (method) =
    """
    img = cv.imread(image, 0)
    temp = cv.imread(template, 0)
    # Resize images to (roughly) match size of template
    temp = imutils.resize(temp, width=int(img.shape[1] * 0.04))

    plt.show()
    w, h = temp.shape[::-1]

    # Multiple methods that can be used for template matching, all found at reference
    # Here we select one of them
    meth = eval(method)

    # Apply template matching
    res = cv.matchTemplate(img, temp, meth)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # Take maximum for TM_CCOEFF method
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # Plotting and Beautification
    cv.rectangle(img, top_left, bottom_right, 255, 2)
    plt.subplot(121), plt.title("Matching Result"), plt.xticks([]), plt.yticks([]) # Beautification
    plt.imshow(res, cmap="viridis") # Plot
    plt.subplot(122), plt.title("Detected Point"), plt.xticks([]), plt.yticks([]) # Beautification
    plt.imshow(img, cmap="viridis") # Plot
    plt.suptitle(meth)

    plt.savefig("test123.pdf")
    return


if __name__ == "__main__":
    test_image = "qrcodes/sampleqr.jpg"
    test_template = "qrcodes/12345.jpg"
    test_method = "cv.TM_CCOEFF"
    read_board(test_image, test_template, test_method)
