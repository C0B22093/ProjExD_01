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
    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
        screen.blit(character_img, [400, 300])
        
        
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()