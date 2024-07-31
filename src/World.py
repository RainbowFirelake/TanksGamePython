import Block
import GameSettings
from random import randint


class World:
    def __init__(self, world_map, window):
        self.bullets = []
        self.objects = []
        self.window = window
        self.world_map = world_map
        a = GameSettings.WIDTH // GameSettings.TILE
        b = GameSettings.HEIGHT // GameSettings.TILE

    def create_objects_in_world(self):
        for i in range(len(self.world_map)):
            for j in range(len(self.world_map[i])):
                self.create_object_in_scene_by_index(self.world_map[i][j], j, i)

    def create_object_in_scene_by_index(self, index, x_tile_position, y_tile_position):
        x = x_tile_position * GameSettings.TILE
        y = y_tile_position * GameSettings.TILE

        if index == 1:
            Block.Block(x, y, GameSettings.TILE, self)

        if index == 2:
            pass

        if index == 3:
            pass
