import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    
    character_img = pg.image.load("ex01/fig/3.png")
    character_img = pg.transform.flip(character_img, True, False)
    
    ten_rad_chara = pg.transform.rotozoom(character_img, 10, 1.0)
    chara_lst = [character_img, ten_rad_chara]
    
    tmr = 0 # タイマー
    bg_x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [bg_x, 0])
        if bg_x < -800: 
            screen.blit(bg_img, [bg_x+1600, 0]) # 800から1600まで伸びるので、その間の800を別の背景で補間
        
        screen.blit(chara_lst[tmr%2], [300, 200])

        pg.display.update()
        tmr += 1 
        bg_x -= 1
        # init_img = 0
        if bg_x < -1600: 
            bg_x = 0  
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()