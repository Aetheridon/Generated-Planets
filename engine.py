from ursina import Ursina, Entity, color

app = Ursina()
sphere = Entity(model="sphere", color=color.red, texture="white_cube", scale=2)

def update():
    sphere.rotation_x = sphere.rotation_x + 0.25
    sphere.rotation_y = sphere.rotation_y + 0.5

app.run()