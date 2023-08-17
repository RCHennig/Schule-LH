from mcpi.minecraft import Minecraft
from mcpi import block
import keyboard

# Connect to Minecraft
mct = Minecraft.create()



class Wall:
    def __init__(self, pos, mc, rotated = False):
        self.pos = pos
        self.rotated = rotated
        self.width = 6
        self.height = 5
        self._mc = mc

    # self.material.id = block.WOOD


    def build(self):

        if self.rotated == False:
            self._mc.setBlocks(self.pos.x + 2, self.pos.y, self.pos.z, self.pos.x + self.width + 1, self.pos.y + self.height -1, self.pos.z, block.STONE_BRICK)
        else:
            self._mc.setBlocks(self.pos.x, self.pos.y, self.pos.z + 2, self.pos.x, self.pos.y + self.height - 1, self.pos.z + self.width + 1, block.STONE_BRICK)

class WallWithWindow(Wall):
    def __init__(self, pos, _mc, rotated = False):
        super().__init__(pos, _mc, rotated)

    def build(self):
        super().build()

        if self.rotated == False:
            self._mc.setBlocks(self.pos.x + 3, self.pos.y + 2, self.pos.z, self.pos.x + 6, self.pos.y + 3, self.pos.z, block.GLASS_PANE)
        else :
            self._mc.setBlocks(self.pos.x, self.pos.y + 2, self.pos.z + 4, self.pos.x, self.pos.y + 3, self.pos.z + 6, block.GLASS_PANE)

class WallWithDoor(Wall):
    def __init__(self, pos, _mc, rotated = False):
        super().__init__(pos, _mc, rotated)

    def build(self):
        super().build()

        if self.rotated == False:
            self._mc.setBlocks(self.pos.x + 4, self.pos.y, self.pos.z, self.pos.x + 5,self.pos.y + 2, self.pos.z, block.FENCE_GATE)
        else:
            self._mc.setBlocks(self.pos.x, self.pos.y, self.pos.z + 4, self.pos.x, self.pos.y + 2,self.pos.z + 5, block.FENCE_GATE)

while True:
    if keyboard.read_key() == 'b':
        walls = WallWithWindow(mct.player.getTilePos(), Minecraft.create(), True)
        walls.build()
        wall1 = WallWithDoor(mct.player.getTilePos(), Minecraft.create(), False)
        wall1.build()
