
import cv2
import numpy as np
 
for i in range(0,16*28):
    
    img = cv2.imread('image_gl/CHAR'+str(i)+'.png', -1)                            # -1はAlphaを含んだ形式(0:グレー, 1:カラー)
 
    color_lower = np.array([0, 0, 0, 255])                 # 抽出する色の下限(BGR形式)
    color_upper = np.array([64, 64, 64, 255])                 # 抽出する色の上限(BGR形式)
    img_mask = cv2.inRange(img, color_lower, color_upper)    # 範囲からマスク画像を作成
    img_bool = cv2.bitwise_not(img, img, mask=img_mask)      # 元画像とマスク画像の演算(背景を白くする)   
 
    #   img[:, :, 3] = np.where(np.all(img == 0, axis=-1), 0, 255)  # 黒色のみTrueを返し、Alphaを0にする
    
    cv2.imwrite('char/char'+str(i)+".png", img_bool) 
    