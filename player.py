import pygame as pg
import math

WHITE = (255, 255, 255)

class Player(object):
    def __init__(self, scene):
        self.p1 = (160, 215)
        self.p2 = (135, 265)
        self.p3 = (185, 265)
        self.scene = scene
        self.center = (
            int(self.scene.get_size()[0]/ 2),
            int(self.scene.get_size()[1]/ 2)
        )
        self.left = -math.radians(-5)
        self.right = math.radians(5)


    def rotate(self,px, py, center, theta):
        cx = center[0]
    cy = center[1]

    px = point[0]
    py = point[1]

    rx = math.cos(angle)*(px-cx)-math.sin(angle)*(py-cy) + cx
    ry = math.sin(angle)*(px-cx)+math.cos(angle)*(py-cy) + cy

    return rx, ry

    def draw(self, p1, p2, p3):
        global WHITE
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        pg.draw.polygon(
            self.scene, WHITE, [self.p1, self.p2, self.p3], 2
        )

pg.init()
size = (320,480)
screen = pg.display.set_mode(size)
info = screen.copy()
player = Player(screen)

while True:
    player.draw()
    pg.display.update()
    keys = pg.key.get_pressed()
    if keys[K_RIGHT]:
        p1 = rotate(player.p1, player.center, player.right)
        p2 = rotate(player.p2, player.center, player.right)
        p3 = rotate(player.p3, player.center, player.right)
        theta)
        tri = pg.draw.polygon(screen, WHITE, [p1, p2, p3], 2)
        angle -= 5
        angle %= 360