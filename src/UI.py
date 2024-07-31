import pygame
import World


class UI:
    def __init__(self, window, world):
        self.world = world
        self.window = window
        self.fontUI = pygame.font.Font(None, 30)

    def update(self):
        pass

    def draw(self):
        i = 0
        for obj in self.world.objects:
            if obj.type != 'tank':
                continue

            pygame.draw.rect(self.window, obj.color, (5 + i * 70, 5, 22, 22))

            text = self.fontUI.render(str(obj.hp), 1, obj.color)
            rect = text.get_rect(center=(5 + i * 70 + 32, 5 + 11))
            self.window.blit(text, rect)
            i += 1
