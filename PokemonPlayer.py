import pygame
import os


class Player:
    def __init__(self, x, y, path_man_player_animations):
        self.x = 0
        self.y = 0
        self.tmp_x = x + 50
        self.tmp_y = y - 65
        self.height = 19
        self.width = 15
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphics = pygame.image.load(os.path.join(path_man_player_animations, "d1.png"))
        self.pokemon_steps = 0
        self.items = []
        self.key_items = []
        self.pokeballs = []
        self.pokemons = []
        self.main_pokemon = []
        self.pokemon_storage = []
        self.name = "ASH"
        self.blance = 0
        self.pokedex = 0
        self.badges = []
        self.current_location = "STARTING PLACE"
        self.registered_item = "none"
        self.seen = 0
        self.owned = 0

    def move_y(self, v):
        self.y = self.y + v
        self.tmp_y = self.tmp_y + v
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)

    def move_x(self, c):
        self.x = self.x + c
        self.tmp_x = self.tmp_x + c
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        screen.blit(self.graphics, (300, 190))


class PlayerCatching:
    def __init__(self, path_man_player_animations):
        self.grafika = pygame.image.load(os.path.join(path_man_player_animations, "c1.png"))
        self.x = 80
        self.y = 163
        self.height = 60
        self.width = 40
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        screen.blit(self.grafika, (self.x, self.y))
