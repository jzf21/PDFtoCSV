import cv2
import pytesseract

# set tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# read image file
img = cv2.imread("whatsapp.jpeg")

# convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# perform thresholding to create binary image
ret, thresh = cv2.threshold(
    gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# apply dilation to fill gaps in the contours
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
dilation = cv2.dilate(thresh, rect_kernel, iterations=1)

# find contours in the binary image
contours, hierarchy = cv2.findContours(
    dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# create a copy of the original image for visualization purposes
img_copy = img.copy()

# open a file to write the recognized text
with open("recognized.txt", "w") as file:
    # loop through all the contours found
    for cnt in contours:
        # get the coordinates of the bounding rectangle around the contour
        x, y, w, h = cv2.boundingRect(cnt)

        # draw a rectangle around the contour on the original image
        cv2.rectangle(img_copy, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # extract the region of interest containing the contour
        roi = img[y:y+h, x:x+w]

        # apply OCR to the region of interest
        text = pytesseract.image_to_string(roi)

        # write the recognized text to the file
        file.write(text)

# display the original image with the contours drawn on it
cv2.imshow("Contours", img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
