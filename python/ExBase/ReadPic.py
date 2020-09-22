from PIL import Image
import os
import cv2 as cv
import python.ReadImgToForm

pic = Image.open("python\\11.jpg")
# pic = pic.convert("P")
# pic.show()


# #  获取交点坐标
# = picProcess()
# x_val = getCoord(lines_col, flag="col")
# y_val = getCoord(lines_row, flag="row")

def picProcess2(file):
    img = cv.imread(file)
    #为了方便后续操作，将图像统一大小
    img = cv.resize(img, (800, 165))

    img_h = img.shape[0]
    img_w = img.shape[1]
    # 转为灰度图
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    #分离处红色通道
    img_R = cv.split(img)[2]
    # 红色通道图二值化，同时反转，即将原图中红色、白色变黑，黑色变白，便于后续操作
    thr = 100
    ret, img_bin = cv.threshold(img_R, thr, 255, cv.THRESH_BINARY_INV)

    # 滤波器的长度设为9，是为了避免较粗线条的干扰
    kernel_col = np.ones((9, 1))
    kernel_row = np.ones((1, 9))

    #开运算求横线和纵线
    img_open_col = cv.morphologyEx(img_bin, cv.MORPH_OPEN, kernel_col)
    img_open_row = cv.morphologyEx(img_bin, cv.MORPH_OPEN, kernel_row)
    #图片高度较低，为了方便霍夫寻纵线，将图片的高度拉高5倍
    img_open_col = cv.resize(img_open_col, (800, 5 * img_h))

    #霍夫寻线
    lines_col = cv.HoughLinesP(img_open_col, 1, np.pi / 180, 100, minLineLength=int(0.52 * 5 * img_h),maxLineGap=5)
    lines_row = cv.HoughLinesP(img_open_row, 1, np.pi / 180, 100, minLineLength=int(0.75 * img_w),maxLineGap=5)

    return img_w,img_h, img_gray, lines_col, lines_row


img_w, img_h, img_gray, lines_col, lines_row = picProcess2(pic)
