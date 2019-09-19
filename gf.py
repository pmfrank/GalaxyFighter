import pygame as pg
import pygame_ai as pgai
from sys import exit
import math
from random import randint


pg.init()
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
RIGHT = 5
LEFT = -5

size = (320, 480)
screen = pg.display.set_mode(size)

clock = pg.time.Clock()
FPS = 30

p1 = (160, 215)
p2 = (135, 265)
p3 = (185, 265)
center = (160, 240)
theta = math.radians(5)
bullet_speed = 15

screen.fill(BLACK)
eraser = screen.copy()

tri = pg.draw.polygon(screen, WHITE, [p1, p2, p3], 2)
pg.display.update(tri)

enemy_limit = 5
enemies = list()
enemy_rects = [None] * 5


def rotate(point, center, angle):
    cx = center[0]
    cy = center[1]

    px = point[0]
    py = point[1]

    rx = math.cos(angle)*(px-cx)-math.sin(angle)*(py-cy) + cx
    ry = math.sin(angle)*(px-cx)+math.cos(angle)*(py-cy) + cy

    return rx, ry


class Missile():
    def __init__(self, pos, image, angle, speed):
        self.pos = pos
        self.image = image
        self.direction = [0, 0]
        self.speed = speed
        self.angle = angle

    def move(self):
        self.direction[0] = math.sin(-math.radians(self.angle))
        self.direction[1] = -math.cos(math.radians(self.angle))
        self.pos[0] += self.direction[0]*self.speed
        self.pos[1] += self.direction[1]*self.speed


player = pgai.gameobject.GameObject(pos=(160, 240))


class EnemyShip(pgai.gameobject.GameObject):
    def __init__(self, pos=(0, 0)):
        img = pg.Surface((20, 20)).convert_alpha()
        img.fill((255, 255, 255, 0))
        # Draw the circle
        pg.draw.rect(img, RED, [0, 0, 20, 20])
        super(EnemyShip, self).__init__(
            img_surf=img,
            pos=pos,
            max_speed=2,
            max_accel=2,
            max_rotation=40,
            max_angular_accel=2
        )
        # Create a placeholder for the AI
        self.ai = pgai.steering.kinematic.NullSteering()

    def update(self, tick):
        steering = self.ai.get_steering()
        self.steer(steering, tick)
        self.rect.move_ip(self.velocity)


fire = False
bullet = None
angle = 0
new_missile = None
color = BLUE
circle_list = list()

while True:
    clock.tick(FPS)

    if len(circle_list) < enemy_limit:
        circle = EnemyShip(pos=(randint(0, 360), randint(0, 480)))
        circle.ai = pgai.steering.kinematic.Arrive(circle, player)
        circle_list.append(circle)

    for i in range(0, len(circle_list)):
        circle_list[i].update(FPS)

    if fire:
        new_missile.move()
        if new_missile.pos[0] <= 0 or new_missile.pos[0] >= size[0]:
            fire = False
        if new_missile.pos[1] <= 0 or new_missile.pos[1] >= size[1]:
            fire = False

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT]:
        p1 = rotate(p1, center, theta)
        p2 = rotate(p2, center, theta)
        p3 = rotate(p3, center, theta)
        tri = pg.draw.polygon(screen, WHITE, [p1, p2, p3], 2)
        angle -= 5
        angle %= 360
    if keys[pg.K_LEFT]:
        p1 = rotate(p1, center, -theta)
        p2 = rotate(p2, center, -theta)
        p3 = rotate(p3, center, -theta)
        tri = pg.draw.polygon(screen, WHITE, [p1, p2, p3], 2)
        angle += 5
        angle %= 360
    if keys[pg.K_SPACE]:
        fire = True
        pos = [p1[0], p1[1]]
        img = pg.image.load('bullet.png')
        new_missile = Missile(pos, img, angle, bullet_speed)
    screen.blit(eraser, (0, 0))
    if fire:
        screen.blit(new_missile.image, new_missile.pos)
        for x, enemy in enumerate(circle_list):
            if enemy.rect.collidepoint(new_missile.pos):
                circle_list.pop(x)
    tri = pg.draw.polygon(screen, WHITE, [p1, p2, p3], 2)
    if len(circle_list) < enemy_limit:
        circle = EnemyShip(pos=(randint(0, 360), 0))
        circle.ai = pgai.steering.kinematic.Arrive(circle, player)
        circle_list.append(circle)

    for i in range(0, len(circle_list)):
        circle_list[i].update(FPS)
        screen.blit(circle_list[i].image, circle_list[i].rect)
    pg.display.flip()