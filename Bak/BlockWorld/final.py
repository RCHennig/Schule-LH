import mcpi.minecraft as minecraft
import keyboard
import time

mc = minecraft.Minecraft.create()


class Wall():

        def __init__(self, pos: tuple, mc):
            self.width = 6
            self.height = 5
            self.pos = pos
            self.rotated = False
            self.material_id = 98
            self._mc = mc


        def build(self):
            if (self.rotated == True and self.height == 5):
                self._mc.setBlocks([self.pos[0],self.pos[1],self.pos[2],self.pos[0]+self.width-1,self.pos[1]+self.height-1,self.pos[2],self.material_id])

            elif (self.rotated == False and self.height == 5):
                self._mc.setBlocks([self.pos[0],self.pos[1],self.pos[2],self.pos[0],self.pos[1]+self.height-1,self.pos[2]+self.width-2,self.material_id])

class WallWithDoor(Wall):


    def __init__(self,pos, mc):
        super().__init__(pos, mc)
        self.door_material_id = 0


    def build(self):
        super().build()
        if (self.rotated == True and self.height == 5):
            self._mc.setBlocks([self.pos[0],self.pos[1],self.pos[2],self.pos[0]+self.width-1,self.pos[1]+self.height-1,self.pos[2],self.material_id]) #excluding target
            self._mc.setBlocks((self.pos[0]+self.width/2)-1,(self.pos[1]+self.height/2)-1,self.pos[2], (self.pos[0]+self.width/2)-1,(self.pos[1]+self.height/2)-2, self.pos[2],self.door_material_id)

        elif (self.rotated == False and self.height == 5):
            self._mc.setBlocks([self.pos[0],self.pos[1],self.pos[2],self.pos[0],self.pos[1]+self.height-1,self.pos[2]+self.width-2,self.material_id]) #excluding target
            self._mc.setBlocks((self.pos[0]),(self.pos[1]+self.height/2)-1,(self.pos[2]+self.width/2-1), (self.pos[0]),(self.pos[1]+self.height/2)-2, (self.pos[2]+self.width/2)-1,self.door_material_id)


class WallWithWindow(Wall):


    def __init__(self,pos, mc):
        super().__init__(pos, mc)
        self.window_material_id = 0


    def build(self):
        super().build()
        if (self.rotated == True):
            self._mc.setBlocks([self.pos[0],self.pos[1],self.pos[2],self.pos[0]+self.width-1,self.pos[1]+self.height-1,self.pos[2],self.material_id]) 
            self._mc.setBlock(self.pos[0]+self.width/2,self.pos[1]+self.height/2-1,self.pos[2],self.window_material_id) 
            self._mc.setBlock(self.pos[0]+self.width/2,self.pos[1]+self.height/2,self.pos[2],self.window_material_id)
            self._mc.setBlock(self.pos[0]+self.width/2-1,self.pos[1]+self.height/2,self.pos[2],self.window_material_id)
            self._mc.setBlock(self.pos[0]+self.width/2-1,self.pos[1]+self.height/2-1,self.pos[2],self.window_material_id)

        elif (self.rotated == False):
            self._mc.setBlocks([self.pos[0],self.pos[1],self.pos[2],self.pos[0],self.pos[1]+self.height-1,self.pos[2]+self.width-2,self.material_id]) 
            self._mc.setBlock(self.pos[0],self.pos[1]+self.height/2-1,self.pos[2]+self.width/2,self.window_material_id) 
            self._mc.setBlock(self.pos[0],self.pos[1]+self.height/2,self.pos[2]+self.width/2,self.window_material_id)
            self._mc.setBlock(self.pos[0],self.pos[1]+self.height/2,self.pos[2]+self.width/2-1,self.window_material_id)
            self._mc.setBlock(self.pos[0],self.pos[1]+self.height/2-1,self.pos[2]+self.width/2-1,self.window_material_id)

class Roof:
    def __init__(self, pos, mc):
        self.width = 6
        self.depth = 6
        self.roof_material_id = 45
        self.pos = pos
        self.__mc = mc

    def build(self):
        if (self.width == 6 and self.depth == 6):
            self.__mc.setBlocks([self.pos[0],self.pos[1]+5,self.pos[2],self.pos[0]+self.width-1,self.pos[1]+5,self.pos[2] + self.depth -1],self.roof_material_id) 

        elif (self.width == 3 and self.depth == 3):
            self.__mc.setBlocks([self.pos[0], self.pos[1]+3, self.pos[2], self.pos[0]+self.width-1, self.pos[1]+3, self.pos[2]+ self.depth-1], self.roof_material_id)


class House():
    def __init__(self, pos, mc):
        pos = list(mc.player.getPos())
        self.wallFront = WallWithDoor([pos[0], pos[1], pos[2] + 5], mc)
        self.wallFront.rotated = True
        self.wallLeft = WallWithWindow([pos[0], pos[1], pos[2]], mc)
        self.wallRight = WallWithWindow([pos[0] + 5, pos[1], pos[2]], mc)
        self.wallBack = Wall(pos, mc)
        self.wallBack.rotated = True
        self.pos = pos
        self.roof = Roof(pos, mc)
        self.__mc = mc

    def build(self):
        self.wallFront.build()
        self.wallBack.build()
        self.wallLeft.build()
        self.wallRight.build()
        self.roof.build()


while True:
    if keyboard.read_key() == 'b':
        pos = list(mc.player.getPos())
        walls = House(pos, mc)
        walls.build()
        time.sleep(1)
