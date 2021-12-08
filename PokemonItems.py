import os
import pygame

size = width, height = 640, 480
pygame.display.set_caption('Pokemon')
background_color = (255, 255, 255)
screen = pygame.display.set_mode(size)


class Items:
    def __init__(self, name, path_items):
        if name == "Pokeball":
            self.name = "Pokeball"
            self.pocket = "pokeballs"
            self.number = 1
            self.quantity = 0
            self.catch_rate = 1
            self.cost = 200
            self.sell_price = 100
            self.description = "A device for catching wild Pokémon. It's thrown like a ball at a Pokémon," \
                               " comfortably encapsulating its target."
            self.graphics = pygame.image.load(os.path.join(path_items, "item_pokeball.png"))
            self.x = 34
            self.y = 370
        elif name == "Greatball":
            self.name = "Greatball"
            self.pocket = "pokeballs"
            self.number = 2
            self.quantity = 0
            self.catch_rate = 1.5
            self.cost = 600
            self.sell_price = 300
            self.description = "A good, high-performance Poké Ball that provides a higher success rate" \
                               " for catching Pokémon than a standard Poké Ball."
            self.graphics = pygame.image.load(os.path.join(path_items, "item_greatball.png"))
            self.x = 34
            self.y = 370
        elif name == "Ultraball":
            self.name = "Ultraball"
            self.pocket = "pokeballs"
            self.number = 3
            self.quantity = 0
            self.catch_rate = 2
            self.cost = 1200
            self.sell_price = 600
            self.description = "An ultra-high-performance Poké Ball that provides a higher success rate" \
                               " for catching Pokémon than a Great Ball."
            self.graphics = pygame.image.load(os.path.join(path_items, "item_ultraball.png"))
            self.x = 34
            self.y = 370
        elif name == "Masterball":
            self.name = "Masterball"
            self.pocket = "pokeballs"
            self.number = 4
            self.quantity = 0
            self.catch_rate = 10000
            self.cost = 0
            self.sell_price = 0
            self.description = "The best Poké Ball with the ultimate level of performance. With it," \
                               " you will catch any wild Pokémon without fail."
            self.graphics = pygame.image.load(os.path.join(path_items, "item_masterball.png"))
            self.x = 34
            self.y = 370
        elif name == "Potion":
            self.name = "Potion"
            self.pocket = "items"
            self.number = 5
            self.quantity = 0
            self.power = 20
            self.cost = 300
            self.sell_price = 150
            self.description = "A spray-type medicine for treating wounds. " \
                               "It can be used to restore 20 HP to a single Pokémon."
            self.graphics = pygame.image.load(os.path.join(path_items, "item_potion.png"))
            self.x = 38
            self.y = 368
        elif name == "Super Potion":
            self.name = "Super Potion"
            self.pocket = "items"
            self.number = 6
            self.quantity = 0
            self.power = 60
            self.cost = 700
            self.sell_price = 350
            self.description = "A spray-type medicine for treating wounds. " \
                               "It can be used to restore 60 HP to a single Pokémon."
            self.graphics = pygame.image.load(os.path.join(path_items, "item_super_potion.png"))
            self.x = 38
            self.y = 368
        elif name == "Hyper Potion":
            self.name = "Hyper Potion"
            self.pocket = "items"
            self.number = 7
            self.quantity = 0
            self.power = 120
            self.cost = 1500
            self.sell_price = 750
            self.description = "A spray-type medicine for treating wounds. " \
                               "It can be used to restore 120 HP to a single Pokémon."
            self.graphics = pygame.image.load(os.path.join(path_items, "item_hyper_potion.png"))
            self.x = 38
            self.y = 368
        elif name == "Max Potion":
            self.name = "Max Potion"
            self.pocket = "items"
            self.number = 8
            self.quantity = 0
            self.power = 10000
            self.cost = 2500
            self.sell_price = 1250
            self.description = "A spray-type medicine for treating wounds. " \
                               "It can be used to completely restore the max HP of a single Pokémon."
            self.graphics = pygame.image.load(os.path.join(path_items, "item_max_potion.png"))
            self.x = 38
            self.y = 368
        elif name == "Town Map":
            self.name = "Town Map"
            self.pocket = "key_items"
            self.number = 9
            self.quantity = 0
            self.cost = 0
            self.sell_price = 0
            self.description = "A very convenient map that can be viewed anytime. " \
                               "It even shows you your present location in the region."
            self.graphics = pygame.image.load(os.path.join(path_items, "item_town_map.png"))
            self.x = 34
            self.y = 368

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))


class Pokeball:
    def __init__(self, x, y, path_items):
        self.x = x
        self.y = y
        self.height = 10
        self.width = 10
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = pygame.image.load(os.path.join(path_items, "pokeball.png"))

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))

    def collide(self, player):
        if self.shape.colliderect(player):
            return True
        else:
            return False


class Badge:
    def __init__(self, variant, path_items):
        self.graphics = pygame.image.load(os.path.join(path_items, "badge_{}.png".format(variant)))

    def draw(self, x, y, screen):
        screen.blit(self.graphics, (x, y))
