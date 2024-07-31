import pygame
import Resources
import World


class Bang:
    def __init__(self, px, py, world):
        self.world = world
        world.objects.append(self)
        self.type = 'bang'

        self.px, self.py = px, py
        self.frame = 0

    def update(self):
        self.frame += 0.2
        if self.frame >= 3:
            self.world.objects.remove(self)

    def draw(self, window):
        image = Resources.imgBangs[int(self.frame)]
        rect = image.get_rect(center=(self.px, self.py))
        window.blit(image, rect)
