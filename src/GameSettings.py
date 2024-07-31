DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]]
WIDTH, HEIGHT = 1280, 720
FPS = 60

X_BLOCKS_COUNT = 25
Y_BLOCKS_COUNT = 18

TILE = 32


def calculate_tile_size(width, height):
    tile_width = width / X_BLOCKS_COUNT
    tile_height = height / Y_BLOCKS_COUNT
    return min(tile_width, tile_height)
