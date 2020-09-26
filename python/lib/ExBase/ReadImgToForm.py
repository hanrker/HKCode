# Created by 秋沐霖 on 2019/3/8.
from PIL import Image
import pytesseract #OCR识别
import cv2 as cv
import numpy as np
import csv
import time
import os
import requests
from bs4 import BeautifulSoup
from openpyxl.compat import range

# 获取最新图片
def getImage():
    # 当天是否发布报告的标值
    flag = 0
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER',
    }

    # 收益率曲线主页
    YieldCurveUrl='https://www.chinaratings.com.cn/AbsPrice/YieldCurve/'

    # 请求并解析网页
    html = requests.get(YieldCurveUrl, headers=headers)
    html=html.content.decode('UTF-8')
    soup = BeautifulSoup(html, 'lxml')
    #  获取今天日期
    today=time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 获取当前日期，作为图片的名字保存到本地
    img_title=soup.select('body > div.main > div > div.ctr > div.recruit > ul > li > span')[0].text.split('：')[-1]

    if img_title==today:
        flag = 1
        # print(img_title)

        # 获取最新的曲线所在页面的链接
        YieldCurveUrl='https://www.chinaratings.com.cn'+soup.select('body > div.main > div > div.ctr > div.recruit > ul > li > a')[0].get('href')

        # 请求该链接，解析出该图片的下载链接img_url
        html = requests.get(YieldCurveUrl, headers=headers)
        soup = BeautifulSoup(html.text, 'lxml')
        img_url ='https://www.chinaratings.com.cn'+ soup.select('body > div.main > div.ctr > div > div.newsmcont > p > img')[1].get('src')

        # print(img_url)
        rep = requests.get(img_url, headers=headers)

        #将图片写到本地
        with open(r'./img/'+img_title+'.png','wb')as f:
            f.write(rep.content)

    return img_title, flag


#图像预处理
def picProcess():
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

#求交点坐标
def getCoord(lines, flag):
    #求竖线的横坐标
    if flag == "col":
        lines_x = np.sort(lines[:,:,0], axis=None)
        list_x = list(lines_x)

        #合并距离相近的点
        for i in range(len(list_x) - 1):
            if (list_x[i] - list_x[i + 1]) ** 2 <= (img_w/12)**2:
                list_x[i + 1] = list_x[i]

        list_x = list(set(list_x))#去重
        list_x.sort()#排序
        return list_x

    #求横线的纵坐标
    elif flag == "row":
        lines_y = np.sort(lines[:,:,1], axis=None)
        list_y = list(lines_y)

        # 合并距离相近的点
        for i in range(len(list_y) - 1):
            if (list_y[i] - list_y[i + 1]) ** 2 <= (img_h/8)**2:
                list_y[i + 1] = list_y[i]

        list_y = list(set(list_y))  # 去重
        list_y.sort()  # 排序
        return list_y

#识别日期及数值
def recognize():
    kernel_small = np.ones((3, 3))
    text = ['关键期限点曲线值']

    #日期，为报告发布日期
    per_text = png_name
    text.append(per_text)

    add_list = ['360','1080','1800','3600','10800','ABS','RMBS']
    text = text + add_list

    #数值，放大三倍，腐蚀两次，效果较好
    for i in range(2):
        for j in range(5):
            #截取对应的区域
            area = img_gray[(y_val[i+2]+4) :y_val[i+3], (x_val[j+1]+10) :(x_val[j+2]-10)]
            #二值化
            area_ret, area_bin = cv.threshold(area, 190, 255, cv.THRESH_BINARY)
            #放大三倍
            area_bin = cv.resize(area_bin, (0,0), fx=3, fy=3)
            # 腐蚀两次，加粗字体
            area_bin = cv.erode(area_bin, kernel_small, iterations=2)

            #送入OCR识别
            per_text = pytesseract.image_to_string(Image.fromarray(area_bin), lang="ftnum", config="--psm 7")

            #易错修正
            if ' ' in per_text:
                per_text = ''.join(per_text.split()) #去多余空格
            if '..' in per_text:
                per_text.replace('..', '.')

            text.append(per_text)

    #整理顺序，方便写入表格
    index = text[8]
    text[8:13] = text[9:14]
    text[13] = index

    return text

#写入csv
def writeCsv(path):
    with open(path,"w", newline='') as file:
        writer = csv.writer(file, dialect='excel')

        #写表头
        header = ["CurveName", "RateType", "ReportingDate", "TermBase", "Term", "Rate"]
        writer.writerows([header])

        #写ABS数据
        for i in range(2,7):
            writer.writerows([["ABS", "SpotRate", text[1], "D", text[i], text[i+6] ]])
        #写RMBS数据
        for j in range(2,7):
            writer.writerows([["RMBS", "SpotRate", text[1], "D", text[j], text[j+12] ]])


# if __name__ == "__main__":
#     current_dir = os.getcwd()  # 返回当前工作目录
#     files_dir = os.listdir(current_dir)  # 返回指定的文件夹包含的文件或文件夹的名字的列表，

#     png_name, flag = getImage()

#     if flag == 1:
#         if "CSV存放文件夹" not in files_dir:
#             os.mkdir(current_dir + "\\CSV存放文件夹")
#         if "img" not in files_dir:
#             os.mkdir(current_dir + "\\img")

#         os.chdir(".\\img")  # 跳进img文件夹
#         files = os.listdir(".")  # 返回该文件夹下所有文件
#         for file in files:
#             if (os.path.splitext(file)[0] == png_name)and(os.path.splitext(file)[1] == ".png"):

#                 #获取交点坐标
#                 img_w, img_h, img_gray, lines_col, lines_row = picProcess()
#                 x_val = getCoord(lines_col, flag="col")
#                 y_val = getCoord(lines_row, flag="row")

#                 #分割识别
#                 text= recognize()

#                 #写入csv文件
#                 csv_path = current_dir+"\\CSV存放文件夹\\"+os.path.splitext(file)[0]+"_data.csv"
#                 writeCsv(csv_path)
#         os.chdir(current_dir)
#     elif flag == 0:
#         print("今天未发布报告")

