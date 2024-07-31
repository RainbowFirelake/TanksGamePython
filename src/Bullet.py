import pygame
import World
import GameSettings
import Bang

# TODO: name refactoring (px, py - position in world), (dx, dy - move speed in world)
class Bullet:
    def __init__(self, parent, px, py, dx, dy, damage, world):
        self.world = world
        self.world.bullets.append(self)
        self.parent = parent
        self.px, self.py = px, py
        self.dx, self.dy = dx, dy
        self.damage = damage

    def update(self):
        self.px += self.dx
        self.py += self.dy

        if self.px < 0 or self.px > GameSettings.WIDTH or self.py < 0 or self.py > GameSettings.HEIGHT:
            self.world.bullets.remove(self)
            return

        for obj in self.world.objects:
            if obj == self.parent or obj.type == 'bang' or obj.type == 'bonus':
                continue

            if not obj.rect.collidepoint(self.px, self.py):
                continue

            obj.damage(self.damage)
            self.world.bullets.remove(self)
            Bang.Bang(self.px, self.py, self.world)
            break

    def draw(self, window):
        pygame.draw.circle(window, 'yellow', (self.px, self.py), 2)
