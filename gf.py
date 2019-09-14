import pygame as pg
import math


pg.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RIGHT = 5
LEFT = -5

size = (320, 480)
screen = pg.display.set_mode(size)

clock = pg.time.Clock()
FPS = 60

p1 = (160, 215)
p2 = (135, 265)
p3 = (185, 265)
center = (160, 240)
theta = math.radians(5)

screen.fill(BLACK)

tri = pg.draw.polygon(screen, WHITE, [p1, p2, p3], 2)
pg.display.update(tri)


def rotate(point, center, angle):
    cx = center[0]
    cy = center[1]

    px = point[0]
    py = point[1]

    rx = math.cos(angle)*(px-cx)-math.sin(angle)*(py-cy) + cx
    ry = math.sin(angle)*(px-cx)+math.cos(angle)*(py-cy) + cy

    return rx, ry


while True:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT]:
        eraser = pg.draw.polygon(screen, BLACK, [p1, p2, p3], 2)
        p1 = rotate(p1, center, theta)
        p2 = rotate(p2, center, theta)
        p3 = rotate(p3, center, theta)
        tri = pg.draw.polygon(screen, WHITE, [p1, p2, p3], 2)
    if keys[pg.K_LEFT]:
        eraser = pg.draw.polygon(screen, BLACK, [p1, p2, p3], 2)
        p1 = rotate(p1, center, -theta)
        p2 = rotate(p2, center, -theta)
        p3 = rotate(p3, center, -theta)
        tri = pg.draw.polygon(screen, WHITE, [p1, p2, p3], 2)

    pg.display.flip()