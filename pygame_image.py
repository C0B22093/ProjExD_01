import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    #bg_img2 = pg.transform.flip(bg_img, True, False)
    bg_lst = [bg_img, pg.transform.flip(bg_img, True, False)]*2
    
    character_img = pg.image.load("ex01/fig/3.png")
    character_img = pg.transform.flip(character_img, True, False)
    
    
    tmr = 0 # タイマー
    #bg_x = 0
    i = 0
    i_flag = 0
    # mul_val = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        x = tmr%3200
        for h in range(4):
            screen.blit(bg_lst[h], [3200*h-x, 0])
        
        change_rad_chara = pg.transform.rotozoom(character_img, i, 1.0)
        chara_lst = [change_rad_chara]
        

        # screen.blit(bg_img, [bg_x, 0])
            
        
        # if bg_x < -800*mul_val:
        #     screen.blit(bg_img2, [bg_x+1600*mul_val, 0]) # 800から1600まで伸びるので、その間の800を別の背景で補間
        
        # bg_img3 = pg.transform.flip(bg_img2, True, False)
        # if bg_x > -800 and bg_flag == 1:
        #     screen.blit(bg_img3, [bg_x, 0])
        
        screen.blit(chara_lst[0], [300, 200])

        tmr += 1 
        # bg_x -= 1
        
        if i_flag == 0:
            i += 1
            if i >= 10:
                i_flag = 1
        else:
            i -= 1
            if i <= 0:
                i_flag = 0
        
        # if bg_x == -800: # -800に到達したら、掛算の因数を更新
        #     mul_val += 1
        # if bg_x < -1600: 
        #     bg_x = 0
        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()