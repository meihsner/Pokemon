import pygame
import os
import random
import math
from PokemonMoves import Moves

size = width, height = 640, 480
pygame.display.set_caption('Pokemon')
background_color = (255, 255, 255)
screen = pygame.display.set_mode(size)


def leveling(level):
    total_exp = pow(level, 3)
    next_level = pow((level + 1), 3)
    to_next_level = next_level - total_exp
    return total_exp, next_level, to_next_level


class PokemonType:
    def __init__(self, typ, path_visual_elements):
        self.type = typ
        if self.type == "normal":
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "type_normal.png"))
        elif self.type == "fight":
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "type_fight.png"))
        elif self.type == "flying":
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "type_flying.png"))
        elif self.type == "poison":
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "type_poison.png"))
        elif self.type == "ground":
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "type_ground.png"))
        elif self.type == "rock":
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "type_rock.png"))
        elif self.type == "bug":
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "type_bug.png"))
        elif self.type == "ghost":
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "type_ghost.png"))
        elif self.type == "steel":
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "type_steel.png"))
        elif self.type == "fire":
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "type_fire.png"))
        elif self.type == "water":
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "type_water.png"))
        elif self.type == "grass":
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "type_grass.png"))
        elif self.type == "electric":
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "type_electric.png"))
        elif self.type == "psychic":
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "type_psychic.png"))
        elif self.type == "ice":
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "type_ice.png"))
        elif self.type == "dragon":
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "type_dragon.png"))
        elif self.type == "dark":
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "type_dark.png"))
        elif self.type == "unknown":
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "unknown.png"))

    def draw(self, x, y):
        screen.blit(self.graphics, (x, y))


class Pokemon:
    def __init__(self, number, path_pokemons, path_audio, path_moves_animations, path_exp_bar, path_hp_bar):
        self.number = number
        self.location = "Starting"
        # self.location = gracz.current_location

        if number == 1:
            self.graphics = pygame.image.load(os.path.join(path_pokemons, "charmander.png"))
            self.name = "Charmander"
            self.level = random.randint(2, 4)
            self.starting_level = self.level
            self.menu_graphics = pygame.image.load(os.path.join(path_pokemons, "charmander2.png"))
            self.battle_graphics = pygame.image.load(os.path.join(path_pokemons, "charmander3.png"))
            self.x_battle = 80
            self.y_battle = 162
            self.type = ["fire"]
            self.total_exp, self.next_level, self.to_next_level = leveling(self.level)
            self.exp = 0
            self.to_next_level_exp = self.to_next_level - self.exp
            self.nature = "UNKNOWN"
            self.ability = "UNKNOWN"
            self.moves = [Moves("Scratch", path_audio, path_moves_animations),
                          Moves("Growl", path_audio, path_moves_animations),
                          Moves("Ember", path_audio, path_moves_animations),
                          Moves("Smokescreen", path_audio, path_moves_animations)]
            self.exp_value = 62
            self.holding_item = "none"

            self.base_hp = 39
            self.base_attack = 52
            self.base_defense = 43
            self.base_sp_atk = 60
            self.base_sp_def = 50
            self.base_speed = 65

            self.IV_hp = random.randint(0, 15)
            self.IV_attack = random.randint(0, 15)
            self.IV_defense = random.randint(0, 15)
            self.IV_sp_atk = random.randint(0, 15)
            self.IV_sp_def = random.randint(0, 15)
            self.IV_speed = random.randint(0, 15)

            self.battle_count = 0  # max = 65535 \\\ + 100 za walkę

            self.EV_hp = 0 + (100 * self.battle_count)
            self.EV_attack = 0 + (100 * self.battle_count)
            self.EV_defense = 0 + (100 * self.battle_count)
            self.EV_sp_atk = 0 + (100 * self.battle_count)
            self.EV_sp_def = 0 + (100 * self.battle_count)
            self.EV_speed = 0 + (100 * self.battle_count)

            self.hp = round(((((self.base_hp + self.IV_hp) * 2 +
                               (math.sqrt(self.EV_hp) / 4)) * self.level) / 100) + self.level + 10)
            self.current_hp = self.hp
            self.attack = round(((((self.base_attack + self.IV_attack) * 2 +
                                   (math.sqrt(self.EV_attack) / 4)) * self.level) / 100) + 5)
            self.current_attack = self.attack
            self.defense = round(((((self.base_defense + self.IV_defense) * 2 +
                                    (math.sqrt(self.EV_defense) / 4)) * self.level) / 100) + 5)
            self.current_defense = self.defense
            self.sp_atk = round(((((self.base_sp_atk + self.IV_sp_atk) * 2 +
                                   (math.sqrt(self.EV_sp_atk) / 4)) * self.level) / 100) + 5)
            self.current_sp_atk = self.sp_atk
            self.sp_def = round(((((self.base_sp_def + self.IV_sp_def) * 2 +
                                   (math.sqrt(self.EV_sp_def) / 4)) * self.level) / 100) + 5)
            self.current_sp_def = self.sp_def
            self.speed = round(((((self.base_speed + self.IV_speed) * 2 +
                                  (math.sqrt(self.EV_speed) / 4)) * self.level) / 100) + 5)
            self.current_speed = self.speed
            self.current_accuracy = 100

            self.hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_1.png"))
            self.exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_100.png"))

            self.new_attack_level = [6, 8]
            self.new_attack = ["Ember", "Smokescreen"]

            if random.randint(1, 100) <= 88:
                self.sex = "men"
                self.sex_x = 180
                self.sex_y = 84
                self.sex_graphics = pygame.image.load(os.path.join(path_pokemons, "men_sex.png"))
            else:
                self.sex = "women"
                self.sex_x = 180
                self.sex_y = 82
                self.sex_graphics = pygame.image.load(os.path.join(path_pokemons, "women_sex.png"))

        elif number == 2:
            self.graphics = pygame.image.load(os.path.join(path_pokemons, "squirtle.png"))
            self.name = "Squirtle"
            self.level = random.randint(2, 4)
            self.starting_level = self.level
            self.menu_graphics = pygame.image.load(os.path.join(path_pokemons, "squirtle2.png"))
            self.battle_graphics = pygame.image.load(os.path.join(path_pokemons, "squirtle3.png"))
            self.x_battle = 80
            self.y_battle = 196
            self.type = ["water"]
            self.total_exp, self.next_level, self.to_next_level = leveling(self.level)
            self.exp = 0
            self.to_next_level_exp = self.to_next_level - self.exp
            self.nature = "UNKNOWN"
            self.ability = "UNKNOWN"
            self.moves = [Moves("Tackle", path_audio, path_moves_animations),
                          Moves("Tail Whip", path_audio, path_moves_animations),
                          Moves("Water gun", path_audio, path_moves_animations)]
            self.exp_value = 63
            self.holding_item = "none"

            self.base_hp = 44
            self.base_attack = 48
            self.base_defense = 65
            self.base_sp_atk = 50
            self.base_sp_def = 64
            self.base_speed = 43

            self.IV_hp = random.randint(0, 15)
            self.IV_attack = random.randint(0, 15)
            self.IV_defense = random.randint(0, 15)
            self.IV_sp_atk = random.randint(0, 15)
            self.IV_sp_def = random.randint(0, 15)
            self.IV_speed = random.randint(0, 15)

            self.battle_count = 0  # max = 65535 \\\ + 100 za walkę

            self.EV_hp = 0 + (100 * self.battle_count)
            self.EV_attack = 0 + (100 * self.battle_count)
            self.EV_defense = 0 + (100 * self.battle_count)
            self.EV_sp_atk = 0 + (100 * self.battle_count)
            self.EV_sp_def = 0 + (100 * self.battle_count)
            self.EV_speed = 0 + (100 * self.battle_count)

            self.hp = round(((((self.base_hp + self.IV_hp) * 2 +
                               (math.sqrt(self.EV_hp) / 4)) * self.level) / 100) + self.level + 10)
            self.current_hp = self.hp
            self.attack = round(((((self.base_attack + self.IV_attack) * 2 +
                                   (math.sqrt(self.EV_attack) / 4)) * self.level) / 100) + 5)
            self.current_attack = self.attack
            self.defense = round(((((self.base_defense + self.IV_defense) * 2 +
                                    (math.sqrt(self.EV_defense) / 4)) * self.level) / 100) + 5)
            self.current_defense = self.defense
            self.sp_atk = round(((((self.base_sp_atk + self.IV_sp_atk) * 2 +
                                   (math.sqrt(self.EV_sp_atk) / 4)) * self.level) / 100) + 5)
            self.current_sp_atk = self.sp_atk
            self.sp_def = round(((((self.base_sp_def + self.IV_sp_def) * 2 +
                                   (math.sqrt(self.EV_sp_def) / 4)) * self.level) / 100) + 5)
            self.current_sp_def = self.sp_def
            self.speed = round(((((self.base_speed + self.IV_speed) * 2 +
                                  (math.sqrt(self.EV_speed) / 4)) * self.level) / 100) + 5)
            self.current_speed = self.speed
            self.current_accuracy = 100

            self.hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_1.png"))
            self.exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_100.png"))

            self.new_attack_level = [6, 8]
            self.new_attack = ["Water gun", "Withdraw"]

            if random.randint(1, 100) <= 88:
                self.sex = "men"
                self.sex_x = 134
                self.sex_y = 84
                self.sex_graphics = pygame.image.load(os.path.join(path_pokemons, "men_sex.png"))
            else:
                self.sex = "women"
                self.sex_x = 130
                self.sex_y = 82
                self.sex_graphics = pygame.image.load(os.path.join(path_pokemons, "women_sex.png"))

        elif number == 3:
            self.graphics = pygame.image.load(os.path.join(path_pokemons, "bulbasaur.png"))
            self.name = "Bulbasaur"
            self.level = random.randint(2, 4)
            self.starting_level = self.level
            self.menu_graphics = pygame.image.load(os.path.join(path_pokemons, "bulbasaur2.png"))
            self.battle_graphics = pygame.image.load(os.path.join(path_pokemons, "bulbasaur3.png"))
            self.x_battle = 80
            self.y_battle = 200
            self.type = ["grass"]
            self.total_exp, self.next_level, self.to_next_level = leveling(self.level)
            self.exp = 0
            self.to_next_level_exp = self.to_next_level - self.exp
            self.nature = "UNKNOWN"
            self.ability = "UNKNOWN"
            self.moves = [Moves("Tackle", path_audio, path_moves_animations),
                          Moves("Growl", path_audio, path_moves_animations)]
            self.exp_value = 64
            self.holding_item = "none"

            self.base_hp = 45
            self.base_attack = 49
            self.base_defense = 49
            self.base_sp_atk = 65
            self.base_sp_def = 65
            self.base_speed = 45

            self.IV_hp = random.randint(0, 15)
            self.IV_attack = random.randint(0, 15)
            self.IV_defense = random.randint(0, 15)
            self.IV_sp_atk = random.randint(0, 15)
            self.IV_sp_def = random.randint(0, 15)
            self.IV_speed = random.randint(0, 15)

            self.battle_count = 0  # max = 65535 \\\ + 100 za walkę

            self.EV_hp = 0 + (100 * self.battle_count)
            self.EV_attack = 0 + (100 * self.battle_count)
            self.EV_defense = 0 + (100 * self.battle_count)
            self.EV_sp_atk = 0 + (100 * self.battle_count)
            self.EV_sp_def = 0 + (100 * self.battle_count)
            self.EV_speed = 0 + (100 * self.battle_count)

            self.hp = round(((((self.base_hp + self.IV_hp) * 2 +

                               (math.sqrt(self.EV_hp) / 4)) * self.level) / 100) + self.level + 10)
            self.current_hp = self.hp
            self.attack = round(((((self.base_attack + self.IV_attack) * 2 +
                                   (math.sqrt(self.EV_attack) / 4)) * self.level) / 100) + 5)
            self.current_attack = self.attack
            self.defense = round(((((self.base_defense + self.IV_defense) * 2 +
                                    (math.sqrt(self.EV_defense) / 4)) * self.level) / 100) + 5)
            self.current_defense = self.defense
            self.sp_atk = round(((((self.base_sp_atk + self.IV_sp_atk) * 2 +
                                   (math.sqrt(self.EV_sp_atk) / 4)) * self.level) / 100) + 5)
            self.current_sp_atk = self.sp_atk
            self.sp_def = round(((((self.base_sp_def + self.IV_sp_def) * 2 +
                                   (math.sqrt(self.EV_sp_def) / 4)) * self.level) / 100) + 5)
            self.current_sp_def = self.sp_def
            self.speed = round(((((self.base_speed + self.IV_speed) * 2 +
                                  (math.sqrt(self.EV_speed) / 4)) * self.level) / 100) + 5)
            self.current_speed = self.speed
            self.current_accuracy = 100

            self.hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_1.png"))
            self.exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_100.png"))

            self.new_attack_level = [6, 8]
            self.new_attack = ["Vine Whip", "Growth"]

            if random.randint(1, 100) <= 88:
                self.sex = "men"
                self.sex_x = 180
                self.sex_y = 84
                self.sex_graphics = pygame.image.load(os.path.join(path_pokemons, "men_sex.png"))
            else:
                self.sex = "women"
                self.sex_x = 180
                self.sex_y = 82
                self.sex_graphics = pygame.image.load(os.path.join(path_pokemons, "women_sex.png"))

        elif number == 4:
            self.graphics = pygame.image.load(os.path.join(path_pokemons, "pidgey.png"))
            self.name = "Pidgey"
            self.level = random.randint(2, 4)
            self.starting_level = self.level
            self.menu_graphics = pygame.image.load(os.path.join(path_pokemons, "pidgey2.png"))
            self.battle_graphics = pygame.image.load(os.path.join(path_pokemons, "pidgey3.png"))
            self.x_battle = 80
            self.y_battle = 168
            self.type = ["normal"]
            self.total_exp, self.next_level, self.to_next_level = leveling(self.level)
            self.exp = 0
            self.to_next_level_exp = self.to_next_level - self.exp
            self.nature = "UNKNOWN"
            self.ability = "UNKNOWN"
            self.moves = [Moves("Tackle", path_audio, path_moves_animations),
                          Moves("Sand attack", path_audio, path_moves_animations)]
            self.exp_value = 64
            self.holding_item = "none"

            self.base_hp = 40
            self.base_attack = 45
            self.base_defense = 40
            self.base_sp_atk = 35
            self.base_sp_def = 35
            self.base_speed = 56

            self.IV_hp = random.randint(0, 15)
            self.IV_attack = random.randint(0, 15)
            self.IV_defense = random.randint(0, 15)
            self.IV_sp_atk = random.randint(0, 15)
            self.IV_sp_def = random.randint(0, 15)
            self.IV_speed = random.randint(0, 15)

            self.battle_count = 0  # max = 65535 \\\ + 100 za walkę

            self.EV_hp = 0 + (100 * self.battle_count)
            self.EV_attack = 0 + (100 * self.battle_count)
            self.EV_defense = 0 + (100 * self.battle_count)
            self.EV_sp_atk = 0 + (100 * self.battle_count)
            self.EV_sp_def = 0 + (100 * self.battle_count)
            self.EV_speed = 0 + (100 * self.battle_count)

            self.hp = round(((((self.base_hp + self.IV_hp) * 2 +
                               (math.sqrt(self.EV_hp) / 4)) * self.level) / 100) + self.level + 10)
            self.current_hp = self.hp
            self.attack = round(((((self.base_attack + self.IV_attack) * 2 +
                                   (math.sqrt(self.EV_attack) / 4)) * self.level) / 100) + 5)
            self.current_attack = self.attack
            self.defense = round(((((self.base_defense + self.IV_defense) * 2 +
                                    (math.sqrt(self.EV_defense) / 4)) * self.level) / 100) + 5)
            self.current_defense = self.defense
            self.sp_atk = round(((((self.base_sp_atk + self.IV_sp_atk) * 2 +
                                   (math.sqrt(self.EV_sp_atk) / 4)) * self.level) / 100) + 5)
            self.current_sp_atk = self.sp_atk
            self.sp_def = round(((((self.base_sp_def + self.IV_sp_def) * 2 +
                                   (math.sqrt(self.EV_sp_def) / 4)) * self.level) / 100) + 5)
            self.current_sp_def = self.sp_def
            self.speed = round(((((self.base_speed + self.IV_speed) * 2 +
                                  (math.sqrt(self.EV_speed) / 4)) * self.level) / 100) + 5)
            self.current_speed = self.speed
            self.current_accuracy = 100

            self.hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_1.png"))
            self.exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_100.png"))

            self.new_attack_level = [20]
            self.new_attack = ["Gust"]

            if random.randint(1, 100) <= 88:
                self.sex = "men"
                self.sex_x = 180
                self.sex_y = 84
                self.sex_graphics = pygame.image.load(os.path.join(path_pokemons, "men_sex.png"))
            else:
                self.sex = "women"
                self.sex_x = 180
                self.sex_y = 82
                self.sex_graphics = pygame.image.load(os.path.join(path_pokemons, "women_sex.png"))

    def draw(self, x, y):
        screen.blit(self.graphics, (x, y))

    def draw_menu(self, x, y):
        screen.blit(self.menu_graphics, (x, y))

    def draw_battle(self):
        screen.blit(self.battle_graphics, (self.x_battle, self.y_battle))

    def draw_hp_bar(self, x, y):
        screen.blit(self.hp_bar_graphics, (x, y))

    def draw_exp_bar(self, x, y):
        screen.blit(self.exp_bar_graphics, (x, y))
