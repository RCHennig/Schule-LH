from mcpi.minecraft import Minecraft
from mcpi import block
import keyboard

# Connect to Minecraft
mc = Minecraft.create()

# Determine the Player's current position.
x, y, z = mc.player.getTilePos()

while True:
    if keyboard.read_key() == 'b':
        mc.setBlock(x + 2, y, z, block.FURNACE_ACTIVE)
        mc.setBlock(x + 2, y + 1, z, block.DIAMOND_BLOCK)
        mc.setBlock(x + 2, y + 2, z, block.LAVA_STATIONARY)