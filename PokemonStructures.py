import pygame
import os


class Structure:
    def __init__(self, x, y, path_structures):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.height = 15
        self.width = 15
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = None

    def update(self, player):
        self.x = self.start_x - player.x
        self.y = self.start_y - player.y

    def draw(self, screen):
        screen.blit(self.graphics, (self.x, self.y))


class CollideStructure(Structure):
    def collide(self, player):
        if self.shape.colliderect(player):
            return True
        else:
            return False


class House(CollideStructure):
    def __init__(self, x, y, path_structures):
        super().__init__(x, y, path_structures)
        self.height = 100
        self.width = 200
        self.graphics = pygame.image.load(os.path.join(path_structures, "house.png"))


class Lab(CollideStructure):
    def __init__(self, x, y, path_structures):
        super().__init__(x, y, path_structures)
        self.height = 100
        self.width = 200
        self.graphics = pygame.image.load(os.path.join(path_structures, "oak_lab.png"))


class GrassBackground(Structure):
    def __init__(self, x, y, path_structures):
        super().__init__(x, y, path_structures)
        self.height = 100
        self.width = 200
        self.graphics = pygame.image.load(os.path.join(path_structures, "grass_background.png"))


class Mailbox(CollideStructure):
    def __init__(self, x, y, path_structures):
        super().__init__(x, y, path_structures)
        self.height = 100
        self.width = 200
        self.graphics = pygame.image.load(os.path.join(path_structures, "mailbox.png"))


class Path(Structure):
    def __init__(self, x, y, variant, path_structures):
        super().__init__(x, y, path_structures)
        self.height = 32
        self.width = 32
        if variant == 1:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "path_C.png"))
        elif variant == 2:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "path_NW.png"))
        elif variant == 3:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "path_N.png"))
        elif variant == 4:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "path_NE.png"))
        elif variant == 5:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "path_W.png"))
        elif variant == 6:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "path_E.png"))
        elif variant == 7:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "path_SW.png"))
        elif variant == 8:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "path_S.png"))
        elif variant == 9:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "path_SE.png"))


class PathEntrance(Structure):
    def __init__(self, x, y, variant, path_structures):
        super().__init__(x, y, path_structures)
        self.height = 32
        self.width = 32
        if variant == 1:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "path_ANE.png"))
        elif variant == 2:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "path_ANW.png"))
        elif variant == 3:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "path_ASE.png"))
        elif variant == 4:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "path_ASW.png"))


class WaterEdge(CollideStructure):
    def __init__(self, x, y, variant, path_structures):
        super().__init__(x, y, path_structures)
        self.height = 32
        self.width = 32
        if variant == 1:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "water_edge_C.png"))
        elif variant == 2:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "water_edge_NW.png"))
        elif variant == 3:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "water_edge_N.png"))
        elif variant == 4:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "water_edge_NE.png"))
        elif variant == 5:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "water_edge_W.png"))
        elif variant == 6:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "water_edge_E.png"))
        elif variant == 7:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "water_edge_SW.png"))
        elif variant == 8:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "water_edge_S.png"))
        elif variant == 9:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "water_edge_SE.png"))


class WhiteFence(CollideStructure):
    def __init__(self, x, y, variant, path_structures):
        super().__init__(x, y, path_structures)
        self.height = 30
        self.width = 30
        if variant == 1:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "fence_white_N.png"))
        elif variant == 2:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "fence_white_E.png"))
        elif variant == 3:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "fence_white_NE.png"))
        elif variant == 4:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "fence_white_W.png"))
        elif variant == 5:
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "fence_white_NW.png"))


class WhiteSign(CollideStructure):
    def __init__(self, x, y, path_structures):
        super().__init__(x, y, path_structures)
        self.height = 100
        self.width = 200
        self.graphics = pygame.image.load(os.path.join(path_structures, "sign_white.png"))


class BrownSign(CollideStructure):
    def __init__(self, x, y, path_structures):
        super().__init__(x, y, path_structures)
        self.height = 100
        self.width = 200
        self.graphics = pygame.image.load(os.path.join(path_structures, "sign_brown.png"))


class Flower(Structure):
    def __init__(self, x, y, path_structures):
        super().__init__(x, y, path_structures)
        self.height = 100
        self.width = 200
        self.graphics = pygame.image.load(os.path.join(path_structures, "flower.png"))


class Tree(CollideStructure):
    def __init__(self, x, y, path_structures):
        super().__init__(x, y, path_structures)
        self.height = 100
        self.width = 200
        self.graphics = pygame.image.load(os.path.join(path_structures, "tree.png"))


class Grass(CollideStructure):
    def __init__(self, x, y, path_structures):
        super().__init__(x, y, path_structures)
        self.height = 50
        self.width = 50
        self.graphics = pygame.image.load(os.path.join(path_structures, "grass.png"))
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, player):
        super().update(player)
        self.shape = pygame.Rect(self.x + 30, self.y - 600, self.width, self.height)
