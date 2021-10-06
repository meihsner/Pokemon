import pygame
import os


class Plant1:
    def __init__(self, x, y, path_structures):
        self.size = 10
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.height = 15
        self.width = 15
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = pygame.image.load(os.path.join(path_structures, "grass1.png"))

    def update(self, player):
        self.x = self.start_x + player.x
        self.y = self.start_y + player.y

    def draw(self, screen):
        screen.blit(self.graphics, (self.x, self.y))

    def collide(self, player):

        if self.shape.colliderect(player):
            return True
        else:
            return False


class Tree1:
    def __init__(self, x, y, path_structures):
        self.size = 10
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.height = 90
        self.width = 70
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = pygame.image.load(os.path.join(path_structures, "tree1.png"))

    def update(self, player):
        self.x = self.start_x + player.x
        self.y = self.start_y + player.y

    def draw(self, screen):
        screen.blit(self.graphics, (self.x, self.y))

    def collide(self, player):
        if self.shape.colliderect(player):
            return True
        else:
            return False


class Fence:
    def __init__(self, x, y, variant, path_structures):
        self.size = 10
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        if variant == 1:
            self.height = 30
            self.width = 24
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "N_fence.png"))
        elif variant == 2:
            self.height = 30
            self.width = 24
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "S_fence.png"))
        elif variant == 3:
            self.height = 61
            self.width = 12
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "E_fence.png"))
        elif variant == 4:
            self.height = 61
            self.width = 12
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "W_fence.png"))
        elif variant == 5:
            self.height = 20
            self.width = 10
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "NE_fence.png"))
        elif variant == 6:
            self.height = 20
            self.width = 10
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "NW_fence.png"))
        elif variant == 7:
            self.height = 20
            self.width = 10
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "SE_fence.png"))
        elif variant == 8:
            self.height = 20
            self.width = 10
            self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
            self.graphics = pygame.image.load(os.path.join(path_structures, "SW_fence.png"))

    def update(self, player):
        self.x = self.start_x + player.x
        self.y = self.start_y + player.y

    def draw(self, screen):
        screen.blit(self.graphics, (self.x, self.y))

    def collide(self, player):
        if self.shape.colliderect(player):
            return True
        else:
            return False


class House:
    def __init__(self, x, y, path_structures):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.height = 100
        self.width = 200
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = pygame.image.load(os.path.join(path_structures, "house.png"))

    def update(self, player):
        self.x = self.start_x - player.x
        self.y = self.start_y - player.y

    def draw(self, screen):
        screen.blit(self.graphics, (self.x, self.y))

    def collide(self, player):
        if self.shape.colliderect(player):
            return True
        else:
            return False


class Lab:
    def __init__(self, x, y, path_structures):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.height = 100
        self.width = 200
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = pygame.image.load(os.path.join(path_structures, "oak_lab.png"))

    def update(self, player):
        self.x = self.start_x - player.x
        self.y = self.start_y - player.y

    def draw(self, screen):
        screen.blit(self.graphics, (self.x, self.y))

    def collide(self, player):
        if self.shape.colliderect(player):
            return True
        else:
            return False


class GrassBackground:
    def __init__(self, x, y, path_structures):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.height = 100
        self.width = 200
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = pygame.image.load(os.path.join(path_structures, "grass_background.png"))

    def update(self, player):
        self.x = self.start_x - player.x
        self.y = self.start_y - player.y

    def draw(self, screen):
        screen.blit(self.graphics, (self.x, self.y))


class Mailbox:
    def __init__(self, x, y, path_structures):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.height = 100
        self.width = 200
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = pygame.image.load(os.path.join(path_structures, "mailbox.png"))

    def update(self, player):
        self.x = self.start_x - player.x
        self.y = self.start_y - player.y

    def draw(self, screen):
        screen.blit(self.graphics, (self.x, self.y))

    def collide(self, player):
        if self.shape.colliderect(player):
            return True
        else:
            return False


class Path:
    def __init__(self, x, y, variant, path_structures):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
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

    def update(self, player):
        self.x = self.start_x - player.x
        self.y = self.start_y - player.y

    def draw(self, screen):
        screen.blit(self.graphics, (self.x, self.y))

    def collide(self, player):
        if self.shape.colliderect(player):
            return True
        else:
            return False


class PathEntrance:
    def __init__(self, x, y, variant, path_structures):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
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

    def update(self, player):
        self.x = self.start_x - player.x
        self.y = self.start_y - player.y

    def draw(self, screen):
        screen.blit(self.graphics, (self.x, self.y))

    def collide(self, player):
        if self.shape.colliderect(player):
            return True
        else:
            return False


class WaterEdge:
    def __init__(self, x, y, variant, path_structures):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
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

    def update(self, player):
        self.x = self.start_x - player.x
        self.y = self.start_y - player.y

    def draw(self, screen):
        screen.blit(self.graphics, (self.x, self.y))

    def collide(self, player):
        if self.shape.colliderect(player):
            return True
        else:
            return False


class WhiteFence:
    def __init__(self, x, y, variant, path_structures):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
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

    def update(self, player):
        self.x = self.start_x - player.x
        self.y = self.start_y - player.y

    def draw(self, screen):
        screen.blit(self.graphics, (self.x, self.y))

    def collide(self, player):
        if self.shape.colliderect(player):
            return True
        else:
            return False


class WhiteSign:
    def __init__(self, x, y, path_structures):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.height = 100
        self.width = 200
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = pygame.image.load(os.path.join(path_structures, "sign_white.png"))

    def update(self, player):
        self.x = self.start_x - player.x
        self.y = self.start_y - player.y

    def draw(self, screen):
        screen.blit(self.graphics, (self.x, self.y))

    def collide(self, player):
        if self.shape.colliderect(player):
            return True
        else:
            return False


class BrownSign:
    def __init__(self, x, y, path_structures):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.height = 100
        self.width = 200
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = pygame.image.load(os.path.join(path_structures, "sign_brown.png"))

    def update(self, player):
        self.x = self.start_x - player.x
        self.y = self.start_y - player.y

    def draw(self, screen):
        screen.blit(self.graphics, (self.x, self.y))

    def collide(self, player):
        if self.shape.colliderect(player):
            return True
        else:
            return False


class Flower:
    def __init__(self, x, y, path_structures):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.height = 100
        self.width = 200
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = pygame.image.load(os.path.join(path_structures, "flower.png"))

    def update(self, player):
        self.x = self.start_x - player.x
        self.y = self.start_y - player.y

    def draw(self, screen):
        screen.blit(self.graphics, (self.x, self.y))

    def collide(self, player):
        if self.shape.colliderect(player):
            return True
        else:
            return False


class Tree:
    def __init__(self, x, y, path_structures):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.height = 100
        self.width = 200
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = pygame.image.load(os.path.join(path_structures, "tree.png"))

    def update(self, player):
        self.x = self.start_x - player.x
        self.y = self.start_y - player.y

    def draw(self, screen):
        screen.blit(self.graphics, (self.x, self.y))

    def collide(self, player):
        if self.shape.colliderect(player):
            return True
        else:
            return False


class Grass:
    def __init__(self, x, y, path_structures):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.height = 50
        self.width = 50
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.grafika = pygame.image.load(os.path.join(path_structures, "grass.png"))

    def update(self, player):
        self.x = self.start_x - player.x
        self.y = self.start_y - player.y
        self.shape = pygame.Rect(self.x + 30, self.y - 600, self.width, self.height)

    def draw(self, screen):
        screen.blit(self.grafika, (self.x, self.y))

    def collide(self, player):
        if self.shape.colliderect(player):
            return True
        else:
            return False


class Background:
    def __init__(self):
        self.height = 640
        self.width = 480
        self.graphics = pygame.image.load(os.path.join("grass_background.png"))

    def draw(self, screen):
        screen.blit(self.graphics, (0, 0))
