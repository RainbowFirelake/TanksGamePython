import pygame
import GameSettings
import Resources
import World
from Bullet import Bullet


class Tank:
    def __init__(self, color, px, py, direct, key_list, world):
        self.world = world
        self.world.objects.append(self)

        self.type = 'tank'

        self.color = color
        self.rect = pygame.Rect(px, py, GameSettings.TILE, GameSettings.TILE)
        self.direct = direct
        self.moveSpeed = 2
        self.hp = 5

        self.shotTimer = 0
        self.shotDelay = 60
        self.bulletSpeed = 5
        self.bulletDamage = 1

        self.keyLEFT = key_list[0]
        self.keyRIGHT = key_list[1]
        self.keyUP = key_list[2]
        self.keyDOWN = key_list[3]
        self.keySHOT = key_list[4]

        self.rank = 0
        self.image = pygame.transform.rotate(Resources.imgTanks[self.rank], -self.direct * 90)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        keys = pygame.key.get_pressed()

        self.bulletSpeed = TankParameters.BULLET_SPEED[self.rank]
        self.bulletDamage = TankParameters.BULLET_DAMAGE[self.rank]
        self.moveSpeed = TankParameters.MOVE_SPEED[self.rank]
        self.shotDelay = TankParameters.SHOT_DELAY[self.rank]

        self.image = pygame.transform.rotate(Resources.imgTanks[self.rank], -self.direct * 90)
        self.image = pygame.transform.scale(self.image, (GameSettings.TILE - 5, GameSettings.TILE - 5))
        self.rect = self.image.get_rect(center=self.rect.center)

        oldX, oldY = self.rect.topleft
        if keys[self.keyLEFT]:
            self.rect.x -= self.moveSpeed
            self.direct = 3
        elif keys[self.keyRIGHT]:
            self.rect.x += self.moveSpeed
            self.direct = 1
        elif keys[self.keyUP]:
            self.rect.y -= self.moveSpeed
            self.direct = 0
        elif keys[self.keyDOWN]:
            self.rect.y += self.moveSpeed
            self.direct = 2

        for obj in self.world.objects:
            if obj != self and obj.type == 'block' and self.rect.colliderect(obj.rect):
                self.rect.topleft = oldX, oldY

        if keys[self.keySHOT] and self.shotTimer == 0:
            dx = GameSettings.DIRECTS[self.direct][0] * self.bulletSpeed
            dy = GameSettings.DIRECTS[self.direct][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bulletDamage, self.world)
            self.shotTimer = self.shotDelay

        if self.shotTimer > 0:
            self.shotTimer -= 1

    def draw(self, window):
        window.blit(self.image, self.rect)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            self.world.objects.remove(self)
            print(self.color, 'dead')


class TankParameters:
    MOVE_SPEED = [1, 2, 2, 1, 2, 3, 3, 2]
    BULLET_SPEED = [4, 5, 6, 5, 5, 5, 6, 7]
    BULLET_DAMAGE = [1, 1, 2, 3, 2, 2, 3, 4]
    SHOT_DELAY = [60, 50, 30, 40, 30, 25, 25, 30]