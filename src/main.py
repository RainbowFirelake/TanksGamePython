import pygame
from random import randint

from Tank import Tank
import GameSettings
import World
import Block
from UI import UI
from Bonus import Bonus
import Resources

pygame.init()

window = pygame.display.set_mode((GameSettings.WIDTH, GameSettings.HEIGHT))
width, height = window.get_size()
GameSettings.TILE = GameSettings.calculate_tile_size(width, height)
clock = pygame.time.Clock()

world = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
]

scene = World.World(world, window)
scene.create_objects_in_world()
ui = UI(window, scene)

Tank('blue', 100, 275, 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE), scene)
Tank('red', 650, 275, 0, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_KP_ENTER), scene)

#
# for _ in range(50):
#     while True:
#         x = randint(0, GameSettings.WIDTH // GameSettings.TILE - 1) * GameSettings.TILE
#         y = randint(1, GameSettings.HEIGHT // GameSettings.TILE - 1) * GameSettings.TILE
#
#         # print("x = ", x)
#         # print(GameSettings.WIDTH // GameSettings.TILE)
#         # print("y = ", y)
#         # print(GameSettings.HEIGHT // GameSettings.TILE)
#
#         rect = pygame.Rect(x, y, GameSettings.TILE, GameSettings.TILE)
#         fined = False
#
#         for obj in scene.objects:
#             if rect.colliderect(obj.rect):
#                 fined = True
#
#         if not fined:
#             break
#
#     Block.Block(x, y, GameSettings.TILE, scene)

bonus_timer = randint(120, 240)

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()

    if bonus_timer > 0:
        bonus_timer -= 1
    else:
        Bonus(
            randint(50, GameSettings.WIDTH - 50),
            randint(50, GameSettings.HEIGHT - 50),
            randint(0, len(Resources.imgBonuses) - 1),
            scene)
        bonus_timer = randint(120, 240)

    for bullet in scene.bullets:
        bullet.update()

    for obj in scene.objects:
        obj.update()

    ui.update()

    window.fill('black')

    for bullet in scene.bullets:
        bullet.draw(window)

    for obj in scene.objects:
        obj.draw(window)

    ui.draw()

    pygame.display.update()
    clock.tick(GameSettings.FPS)

pygame.quit()
