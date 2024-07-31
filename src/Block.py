import pygame

import GameSettings
import Resources


class Block:
    def __init__(self, px, py, size, world):
        self.world = world
        world.objects.append(self)

        self.type = 'block'
        self.rect = pygame.Rect(px, py, size, size)
        self.hp = 1

        self.scaled_texture = pygame.transform.scale(Resources.imgBrick, (GameSettings.TILE, GameSettings.TILE))

    def update(self):
        pass

    def draw(self, window):
        window.blit(self.scaled_texture, self.rect)

    def damage(self, value):
        self.hp -= value

        if self.hp <= 0:
            self.world.objects.remove(self)