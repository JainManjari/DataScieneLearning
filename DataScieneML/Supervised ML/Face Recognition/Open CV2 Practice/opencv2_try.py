import cv2

img=cv2.imread("2.jpg")
gray=cv2.imread("2.jpg",cv2.IMREAD_GRAYSCALE)

#first argument is always the "title"
cv2.imshow("Img ",img) #here, cv2 reads the img directly as RGB unlike Matplotlib where we have to convert the image
cv2.imshow("Gray ",gray)

#Here the program will stop if any key is pressed
cv2.waitKey(0) #0 => wait for infinitely, otherwise if we give 35 then it will wait for 35 milli seconds

cv2.destroyAllWindows()