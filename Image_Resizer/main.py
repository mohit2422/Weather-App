import cv2

# Configurable Parameters
source = "mohit.jpg"
destination = 'new_Image.jpg'
scale_percent = 50

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("My PIC", src)

cv2.waitKey(0)

#percent by which the image is resized

#calculate the 50 percent of original dimensions
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# dsize
dsize = (new_width, new_height)

# resize image
output = cv2.resize(src, dsize)

cv2.imwrite(destination,output)
# cv2.waitKey(0)