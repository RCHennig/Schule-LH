from mcpi.minecraft import Minecraft
from mcpi import block
import keyboard

# Connect to Minecraft
mc = Minecraft.create()



class Wall:
    def __init__(self, pos):
        self.pos = pos
        self.rotate = False
        self.width = 6
        self.height = 5
        self._mc = Minecraft.create()

    # self.material.id = block.WOOD

    def build(self, rotated):
        if rotated:
            mc.setBlocks(pos.x + 2, pos.y, pos.z, pos.x + self.width + 2, pos.y + self.height, pos.z, block.WOOD)

        else:
            mc.setBlocks(pos.x, pos.y, pos.z + 2, pos.x, pos.y + self.height, pos.z + self.width + 2, block.WOOD)


class WallWithWindow(Wall):
    def __init__(self, pos, width, height, rotate, mc):
        super().__init__(pos, width, height, rotate, mc)

    def build(self, rotated):
        Wall.build(rotated)
        if rotated:
            mc.setBlocks(pos.x + 3, pos.y +1, pos.z, pos.x + self.width + 1, pos.y + self.height -1, pos.z, block.DIAMOND_BLOCK)

        else:
            mc.setBlocks(pos.x, pos.y, pos.z + 2, pos.x, pos.y + self.height, pos.z + self.width + 2, block.WOOD)


while True:
    if keyboard.read_key() == 'b':
        pos = mc.player.getTilePos()
        walls = WallWithWindow(pos)
        walls.build(False)
        walls.build(True)
