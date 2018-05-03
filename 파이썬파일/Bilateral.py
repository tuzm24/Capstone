import cv2
import numpy as np
import cmath

def nothing(x):
    pass
def psnr(target, ref):
    import cv2
    target_data = np.array(target, dtype=np.float64)
    ref_data = np.array(ref,dtype=np.float64)

    diff = ref_data - target_data
    diff = diff.flatten()
    rmse = cmath.sqrt(np.mean(diff ** 2.))
    return 20 * cmath.log10(255 / rmse)

img = cv2.imread('lena_org.png')
jpg = cv2.imread('lena_org.jpg')
bi = cv2.bilateralFilter(jpg, 31, 10,10)
print("jpg 사진 PSNR : ", psnr(img,jpg))
print("bilateral 사진 PSNR", psnr(img, bi))


cv2.namedWindow('image')
cv2.createTrackbar('sigma_s', 'image', 1, 20, nothing)
cv2.createTrackbar('sigma_r', 'image', 0, 20, nothing)

while(1):
    if cv2.waitKey(1) & 0xFF == 27:
        break
    k = cv2.getTrackbarPos('sigma_s', 'image')
    k2 = cv2.getTrackbarPos('sigma_r', 'image')

    if k2==0:
        dst = cv2.GaussianBlur(img, (31,31), k)
    else:
        dst = cv2.bilateralFilter(img, 31, k*10, k2*10)
    if k==0:
        break
    cv2.imshow('image', dst)
cv2.destroyAllWindows()