import pygame
import os


class NPC1:
    def __init__(self, x, y, path_NPC):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.height = 32
        self.width = 32
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = pygame.image.load(os.path.join(path_NPC, "NPC1_S.png"))

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


class NPC2:
    def __init__(self, x, y, path_NPC):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.height = 32
        self.width = 32
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = pygame.image.load(os.path.join(path_NPC, "NPC2_W.png"))

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


class NurseNPC:
    def __init__(self, x, y, path_NPC):
        self.x = x
        self.y = y
        self.height = 20
        self.width = 16
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = pygame.image.load(os.path.join(path_NPC, "nurse_1.png"))
        self.name = "Nurse Joy"

    def move_y(self, v):
        self.y = self.y + v
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)

    def move_x(self, c):
        self.x = self.x + c
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        screen.blit(self.graphics, (self.x, self.y))

    def collide(self, player):
        if self.shape.colliderect(player):
            return True
        else:
            return False


class SellerNPC:
    def __init__(self, x, y, path_NPC):
        self.x = x
        self.y = y
        self.height = 20
        self.width = 16
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = pygame.image.load(os.path.join(path_NPC, "seller_1.png"))
        self.name = "Seller Bil"

    def move_y(self, v):
        self.y = self.y + v
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)

    def move_x(self, c):
        self.x = self.x + c
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        screen.blit(self.graphics, (self.x, self.y))

    def collide(self, player):
        if self.shape.colliderect(player):
            return True
        else:
            return False
