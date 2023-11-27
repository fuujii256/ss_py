import pygame
import sys
import random
import cv2

# 画像の読み込み
img_galaxy1 = pygame.image.load("image_gl/star1.png")
img_galaxy2 = pygame.image.load("image_gl/star2.png")
img_galaxy3 = pygame.image.load("image_gl/star3.png")
img_galaxy4 = pygame.image.load("image_gl/star4.png")

img_galaxy1 = pygame.transform.smoothscale(img_galaxy1,(16,16))
img_galaxy2 = pygame.transform.smoothscale(img_galaxy2,(16,16))
img_galaxy3 = pygame.transform.smoothscale(img_galaxy3,(16,16))
img_galaxy4 = pygame.transform.smoothscale(img_galaxy4,(16,16))

img_bg = pygame.image.load("image_gl/bg1.png")

im1 = cv2.imread("char/char32.png",-1)
im2 = cv2.imread("char/char33.png",-1)
im3 = cv2.imread("char/char34.png",-1)
im4 = cv2.imread("char/char35.png",-1)
im5 = cv2.imread("char/char36.png",-1)
im6 = cv2.imread("char/char37.png",-1)
im7 = cv2.imread("char/char38.png",-1)
im8 = cv2.imread("char/char39.png",-1)

im9 = cv2.hconcat([im1, im2])
im10 = cv2.hconcat([im3, im4])

im11= cv2.hconcat([im5, im6])
im12 = cv2.hconcat([im7, im8])

ss_ship1 = cv2.vconcat([im11, im9])
ss_ship2 = cv2.vconcat([im11, im10])
ss_ship3 = cv2.vconcat([im12, im9])
ss_ship4 = cv2.vconcat([im12, im10])

cv2.imwrite("image_gl/ss_ship1.png", ss_ship1)
cv2.imwrite("image_gl/ss_ship2.png", ss_ship2)
cv2.imwrite("image_gl/ss_ship3.png", ss_ship3)
cv2.imwrite("image_gl/ss_ship4.png", ss_ship4)


temp1 = pygame.image.load("image_gl/ss_ship1.png")
temp2 = pygame.image.load("image_gl/ss_ship2.png")
temp3 = pygame.image.load("image_gl/ss_ship3.png")
temp4 = pygame.image.load("image_gl/ss_ship4.png")

img_ss_ship1 = [pygame.transform.smoothscale(temp1,(32,32)), pygame.transform.smoothscale(temp3,(32,32))] 
img_ss_ship2 = [pygame.transform.smoothscale(temp2,(32,32)), pygame.transform.smoothscale(temp4,(32,32))] 
bg_x = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]               
bg_y = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        

ss_x = 256
ss_y = 224

ss_x = 480
ss_y = 360
sht= 0
#ショットボタンの状態

sht_no = 0
#ショットの番号

sht_max = 8
#ショットの最大数　LV0=8 LV1=8 LV2=12 LV3=20　リニアに変わる

sht_lv = 0  
#ショットのレベル値

msl_f = [False]*sht_max
msl_x = [0]*sht_max
msl_y = [0]*sht_max


def set_shot():   
    global sht_no,sht_lv,sht,sht_f
    sht_f[sht_no] = True
    if sht_lv ==0:
         #shot immage = 0のイメージ
        sht_lv =0      
        
def move_starship(scrn, key):
# 自機の移動
    global ss_x, ss_y,sht,sht_no,sht_lv
    
    if key[pygame.K_1] == 1:
        sht_lv = sht_lv +1
        if sht_lv >3: sht_lv= 0
    
    if key[pygame.K_UP] == 1:
        ss_y = ss_y - 5
        if ss_y < 108:
            ss_y = 108
    if key[pygame.K_DOWN] == 1:
        ss_y = ss_y + 5
        if ss_y > 452:
            ss_y = 452
    if key[pygame.K_LEFT] == 1:
        ss_x = ss_x - 5
        if ss_x < 64:
            ss_x = 64
    if key[pygame.K_RIGHT] == 1:
        ss_x = ss_x + 5
        if ss_x > 480:
            ss_x = 480

            
    if key[pygame.K_SPACE] ==1: 
        if sht==0:
            sht=10
            hoge = pygame.mixer.Sound("sound/shot.WAV")
            hoge.play()
            if sht_no <5: 
                sht_no= sht_no +1
                #set_shot()                        #自分の機体のショットをセット
    else:
        sht=0

    if sht >0: sht=sht -1
                                #自機の表示
    scrn.blit(img_ss_ship1[1], [ss_x-37, ss_y-48])
    if tmr %8 == 0:
        scrn.blit(img_ss_ship2[1], [ss_x-37, ss_y-48])

#    if tmr %8 == 0: 
#        scrn.blit(img_sship, [ss_x-37, ss_y-24], [64,62,64,28])
#    else:
#        scrn.blit(img_sship, [ss_x-37, ss_y-24], [0,62,64,28])

def main(): # メインループ
    global bg_x
    global bg_y
    global tmr 
    global bg1_x
    global bg1_y
 
    #星の初期位置の設定
    for w in range(40):
        bg_x[w]=random.randint(0,959)
    for w in range(40):
        bg_y[w]=random.randint(0,719)

    tmr = 00

    bg1_x =0
    bg1_y =-1500

    hsp = 0
    bg_on = 0
    stmr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for w in range(40):
        stmr[w]=random.randint(0,8)


#画面の初期化
    scn_width = 512   #表示画面の大きさ、ファミコン（256×224）の２倍で設定。
    scn_height = 448 
    pygame.init()
    pygame.display.set_caption("StarSolder EX.")
    screen = pygame.display.set_mode((scn_width, scn_height))
    #フォントの用意
    font1 = pygame.font.SysFont('meiryo', 40)   
    clock = pygame.time.Clock()

    while True:
        screen.fill((0,0,0))
        text1 = font1.render(str(tmr) + str(hsp), True, (255,255,255))
        screen.blit(text1, (0,0))
        tmr = tmr +1
        #ゲームスタートからの経過時間でのイベントを記述
        if tmr < 150: hsp=16
        elif tmr < 300: hsp=4
        else: hsp =1 
       # 
        if tmr >800: bg_on=1    
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    screen = pygame.display.set_mode((scn_width, scn_height), pygame.FULLSCREEN)
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((scn_width, scn_height))

        # 星のスクロール
        for num in range(40):
            bg_y[num] = (bg_y[num] + ((num%2)+1)*hsp)%720       
            if tmr %20 == 0:
                stmr[num] = stmr[num] +1
                if stmr[num] == 9: 
                    stmr[num] = 0
            if stmr[num] == 1: screen.blit(img_galaxy1, [bg_x[num], bg_y[num]])
            if stmr[num] == 2: screen.blit(img_galaxy2, [bg_x[num], bg_y[num]])
            if stmr[num] == 3: screen.blit(img_galaxy3, [bg_x[num], bg_y[num]])          
            if stmr[num] == 4: screen.blit(img_galaxy2, [bg_x[num], bg_y[num]]) 
            if stmr[num] == 5: screen.blit(img_galaxy3, [bg_x[num], bg_y[num]])
            if stmr[num] == 6: screen.blit(img_galaxy2, [bg_x[num], bg_y[num]])
            if stmr[num] == 7: screen.blit(img_galaxy1, [bg_x[num], bg_y[num]])          
            if stmr[num] == 8: screen.blit(img_galaxy4, [bg_x[num], bg_y[num]])

        # BGのスクロール
        if bg_on ==1:
            bg1_x = 80-ss_x
            bg1_y = bg1_y + tmr*1/720
            screen.blit(img_bg, [bg1_x, bg1_y])
        
        key = pygame.key.get_pressed()
        move_starship(screen, key)

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
