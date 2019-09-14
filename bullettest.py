import pygame as pg
import math
import sys

pg.init()
width = 320
hieght = 480

angle = 0

screen = pg.display.set_mode((width, hieght))
pg.key.set_repeat(100, 200)
clock = pg.time.Clock()
FPS = 60
fire = False
pos = (0, 0)


while True:
    clock.tick(FPS)
    if fire:
        pg.draw.circle(screen, (0, 0, 0), pos, 3)
        pg.display.flip()
        dirx = -math.sin(math.radians(angle))
        diry = math.cos(-math.radians(angle))
        px = int(round(dirx) * 5) + pos[0]
        py = int(round(diry) * 5) + pos[1]
        pos = (int(round(px)), int(round(py)))
        pg.draw.circle(screen, (255, 255, 255), pos, 3)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                angle += 5
                angle %= 360
            if event.key == pg.K_LEFT:
                angle -= 5
                angle %= 360
            if event.key == pg.K_SPACE:
                fire = True
                pos = (int(width/2), int(hieght/2))

            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
    print(angle)
    print(math.radians(angle))
    pg.display.flip()
    # print(screen.get_size())
