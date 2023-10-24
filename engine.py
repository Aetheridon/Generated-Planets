import random

from ursina import Ursina, Entity, color

app = Ursina()

class Planet():
    def __init__(self):
        self.model = "sphere"
        self.color = color.red
        self.texture = "white_cube"
        self.scale = random.randint(1, 5)
    
    def generate_planet(self):
        planet = Entity(model=self.model, color=self.color, texture=self.texture, scale=self.scale)
        return planet

planet_obj = Planet()
print(f"scale: {planet_obj.scale}")
generated_planet = planet_obj.generate_planet()

def update():
    generated_planet.rotation_x = generated_planet.rotation_x + 0.25
    generated_planet.rotation_y = generated_planet.rotation_y + 0.5

app.run()