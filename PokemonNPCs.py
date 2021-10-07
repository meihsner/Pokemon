import pygame
import os


class NPCModel:
    def __init__(self, x, y, path_NPC):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.height = 1
        self.width = 1
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = None
        self.name = "None"

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


class NPCMovingModel(NPCModel):
    def move_y(self, v):
        self.y = self.y + v
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)

    def move_x(self, c):
        self.x = self.x + c
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)


class NPC1(NPCModel):
    def __init__(self, x, y, path_NPC):
        super().__init__(x, y, path_NPC)
        self.height = 32
        self.width = 32
        self.graphics = pygame.image.load(os.path.join(path_NPC, "NPC1_S.png"))
        self.name = "No name"


class NPC2(NPCModel):
    def __init__(self, x, y, path_NPC):
        super().__init__(x, y, path_NPC)
        self.height = 32
        self.width = 32
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = pygame.image.load(os.path.join(path_NPC, "NPC2_W.png"))
        self.name = "No name"


class NurseNPC(NPCMovingModel):
    def __init__(self, x, y, path_NPC):
        super().__init__(x, y, path_NPC)
        self.height = 20
        self.width = 16
        self.graphics = pygame.image.load(os.path.join(path_NPC, "nurse_1.png"))
        self.name = "Nurse Joy"


class SellerNPC(NPCMovingModel):
    def __init__(self, x, y, path_NPC):
        super().__init__(x, y, path_NPC)
        self.height = 20
        self.width = 16
        self.graphics = pygame.image.load(os.path.join(path_NPC, "seller_1.png"))
        self.name = "Seller Bil"
