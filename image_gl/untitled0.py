#ライブラリのインポート
import cv2
import numpy as np
#画像の読み込み
img=cv2.imread("image_gl/tikei_bg.png",cv2.IMREAD_COLOR)
#h,w=img.shape[:2]
split_x=6
split_y=6
#画像の分割処理
cx=0
cy=0
for j in range(split_x):
    for i in range(split_y):
        split_pic=img[cy:cy+int(h/split_y),cx:cx+int(w/split_x),:]
        cv2.imwrite('tikei_bg/split_y'+str(i)+'_x'+str(j)+'.jpg',split_pic)
        cy=cy+int(h/split_y)
    cy=0
    cx=cx+int(w/split_x)
