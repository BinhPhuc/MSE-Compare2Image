import cv2 
import numpy as np

def mse(img1, img2):
    height, width = img1.shape
    gap = cv2.subtract(img1, img2)
    error = np.sum(gap**2)
    mse = error/(float(height * width)) 
    return mse, gap

#input
panda_1 = cv2.imread('input/panda_1.jpg')
panda_2 = cv2.imread('input/panda_2.jpg')
# convert to grayscale
panda_1 = cv2.cvtColor(panda_1, cv2.COLOR_BGR2GRAY)
panda_2 = cv2.cvtColor(panda_2, cv2.COLOR_BGR2GRAY)
# the height, width and the number of channels must be the same

# pd1 = cv2.imread('deobietdattenlagi/pd1.jpg')
# pd2 = cv2.imread('deobietdattenlagi/pd2.jpg')
# pd1 = cv2.cvtColor(pd1, cv2.COLOR_BGR2GRAY)
# pd2 = cv2.cvtColor(pd2, cv2.COLOR_BGR2GRAY)
# std_height = pd1.shape[0]
# std_width = pd1.shape[1]
# std_dim = (std_width, std_height)
# pd2 = cv2.resize(pd2, std_dim, interpolation = cv2.INTER_AREA)

# print("Pd1 shape: ", pd1.shape)
# print("Pd2 shape: ", pd2.shape)

error, gap = mse(panda_1, panda_2)

print("Image matching Error between the two images:" ,error)

cv2.imshow("gap", gap)
cv2.waitKey(0)
cv2.destroyAllWindows()
