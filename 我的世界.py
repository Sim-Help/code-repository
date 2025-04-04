from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app=Ursina()

grass_texture=load_texture('assets/grass_block.png')
stone_texture=load_texture('assets/stone_block.png')
brick_texture=load_texture('assets/brick_block.png')
dirt_texture=load_texture('assets/dirt_block.png')
sky_texture=load_texture('assets/skybox.png')
arm_texture=load_texture('assets/arm_texture.png')
punch_sound=Audio('assets/punch_sound',loop=False, autoplay=False)
block_pick=1

window.fps_counter.enabled=False

def update():
    global block_pick
    if held_keys['1']: block_pick=1
    if held_keys['2']: block_pick=2
    if held_keys['3']: block_pick=3
    if held_keys['4']: block_pick=4
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

class Block(Button):
    def __init__(self,position=(0,0,0),texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0,0,random.uniform(0.9,1)),
            scale=0.5
        )
    def input(self, key):
        if self.hovered:
            if key=='left mouse down':
                punch_sound.play()
            if key=='right mouse down':
                punch_sound.play()
            if key=='left mouse down':
                if block_pick==1:block=Block(position=self.position+mouse.normal,texture=grass_texture)
            if key=='left mouse down':
                if block_pick==2:block=Block(position=self.position+mouse.normal,texture=stone_texture)
            if key=='left mouse down':
                if block_pick==3:block=Block(position=self.position+mouse.normal,texture=brick_texture)
            if key=='left mouse down':
                if block_pick==4:block=Block(position=self.position+mouse.normal,texture=dirt_texture)
            if key=='right mouse down':
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=sky_texture,
            scale=150,
            double_sided=True
        )

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='assets/arm',
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150,-10,0),
            position=Vec2(0.4,-0.6)
        )
    def active(self):
        self.position=Vec2(0.3,-0.5)
    def passive(self):
        self.position=Vec2(0.4,-0.6)

for z in range(8):
    for x in range(8):
        block=Block(position=(x,0,z))
sky=Sky()
player=FirstPersonController()
hand=Hand()
with open('password_file.txt','r',encoding='utf-8') as pwd_f:
    if pwd_f.read()=='XXXXX-XXXXX-XXXXX-XXXXX-XXXXX':
        print('with pwd is true')
    else:
        print('with pwd is false')

app.run()