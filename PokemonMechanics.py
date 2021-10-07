import pygame
import os
import math
from datetime import datetime
from PokemonPokemons import *
from PokemonItems import *
from PokemonNPCs import *
from PokemonMaps import *
from PokemonPlayer import *
from PokemonVisualElements import *
import sys


size = width, height = 640, 480
pygame.display.set_caption('Pokemon')
background_color = (255, 255, 255)
screen = pygame.display.set_mode(size)


def type_text(text, text_x, text_y, size, color):
    font = pygame.font.SysFont("Arial", size)
    rend = font.render(text, True, color)
    screen.blit(rend, (text_x, text_y))


def gain_exp(exp_value, level, battle_pokemon_list):
    a = 1  # 1 if wild pokemon, 1.5 if trainer pokemon
    t = 1  # 1 if the winning Pokemon's is its Original Trainer, 1.5 if the Pokemon was gained in a domestic trade
    b = exp_value  # pokemon.exp_value
    e = 1  # 1.5 if pokemon is holding lucky egg, otherwise 1
    L = level  # pokemon.level
    p = 1  # 1 if no Exp. Point Power
    f = 1  # 1.2 if the Pokemon has an Affection of two hearts or more, otherwise 1
    v = 1
    s = len(
        battle_pokemon_list)  # The number of Pokemon that participated in the battle and have not fainted
    EXP = round((a * t * b * e * L * p * f * v) / (7 * s))
    return EXP


def switch_pokemon_battle(battle_pokemon_list, switch_pkm, pokemon_exist, player):
    if pokemon_exist:
        add_to_list = "True"
        # for i in range(0, len(battle_pokemon_list)):
        #     if switch_pkm == battle_pokemon_list[i]:
        #         add_to_list = "True"
        #         break
        # if add_to_list == "False":
        #     battle_pokemon_list.append(switch_pkm)
        add_to_list = "True"
        if switch_pkm in battle_pokemon_list:
            add_to_list = "False"
        if add_to_list == "True":
            battle_pokemon_list.append(switch_pkm)

        switched_pkm = "True"
        pkm_attack_2 = "True"
        window_state = "enemy_turn"
        battle_pkm = switch_pkm
    else:
        battle_pkm = player.main_pokemon[0]
        window_state = "pokemon_menu"
        pkm_attack_2 = "False"
        switched_pkm = "False"

    return battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm


def effectiveness(move_type, enemy_pokemon_type):
    move_type_list = ['normal', 'fight', 'flying', 'poison', 'ground', 'rock', 'bug', 'ghost', 'steel', 'fire', 'water',
                      'grass', 'electric', 'psychic', 'ice', 'dragon', 'dark', 'fairy']
    enemy_pokemon_type_list = ['normal', 'fight', 'flying', 'poison', 'ground', 'rock', 'bug', 'ghost', 'steel', 'fire',
                               'water', 'grass', 'electric', 'psychic', 'ice', 'dragon', 'dark', 'fairy']
    effectiveness_table = [[1, 1, 1, 1, 1, 0.5, 1, 0, 0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                           [2, 1, 0.5, 0.5, 1, 2, 0.5, 0, 2, 1, 1, 1, 1, 0.5, 2, 1, 2, 0.5],
                           [1, 2, 1, 1, 1, 0.5, 2, 1, 0.5, 1, 1, 2, 0.5, 1, 1, 1, 1, 1],
                           [1, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 0, 1, 1, 2, 1, 1, 1, 1, 1, 2],
                           [1, 1, 0, 2, 1, 2, 0.5, 1, 2, 2, 1, 0.5, 2, 1, 1, 1, 1, 1],
                           [1, 0.5, 2, 1, 0.5, 1, 2, 1, 0.5, 2, 1, 1, 1, 1, 2, 1, 1, 1],
                           [1, 0.5, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 0.5, 1, 2, 1, 2, 1, 1, 2, 0.5],
                           [0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 1],
                           [1, 1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 1, 2, 1, 1, 2],
                           [1, 1, 1, 1, 1, 0.5, 2, 1, 2, 0.5, 0.5, 2, 1, 1, 2, 0.5, 1, 1],
                           [1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 1, 0.5, 1, 1],
                           [1, 1, 0.5, 0.5, 2, 2, 0.5, 1, 0.5, 0.5, 2, 0.5, 1, 1, 1, 0.5, 1, 1],
                           [1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 0.5, 1, 1],
                           [1, 2, 1, 2, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 0.5, 1, 1, 0, 1],
                           [1, 1, 2, 1, 2, 1, 1, 1, 0.5, 0.5, 0.5, 2, 1, 1, 0.5, 2, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 1, 1, 2, 1, 0],
                           [1, 0.5, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 0.5],
                           [1, 2, 1, 0.5, 1, 1, 1, 1, 0.5, 0.5, 1, 1, 1, 1, 1, 2, 2, 1]]

    for i in range(0, len(move_type_list)):
        if move_type == move_type_list[i]:
            number1 = i
    for j in range(0, len(enemy_pokemon_type_list)):
        if enemy_pokemon_type == enemy_pokemon_type_list[j]:
            number2 = j
    effectiveness_type_modifier = effectiveness_table[number1][number2]
    if effectiveness_type_modifier == 1:
        effectiveness_status = "none"
    elif effectiveness_type_modifier == 0:
        effectiveness_status = "not effective"
    elif effectiveness_type_modifier == 0.5:
        effectiveness_status = "not very effective"
    elif effectiveness_type_modifier == 2:
        effectiveness_status = "super effective"

    return effectiveness_type_modifier, effectiveness_status


def health_bar_status(current_hp, hp, path_hp_bar):
    if current_hp == hp:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_1.png"))
    elif round((current_hp / hp) * 100) == 99 or round((current_hp / hp) * 100) == 98:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_2.png"))
    elif round((current_hp / hp) * 100) == 97 or round((current_hp / hp) * 100) == 96:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_3.png"))
    elif round((current_hp / hp) * 100) == 95:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_4.png"))
    elif round((current_hp / hp) * 100) == 94 or round((current_hp / hp) * 100) == 93:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_5.png"))
    elif round((current_hp / hp) * 100) == 92:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_6.png"))
    elif round((current_hp / hp) * 100) == 91:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_7.png"))
    elif round((current_hp / hp) * 100) == 90 or round((current_hp / hp) * 100) == 89:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_8.png"))
    elif round((current_hp / hp) * 100) == 88:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_9.png"))
    elif round((current_hp / hp) * 100) == 86 or round((current_hp / hp) * 100) == 87:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_10.png"))
    elif round((current_hp / hp) * 100) == 85:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_11.png"))
    elif round((current_hp / hp) * 100) == 83 or round((current_hp / hp) * 100) == 84:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_12.png"))
    elif round((current_hp / hp) * 100) == 82:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_13.png"))
    elif round((current_hp / hp) * 100) == 80 or round((current_hp / hp) * 100) == 81:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_14.png"))
    elif round((current_hp / hp) * 100) == 79:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_15.png"))
    elif round((current_hp / hp) * 100) == 77 or round((current_hp / hp) * 100) == 78:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_16.png"))
    elif round((current_hp / hp) * 100) == 76:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_17.png"))
    elif round((current_hp / hp) * 100) == 74 or round((current_hp / hp) * 100) == 75:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_18.png"))
    elif round((current_hp / hp) * 100) == 73:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_19.png"))
    elif round((current_hp / hp) * 100) == 71 or round((current_hp / hp) * 100) == 72:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_20.png"))
    elif round((current_hp / hp) * 100) == 70:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_21.png"))
    elif round((current_hp / hp) * 100) == 68 or round((current_hp / hp) * 100) == 69:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_22.png"))
    elif round((current_hp / hp) * 100) == 66 or round((current_hp / hp) * 100) == 67:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_23.png"))
    elif round((current_hp / hp) * 100) == 64 or round((current_hp / hp) * 100) == 65:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_24.png"))
    elif round((current_hp / hp) * 100) == 62 or round((current_hp / hp) * 100) == 63:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_25.png"))
    elif round((current_hp / hp) * 100) == 60 or round((current_hp / hp) * 100) == 61:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_26.png"))
    elif round((current_hp / hp) * 100) == 59 or round((current_hp / hp) * 100) == 58:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_27.png"))
    elif round((current_hp / hp) * 100) == 57 or round((current_hp / hp) * 100) == 56:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_28.png"))
    elif round((current_hp / hp) * 100) == 55 or round((current_hp / hp) * 100) == 54:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_29.png"))
    elif round((current_hp / hp) * 100) == 52 or round((current_hp / hp) * 100) == 53:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_30.png"))
    elif round((current_hp / hp) * 100) == 50 or round((current_hp / hp) * 100) == 51:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_31.png"))
    elif round((current_hp / hp) * 100) == 48 or round((current_hp / hp) * 100) == 49:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_32.png"))
    elif round((current_hp / hp) * 100) == 47:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_33.png"))
    elif round((current_hp / hp) * 100) == 45 or round((current_hp / hp) * 100) == 46:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_34.png"))
    elif round((current_hp / hp) * 100) == 43 or round((current_hp / hp) * 100) == 44:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_35.png"))
    elif round((current_hp / hp) * 100) == 41 or round((current_hp / hp) * 100) == 42:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_36.png"))
    elif round((current_hp / hp) * 100) == 39 or round((current_hp / hp) * 100) == 40:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_37.png"))
    elif round((current_hp / hp) * 100) == 37 or round((current_hp / hp) * 100) == 38:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_38.png"))
    elif round((current_hp / hp) * 100) == 35 or round((current_hp / hp) * 100) == 36:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_39.png"))
    elif round((current_hp / hp) * 100) == 34:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_40.png"))
    elif round((current_hp / hp) * 100) == 33:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_41.png"))
    elif round((current_hp / hp) * 100) == 31 or round((current_hp / hp) * 100) == 32:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_42.png"))
    elif round((current_hp / hp) * 100) == 30:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_43.png"))
    elif round((current_hp / hp) * 100) == 28 or round((current_hp / hp) * 100) == 29:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_44.png"))
    elif round((current_hp / hp) * 100) == 26 or round((current_hp / hp) * 100) == 27:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_45.png"))
    elif round((current_hp / hp) * 100) == 24 or round((current_hp / hp) * 100) == 25:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_46.png"))
    elif round((current_hp / hp) * 100) == 23:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_47.png"))
    elif round((current_hp / hp) * 100) == 22:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_48.png"))
    elif round((current_hp / hp) * 100) == 20 or round((current_hp / hp) * 100) == 21:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_49.png"))
    elif round((current_hp / hp) * 100) == 19:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_50.png"))
    elif round((current_hp / hp) * 100) == 18:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_51.png"))
    elif round((current_hp / hp) * 100) == 17:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_52.png"))
    elif round((current_hp / hp) * 100) == 16:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_53.png"))
    elif round((current_hp / hp) * 100) == 14 or round((current_hp / hp) * 100) == 15:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_54.png"))
    elif round((current_hp / hp) * 100) == 13:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_55.png"))
    elif round((current_hp / hp) * 100) == 12 or round((current_hp / hp) * 100) == 11:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_56.png"))
    elif round((current_hp / hp) * 100) == 10 or round((current_hp / hp) * 100) == 9:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_57.png"))
    elif round((current_hp / hp) * 100) == 8 or round((current_hp / hp) * 100) == 7:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_58.png"))
    elif round((current_hp / hp) * 100) == 5 or round((current_hp / hp) * 100) == 6:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_59.png"))
    elif round((current_hp / hp) * 100) == 3 or round((current_hp / hp) * 100) == 4:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_60.png"))
    elif round((current_hp / hp) * 100) == 1 or round((current_hp / hp) * 100) == 2:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_61.png"))
    elif round((current_hp / hp) * 100) == 0:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_62.png"))
    else:
        hp_bar_graphics = pygame.image.load(os.path.join(path_hp_bar, "hp_bar_1.png"))

    return hp_bar_graphics


def exp_bar_status(exp, to_next_level, path_exp_bar):
    if round((exp / to_next_level) * 100) >= 100:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_1.png"))
    elif round((exp / to_next_level) * 100) == 99:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_2.png"))
    elif round((exp / to_next_level) * 100) == 98:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_3.png"))
    elif round((exp / to_next_level) * 100) == 97:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_4.png"))
    elif round((exp / to_next_level) * 100) == 96:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_5.png"))
    elif round((exp / to_next_level) * 100) == 95:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_6.png"))
    elif round((exp / to_next_level) * 100) == 94:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_7.png"))
    elif round((exp / to_next_level) * 100) == 93:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_8.png"))
    elif round((exp / to_next_level) * 100) == 92:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_9.png"))
    elif round((exp / to_next_level) * 100) == 91:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_10.png"))
    elif round((exp / to_next_level) * 100) == 90:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_11.png"))
    elif round((exp / to_next_level) * 100) == 89:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_12.png"))
    elif round((exp / to_next_level) * 100) == 88:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_13.png"))
    elif round((exp / to_next_level) * 100) == 87:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_14.png"))
    elif round((exp / to_next_level) * 100) == 86:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_15.png"))
    elif round((exp / to_next_level) * 100) == 85:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_16.png"))
    elif round((exp / to_next_level) * 100) == 84:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_17.png"))
    elif round((exp / to_next_level) * 100) == 83:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_18.png"))
    elif round((exp / to_next_level) * 100) == 82:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_19.png"))
    elif round((exp / to_next_level) * 100) == 81:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_20.png"))
    elif round((exp / to_next_level) * 100) == 80:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_21.png"))
    elif round((exp / to_next_level) * 100) == 79:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_22.png"))
    elif round((exp / to_next_level) * 100) == 78:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_23.png"))
    elif round((exp / to_next_level) * 100) == 77:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_24.png"))
    elif round((exp / to_next_level) * 100) == 76:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_25.png"))
    elif round((exp / to_next_level) * 100) == 75:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_26.png"))
    elif round((exp / to_next_level) * 100) == 74:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_27.png"))
    elif round((exp / to_next_level) * 100) == 73:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_28.png"))
    elif round((exp / to_next_level) * 100) == 72:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_29.png"))
    elif round((exp / to_next_level) * 100) == 71:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_30.png"))
    elif round((exp / to_next_level) * 100) == 70:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_31.png"))
    elif round((exp / to_next_level) * 100) == 69:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_32.png"))
    elif round((exp / to_next_level) * 100) == 68:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_33.png"))
    elif round((exp / to_next_level) * 100) == 67:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_34.png"))
    elif round((exp / to_next_level) * 100) == 66:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_35.png"))
    elif round((exp / to_next_level) * 100) == 65:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_36.png"))
    elif round((exp / to_next_level) * 100) == 64:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_37.png"))
    elif round((exp / to_next_level) * 100) == 63:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_38.png"))
    elif round((exp / to_next_level) * 100) == 62:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_39.png"))
    elif round((exp / to_next_level) * 100) == 61:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_40.png"))
    elif round((exp / to_next_level) * 100) == 60:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_41.png"))
    elif round((exp / to_next_level) * 100) == 59:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_42.png"))
    elif round((exp / to_next_level) * 100) == 58:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_43.png"))
    elif round((exp / to_next_level) * 100) == 57:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_44.png"))
    elif round((exp / to_next_level) * 100) == 56:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_45.png"))
    elif round((exp / to_next_level) * 100) == 55:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_46.png"))
    elif round((exp / to_next_level) * 100) == 54:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_47.png"))
    elif round((exp / to_next_level) * 100) == 53:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_48.png"))
    elif round((exp / to_next_level) * 100) == 52:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_49.png"))
    elif round((exp / to_next_level) * 100) == 51:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_50.png"))
    elif round((exp / to_next_level) * 100) == 50:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_51.png"))
    elif round((exp / to_next_level) * 100) == 49:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_52.png"))
    elif round((exp / to_next_level) * 100) == 48:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_53.png"))
    elif round((exp / to_next_level) * 100) == 47:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_54.png"))
    elif round((exp / to_next_level) * 100) == 46:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_55.png"))
    elif round((exp / to_next_level) * 100) == 45:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_56.png"))
    elif round((exp / to_next_level) * 100) == 44:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_57.png"))
    elif round((exp / to_next_level) * 100) == 43:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_58.png"))
    elif round((exp / to_next_level) * 100) == 42:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_59.png"))
    elif round((exp / to_next_level) * 100) == 41:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_60.png"))
    elif round((exp / to_next_level) * 100) == 39:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_61.png"))
    elif round((exp / to_next_level) * 100) == 38:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_62.png"))
    elif round((exp / to_next_level) * 100) == 37:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_63.png"))
    elif round((exp / to_next_level) * 100) == 36:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_64.png"))
    elif round((exp / to_next_level) * 100) == 35:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_65.png"))
    elif round((exp / to_next_level) * 100) == 34:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_66.png"))
    elif round((exp / to_next_level) * 100) == 33:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_67.png"))
    elif round((exp / to_next_level) * 100) == 32:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_68.png"))
    elif round((exp / to_next_level) * 100) == 31:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_69.png"))
    elif round((exp / to_next_level) * 100) == 30:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_70.png"))
    elif round((exp / to_next_level) * 100) == 29:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_71.png"))
    elif round((exp / to_next_level) * 100) == 28:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_72.png"))
    elif round((exp / to_next_level) * 100) == 27:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_73.png"))
    elif round((exp / to_next_level) * 100) == 26:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_74.png"))
    elif round((exp / to_next_level) * 100) == 25:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_75.png"))
    elif round((exp / to_next_level) * 100) == 24:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_76.png"))
    elif round((exp / to_next_level) * 100) == 23:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_77.png"))
    elif round((exp / to_next_level) * 100) == 22:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_78.png"))
    elif round((exp / to_next_level) * 100) == 21:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_79.png"))
    elif round((exp / to_next_level) * 100) == 20:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_80.png"))
    elif round((exp / to_next_level) * 100) == 19:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_81.png"))
    elif round((exp / to_next_level) * 100) == 18:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_82.png"))
    elif round((exp / to_next_level) * 100) == 17:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_83.png"))
    elif round((exp / to_next_level) * 100) == 16:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_84.png"))
    elif round((exp / to_next_level) * 100) == 15:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_85.png"))
    elif round((exp / to_next_level) * 100) == 14:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_86.png"))
    elif round((exp / to_next_level) * 100) == 13:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_87.png"))
    elif round((exp / to_next_level) * 100) == 12:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_88.png"))
    elif round((exp / to_next_level) * 100) == 11:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_89.png"))
    elif round((exp / to_next_level) * 100) == 10:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_90.png"))
    elif round((exp / to_next_level) * 100) == 9:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_91.png"))
    elif round((exp / to_next_level) * 100) == 8:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_92.png"))
    elif round((exp / to_next_level) * 100) == 7:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_93.png"))
    elif round((exp / to_next_level) * 100) == 6:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_94.png"))
    elif round((exp / to_next_level) * 100) == 5:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_95.png"))
    elif round((exp / to_next_level) * 100) == 4:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_96.png"))
    elif round((exp / to_next_level) * 100) == 3:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_97.png"))
    elif round((exp / to_next_level) * 100) == 2:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_98.png"))
    elif round((exp / to_next_level) * 100) == 1:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_99.png"))
    elif round((exp / to_next_level) * 100) == 0:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_100.png"))
    else:
        exp_bar_graphics = pygame.image.load(os.path.join(path_exp_bar, "exp_bar_100.png"))

    return exp_bar_graphics


def regen_pp(pokemon):
    if len(pokemon.moves) == 1:
        pokemon.moves[0].current_pp = pokemon.moves[0].pp
    elif len(pokemon.moves) == 2:
        pokemon.moves[0].current_pp = pokemon.moves[0].pp
        pokemon.moves[1].current_pp = pokemon.moves[1].pp
    elif len(pokemon.moves) == 3:
        pokemon.moves[0].current_pp = pokemon.moves[0].pp
        pokemon.moves[1].current_pp = pokemon.moves[1].pp
        pokemon.moves[2].current_pp = pokemon.moves[2].pp
    elif len(pokemon.moves) == 4:
        pokemon.moves[0].current_pp = pokemon.moves[0].pp
        pokemon.moves[1].current_pp = pokemon.moves[1].pp
        pokemon.moves[2].current_pp = pokemon.moves[2].pp
        pokemon.moves[3].current_pp = pokemon.moves[3].pp


def leveling(level):
    # if level <= 50:
    #     total_exp = round((((level) ^ 3) * (100 - level)) / 50)
    # elif level <= 68 and level > 50:
    #     total_exp = round((((level) ^ 3) * (150 - level)) / 100)
    # elif level <= 98 and level > 68:
    #     total_exp = round((((level) ^ 3) * ((1911 - (10 * level)) / 3)) / 500)
    # elif level <= 100 and level > 98:
    #     total_exp = round((((level) ^ 3) * (160 - level)) / 100)
    #
    # if level <= 50:
    #     next_level = round((((level+1) ^ 3) * (100 - level+1)) / 50)
    # elif level <= 68 and level > 50:
    #     next_level = round((((level+1) ^ 3) * (150 - level+1)) / 100)
    # elif level <= 98 and level > 68:
    #     next_level = round((((level+1) ^ 3) * ((1911 - (10 * level+1)) / 3)) / 500)
    # elif level <= 100 and level > 98:
    #     next_level = round((((level+1) ^ 3) * (160 - level+1)) / 100)

    total_exp = pow(level, 3)
    next_level = pow((level + 1), 3)

    to_next_level = next_level - total_exp

    return total_exp, next_level, to_next_level


def level_up(level, base_hp, IV_hp, EV_hp, base_attack, IV_attack, EV_attack, base_defense, IV_defense, EV_defense,
             base_sp_atk, IV_sp_atk, EV_sp_atk, base_sp_def, IV_sp_def, EV_sp_def, base_speed, IV_speed, EV_speed):
    hp = round(((((base_hp + IV_hp) * 2 + (math.sqrt(EV_hp) / 4)) * level) / 100) + level + 10)
    current_hp = hp
    attack = round(((((base_attack + IV_attack) * 2 + (math.sqrt(EV_attack) / 4)) * level) / 100) + 5)
    current_attack = attack
    defense = round(((((base_defense + IV_defense) * 2 + (math.sqrt(EV_defense) / 4)) * level) / 100) + 5)
    current_defense = defense
    sp_atk = round(((((base_sp_atk + IV_sp_atk) * 2 + (math.sqrt(EV_sp_atk) / 4)) * level) / 100) + 5)
    current_sp_atk = sp_atk
    sp_def = round(((((base_sp_def + IV_sp_def) * 2 + (math.sqrt(EV_sp_def) / 4)) * level) / 100) + 5)
    current_sp_def = sp_def
    speed = round(((((base_speed + IV_speed) * 2 + (math.sqrt(EV_speed) / 4)) * level) / 100) + 5)
    current_speed = speed

    return hp, current_hp, attack, current_attack, defense, current_defense, sp_atk,\
        current_sp_atk, sp_def, current_sp_def, speed, current_speed


def redrawGameWindow(path_boy_player_animations, window_state, player, up, down, right, left, steps):
    player_right = [pygame.image.load(os.path.join(path_boy_player_animations, "r1.png")),
                    pygame.image.load(os.path.join(path_boy_player_animations, "r2.png")),
                    pygame.image.load(os.path.join(path_boy_player_animations, "r3.png")),
                    pygame.image.load(os.path.join(path_boy_player_animations, "r4.png"))]
    player_left = [pygame.image.load(os.path.join(path_boy_player_animations, "l1.png")),
                   pygame.image.load(os.path.join(path_boy_player_animations, "l2.png")),
                   pygame.image.load(os.path.join(path_boy_player_animations, "l3.png")),
                   pygame.image.load(os.path.join(path_boy_player_animations, "l4.png"))]
    player_up = [pygame.image.load(os.path.join(path_boy_player_animations, "u1.png")),
                 pygame.image.load(os.path.join(path_boy_player_animations, "u2.png")),
                 pygame.image.load(os.path.join(path_boy_player_animations, "u3.png")),
                 pygame.image.load(os.path.join(path_boy_player_animations, "u4.png"))]
    player_down = [pygame.image.load(os.path.join(path_boy_player_animations, "d1.png")),
                   pygame.image.load(os.path.join(path_boy_player_animations, "d2.png")),
                   pygame.image.load(os.path.join(path_boy_player_animations, "d3.png")),
                   pygame.image.load(os.path.join(path_boy_player_animations, "d4.png"))]
    player_stand = [pygame.image.load(os.path.join(path_boy_player_animations, "d1.png"))]

    pygame.display.update()
    if window_state == "game":
        if steps + 1 >= 12:
            steps = 0
        if left:
            player.graphics = player_left[steps // 3]
            steps = steps + 1
        elif right:
            player.graphics = player_right[steps // 3]
            steps = steps + 1
        elif up:
            player.graphics = player_up[steps // 3]
            steps = steps + 1
        elif down:
            player.graphics = player_down[steps // 3]
            steps = steps + 1
    return steps



def game(player, screen, path_NPC, path_audio, path_moves_animation, path_items, path_pokemons, path_exp_bar,
         path_hp_bar, path_structures, path_moves_animations, path_boy_player_animations, path_visual_elements):

    up = False
    down = False
    right = False
    left = False
    steps = 0
    window_state = "menu"

    clock = pygame.time.Clock()
    pokemonCounter = 0
    dy = 0
    dx = 0
    pokemon_exist = False
    cursor = MenuCursor(path_visual_elements)
    menu = EnterMenu(path_visual_elements)
    cursor_menu = MenuCursor(path_visual_elements)
    cursor_menu.x = 30
    cursor_menu.y = 30
    inv = Inventory(path_visual_elements)
    bag = Backpack(path_visual_elements)
    cursor_bag = MenuCursor(path_visual_elements)
    cursor_bag.x = 247
    cursor_bag.y = 53
    cursor_bag_items = MenuCursor(path_visual_elements)
    cursor_bag_items.x = 478
    cursor_bag_items.y = 279
    cursor_bag_pokeballs = MenuCursor(path_visual_elements)
    cursor_bag_pokeballs.x = 478
    cursor_bag_pokeballs.y = 319
    cursor_toss_bag_items = MenuCursor(path_visual_elements)
    cursor_toss_bag_items.x = 478
    cursor_toss_bag_items.y = 359
    cursor_toss_bag_pokeballs = MenuCursor(path_visual_elements)
    cursor_toss_bag_pokeballs.x = 478
    cursor_toss_bag_pokeballs.y = 359
    cursor_switch_items = MenuCursor(path_visual_elements)
    cursor_switch_items.x = 423
    cursor_switch_items.y = 236
    cursor_bag_key_items = MenuCursor(path_visual_elements)
    cursor_bag_key_items.x = 478
    cursor_bag_key_items.y = 319
    pokemon_item_cursor = MenuCursor(path_visual_elements)
    pokemon_item_cursor.x = 510
    pokemon_item_cursor.y = 319
    pokemon_selection_menu = PokemonMenu(path_visual_elements)
    selection = PokemonMenuMain(path_visual_elements)
    pokemon_menu_d1 = PokemonMenuCancel(path_visual_elements)
    pkm_menu_cursor = PokemonMenuCursor(path_visual_elements)
    use_bag_items_cursor = PokemonMenuCursor(path_visual_elements)
    give_items_cursor = PokemonMenuCursor(path_visual_elements)
    pkm_menu_1 = PokemonMenuMain2(path_visual_elements)
    pkm_menu_2 = PokemonMenuMain2(path_visual_elements)
    pkm_menu_3 = PokemonMenuMain2(path_visual_elements)
    pkm_menu_4 = PokemonMenuMain2(path_visual_elements)
    pkm_menu_5 = PokemonMenuMain2(path_visual_elements)
    selected_pkm_cursor_1 = SelectedPokemonCursor(path_visual_elements)
    player_card_1 = TrainerCard(path_visual_elements)
    player_card_2 = TrainerCard(path_visual_elements)
    player_card_2.graphics = pygame.image.load(os.path.join(path_visual_elements, "trainer_card_2.png"))
    badge_1 = Badge(1, path_items)
    badge_2 = Badge(2, path_items)
    badge_3 = Badge(3, path_items)
    badge_4 = Badge(4, path_items)
    badge_5 = Badge(5, path_items)
    badge_6 = Badge(6, path_items)
    badge_7 = Badge(7, path_items)
    badge_8 = Badge(8, path_items)
    badge_counter = 0
    pkm_summary = PokemonSummary(path_visual_elements)
    moves_cursor = MoveCursor(path_visual_elements)
    moves_learn_cursor = MoveCursor(path_visual_elements)
    b_info = BattleInfo(path_visual_elements)
    battle_menu_1 = BattleMenu(1, path_visual_elements)
    battle_menu_2 = BattleMenu(2, path_visual_elements)
    b_cursor = BattleCursor(path_visual_elements)
    animation_counter = 20
    animation_counter2 = 20
    NPC_nurse = NurseNPC(50, 50, path_NPC)
    NPC_seller = SellerNPC(100, 50, path_NPC)
    level_up_menu = LevelUpInfo(path_visual_elements)
    o1 = Options1(path_visual_elements)
    o2 = Options2(path_visual_elements)
    o3 = Options3(path_visual_elements)
    o_cursor = OptionCursor(path_visual_elements)
    pkm_caught = PokemonCaught(path_boy_player_animations)
    pkm_uncaught = PokemonUncaught(path_boy_player_animations)
    change_skill_bg = ChangeSkillBackground(path_visual_elements)
    change_skill_m = ChangeSkillMenu(path_visual_elements)
    change_skill_c = ChangeSkillCursor(path_visual_elements)
    change_skill_c_2 = ChangeSkillCursor(path_visual_elements)
    selected_item_m1 = SelectedItemMenu(1, path_visual_elements)
    selected_item_m2 = SelectedItemMenu(2, path_visual_elements)
    selected_item_m3 = SelectedItemMenu(3, path_visual_elements)
    selected_item_m4 = SelectedItemMenu(4, path_visual_elements)
    pkm_item_menu = PokemonItemMenu(path_visual_elements)
    c_use_item = CannotUseItem(path_visual_elements)
    toss_times = 1
    cursor_up = CursorUpDown("up", path_visual_elements)
    cursor_up.x = 520
    cursor_up.y = 340
    cursor_down = CursorUpDown("down", path_visual_elements)
    cursor_down.x = 520
    cursor_down.y = 414
    cursor_up_dex = CursorUpDown("up", path_visual_elements)
    cursor_up_dex.x = 492
    cursor_up_dex.y = 66
    cursor_down_dex = CursorUpDown("down", path_visual_elements)
    cursor_down_dex.x = 492
    cursor_down_dex.y = 386
    toss_number = 1
    held_item_icon = HeldItemIcon(path_visual_elements)
    effect_screen = EffectMenu(path_visual_elements)
    battle_pokemon_list = []
    giving_item = "False"
    world_map = MapItem(path_visual_elements)
    m_cursor = MapCursor(path_visual_elements)
    Map_dy = 0
    Map_dx = 0
    map_c = 1
    register_item = RegisterItem(path_visual_elements)
    back_register = "none"
    pkd_table = PokedexTable(path_visual_elements)
    pokedex_table_c = PokedexTableCursor(path_visual_elements)
    pokedex_table_c2 = PokedexTableCursor(path_visual_elements)
    pokedex_table_c2.x = 54
    pokedex_table_c2.y = 85
    pokedex_icon = PokedexIcon(path_visual_elements)
    pallet_town = PalletTown(path_structures)

    while True:
        clock.tick(20)  # set FPS (default: 20)
        time = datetime.now().time()
        time = time.strftime("%H:%M:%S")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_UP:
                    if window_state == "game":
                        dy = -5
                        up = True
                        down = False
                    elif window_state == "encounter":
                        if cursor.y == 408:
                            cursor.y = 356
                        elif cursor.y == 356:
                            cursor.y = 356

                    elif window_state == "enter_menu":
                        if cursor_menu.y == 30:
                            cursor_menu.y = 30
                        else:
                            cursor_menu.y = cursor_menu.y - 40

                    elif window_state == "bag_items" or window_state == "bag_key_items" or window_state == "bag_pokeballs":
                        if cursor_bag.y != 53:
                            cursor_bag.y = cursor_bag.y - 45

                    elif window_state == "pokemon_menu" or window_state == "switch_pokemon":
                        if pkm_menu_cursor.y != 67 and pkm_menu_cursor.x == 245:
                            pkm_menu_cursor.y = pkm_menu_cursor.y - 66
                        elif pkm_menu_cursor.y == 67 and pkm_menu_cursor.x == 245:
                            pkm_menu_cursor.y = 67
                        elif pkm_menu_cursor.y == 401 and pkm_menu_cursor.x == 482:
                            pkm_menu_cursor.y = 331
                            pkm_menu_cursor.x = 245

                    elif window_state == "use_bag_items":
                        if use_bag_items_cursor.y != 67 and use_bag_items_cursor.x == 245:
                            use_bag_items_cursor.y = use_bag_items_cursor.y - 66
                        elif use_bag_items_cursor.y == 67 and use_bag_items_cursor.x == 245:
                            use_bag_items_cursor.y = 67
                        elif use_bag_items_cursor.y == 401 and use_bag_items_cursor.x == 482:
                            use_bag_items_cursor.y = 331
                            use_bag_items_cursor.x = 245

                    elif window_state == "give_items":
                        if give_items_cursor.y != 67 and give_items_cursor.x == 245:
                            give_items_cursor.y = give_items_cursor.y - 66
                        elif give_items_cursor.y == 67 and give_items_cursor.x == 245:
                            give_items_cursor.y = 67
                        elif give_items_cursor.y == 401 and give_items_cursor.x == 482:
                            give_items_cursor.y = 331
                            give_items_cursor.x = 245

                    elif window_state == "selected_pokemon":
                        if selected_pkm_cursor_1.y != 280:
                            selected_pkm_cursor_1.y = selected_pkm_cursor_1.y - 41
                        elif selected_pkm_cursor_1.y == 280:
                            selected_pkm_cursor_1.y = 280

                    elif window_state == "pokemon_summary_moves_2":
                        if moves_cursor.y != 75:
                            moves_cursor.y = moves_cursor.y - 74
                        elif moves_cursor.y == 75:
                            moves_cursor.y = 75

                    elif window_state == "attack_learning_2_4":
                        if moves_learn_cursor.y != 75:
                            moves_learn_cursor.y = moves_learn_cursor.y - 74
                        elif moves_learn_cursor.y == 75:
                            moves_learn_cursor.y = 75

                    elif window_state == "battle":
                        if b_cursor.y == 357:
                            b_cursor.y = 357
                        else:
                            b_cursor.y = 357

                    elif window_state == "option":
                        if o_cursor.y == 196:
                            o_cursor.y = 196
                        else:
                            o_cursor.y = o_cursor.y - 34

                    elif window_state == "attack_learning_2_3":
                        if change_skill_c.y != 240:
                            change_skill_c.y = change_skill_c.y - 40
                        else:
                            change_skill_c.y = 240

                    elif window_state == "stop_attack_learning":
                        if change_skill_c_2.y != 240:
                            change_skill_c_2.y = change_skill_c_2.y - 40
                        else:
                            change_skill_c_2.y = 240

                    elif window_state == "selected_bag_items":
                        if cursor_bag_items.y != 279:
                            cursor_bag_items.y = cursor_bag_items.y - 40
                        else:
                            cursor_bag_items.y = 279

                    elif window_state == "selected_bag_key_items":
                        if cursor_bag_key_items.y != 319:
                            cursor_bag_key_items.y = cursor_bag_key_items.y - 40
                        else:
                            cursor_bag_key_items.y = 319

                    elif window_state == "pokemon_item":
                        if pokemon_item_cursor.y != 319:
                            pokemon_item_cursor.y = pokemon_item_cursor.y - 40
                        else:
                            pokemon_item_cursor.y = 319

                    elif window_state == "selected_bag_pokeballs":
                        if cursor_bag_pokeballs.y != 319:
                            cursor_bag_pokeballs.y = cursor_bag_pokeballs.y - 40
                        else:
                            cursor_bag_pokeballs.y = 319

                    elif window_state == "toss_bag_items_1":
                        if cursor_toss_bag_items.y != 359:
                            cursor_toss_bag_items.y = 359
                        else:
                            cursor_toss_bag_items.y = 359

                    elif window_state == "toss_bag_pokeballs_1":
                        if cursor_toss_bag_pokeballs.y != 359:
                            cursor_toss_bag_pokeballs.y = 359
                        else:
                            cursor_toss_bag_pokeballs.y = 359

                    elif window_state == "give_items4":
                        if cursor_switch_items.y != 236:
                            cursor_switch_items.y = 236
                        else:
                            cursor_switch_items.y = 236

                    elif window_state == "toss_bag_items_2":
                        if toss_number < selected_item.quantity:
                            toss_number = toss_number + 1
                        elif toss_number == selected_item.quantity:
                            toss_number = 1

                    elif window_state == "toss_bag_pokeballs_2":
                        if toss_number < selected_item.quantity:
                            toss_number = toss_number + 1
                        elif toss_number == selected_item.quantity:
                            toss_number = 1

                    elif window_state == "use_bag_key_items" and selected_item.name == "Town Map":
                        Map_dy = -12

                    elif window_state == "pokedex_table":
                        if pokedex_table_c.y == 125:
                            pokedex_table_c.y = 125
                        elif pokedex_table_c.y > 195:
                            pokedex_table_c.y = pokedex_table_c.y - 37
                        elif pokedex_table_c.y == 195:
                            pokedex_table_c.y = 125

                    elif window_state == "pokedex_table2":
                        if pokedex_table_c2.y == 378:
                            pokedex_table_c2.y = 336
                        elif pokedex_table_c2.y <= 336 and pokedex_table_c2.y != 225 and pokedex_table_c2.y != 85:
                            pokedex_table_c2.y = pokedex_table_c2.y - 37
                        elif pokedex_table_c2.y == 225:
                            pokedex_table_c2.y = 159
                        elif pokedex_table_c2.y == 85:
                            window_state = "pokedex_table"

                    pygame.display.update()

                elif event.key == pygame.K_DOWN:
                    if window_state == "game":
                        dy = 5
                        up = False
                        down = True
                    elif window_state == "encounter":
                        if cursor.y == 356:
                            cursor.y = 408
                        elif cursor.y == 408:
                            cursor.y = 408

                    elif window_state == "enter_menu":
                        if cursor_menu.y == 270:
                            cursor_menu.y = 270
                        else:
                            cursor_menu.y = cursor_menu.y + 40

                    elif window_state == "bag_items" or window_state == "bag_key_items" or window_state == "bag_pokeballs":
                        if cursor_bag.y != 233:
                            cursor_bag.y = cursor_bag.y + 45

                    elif window_state == "pokemon_menu" or window_state == "switch_pokemon":
                        if pkm_menu_cursor.y != 331 and pkm_menu_cursor.x == 245:
                            pkm_menu_cursor.y = pkm_menu_cursor.y + 66
                        elif pkm_menu_cursor.y == 331 and pkm_menu_cursor.x == 245:
                            pkm_menu_cursor.y = 401
                            pkm_menu_cursor.x = 482

                    elif window_state == "use_bag_items":
                        if use_bag_items_cursor.y != 331 and use_bag_items_cursor.x == 245:
                            use_bag_items_cursor.y = use_bag_items_cursor.y + 66
                        elif use_bag_items_cursor.y == 331 and use_bag_items_cursor.x == 245:
                            use_bag_items_cursor.y = 401
                            use_bag_items_cursor.x = 482

                    elif window_state == "give_items":
                        if give_items_cursor.y != 331 and give_items_cursor.x == 245:
                            give_items_cursor.y = give_items_cursor.y + 66
                        elif give_items_cursor.y == 331 and give_items_cursor.x == 245:
                            give_items_cursor.y = 401
                            give_items_cursor.x = 482

                    elif window_state == "selected_pokemon":
                        if selected_pkm_cursor_1.y != 403:
                            selected_pkm_cursor_1.y = selected_pkm_cursor_1.y + 41
                        elif selected_pkm_cursor_1.y == 403:
                            selected_pkm_cursor_1.y = 403

                    elif window_state == "pokemon_summary_moves_2":
                        if moves_cursor.y != 297:
                            moves_cursor.y = moves_cursor.y + 74
                        elif moves_cursor.y == 297:
                            moves_cursor.y = 297

                    elif window_state == "attack_learning_2_4":
                        if moves_learn_cursor.y != 371:
                            moves_learn_cursor.y = moves_learn_cursor.y + 74
                        elif moves_learn_cursor.y == 371:
                            moves_learn_cursor.y = 371

                    elif window_state == "battle":
                        if b_cursor.y == 405:
                            b_cursor.y = 405
                        else:
                            b_cursor.y = 405

                    elif window_state == "option":
                        if o_cursor.y == 400:
                            o_cursor.y = 400
                        else:
                            o_cursor.y = o_cursor.y + 34

                    elif window_state == "attack_learning_2_3":
                        if change_skill_c.y == 240:
                            change_skill_c.y = change_skill_c.y + 40
                        else:
                            change_skill_c.y = 280

                    elif window_state == "stop_attack_learning":
                        if change_skill_c_2.y == 240:
                            change_skill_c_2.y = change_skill_c_2.y + 40
                        else:
                            change_skill_c_2.y = 280

                    elif window_state == "selected_bag_items":
                        if cursor_bag_items.y != 399:
                            cursor_bag_items.y = cursor_bag_items.y + 40
                        else:
                            cursor_bag_items.y = 399

                    elif window_state == "selected_bag_key_items":
                        if cursor_bag_key_items.y != 399:
                            cursor_bag_key_items.y = cursor_bag_key_items.y + 40
                        else:
                            cursor_bag_key_items.y = 399

                    elif window_state == "pokemon_item":
                        if pokemon_item_cursor.y != 399:
                            pokemon_item_cursor.y = pokemon_item_cursor.y + 40
                        else:
                            pokemon_item_cursor.y = 399

                    elif window_state == "selected_bag_pokeballs":
                        if cursor_bag_pokeballs.y != 399:
                            cursor_bag_pokeballs.y = cursor_bag_pokeballs.y + 40
                        else:
                            cursor_bag_pokeballs.y = 399

                    elif window_state == "toss_bag_items_1":
                        if cursor_toss_bag_items.y != 399:
                            cursor_toss_bag_items.y = 399
                        else:
                            cursor_toss_bag_items.y = 399

                    elif window_state == "toss_bag_pokeballs_1":
                        if cursor_toss_bag_pokeballs.y != 399:
                            cursor_toss_bag_pokeballs.y = 399
                        else:
                            cursor_toss_bag_pokeballs.y = 399

                    elif window_state == "give_items4":
                        if cursor_switch_items.y != 270:
                            cursor_switch_items.y = 270
                        else:
                            cursor_switch_items.y = 270

                    elif window_state == "toss_bag_items_2":
                        if toss_number != 1:
                            toss_number = toss_number - 1
                        elif toss_number == 1:
                            toss_number = selected_item.quantity

                    elif window_state == "toss_bag_pokeballs_2":
                        if toss_number != 1:
                            toss_number = toss_number - 1
                        elif toss_number == 1:
                            toss_number = selected_item.quantity

                    elif window_state == "use_bag_key_items" and selected_item.name == "Town Map":
                        Map_dy = 12

                    elif window_state == "pokedex_table":
                        if pokedex_table_c.y == 125:
                            pokedex_table_c.y = pokedex_table_c.y + 70
                        elif pokedex_table_c.y > 125 and pokedex_table_c.y < 380:
                            pokedex_table_c.y = pokedex_table_c.y + 37
                        elif pokedex_table_c.y == 380:
                            window_state = "pokedex_table2"

                    elif window_state == "pokedex_table2":
                        if pokedex_table_c2.y < 380 and pokedex_table_c2.y != 159 and \
                                pokedex_table_c2.y != 336 and pokedex_table_c2.y != 378:
                            pokedex_table_c2.y = pokedex_table_c2.y + 37
                        elif pokedex_table_c2.y == 159:
                            pokedex_table_c2.y = pokedex_table_c2.y + 66
                        elif pokedex_table_c2.y == 336:
                            pokedex_table_c2.y = pokedex_table_c2.y + 42
                        elif pokedex_table_c2.y == 378:
                            pokedex_table_c2.y = 378
                    pygame.display.update()

                elif event.key == pygame.K_LEFT:
                    if window_state == "game":
                        dx = -5
                        left = True
                        right = False
                    elif window_state == "encounter":
                        if cursor.x == 385:
                            cursor.x = 385
                        elif cursor.x == 540:
                            cursor.x = 385

                    elif window_state == "bag_key_items" and window_state != "bag_items":
                        window_state = "bag_items"

                    elif window_state == "bag_pokeballs" and window_state != "bag_key_items":
                        window_state = "bag_key_items"

                    elif window_state == "pokemon_menu" or window_state == "switch_pokemon":
                        if pkm_menu_cursor.x != 8 and pkm_menu_cursor.y != 150:
                            pkm_menu_cursor.x = 8
                            pkm_menu_cursor.y = 150

                    elif window_state == "use_bag_items":
                        if use_bag_items_cursor.x != 8 and use_bag_items_cursor.y != 150:
                            use_bag_items_cursor.x = 8
                            use_bag_items_cursor.y = 150

                    elif window_state == "give_items":
                        if give_items_cursor.x != 8 and give_items_cursor.y != 150:
                            give_items_cursor.x = 8
                            give_items_cursor.y = 150

                    elif window_state == "pokemon_summary_skills":
                        window_state = "pokemon_summary_info"
                    elif window_state == "pokemon_summary_moves":
                        window_state = "pokemon_summary_skills"

                    elif window_state == "battle":
                        if b_cursor.x == 36:
                            b_cursor.x = 36
                        else:
                            b_cursor.x = 36

                    elif window_state == "use_bag_key_items" and selected_item.name == "Town Map":
                        Map_dx = -14

                    pygame.display.update()

                elif event.key == pygame.K_RIGHT:
                    if window_state == "game":
                        dx = 5
                        right = True
                        left = False
                    elif window_state == "encounter":
                        if cursor.x == 540:
                            cursor.x = 540
                        elif cursor.x == 385:
                            cursor.x = 540

                    elif window_state == "bag_items" and window_state != "bag_key_items":
                        window_state = "bag_key_items"

                    elif window_state == "bag_key_items" and window_state != "bag_pokeballs":
                        window_state = "bag_pokeballs"

                    elif window_state == "pokemon_menu" or window_state == "switch_pokemon":
                        if pkm_menu_cursor.x == 8 and pkm_menu_cursor.y == 150:
                            pkm_menu_cursor.x = 245
                            pkm_menu_cursor.y = 67

                    elif window_state == "use_bag_items":
                        if use_bag_items_cursor.x == 8 and use_bag_items_cursor.y == 150:
                            use_bag_items_cursor.x = 245
                            use_bag_items_cursor.y = 67

                    elif window_state == "give_items":
                        if give_items_cursor.x == 8 and give_items_cursor.y == 150:
                            give_items_cursor.x = 245
                            give_items_cursor.y = 67

                    elif window_state == "pokemon_summary_info":
                        window_state = "pokemon_summary_skills"
                    elif window_state == "pokemon_summary_skills":
                        window_state = "pokemon_summary_moves"

                    elif window_state == "battle":
                        if b_cursor.x == 222:
                            b_cursor.x = 222
                        else:
                            b_cursor.x = 222

                    elif window_state == "use_bag_key_items" and selected_item.name == "Town Map":
                        Map_dx = 14

                    pygame.display.update()

                elif event.key == pygame.K_SPACE:
                    if window_state == "menu":
                        item = Items("Pokeball", path_items)
                        item.quantity = 10
                        player.pokeballs.append(item)
                        item = Items("Greatball", path_items)
                        item.quantity = 5
                        player.pokeballs.append(item)
                        item = Items("Ultraball", path_items)
                        item.quantity = 1
                        player.pokeballs.append(item)
                        item = Items("Potion", path_items)
                        item.quantity = 4
                        player.items.append(item)
                        item = Items("Super Potion", path_items)
                        item.quantity = 3
                        player.items.append(item)
                        item = Items("Hyper Potion", path_items)
                        item.quantity = 2
                        player.items.append(item)
                        item = Items("Max Potion", path_items)
                        item.quantity = 1
                        player.items.append(item)
                        item = Items("Town Map", path_items)
                        item.quantity = 1
                        player.key_items.append(item)

                        pokemon = Pokemon(1, path_pokemons, path_audio, path_moves_animations, path_exp_bar,
                                          path_hp_bar)
                        leveling_pokemon = pokemon
                        leveling_pokemon.level = 5
                        leveling_pokemon.hp, leveling_pokemon.current_hp, leveling_pokemon.attack, leveling_pokemon.current_attack, leveling_pokemon.defense, leveling_pokemon.current_defense, leveling_pokemon.sp_atk, leveling_pokemon.current_sp_atk, leveling_pokemon.sp_def, leveling_pokemon.current_sp_def, leveling_pokemon.speed, leveling_pokemon.current_speed = level_up(
                            leveling_pokemon.level, leveling_pokemon.base_hp, leveling_pokemon.IV_hp,
                            leveling_pokemon.EV_hp, leveling_pokemon.base_attack, leveling_pokemon.IV_attack,
                            leveling_pokemon.EV_attack, leveling_pokemon.base_defense, leveling_pokemon.IV_defense,
                            leveling_pokemon.EV_defense, leveling_pokemon.base_sp_atk, leveling_pokemon.IV_sp_atk,
                            leveling_pokemon.EV_sp_atk, leveling_pokemon.base_sp_def, leveling_pokemon.IV_sp_def,
                            leveling_pokemon.EV_sp_def, leveling_pokemon.base_speed, leveling_pokemon.IV_speed,
                            leveling_pokemon.EV_speed)
                        leveling_pokemon.total_exp, leveling_pokemon.next_level, leveling_pokemon.to_next_level = leveling(
                            leveling_pokemon.level)
                        leveling_pokemon.exp = 0
                        leveling_pokemon.to_next_level_exp = leveling_pokemon.to_next_level - leveling_pokemon.exp
                        leveling_pokemon.exp_bar_graphics = exp_bar_status(leveling_pokemon.exp,
                                                                           leveling_pokemon.to_next_level, path_exp_bar)
                        player.main_pokemon.append(pokemon)
                        pokemon = Pokemon(2, path_pokemons, path_audio, path_moves_animations, path_exp_bar,
                                          path_hp_bar)
                        player.pokemons.append(pokemon)
                        pokemon = Pokemon(3, path_pokemons, path_audio, path_moves_animations, path_exp_bar,
                                          path_hp_bar)
                        player.pokemons.append(pokemon)
                        pokemon = Pokemon(2, path_pokemons, path_audio, path_moves_animations, path_exp_bar,
                                          path_hp_bar)
                        player.pokemons.append(pokemon)
                        pokemon = Pokemon(1, path_pokemons, path_audio, path_moves_animations, path_exp_bar,
                                          path_hp_bar)
                        player.pokemons.append(pokemon)
                        pokemon = Pokemon(4, path_pokemons, path_audio, path_moves_animations, path_exp_bar,
                                          path_hp_bar)
                        player.pokemons.append(pokemon)

                        player.badges.append(badge_1)
                        player.badges.append(badge_2)
                        player.badges.append(badge_3)
                        player.badges.append(badge_4)
                        player.badges.append(badge_5)
                        player.badges.append(badge_6)
                        player.badges.append(badge_7)
                        player.badges.append(badge_8)
                        dy = 0
                        dx = 0
                        window_state = "game"
                        pygame.mixer.music.load(os.path.join(path_audio, 'road.wav'))
                        pygame.mixer.music.play(-1)

                elif event.key == pygame.K_z:
                    if pokemon_exist and window_state == "encounter":
                        if cursor.x == 540 and cursor.y == 408:
                            window_state = "game"
                            pygame.mixer.music.load(os.path.join(path_audio, 'road.wav'))
                            pygame.mixer.music.play(-1)
                            run_effect = pygame.mixer.Sound(os.path.join(path_audio, 'run_sound.wav'))
                            run_effect.play()
                            up = False
                            down = False
                            right = False
                            left = False
                            steps = 0
                            dx = 0
                            dy = 0
                            pokemon_exist = False

                        elif cursor.x == 540 and cursor.y == 356:
                            window_state = "bag_items"

                        elif cursor.x == 385 and cursor.y == 408:
                            window_state = "pokemon_menu"

                        elif cursor.x == 385 and cursor.y == 356:
                            window_state = "battle"

                    elif pokemon_exist and window_state == "bag_pokeballs":
                        if cursor_bag.y == 53 and player.pokeballs[0].quantity != 0:
                            player.pokeballs[0].quantity = (player.pokeballs[0].quantity - 1)
                            pokemon_catching_counter = 0
                            pokemon_catching_animation = 0

                            M = random.randint(0, 255)
                            f = round((pokemon.hp * 255 * 4) / (pokemon.current_hp * 12))
                            if f >= M:
                                window_state = "pokemon_catching"
                            else:
                                window_state = "pokemon_uncatching"

                        if cursor_bag.y == 98 and player.pokeballs[1].quantity != 0:
                            player.pokeballs[1].quantity = (player.pokeballs[1].quantity - 1)
                            pokemon_catching_counter = 0
                            pokemon_catching_animation = 0

                            M = random.randint(0, 255)
                            f = round((pokemon.hp * 255 * 4) / (pokemon.current_hp * 12))
                            if f >= M:
                                window_state = "pokemon_catching"
                            else:
                                window_state = "pokemon_uncatching"

                        if cursor_bag.y == 143 and player.pokeballs[2].quantity != 0:
                            player.pokeballs[2].quantity = (player.pokeballs[2].quantity - 1)
                            pokemon_catching_counter = 0
                            pokemon_catching_animation = 0
                            M = random.randint(0, 255)
                            f = round((pokemon.hp * 255 * 4) / (pokemon.current_hp * 12))

                            if f >= M:
                                window_state = "pokemon_catching"
                            else:
                                window_state = "pokemon_uncatching"

                    elif window_state == "enter_menu":
                        if cursor_menu.y == 270:
                            window_state = "game"
                        elif cursor_menu.y == 30:
                            window_state = "pokedex_table"
                        elif cursor_menu.y == 110:
                            window_state = "bag_items"
                        elif cursor_menu.y == 70:
                            window_state = "pokemon_menu"
                        elif cursor_menu.y == 150:
                            window_state = "player_card_1"
                        elif cursor_menu.y == 230:
                            window_state = "option"

                    elif window_state == "player_card_1":
                        window_state = "player_card_2"

                    elif window_state == "player_card_2":
                        window_state = "player_card_1"

                    elif window_state == "pokemon_menu":
                        if pkm_menu_cursor.y == 401 and pkm_menu_cursor.x == 482:
                            window_state = "game"
                        if pkm_menu_cursor.x == 8 and pkm_menu_cursor.y == 150:
                            window_state = "selected_pokemon"
                            selected_pkm = player.main_pokemon[0]
                        elif pkm_menu_cursor.x == 245 and pkm_menu_cursor.y == 67 and len(player.pokemons) > 0:
                            window_state = "selected_pokemon"
                            selected_pkm = player.pokemons[0]
                        elif pkm_menu_cursor.x == 245 and pkm_menu_cursor.y == 133 and len(player.pokemons) > 1:
                            window_state = "selected_pokemon"
                            selected_pkm = player.pokemons[1]
                        elif pkm_menu_cursor.x == 245 and pkm_menu_cursor.y == 199 and len(player.pokemons) > 2:
                            window_state = "selected_pokemon"
                            selected_pkm = player.pokemons[2]
                        elif pkm_menu_cursor.x == 245 and pkm_menu_cursor.y == 265 and len(player.pokemons) > 3:
                            window_state = "selected_pokemon"
                            selected_pkm = player.pokemons[3]
                        elif pkm_menu_cursor.x == 245 and pkm_menu_cursor.y == 331 and len(player.pokemons) > 4:
                            window_state = "selected_pokemon"
                            selected_pkm = player.pokemons[4]

                    elif window_state == "use_bag_items":
                        if use_bag_items_cursor.y == 401 and use_bag_items_cursor.x == 482:
                            window_state = "game"
                        if use_bag_items_cursor.x == 8 and use_bag_items_cursor.y == 150:
                            selected_pkm = player.main_pokemon[0]
                            if selected_item.name == "Potion" or selected_item.name == "Super Potion" or selected_item.name == "Hyper Potion" or selected_item.name == "Max Potion":
                                if selected_pkm.current_hp != selected_pkm.hp:
                                    selected_pkm.current_hp = selected_pkm.current_hp + selected_item.power
                                    revive_effect = pygame.mixer.Sound(os.path.join(path_audio, 'revive_sound.wav'))
                                    revive_effect.play()
                                    selected_item.quantity = selected_item.quantity - 1
                                    if selected_pkm.current_hp > selected_pkm.hp:
                                        selected_pkm.current_hp = selected_pkm.hp
                                    selected_pkm.hp_bar_graphics = health_bar_status(selected_pkm.current_hp,
                                                                                     selected_pkm.hp, path_hp_bar)
                                    window_state = "bag_items"
                                elif selected_pkm.current_hp == selected_pkm.hp:
                                    window_state = "cannot_use_items"
                        elif use_bag_items_cursor.x == 245 and use_bag_items_cursor.y == 67 and len(
                                player.pokemons) > 0:
                            selected_pkm = player.pokemons[0]
                            if selected_item.name == "Potion" or selected_item.name == "Super Potion" or selected_item.name == "Hyper Potion" or selected_item.name == "Max Potion":
                                if selected_pkm.current_hp != selected_pkm.hp:
                                    selected_pkm.current_hp = selected_pkm.current_hp + selected_item.power
                                    revive_effect = pygame.mixer.Sound(os.path.join(path_audio, 'revive_sound.wav'))
                                    revive_effect.play()
                                    selected_item.quantity = selected_item.quantity - 1
                                    if selected_pkm.current_hp > selected_pkm.hp:
                                        selected_pkm.current_hp = selected_pkm.hp
                                    selected_pkm.hp_bar_graphics = health_bar_status(selected_pkm.current_hp,
                                                                                     selected_pkm.hp, path_hp_bar)
                                    window_state = "bag_items"
                                elif selected_pkm.current_hp == selected_pkm.hp:
                                    window_state = "cannot_use_items"
                        elif use_bag_items_cursor.x == 245 and use_bag_items_cursor.y == 133 and len(
                                player.pokemons) > 1:
                            selected_pkm = player.pokemons[1]
                            if selected_item.name == "Potion" or selected_item.name == "Super Potion" or selected_item.name == "Hyper Potion" or selected_item.name == "Max Potion":
                                if selected_pkm.current_hp != selected_pkm.hp:
                                    selected_pkm.current_hp = selected_pkm.current_hp + selected_item.power
                                    revive_effect = pygame.mixer.Sound(os.path.join(path_audio, 'revive_sound.wav'))
                                    revive_effect.play()
                                    selected_item.quantity = selected_item.quantity - 1
                                    if selected_pkm.current_hp > selected_pkm.hp:
                                        selected_pkm.current_hp = selected_pkm.hp
                                    selected_pkm.hp_bar_graphics = health_bar_status(selected_pkm.current_hp,
                                                                                     selected_pkm.hp, path_hp_bar)
                                    window_state = "bag_items"
                                elif selected_pkm.current_hp == selected_pkm.hp:
                                    window_state = "cannot_use_items"
                        elif use_bag_items_cursor.x == 245 and use_bag_items_cursor.y == 199 and len(
                                player.pokemons) > 2:
                            selected_pkm = player.pokemons[2]
                            if selected_item.name == "Potion" or selected_item.name == "Super Potion" or selected_item.name == "Hyper Potion" or selected_item.name == "Max Potion":
                                if selected_pkm.current_hp != selected_pkm.hp:
                                    selected_pkm.current_hp = selected_pkm.current_hp + selected_item.power
                                    revive_effect = pygame.mixer.Sound(os.path.join(path_audio, 'revive_sound.wav'))
                                    revive_effect.play()
                                    selected_item.quantity = selected_item.quantity - 1
                                    if selected_pkm.current_hp > selected_pkm.hp:
                                        selected_pkm.current_hp = selected_pkm.hp
                                    selected_pkm.hp_bar_graphics = health_bar_status(selected_pkm.current_hp,
                                                                                     selected_pkm.hp, path_hp_bar)
                                    window_state = "bag_items"
                                elif selected_pkm.current_hp == selected_pkm.hp:
                                    window_state = "cannot_use_items"
                        elif use_bag_items_cursor.x == 245 and use_bag_items_cursor.y == 265 and len(
                                player.pokemons) > 3:
                            selected_pkm = player.pokemons[3]
                            if selected_item.name == "Potion" or selected_item.name == "Super Potion" or selected_item.name == "Hyper Potion" or selected_item.name == "Max Potion":
                                if selected_pkm.current_hp != selected_pkm.hp:
                                    selected_pkm.current_hp = selected_pkm.current_hp + selected_item.power
                                    revive_effect = pygame.mixer.Sound(os.path.join(path_audio, 'revive_sound.wav'))
                                    revive_effect.play()
                                    selected_item.quantity = selected_item.quantity - 1
                                    if selected_pkm.current_hp > selected_pkm.hp:
                                        selected_pkm.current_hp = selected_pkm.hp
                                    selected_pkm.hp_bar_graphics = health_bar_status(selected_pkm.current_hp,
                                                                                     selected_pkm.hp, path_hp_bar)
                                    window_state = "bag_items"
                                elif selected_pkm.current_hp == selected_pkm.hp:
                                    window_state = "cannot_use_items"
                        elif use_bag_items_cursor.x == 245 and use_bag_items_cursor.y == 331 and len(
                                player.pokemons) > 4:
                            selected_pkm = player.pokemons[4]
                            if selected_item.name == "Potion" or selected_item.name == "Super Potion" or selected_item.name == "Hyper Potion" or selected_item.name == "Max Potion":
                                if selected_pkm.current_hp != selected_pkm.hp:
                                    selected_pkm.current_hp = selected_pkm.current_hp + selected_item.power
                                    revive_effect = pygame.mixer.Sound(os.path.join(path_audio, 'revive_sound.wav'))
                                    revive_effect.play()
                                    selected_item.quantity = selected_item.quantity - 1
                                    if selected_pkm.current_hp > selected_pkm.hp:
                                        selected_pkm.current_hp = selected_pkm.hp
                                    selected_pkm.hp_bar_graphics = health_bar_status(selected_pkm.current_hp,
                                                                                     selected_pkm.hp, path_hp_bar)
                                    window_state = "bag_items"
                                elif selected_pkm.current_hp == selected_pkm.hp:
                                    window_state = "cannot_use_items"

                    elif window_state == "give_items":
                        if give_items_cursor.y == 401 and give_items_cursor.x == 482:
                            window_state = "game"
                        if give_items_cursor.x == 8 and give_items_cursor.y == 150:
                            selected_pkm = player.main_pokemon[0]
                            if selected_pkm.holding_item == "none":
                                selected_pkm.holding_item = selected_item
                                selected_item.quantity = selected_item.quantity - 1
                                window_state = "give_items2"
                            else:
                                tmp_item = selected_pkm.holding_item
                                window_state = "give_items3"
                        elif give_items_cursor.x == 245 and give_items_cursor.y == 67 and len(player.pokemons) > 0:
                            selected_pkm = player.pokemons[0]
                            if selected_pkm.holding_item == "none":
                                selected_pkm.holding_item = selected_item
                                selected_item.quantity = selected_item.quantity - 1
                                window_state = "give_items2"
                            else:
                                tmp_item = selected_pkm.holding_item
                                window_state = "give_items3"
                        elif give_items_cursor.x == 245 and give_items_cursor.y == 133 and len(player.pokemons) > 1:
                            selected_pkm = player.pokemons[1]
                            if selected_pkm.holding_item == "none":
                                selected_pkm.holding_item = selected_item
                                selected_item.quantity = selected_item.quantity - 1
                                window_state = "give_items2"
                            else:
                                tmp_item = selected_pkm.holding_item
                                window_state = "give_items3"
                        elif give_items_cursor.x == 245 and give_items_cursor.y == 199 and len(player.pokemons) > 2:
                            selected_pkm = player.pokemons[2]
                            if selected_pkm.holding_item == "none":
                                selected_pkm.holding_item = selected_item
                                selected_item.quantity = selected_item.quantity - 1
                                window_state = "give_items2"
                            else:
                                tmp_item = selected_pkm.holding_item
                                window_state = "give_items3"
                        elif give_items_cursor.x == 245 and give_items_cursor.y == 265 and len(player.pokemons) > 3:
                            selected_pkm = player.pokemons[3]
                            if selected_pkm.holding_item == "none":
                                selected_pkm.holding_item = selected_item
                                selected_item.quantity = selected_item.quantity - 1
                                window_state = "give_items2"
                            else:
                                tmp_item = selected_pkm.holding_item
                                window_state = "give_items3"
                        elif give_items_cursor.x == 245 and give_items_cursor.y == 331 and len(player.pokemons) > 4:
                            selected_pkm = player.pokemons[4]
                            if selected_pkm.holding_item == "none":
                                selected_pkm.holding_item = selected_item
                                selected_item.quantity = selected_item.quantity - 1
                                window_state = "give_items2"
                            else:
                                tmp_item = selected_pkm.holding_item
                                window_state = "give_items3"

                    elif window_state == "switch_pokemon":
                        if pkm_menu_cursor.y == 401 and pkm_menu_cursor.x == 482:
                            window_state = "game"
                        if pkm_menu_cursor.x == 8 and pkm_menu_cursor.y == 150:
                            switch_pkm = player.main_pokemon[0]
                            if selected_pkm == player.main_pokemon[0]:
                                tmp_pkm = selected_pkm
                                player.main_pokemon[0] = switch_pkm
                                player.main_pokemon[0] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[0]:
                                tmp_pkm = selected_pkm
                                player.pokemons[0] = switch_pkm
                                player.main_pokemon[0] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[1]:
                                tmp_pkm = selected_pkm
                                player.pokemons[1] = switch_pkm
                                player.main_pokemon[0] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[2]:
                                tmp_pkm = selected_pkm
                                player.pokemons[2] = switch_pkm
                                player.main_pokemon[0] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[3]:
                                tmp_pkm = selected_pkm
                                player.pokemons[3] = switch_pkm
                                player.main_pokemon[0] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[4]:
                                tmp_pkm = selected_pkm
                                player.pokemons[4] = switch_pkm
                                player.main_pokemon[0] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                        elif pkm_menu_cursor.x == 245 and pkm_menu_cursor.y == 67 and len(player.pokemons) > 0:
                            switch_pkm = player.pokemons[0]
                            if selected_pkm == player.main_pokemon[0]:
                                tmp_pkm = selected_pkm
                                player.main_pokemon[0] = switch_pkm
                                player.pokemons[0] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[0]:
                                tmp_pkm = selected_pkm
                                player.pokemons[0] = switch_pkm
                                player.pokemons[0] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[1]:
                                tmp_pkm = selected_pkm
                                player.pokemons[1] = switch_pkm
                                player.pokemons[0] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[2]:
                                tmp_pkm = selected_pkm
                                player.pokemons[2] = switch_pkm
                                player.pokemons[0] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[3]:
                                tmp_pkm = selected_pkm
                                player.pokemons[3] = switch_pkm
                                player.pokemons[0] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[4]:
                                tmp_pkm = selected_pkm
                                player.pokemons[4] = switch_pkm
                                player.pokemons[0] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                        elif pkm_menu_cursor.x == 245 and pkm_menu_cursor.y == 133 and len(player.pokemons) > 1:
                            switch_pkm = player.pokemons[1]
                            if selected_pkm == player.main_pokemon[0]:
                                tmp_pkm = selected_pkm
                                player.main_pokemon[0] = switch_pkm
                                player.pokemons[1] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[0]:
                                tmp_pkm = selected_pkm
                                player.pokemons[0] = switch_pkm
                                player.pokemons[1] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[1]:
                                tmp_pkm = selected_pkm
                                player.pokemons[1] = switch_pkm
                                player.pokemons[1] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[2]:
                                tmp_pkm = selected_pkm
                                player.pokemons[2] = switch_pkm
                                player.pokemons[1] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[3]:
                                tmp_pkm = selected_pkm
                                player.pokemons[3] = switch_pkm
                                player.pokemons[1] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[4]:
                                tmp_pkm = selected_pkm
                                player.pokemons[4] = switch_pkm
                                player.pokemons[1] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                        elif pkm_menu_cursor.x == 245 and pkm_menu_cursor.y == 199 and len(player.pokemons) > 2:
                            switch_pkm = player.pokemons[2]
                            if selected_pkm == player.main_pokemon[0]:
                                tmp_pkm = selected_pkm
                                player.main_pokemon[0] = switch_pkm
                                player.pokemons[2] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[0]:
                                tmp_pkm = selected_pkm
                                player.pokemons[0] = switch_pkm
                                player.pokemons[2] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[1]:
                                tmp_pkm = selected_pkm
                                player.pokemons[1] = switch_pkm
                                player.pokemons[2] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[2]:
                                tmp_pkm = selected_pkm
                                player.pokemons[2] = switch_pkm
                                player.pokemons[2] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[3]:
                                tmp_pkm = selected_pkm
                                player.pokemons[3] = switch_pkm
                                player.pokemons[2] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[4]:
                                tmp_pkm = selected_pkm
                                player.pokemons[4] = switch_pkm
                                player.pokemons[2] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                        elif pkm_menu_cursor.x == 245 and pkm_menu_cursor.y == 265 and len(player.pokemons) > 3:
                            switch_pkm = player.pokemons[3]
                            if selected_pkm == player.main_pokemon[0]:
                                tmp_pkm = selected_pkm
                                player.main_pokemon[0] = switch_pkm
                                player.pokemons[3] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[0]:
                                tmp_pkm = selected_pkm
                                player.pokemons[0] = switch_pkm
                                player.pokemons[3] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[1]:
                                tmp_pkm = selected_pkm
                                player.pokemons[1] = switch_pkm
                                player.pokemons[3] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[2]:
                                tmp_pkm = selected_pkm
                                player.pokemons[2] = switch_pkm
                                player.pokemons[3] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[3]:
                                tmp_pkm = selected_pkm
                                player.pokemons[3] = switch_pkm
                                player.pokemons[3] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[4]:
                                tmp_pkm = selected_pkm
                                player.pokemons[4] = switch_pkm
                                player.pokemons[3] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                        elif pkm_menu_cursor.x == 245 and pkm_menu_cursor.y == 331 and len(player.pokemons) > 4:
                            switch_pkm = player.pokemons[4]
                            if selected_pkm == player.main_pokemon[0]:
                                tmp_pkm = selected_pkm
                                player.main_pokemon[0] = switch_pkm
                                player.pokemons[4] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[0]:
                                tmp_pkm = selected_pkm
                                player.pokemons[0] = switch_pkm
                                player.pokemons[4] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[1]:
                                tmp_pkm = selected_pkm
                                player.pokemons[1] = switch_pkm
                                player.pokemons[4] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[2]:
                                tmp_pkm = selected_pkm
                                player.pokemons[2] = switch_pkm
                                player.pokemons[4] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[3]:
                                tmp_pkm = selected_pkm
                                player.pokemons[3] = switch_pkm
                                player.pokemons[4] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)
                            elif selected_pkm == player.pokemons[4]:
                                tmp_pkm = selected_pkm
                                player.pokemons[4] = switch_pkm
                                player.pokemons[4] = tmp_pkm
                                battle_pokemon_list, switched_pkm, pkm_attack_2, window_state, battle_pkm = switch_pokemon_battle(
                                    battle_pokemon_list, switch_pkm, pokemon_exist, player)

                    elif window_state == "selected_pokemon":
                        if selected_pkm_cursor_1.y == 403:
                            window_state = "pokemon_menu"
                        elif selected_pkm_cursor_1.y == 280:
                            window_state = "pokemon_summary_info"
                        elif selected_pkm_cursor_1.y == 321:
                            window_state = "switch_pokemon"
                        elif selected_pkm_cursor_1.y == 362:
                            window_state = "pokemon_item"

                    elif window_state == "pokemon_summary_info" or window_state == "pokemon_summary_skills":
                        window_state = "pokemon_menu"

                    elif window_state == "pokemon_summary_moves":
                        window_state = "pokemon_summary_moves_2"

                    elif window_state == "encounter_1":
                        if turn == "player":
                            window_state = "encounter"
                        else:
                            window_state = "enemy_turn"
                            pkm_attack_2 = "True"

                    elif window_state == "attack_learning_1":
                        window_state = "game"
                        pygame.mixer.music.load(os.path.join(path_audio, 'road.wav'))
                        pygame.mixer.music.play(-1)
                        up = False
                        down = False
                        right = False
                        left = False
                        steps = 0
                        dx = 0
                        dy = 0

                    elif window_state == "battle":
                        if b_cursor.x == 36 and b_cursor.y == 357 and battle_pkm.moves[0].current_pp > 0:
                            pkm_attack = True
                            used_move = battle_pkm.moves[0]
                            used_move.current_pp = used_move.current_pp - 1
                            status = "none"
                            if used_move.category == "physical" or used_move.category == "special":
                                type_modifier, status = effectiveness(used_move.type, pokemon.type[0])
                                damage = (round(((((2 * battle_pkm.level) / 5 + 2) * used_move.power * (
                                        battle_pkm.attack / pokemon.current_defense)) / 50) + 2)) * type_modifier
                                pokemon.current_hp = (pokemon.current_hp - damage)
                                pokemon.current_attack = (pokemon.current_attack - used_move.atk_debuff)
                                pokemon.current_defense = (pokemon.current_defense - used_move.def_debuff)
                                pokemon.current_speed = (pokemon.current_speed - used_move.spd_debuff)
                                pokemon.current_accuracy = (pokemon.current_accuracy - used_move.acc_debuff)

                                battle_pkm.current_attack = (battle_pkm.current_attack + used_move.atk_buff)
                                battle_pkm.current_defense = (battle_pkm.current_defense + used_move.def_buff)
                                battle_pkm.current_speed = (battle_pkm.current_speed + used_move.spd_buff)
                                battle_pkm.current_accuracy = (battle_pkm.current_accuracy + used_move.acc_buff)
                            elif used_move.category == "status":
                                damage = 0
                                pokemon.current_hp = (pokemon.current_hp - damage)
                                pokemon.current_attack = (pokemon.current_attack - used_move.atk_debuff)
                                pokemon.current_defense = (pokemon.current_defense - used_move.def_debuff)
                                pokemon.current_speed = (pokemon.current_speed - used_move.spd_debuff)
                                pokemon.current_accuracy = (pokemon.current_accuracy - used_move.acc_debuff)

                                battle_pkm.current_attack = (battle_pkm.current_attack + used_move.atk_buff)
                                battle_pkm.current_defense = (battle_pkm.current_defense + used_move.def_buff)
                                battle_pkm.current_speed = (battle_pkm.current_speed + used_move.spd_buff)
                                battle_pkm.current_accuracy = (battle_pkm.current_accuracy + used_move.acc_buff)

                        elif b_cursor.x == 222 and b_cursor.y == 357 and len(battle_pkm.moves) >= 2 and \
                                battle_pkm.moves[1].current_pp > 0:
                            pkm_attack = True
                            used_move = battle_pkm.moves[1]
                            used_move.current_pp = used_move.current_pp - 1
                            status = "none"
                            if used_move.category == "physical" or used_move.category == "special":
                                type_modifier, status = effectiveness(used_move.type, pokemon.type[0])
                                damage = (round(((((2 * battle_pkm.level) / 5 + 2) * used_move.power * (
                                        battle_pkm.attack / pokemon.current_defense)) / 50) + 2)) * type_modifier
                                pokemon.current_hp = (pokemon.current_hp - damage)
                                pokemon.current_attack = (pokemon.current_attack - used_move.atk_debuff)
                                pokemon.current_defense = (pokemon.current_defense - used_move.def_debuff)
                                pokemon.current_speed = (pokemon.current_speed - used_move.spd_debuff)
                                pokemon.current_accuracy = (pokemon.current_accuracy - used_move.acc_debuff)

                                battle_pkm.current_attack = (battle_pkm.current_attack + used_move.atk_buff)
                                battle_pkm.current_defense = (battle_pkm.current_defense + used_move.def_buff)
                                battle_pkm.current_speed = (battle_pkm.current_speed + used_move.spd_buff)
                                battle_pkm.current_accuracy = (battle_pkm.current_accuracy + used_move.acc_buff)
                            elif used_move.category == "status":
                                damage = 0
                                pokemon.current_hp = (pokemon.current_hp - damage)
                                pokemon.current_attack = (pokemon.current_attack - used_move.atk_debuff)
                                pokemon.current_defense = (pokemon.current_defense - used_move.def_debuff)
                                pokemon.current_speed = (pokemon.current_speed - used_move.spd_debuff)
                                pokemon.current_accuracy = (pokemon.current_accuracy - used_move.acc_debuff)

                                battle_pkm.current_attack = (battle_pkm.current_attack + used_move.atk_buff)
                                battle_pkm.current_defense = (battle_pkm.current_defense + used_move.def_buff)
                                battle_pkm.current_speed = (battle_pkm.current_speed + used_move.spd_buff)
                                battle_pkm.current_accuracy = (battle_pkm.current_accuracy + used_move.acc_buff)

                        elif b_cursor.x == 36 and b_cursor.y == 405 and len(battle_pkm.moves) >= 3 and \
                                battle_pkm.moves[2].current_pp > 0:
                            pkm_attack = True
                            used_move = battle_pkm.moves[2]
                            used_move.current_pp = used_move.current_pp - 1
                            status = "none"
                            if used_move.category == "physical" or used_move.category == "special":
                                type_modifier, status = effectiveness(used_move.type, pokemon.type[0])
                                damage = (round(((((2 * battle_pkm.level) / 5 + 2) * used_move.power * (
                                        battle_pkm.attack / pokemon.current_defense)) / 50) + 2)) * type_modifier
                                pokemon.current_hp = (pokemon.current_hp - damage)
                                pokemon.current_attack = (pokemon.current_attack - used_move.atk_debuff)
                                pokemon.current_defense = (pokemon.current_defense - used_move.def_debuff)
                                pokemon.current_speed = (pokemon.current_speed - used_move.spd_debuff)
                                pokemon.current_accuracy = (pokemon.current_accuracy - used_move.acc_debuff)

                                battle_pkm.current_attack = (battle_pkm.current_attack + used_move.atk_buff)
                                battle_pkm.current_defense = (battle_pkm.current_defense + used_move.def_buff)
                                battle_pkm.current_speed = (battle_pkm.current_speed + used_move.spd_buff)
                                battle_pkm.current_accuracy = (battle_pkm.current_accuracy + used_move.acc_buff)
                            elif used_move.category == "status":
                                damage = 0
                                pokemon.current_hp = (pokemon.current_hp - damage)
                                pokemon.current_attack = (pokemon.current_attack - used_move.atk_debuff)
                                pokemon.current_defense = (pokemon.current_defense - used_move.def_debuff)
                                pokemon.current_speed = (pokemon.current_speed - used_move.spd_debuff)
                                pokemon.current_accuracy = (pokemon.current_accuracy - used_move.acc_debuff)

                                battle_pkm.current_attack = (battle_pkm.current_attack + used_move.atk_buff)
                                battle_pkm.current_defense = (battle_pkm.current_defense + used_move.def_buff)
                                battle_pkm.current_speed = (battle_pkm.current_speed + used_move.spd_buff)
                                battle_pkm.current_accuracy = (battle_pkm.current_accuracy + used_move.acc_buff)

                        elif b_cursor.x == 222 and b_cursor.y == 405 and len(battle_pkm.moves) >= 4 and \
                                battle_pkm.moves[3].current_pp > 0:
                            pkm_attack = True
                            used_move = battle_pkm.moves[3]
                            used_move.current_pp = used_move.current_pp - 1
                            status = "none"
                            if used_move.category == "physical" or used_move.category == "special":
                                type_modifier, status = effectiveness(used_move.type, pokemon.type[0])
                                damage = (round(((((2 * battle_pkm.level) / 5 + 2) * used_move.power * (
                                        battle_pkm.attack / pokemon.current_defense)) / 50) + 2)) * type_modifier
                                pokemon.current_hp = (pokemon.current_hp - damage)
                                pokemon.current_attack = (pokemon.current_attack - used_move.atk_debuff)
                                pokemon.current_defense = (pokemon.current_defense - used_move.def_debuff)
                                pokemon.current_speed = (pokemon.current_speed - used_move.spd_debuff)
                                pokemon.current_accuracy = (pokemon.current_accuracy - used_move.acc_debuff)

                                battle_pkm.current_attack = (battle_pkm.current_attack + used_move.atk_buff)
                                battle_pkm.current_defense = (battle_pkm.current_defense + used_move.def_buff)
                                battle_pkm.current_speed = (battle_pkm.current_speed + used_move.spd_buff)
                                battle_pkm.current_accuracy = (battle_pkm.current_accuracy + used_move.acc_buff)
                            elif used_move.category == "status":
                                damage = 0
                                pokemon.current_hp = (pokemon.current_hp - damage)
                                pokemon.current_attack = (pokemon.current_attack - used_move.atk_debuff)
                                pokemon.current_defense = (pokemon.current_defense - used_move.def_debuff)
                                pokemon.current_speed = (pokemon.current_speed - used_move.spd_debuff)
                                pokemon.current_accuracy = (pokemon.current_accuracy - used_move.acc_debuff)

                                battle_pkm.current_attack = (battle_pkm.current_attack + used_move.atk_buff)
                                battle_pkm.current_defense = (battle_pkm.current_defense + used_move.def_buff)
                                battle_pkm.current_speed = (battle_pkm.current_speed + used_move.spd_buff)
                                battle_pkm.current_accuracy = (battle_pkm.current_accuracy + used_move.acc_buff)

                        sound_counter = 0
                        animation_counter = 0
                        window_state = "move_animation"

                    elif window_state == "enemy_turn":
                        window_state = "encounter"

                    elif window_state == "game":
                        if NPC_nurse.collide(player.shape):
                            player.main_pokemon[0].current_hp = player.main_pokemon[0].hp
                            regen_pp(player.main_pokemon[0])
                            revive_effect = pygame.mixer.Sound(os.path.join(path_audio, 'revive_sound.wav'))
                            revive_effect.play()
                            player.main_pokemon[0].hp_bar_graphics = health_bar_status(
                                player.main_pokemon[0].current_hp,
                                player.main_pokemon[0].hp, path_hp_bar)
                            if len(player.pokemons) == 1:
                                player.pokemons[0].current_hp = player.pokemons[0].hp
                                player.pokemons[0].hp_bar_graphics = health_bar_status(player.pokemons[0].current_hp,
                                                                                       player.pokemons[0].hp,
                                                                                       path_hp_bar)
                                regen_pp(player.pokemons[0])
                            elif len(player.pokemons) == 2:
                                player.pokemons[0].current_hp = player.pokemons[0].hp
                                player.pokemons[0].hp_bar_graphics = health_bar_status(player.pokemons[0].current_hp,
                                                                                       player.pokemons[0].hp,
                                                                                       path_hp_bar)
                                player.pokemons[1].current_hp = player.pokemons[1].hp
                                player.pokemons[1].hp_bar_graphics = health_bar_status(player.pokemons[1].current_hp,
                                                                                       player.pokemons[1].hp,
                                                                                       path_hp_bar)
                                regen_pp(player.pokemons[0])
                                regen_pp(player.pokemons[1])
                            elif len(player.pokemons) == 3:
                                player.pokemons[0].current_hp = player.pokemons[0].hp
                                player.pokemons[0].hp_bar_graphics = health_bar_status(player.pokemons[0].current_hp,
                                                                                       player.pokemons[0].hp,
                                                                                       path_hp_bar)
                                player.pokemons[1].current_hp = player.pokemons[1].hp
                                player.pokemons[1].hp_bar_graphics = health_bar_status(player.pokemons[1].current_hp,
                                                                                       player.pokemons[1].hp,
                                                                                       path_hp_bar)
                                player.pokemons[2].current_hp = player.pokemons[2].hp
                                player.pokemons[2].hp_bar_graphics = health_bar_status(player.pokemons[2].current_hp,
                                                                                       player.pokemons[2].hp,
                                                                                       path_hp_bar)
                                regen_pp(player.pokemons[0])
                                regen_pp(player.pokemons[1])
                                regen_pp(player.pokemons[2])
                            elif len(player.pokemons) == 4:
                                player.pokemons[0].current_hp = player.pokemons[0].hp
                                player.pokemons[0].hp_bar_graphics = health_bar_status(player.pokemons[0].current_hp,
                                                                                       player.pokemons[0].hp,
                                                                                       path_hp_bar)
                                player.pokemons[1].current_hp = player.pokemons[1].hp
                                player.pokemons[1].hp_bar_graphics = health_bar_status(player.pokemons[1].current_hp,
                                                                                       player.pokemons[1].hp,
                                                                                       path_hp_bar)
                                player.pokemons[2].current_hp = player.pokemons[2].hp
                                player.pokemons[2].hp_bar_graphics = health_bar_status(player.pokemons[2].current_hp,
                                                                                       player.pokemons[2].hp,
                                                                                       path_hp_bar)
                                player.pokemons[3].current_hp = player.pokemons[3].hp
                                player.pokemons[3].hp_bar_graphics = health_bar_status(player.pokemons[3].current_hp,
                                                                                       player.pokemons[3].hp,
                                                                                       path_hp_bar)
                                regen_pp(player.pokemons[0])
                                regen_pp(player.pokemons[1])
                                regen_pp(player.pokemons[2])
                                regen_pp(player.pokemons[3])
                            elif len(player.pokemons) == 5:
                                player.pokemons[0].current_hp = player.pokemons[0].hp
                                player.pokemons[0].hp_bar_graphics = health_bar_status(player.pokemons[0].current_hp,
                                                                                       player.pokemons[0].hp,
                                                                                       path_hp_bar)
                                player.pokemons[1].current_hp = player.pokemons[1].hp
                                player.pokemons[1].hp_bar_graphics = health_bar_status(player.pokemons[1].current_hp,
                                                                                       player.pokemons[1].hp,
                                                                                       path_hp_bar)
                                player.pokemons[2].current_hp = player.pokemons[2].hp
                                player.pokemons[2].hp_bar_graphics = health_bar_status(player.pokemons[2].current_hp,
                                                                                       player.pokemons[2].hp,
                                                                                       path_hp_bar)
                                player.pokemons[3].current_hp = player.pokemons[3].hp
                                player.pokemons[3].hp_bar_graphics = health_bar_status(player.pokemons[3].current_hp,
                                                                                       player.pokemons[3].hp,
                                                                                       path_hp_bar)
                                player.pokemons[4].current_hp = player.pokemons[4].hp
                                player.pokemons[4].hp_bar_graphics = health_bar_status(player.pokemons[4].current_hp,
                                                                                       player.pokemons[4].hp,
                                                                                       path_hp_bar)
                                regen_pp(player.pokemons[0])
                                regen_pp(player.pokemons[1])
                                regen_pp(player.pokemons[2])
                                regen_pp(player.pokemons[3])
                                regen_pp(player.pokemons[3])

                        if NPC_seller.collide(player.shape):
                            player.pokeballs[0].quantity = (player.pokeballs[0].quantity + 1)
                            pay_effect = pygame.mixer.Sound(os.path.join(path_audio, 'pay_sound.wav'))
                            pay_effect.play()
                    elif window_state == "level_up":
                        window_state = "level_up2"

                    elif window_state == "level_up2":
                        window_state = "game"
                        pygame.mixer.music.load(os.path.join(path_audio, 'road.wav'))
                        pygame.mixer.music.play(-1)
                        up = False
                        down = False
                        right = False
                        left = False
                        steps = 0
                        dx = 0
                        dy = 0

                    elif window_state == "fainted_info":
                        gain_exp_counter2 = 0
                        window_state = "gain_exp"

                    elif window_state == "gain_exp":
                        window_state = "game"

                        pygame.mixer.music.load(os.path.join(path_audio, 'road.wav'))
                        pygame.mixer.music.play(-1)
                        up = False
                        down = False
                        right = False
                        left = False
                        steps = 0
                        dx = 0
                        dy = 0

                    elif window_state == "option":
                        window_state = "game"

                    elif window_state == "pokemon_catching" and pokemon_catching_animation == len(
                            pkm_caught.graphics_list):
                        window_state = "game"
                        pygame.mixer.music.load(os.path.join(path_audio, 'road.wav'))
                        pygame.mixer.music.play(-1)
                        up = False
                        down = False
                        right = False
                        left = False
                        steps = 0
                        dx = 0
                        dy = 0

                    elif window_state == "attack_learning_2_1":
                        window_state = "attack_learning_2_2"
                    elif window_state == "attack_learning_2_2":
                        window_state = "attack_learning_2_3"
                    elif window_state == "attack_learning_2_3" and change_skill_c.y == 240:
                        window_state = "attack_learning_2_4"
                    elif window_state == "attack_learning_2_3" and change_skill_c.y == 280:
                        window_state = "stop_attack_learning"

                    elif window_state == "attack_learning_2_4":
                        if moves_learn_cursor.y == 75:
                            move_to_change = leveling_pokemon.moves[0]
                            leveling_pokemon.moves[0] = learning_move
                            window_state = "attack_learning_2_5"
                        elif moves_learn_cursor.y == 149:
                            move_to_change = leveling_pokemon.moves[1]
                            leveling_pokemon.moves[1] = learning_move
                            window_state = "attack_learning_2_5"
                        elif moves_learn_cursor.y == 223:
                            move_to_change = leveling_pokemon.moves[2]
                            leveling_pokemon.moves[2] = learning_move
                            window_state = "attack_learning_2_5"
                        elif moves_learn_cursor.y == 297:
                            move_to_change = leveling_pokemon.moves[3]
                            leveling_pokemon.moves[3] = learning_move
                            window_state = "attack_learning_2_5"

                    elif window_state == "attack_learning_2_5":
                        window_state = "attack_learning_2_6"
                    elif window_state == "attack_learning_2_6":
                        window_state = "attack_learning_2_7"
                    elif window_state == "attack_learning_2_7":
                        window_state = "attack_learning_2_8"
                    elif window_state == "attack_learning_2_8":
                        window_state = "game"
                        pygame.mixer.music.load(os.path.join(path_audio, 'road.wav'))
                        pygame.mixer.music.play(-1)
                        up = False
                        down = False
                        right = False
                        left = False
                        steps = 0
                        dx = 0
                        dy = 0

                    elif window_state == "stop_attack_learning" and change_skill_c_2.y == 240:
                        window_state = "stop_attack_learning_2"
                    elif window_state == "stop_attack_learning" and change_skill_c_2.y == 280:
                        window_state = "attack_learning_2_1"
                    elif window_state == "stop_attack_learning_2":
                        window_state = "game"
                        pygame.mixer.music.load(os.path.join(path_audio, 'road.wav'))
                        pygame.mixer.music.play(-1)
                        up = False
                        down = False
                        right = False
                        left = False
                        steps = 0
                        dx = 0
                        dy = 0

                    elif window_state == "bag_items" and len(player.items) > 0 and cursor_bag.y == 53:
                        if giving_item == "True":
                            selected_item = player.items[0]
                            back = "pokemon_menu"
                            if selected_pkm.holding_item == "none":
                                selected_pkm.holding_item = selected_item
                                selected_item.quantity = selected_item.quantity - 1
                                window_state = "give_items2"
                            else:
                                tmp_item = selected_pkm.holding_item
                                window_state = "give_items3"
                        elif giving_item == "False":
                            selected_item = player.items[0]
                            window_state = "selected_bag_items"
                    elif window_state == "bag_items" and len(player.items) > 1 and cursor_bag.y == 98:
                        if giving_item == "True":
                            selected_item = player.items[1]
                            back = "pokemon_menu"
                            if selected_pkm.holding_item == "none":
                                selected_pkm.holding_item = selected_item
                                selected_item.quantity = selected_item.quantity - 1
                                window_state = "give_items2"
                            else:
                                tmp_item = selected_pkm.holding_item
                                window_state = "give_items3"
                        elif giving_item == "False":
                            selected_item = player.items[1]
                            window_state = "selected_bag_items"
                    elif window_state == "bag_items" and len(player.items) > 2 and cursor_bag.y == 143:
                        if giving_item == "True":
                            selected_item = player.items[2]
                            back = "pokemon_menu"
                            if selected_pkm.holding_item == "none":
                                selected_pkm.holding_item = selected_item
                                selected_item.quantity = selected_item.quantity - 1
                                window_state = "give_items2"
                            else:
                                tmp_item = selected_pkm.holding_item
                                window_state = "give_items3"
                        elif giving_item == "False":
                            selected_item = player.items[2]
                            window_state = "selected_bag_items"
                    elif window_state == "bag_items" and len(player.items) > 3 and cursor_bag.y == 188:
                        if giving_item == "True":
                            selected_item = player.items[3]
                            back = "pokemon_menu"
                            if selected_pkm.holding_item == "none":
                                selected_pkm.holding_item = selected_item
                                selected_item.quantity = selected_item.quantity - 1
                                window_state = "give_items2"
                            else:
                                tmp_item = selected_pkm.holding_item
                                window_state = "give_items3"
                        elif giving_item == "False":
                            selected_item = player.items[3]
                            window_state = "selected_bag_items"
                    elif window_state == "bag_items" and len(player.items) > 4 and cursor_bag.y == 233:
                        if giving_item == "True":
                            selected_item = player.items[4]
                            back = "pokemon_menu"
                            if selected_pkm.holding_item == "none":
                                selected_pkm.holding_item = selected_item
                                selected_item.quantity = selected_item.quantity - 1
                                window_state = "give_items2"
                            else:
                                tmp_item = selected_pkm.holding_item
                                window_state = "give_items3"
                        elif giving_item == "False":
                            selected_item = player.items[4]
                            window_state = "selected_bag_items"

                    elif window_state == "bag_key_items" and len(player.key_items) > 0 and cursor_bag.y == 53:
                        if giving_item == "False":
                            selected_item = player.key_items[0]
                            window_state = "selected_bag_key_items"
                    elif window_state == "bag_key_items" and len(player.key_items) > 1 and cursor_bag.y == 98:
                        if giving_item == "False":
                            selected_item = player.key_items[1]
                            window_state = "selected_bag_key_items"
                    elif window_state == "bag_key_items" and len(player.key_items) > 2 and cursor_bag.y == 143:
                        if giving_item == "False":
                            selected_item = player.key_items[2]
                            window_state = "selected_bag_key_items"
                    elif window_state == "bag_key_items" and len(player.key_items) > 3 and cursor_bag.y == 188:
                        if giving_item == "False":
                            selected_item = player.key_items[3]
                            window_state = "selected_bag_key_items"
                    elif window_state == "bag_key_items" and len(player.key_items) > 4 and cursor_bag.y == 233:
                        if giving_item == "False":
                            selected_item = player.key_items[4]
                            window_state = "selected_bag_key_items"

                    elif window_state == "bag_pokeballs" and len(player.pokeballs) > 0 and cursor_bag.y == 53:
                        if giving_item == "True":
                            selected_item = player.pokeballs[0]
                            back = "pokemon_menu"
                            if selected_pkm.holding_item == "none":
                                selected_pkm.holding_item = selected_item
                                selected_item.quantity = selected_item.quantity - 1
                                window_state = "give_items2"
                            else:
                                tmp_item = selected_pkm.holding_item
                                window_state = "give_items3"
                        elif giving_item == "False":
                            selected_item = player.pokeballs[0]
                            window_state = "selected_bag_pokeballs"
                    elif window_state == "bag_pokeballs" and len(player.pokeballs) > 1 and cursor_bag.y == 98:
                        if giving_item == "True":
                            selected_item = player.pokeballs[1]
                            back = "pokemon_menu"
                            if selected_pkm.holding_item == "none":
                                selected_pkm.holding_item = selected_item
                                selected_item.quantity = selected_item.quantity - 1
                                window_state = "give_items2"
                            else:
                                tmp_item = selected_pkm.holding_item
                                window_state = "give_items3"
                        elif giving_item == "False":
                            selected_item = player.pokeballs[1]
                            window_state = "selected_bag_pokeballs"
                    elif window_state == "bag_pokeballs" and len(player.pokeballs) > 2 and cursor_bag.y == 143:
                        if giving_item == "True":
                            selected_item = player.pokeballs[2]
                            back = "pokemon_menu"
                            if selected_pkm.holding_item == "none":
                                selected_pkm.holding_item = selected_item
                                selected_item.quantity = selected_item.quantity - 1
                                window_state = "give_items2"
                            else:
                                tmp_item = selected_pkm.holding_item
                                window_state = "give_items3"
                        elif giving_item == "False":
                            selected_item = player.pokeballs[2]
                            window_state = "selected_bag_pokeballs"
                    elif window_state == "bag_pokeballs" and len(player.pokeballs) > 3 and cursor_bag.y == 188:
                        if giving_item == "True":
                            selected_item = player.pokeballs[3]
                            back = "pokemon_menu"
                            if selected_pkm.holding_item == "none":
                                selected_pkm.holding_item = selected_item
                                selected_item.quantity = selected_item.quantity - 1
                                window_state = "give_items2"
                            else:
                                tmp_item = selected_pkm.holding_item
                                window_state = "give_items3"
                        elif giving_item == "False":
                            selected_item = player.pokeballs[3]
                            window_state = "selected_bag_pokeballs"
                    elif window_state == "bag_pokeballs" and len(player.pokeballs) > 4 and cursor_bag.y == 233:
                        if giving_item == "True":
                            selected_item = player.pokeballs[4]
                            back = "pokemon_menu"
                            if selected_pkm.holding_item == "none":
                                selected_pkm.holding_item = selected_item
                                selected_item.quantity = selected_item.quantity - 1
                                window_state = "give_items2"
                            else:
                                tmp_item = selected_pkm.holding_item
                                window_state = "give_items3"
                        elif giving_item == "False":
                            selected_item = player.pokeballs[4]
                            window_state = "selected_bag_pokeballs"

                    elif window_state == "selected_bag_items":
                        if cursor_bag_items.y == 279:
                            window_state = "use_bag_items"
                        elif cursor_bag_items.y == 319:
                            back = "bag_items"
                            window_state = "give_items"
                        elif cursor_bag_items.y == 359:
                            if selected_item.quantity == 1:
                                toss_number = 1
                                window_state = "toss_bag_items_1"
                            else:
                                toss_number = 1
                                window_state = "toss_bag_items_2"
                        elif cursor_bag_items.y == 399:
                            window_state = "bag_items"
                    elif window_state == "cannot_use_items":
                        window_state = "bag_items"

                    elif window_state == "selected_bag_key_items":
                        if cursor_bag_key_items.y == 399:
                            window_state = "bag_key_items"
                        elif cursor_bag_key_items.y == 319:
                            window_state = "use_bag_key_items"
                        elif cursor_bag_key_items.y == 359:
                            if selected_item != player.registered_item:
                                player.registered_item = selected_item
                                window_state = "bag_key_items"
                            elif selected_item == player.registered_item:
                                player.registered_item = "none"
                                window_state = "bag_key_items"

                    elif window_state == "selected_bag_pokeballs":
                        if cursor_bag_pokeballs.y == 359:
                            if selected_item.quantity == 1:
                                toss_number = 1
                                window_state = "toss_bag_pokeballs_1"
                            else:
                                toss_number = 1
                                window_state = "toss_bag_pokeballs_2"
                        elif cursor_bag_pokeballs.y == 319:
                            back = "bag_pokeballs"
                            window_state = "give_items"

                    elif window_state == "toss_bag_items_1" and cursor_toss_bag_items.y == 359:
                        toss_times = 0
                        window_state = "toss_bag_items_1_2"
                    elif window_state == "toss_bag_items_1" and cursor_toss_bag_items.y == 399:
                        window_state = "bag_items"
                    elif window_state == "toss_bag_items_1_2":
                        window_state = "bag_items"

                    elif window_state == "toss_bag_pokeballs_1" and cursor_toss_bag_pokeballs.y == 359:
                        toss_times = 0
                        window_state = "toss_bag_pokeballs_1_2"
                    elif window_state == "toss_bag_pokeballs_1" and cursor_toss_bag_pokeballs.y == 399:
                        window_state = "bag_pokeballs"
                    elif window_state == "toss_bag_pokeballs_1_2":
                        window_state = "bag_pokeballs"

                    elif window_state == "toss_bag_items_2":
                        window_state = "toss_bag_items_1"

                    elif window_state == "toss_bag_pokeballs_2":
                        window_state = "toss_bag_pokeballs_1"

                    elif window_state == "give_items2":
                        window_state = back

                    elif window_state == "give_items3":
                        window_state = "give_items4"

                    elif window_state == "give_items4":
                        if cursor_switch_items.y == 236:
                            if tmp_item.pocket == "pokeballs":
                                for i in range(0, len(player.pokeballs)):
                                    if player.pokeballs[i].name == tmp_item.name:
                                        player.pokeballs[i].quantity = player.pokeballs[i].quantity + 1
                            elif tmp_item.pocket == "items":
                                for i in range(0, len(player.items)):
                                    if player.items[i].name == tmp_item.name:
                                        player.items[i].quantity = player.items[i].quantity + 1
                            selected_pkm.holding_item = selected_item
                            selected_item.quantity = selected_item.quantity - 1
                            window_state = "give_items5"
                        elif cursor_switch_items.y == 270:
                            window_state = back

                    elif window_state == "give_items5":
                        window_state = back

                    elif window_state == "pokemon_item":
                        if pokemon_item_cursor.y == 399:
                            window_state = "selected_pokemon"
                        elif pokemon_item_cursor.y == 319:
                            giving_item = "True"
                            window_state = "bag_items"
                        elif pokemon_item_cursor.y == 359:
                            if selected_pkm.holding_item != "none":
                                tmp_holding_item = selected_item
                                if tmp_holding_item.pocket == "pokeballs":
                                    for i in range(0, len(player.pokeballs)):
                                        if player.pokeballs[i].name == tmp_holding_item.name:
                                            player.pokeballs[i].quantity = player.pokeballs[i].quantity + 1
                                elif tmp_holding_item.pocket == "items":
                                    for i in range(0, len(player.items)):
                                        if player.items[i].name == tmp_holding_item.name:
                                            player.items[i].quantity = player.items[i].quantity + 1
                                selected_pkm.holding_item = "none"
                                window_state = "pokemon_item_take"
                            elif selected_pkm.holding_item == "none":
                                window_state = "pokemon_cannot_take_item"

                    elif window_state == "pokemon_item_take":
                        window_state = "pokemon_menu"

                    elif window_state == "pokemon_cannot_take_item":
                        window_state = "pokemon_menu"

                elif event.key == pygame.K_b:
                    if window_state == "game":
                        revive_effect = pygame.mixer.Sound(os.path.join(path_audio, 'menu_sound.wav'))
                        revive_effect.play()
                        window_state = "enter_menu"
                    elif window_state == "enter_menu":
                        window_state = "game"

                elif event.key == pygame.K_c:
                    if window_state == "game":
                        if player.registered_item != "none":
                            selected_item = player.registered_item
                            window_state = "use_bag_key_items"
                            back_register = "game"

                elif event.key == pygame.K_x:
                    if window_state == "game":
                        window_state = "game"

                    elif window_state == "bag_items":
                        window_state = "game"

                    elif window_state == "bag_key_items":
                        window_state = "game"

                    elif window_state == "bag_pokeballs":
                        window_state = "game"

                    elif window_state == "pokemon_menu":
                        window_state = "game"

                    elif pokemon_exist and window_state == "pokemon_menu":
                        window_state = "encounter"

                    elif window_state == "enter_menu":
                        window_state = "game"

                    elif window_state == "selected_pokemon":
                        window_state = "pokemon_menu"

                    elif window_state == "player_card_1" or window_state == "player_card_2":
                        window_state = "game"

                    elif window_state == "pokemon_summary_info" or window_state == "pokemon_summary_skills" or window_state == "pokemon_summary_moves":
                        window_state = "pokemon_menu"

                    elif window_state == "pokemon_summary_moves_2":
                        window_state = "pokemon_summary_moves"

                    elif window_state == "battle":
                        window_state = "encounter"

                    elif window_state == "switch_pokemon":
                        if pokemon_exist == "True":
                            window_state = "encounter"
                        else:
                            window_state = "pokemon_menu"

                    elif window_state == "option":
                        window_state = "game"

                    elif window_state == "attack_learning_2_4":
                        window_state = "stop_attack_learning"

                    elif window_state == "selected_bag_items":
                        window_state = "bag_items"
                    elif window_state == "selected_bag_key_items":
                        window_state = "bag_key_items"
                    elif window_state == "selected_bag_pokeballs":
                        window_state = "bag_pokeballs"

                    elif window_state == "use_bag_items":
                        window_state = "bag_items"
                    elif window_state == "cannot_use_items":
                        window_state = "bag_items"

                    elif window_state == "toss_bag_items_1" or "toss_bag_items_2":
                        window_state = "bag_items"

                    elif window_state == "toss_bag_pokeballs_1" or "toss_bag_pokeballs_2":
                        window_state = "bag_pokeballs"

                    elif window_state == "use_bag_key_items":
                        if back_register == "none":
                            window_state = "bag_key_items"
                        elif back_register == "game":
                            window_state = "game"

                    elif window_state == "pokedex_table":
                        window_state = "game"
                else:
                    up = False
                    down = False
                    right = False
                    left = False
                    steps = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    if window_state == "game":
                        dy = 0
                        dx = 0
                        steps = 0
                        up = False
                        down = False
                    elif window_state == "use_bag_key_items" and selected_item.name == "Town Map":
                        Map_dy = 0
                        Map_dx = 0
                if event.key == pygame.K_DOWN:
                    if window_state == "game":
                        dy = 0
                        dx = 0
                        steps = 0
                        up = False
                        down = False
                    elif window_state == "use_bag_key_items" and selected_item.name == "Town Map":
                        Map_dy = 0
                        Map_dx = 0
                if event.key == pygame.K_LEFT:
                    if window_state == "game":
                        dy = 0
                        dx = 0
                        steps = 0
                        right = False
                        left = False
                    elif window_state == "use_bag_key_items" and selected_item.name == "Town Map":
                        Map_dy = 0
                        Map_dx = 0
                if event.key == pygame.K_RIGHT:
                    if window_state == "game":
                        dy = 0
                        dx = 0
                        steps = 0
                        right = False
                        left = False
                    elif window_state == "use_bag_key_items" and selected_item.name == "Town Map":
                        Map_dy = 0
                        Map_dx = 0

        if window_state == "menu":
            screen.fill((0, 0, 0))
            type_text("Press space to continue...", 234, 350, 20, (50, 255, 50))
            logo = pygame.image.load(os.path.join(path_visual_elements, 'logo_pkm.png'))
            screen.blit(logo, (0, 0))

        elif window_state == "encounter":
            location = player.current_location
            battle_pkm = player.main_pokemon[0]
            screen.fill((0, 0, 0))
            catch_bg = BackgroundCatching(path_visual_elements)
            catch_bg.draw(screen)
            encounter_m = EncounterMenu(path_visual_elements)
            encounter_m.draw(screen)
            battle_pkm.draw_battle()
            pokemon.draw(398, 90)
            if pokemon.current_hp > 0:
                pokemon.hp_bar_graphics = health_bar_status(pokemon.current_hp, pokemon.hp, path_hp_bar)
                pokemon.draw_hp_bar(100, 112)
            else:
                pokemon.hp_bar_graphics = health_bar_status(0, pokemon.hp, path_hp_bar)
                pokemon.draw_hp_bar(100, 112)
            type_text(pokemon.name, 56, 78, 26, (0, 0, 0))
            type_text(str(pokemon.level), 251, 78, 26, (0, 0, 0))
            screen.blit(pokemon.sex_graphics, (pokemon.sex_x, pokemon.sex_y))

            b_info.draw(360, 235)
            type_text(battle_pkm.name, 400, 240, 26, (0, 0, 0))
            type_text(str(battle_pkm.level), 586, 240, 26, (0, 0, 0))
            screen.blit(battle_pkm.sex_graphics, (526, 246))
            if battle_pkm.current_hp > 0:
                battle_pkm.hp_bar_graphics = health_bar_status(battle_pkm.current_hp, battle_pkm.hp, path_hp_bar)
                battle_pkm.draw_hp_bar(437, 272)
            battle_pkm.draw_exp_bar(400, 310)
            type_text(str(battle_pkm.current_hp), 518, 286, 23, (0, 0, 0))
            type_text("/", 550, 286, 23, (0, 0, 0))
            type_text(str(battle_pkm.hp), 572, 286, 23, (0, 0, 0))

            type_text("What will", 40, 350, 32, (255, 255, 255))
            type_text(str(battle_pkm.name) + " do?", 40, 390, 32, (255, 255, 255))
            type_text("FIGHT", 400, 350, 30, (0, 0, 0))
            type_text("BAG", 560, 350, 30, (0, 0, 0))
            type_text("POKEMON", 400, 400, 30, (0, 0, 0))
            type_text("RUN", 560, 400, 30, (0, 0, 0))

            cursor.draw()

        elif window_state == "encounter_1":
            screen.fill((0, 0, 0))
            catch_bg = BackgroundCatching(path_visual_elements)
            catch_bg.draw(screen)
            p_catch = PlayerCatching(path_boy_player_animations)
            p_catch.draw(screen)
            battle_pkm = player.main_pokemon[0]
            pokemon.draw(398, 90)
            pokemon.draw_hp_bar(100, 112)
            type_text(pokemon.name, 56, 78, 26, (0, 0, 0))
            type_text(str(pokemon.level), 251, 78, 26, (0, 0, 0))
            screen.blit(pokemon.sex_graphics, (pokemon.sex_x, pokemon.sex_y))
            type_text("Wild " + str(pokemon.name) + " appeared!", 40, 350, 32, (255, 255, 255))

            if battle_pkm.speed >= pokemon.speed:
                turn = "player"
            else:
                turn = "enemy"
            if battle_pokemon_counter == 0:
                battle_pokemon_list = []
                battle_pokemon_list.append(battle_pkm)
            battle_pokemon_counter = battle_pokemon_counter + 1

        elif window_state == "battle":
            battle_menu_1.draw(0, 326, screen)
            battle_menu_2.draw(438, 326, screen)
            b_cursor.draw()

            if len(battle_pkm.moves) == 1:
                type_text(str(battle_pkm.moves[0].name), 50, 350, 32, (0, 0, 0))
                type_text("-", 236, 350, 32, (0, 0, 0))
                type_text("-", 50, 396, 32, (0, 0, 0))
                type_text("-", 236, 396, 32, (0, 0, 0))
            elif len(battle_pkm.moves) == 2:
                type_text(str(battle_pkm.moves[0].name), 50, 350, 32, (0, 0, 0))
                type_text(str(battle_pkm.moves[1].name), 236, 350, 32, (0, 0, 0))
                type_text("-", 50, 396, 32, (0, 0, 0))
                type_text("-", 236, 396, 32, (0, 0, 0))
            elif len(battle_pkm.moves) == 3:
                type_text(str(battle_pkm.moves[0].name), 50, 350, 32, (0, 0, 0))
                type_text(str(battle_pkm.moves[1].name), 236, 350, 32, (0, 0, 0))
                type_text(str(battle_pkm.moves[2].name), 50, 396, 32, (0, 0, 0))
                type_text("-", 236, 396, 32, (0, 0, 0))
            elif len(battle_pkm.moves) == 4:
                type_text(str(battle_pkm.moves[0].name), 50, 350, 32, (0, 0, 0))
                type_text(str(battle_pkm.moves[1].name), 236, 350, 32, (0, 0, 0))
                type_text(str(battle_pkm.moves[2].name), 50, 396, 32, (0, 0, 0))
                type_text(str(battle_pkm.moves[3].name), 236, 396, 32, (0, 0, 0))

            if b_cursor.x == 36 and b_cursor.y == 357 and len(battle_pkm.moves) >= 1:
                type_text(str(battle_pkm.moves[0].current_pp), 540, 350, 32, (0, 0, 0))
                type_text("/", 574, 350, 32, (0, 0, 0))
                type_text(str(battle_pkm.moves[0].pp), 584, 350, 32, (0, 0, 0))
                type_text("pp", 460, 350, 32, (0, 0, 0))
                type_text("type/" + str(battle_pkm.moves[0].type), 460, 396, 32, (0, 0, 0))
            elif b_cursor.x == 222 and b_cursor.y == 357 and len(battle_pkm.moves) >= 2:
                type_text(str(battle_pkm.moves[1].current_pp), 540, 350, 32, (0, 0, 0))
                type_text("/", 574, 350, 32, (0, 0, 0))
                type_text(str(battle_pkm.moves[1].pp), 584, 350, 32, (0, 0, 0))
                type_text("pp", 460, 350, 32, (0, 0, 0))
                type_text("type/" + str(battle_pkm.moves[1].type), 460, 396, 32, (0, 0, 0))
            elif b_cursor.x == 36 and b_cursor.y == 405 and len(battle_pkm.moves) >= 3:
                type_text(str(battle_pkm.moves[2].current_pp), 540, 350, 32, (0, 0, 0))
                type_text("/", 574, 350, 32, (0, 0, 0))
                type_text(str(battle_pkm.moves[2].pp), 584, 350, 32, (0, 0, 0))
                type_text("pp", 460, 350, 32, (0, 0, 0))
                type_text("type/" + str(battle_pkm.moves[2].type), 460, 396, 32, (0, 0, 0))
            elif b_cursor.x == 222 and b_cursor.y == 405 and len(battle_pkm.moves) >= 4:
                type_text(str(battle_pkm.moves[3].current_pp), 540, 350, 32, (0, 0, 0))
                type_text("/", 574, 350, 32, (0, 0, 0))
                type_text(str(battle_pkm.moves[3].pp), 584, 350, 32, (0, 0, 0))
                type_text("pp", 460, 350, 32, (0, 0, 0))
                type_text("type/" + str(battle_pkm.moves[3].type), 460, 396, 32, (0, 0, 0))

        elif window_state == "move_animation":
            if used_move.current_pp > 0:
                catch_bg.draw(screen)
                battle_pkm.draw_battle()
                pokemon.draw(398, 90)
                if status == "none":
                    type_text(str(battle_pkm.name) + " used " + str(used_move.name) + "!", 40, 350, 32, (255, 255, 255))
                elif status != "none":
                    if animation_counter < len(used_move.graphics_list) - 4:
                        type_text(str(battle_pkm.name) + " used " + str(used_move.name) + "!", 40, 350, 32,
                                  (255, 255, 255))
                    else:
                        type_text("It's " + str(status) + "!", 40, 350, 32, (255, 255, 255))
                if pokemon.current_hp > 0:
                    pokemon.hp_bar_graphics = health_bar_status(pokemon.current_hp, pokemon.hp, path_hp_bar)
                    pokemon.draw_hp_bar(100, 112)
                else:
                    pokemon.hp_bar_graphics = health_bar_status(0, pokemon.hp, path_hp_bar)
                    pokemon.draw_hp_bar(100, 112)
                type_text(pokemon.name, 56, 78, 26, (0, 0, 0))
                type_text(str(pokemon.level), 251, 78, 26, (0, 0, 0))
                screen.blit(pokemon.sex_graphics, (pokemon.sex_x, pokemon.sex_y))

                b_info.draw(360, 235)
                type_text(battle_pkm.name, 400, 240, 26, (0, 0, 0))
                type_text(str(battle_pkm.level), 586, 240, 26, (0, 0, 0))
                screen.blit(battle_pkm.sex_graphics, (526, 246))
                if battle_pkm.current_hp > 0:
                    battle_pkm.hp_bar_graphics = health_bar_status(battle_pkm.current_hp, battle_pkm.hp, path_hp_bar)
                    battle_pkm.draw_hp_bar(437, 272)
                battle_pkm.draw_exp_bar(400, 310)
                type_text(str(battle_pkm.current_hp), 518, 286, 23, (0, 0, 0))
                type_text("/", 550, 286, 23, (0, 0, 0))
                type_text(str(battle_pkm.hp), 572, 286, 23, (0, 0, 0))

                if sound_counter == 0:
                    attack_effect = pygame.mixer.Sound(used_move.sound)
                    attack_effect.play()
                sound_counter = sound_counter + 1
                if animation_counter < len(used_move.graphics_list):
                    graphics = used_move.graphics_list[animation_counter]
                    used_move.draw(graphics)

                elif animation_counter == len(used_move.graphics_list):
                    if animation_counter >= len(used_move.graphics_list):
                        if pokemon.current_hp > 0 and battle_pkm.current_hp > 0:
                            turn = "enemy"
                            window_state = "enemy_turn"
                            pkm_attack_2 = "True"
                            animation_counter2 = 0
                        else:
                            pokemon_exist = False
                            gained_exp = gain_exp(pokemon.exp_value, pokemon.level, battle_pokemon_list)
                            sound_exp_counter = 0
                            gain_exp_counter = 0
                            window_state = "fainted_info"

                animation_counter = animation_counter + 1
            else:
                window_state = "battle"

        elif window_state == "enemy_turn":
            if pokemon.current_hp > 0:
                if len(pokemon.moves) == 1:
                    attack_number = random.randint(0, 0)
                elif len(pokemon.moves) == 2:
                    attack_number = random.randint(0, 1)
                elif len(pokemon.moves) == 3:
                    attack_number = random.randint(0, 2)
                elif len(pokemon.moves) >= 4:
                    attack_number = random.randint(0, 3)

                if pokemon.moves[attack_number].current_pp > 0:

                    if pkm_attack_2 == "True":

                        used_move_2 = pokemon.moves[attack_number]
                        attack_2_effect = pygame.mixer.Sound(used_move_2.sound)
                        attack_2_effect.play()

                        used_move_2.current_pp = used_move_2.current_pp - 1
                        status_2 = "none"
                        if used_move_2.category == "physical" or used_move_2.category == "special":
                            type_modifier_2, status_2 = effectiveness(used_move_2.type, battle_pkm.type[0])
                            damage_2 = (round(((((2 * pokemon.level) / 5 + 2) * used_move_2.power * (
                                    pokemon.attack / battle_pkm.current_defense)) / 50) + 2)) * type_modifier_2
                            battle_pkm.current_hp = (battle_pkm.current_hp - damage_2)
                            battle_pkm.current_attack = (battle_pkm.current_attack - used_move_2.atk_debuff)
                            battle_pkm.current_defense = (battle_pkm.current_defense - used_move_2.def_debuff)
                            battle_pkm.current_speed = (battle_pkm.current_speed - used_move_2.spd_debuff)
                            battle_pkm.current_accuracy = (battle_pkm.current_accuracy - used_move_2.acc_debuff)

                            pokemon.current_attack = (pokemon.current_attack + used_move_2.atk_buff)
                            pokemon.current_defense = (pokemon.current_defense + used_move_2.def_buff)
                            pokemon.current_speed = (pokemon.current_speed + used_move_2.spd_buff)
                            pokemon.current_accuracy = (pokemon.current_accuracy + used_move_2.acc_buff)
                        elif used_move_2.category == "status":
                            damage_2 = 0
                            battle_pkm.current_hp = (battle_pkm.current_hp - damage_2)
                            battle_pkm.current_attack = (battle_pkm.current_attack - used_move_2.atk_debuff)
                            battle_pkm.current_defense = (battle_pkm.current_defense - used_move_2.def_debuff)
                            battle_pkm.current_speed = (battle_pkm.current_speed - used_move_2.spd_debuff)
                            battle_pkm.current_accuracy = (battle_pkm.current_accuracy - used_move_2.acc_debuff)

                            pokemon.current_attack = (pokemon.current_attack + used_move_2.atk_buff)
                            pokemon.current_defense = (pokemon.current_defense + used_move_2.def_buff)
                            pokemon.current_speed = (pokemon.current_speed + used_move_2.spd_buff)
                            pokemon.current_accuracy = (pokemon.current_accuracy + used_move_2.acc_buff)

                    pkm_attack_2 = "False"

                    catch_bg.draw(screen)
                    battle_pkm.draw_battle()
                    pokemon.draw(398, 90)
                    if status_2 == "none":
                        type_text("Enemy " + str(pokemon.name) + " used " + str(used_move_2.name) + "!", 40, 350, 32,
                                  (255, 255, 255))
                    elif status_2 != "none":
                        if animation_counter2 < len(used_move_2.graphics_list_enemy) - 4:
                            type_text("Enemy " + str(pokemon.name) + " used " + str(used_move_2.name) + "!", 40, 350,
                                      32,
                                      (255, 255, 255))
                        else:
                            type_text("It's " + str(status_2) + "!", 40, 350, 32, (255, 255, 255))
                    if battle_pkm.current_hp > 0:
                        pokemon.hp_bar_graphics = health_bar_status(pokemon.current_hp, pokemon.hp, path_hp_bar)
                        pokemon.draw_hp_bar(100, 112)
                    else:
                        pokemon.hp_bar_graphics = health_bar_status(0, pokemon.hp, path_hp_bar)
                        pokemon.draw_hp_bar(100, 112)

                    type_text(pokemon.name, 56, 78, 26, (0, 0, 0))
                    type_text(str(pokemon.level), 251, 78, 26, (0, 0, 0))
                    screen.blit(pokemon.sex_graphics, (pokemon.sex_x, pokemon.sex_y))

                    b_info.draw(360, 235)
                    type_text(battle_pkm.name, 400, 240, 26, (0, 0, 0))
                    type_text(str(battle_pkm.level), 586, 240, 26, (0, 0, 0))
                    screen.blit(battle_pkm.sex_graphics, (526, 246))
                    if battle_pkm.current_hp > 0:
                        battle_pkm.hp_bar_graphics = health_bar_status(battle_pkm.current_hp, battle_pkm.hp,
                                                                       path_hp_bar)
                        battle_pkm.draw_hp_bar(437, 272)
                    else:
                        battle_pkm.hp_bar_graphics = health_bar_status(0, battle_pkm.hp, path_hp_bar)
                        battle_pkm.draw_hp_bar(100, 112)

                    battle_pkm.draw_exp_bar(400, 310)
                    type_text(str(battle_pkm.current_hp), 518, 286, 23, (0, 0, 0))
                    type_text("/", 550, 286, 23, (0, 0, 0))
                    type_text(str(battle_pkm.hp), 572, 286, 23, (0, 0, 0))

                else:
                    if len(pokemon.moves) == 1:
                        attack_number = random.randint(0, 0)
                    elif len(pokemon.moves) == 2:
                        attack_number = random.randint(0, 1)
                    elif len(pokemon.moves) == 3:
                        attack_number = random.randint(0, 2)
                    elif len(pokemon.moves) >= 4:
                        attack_number = random.randint(0, 3)
                    window_state = "enemy turn"

            if animation_counter2 < len(used_move_2.graphics_list_enemy):
                graphics_enemy = used_move_2.graphics_list_enemy[animation_counter2]
                used_move_2.draw(graphics_enemy)

            elif animation_counter2 == len(used_move_2.graphics_list_enemy) + 1:
                pygame.time.wait(800)
                if animation_counter2 >= len(used_move_2.graphics_list_enemy):
                    if pokemon.current_hp > 0 and battle_pkm.current_hp > 0:
                        turn = "player"
                        window_state = "encounter"

                    elif pokemon.current_hp > 0 >= battle_pkm.current_hp:
                        pokemon_exist = False
                        window_state = "game"

                        pygame.mixer.music.load(os.path.join(path_audio, 'road.wav'))
                        pygame.mixer.music.play(-1)
                        up = False
                        down = False
                        right = False
                        left = False
                        steps = 0
                        dx = 0
                        dy = 0
                    elif pokemon.current_hp <= 0 < battle_pkm.current_hp:
                        pokemon_exist = False
                        gained_exp = gain_exp(pokemon.exp_value, pokemon.level, battle_pokemon_list)
                        gain_exp_counter = 0
                        sound_exp_counter = 0
                        window_state = "fainted_info"

            animation_counter2 = animation_counter2 + 1

        elif window_state == "fainted_info":
            catch_bg.draw(screen)
            battle_pkm.draw_battle()
            pokemon.draw(398, 90)
            type_text("Wild " + str(pokemon.name) + " fainted!", 40, 350, 32,
                      (255, 255, 255))
            if pokemon.current_hp > 0:
                pokemon.hp_bar_graphics = health_bar_status(pokemon.current_hp, pokemon.hp, path_hp_bar)
                pokemon.draw_hp_bar(100, 112)
            else:
                pokemon.hp_bar_graphics = health_bar_status(0, pokemon.hp, path_hp_bar)
                pokemon.draw_hp_bar(100, 112)
            type_text(pokemon.name, 56, 78, 26, (0, 0, 0))
            type_text(str(pokemon.level), 251, 78, 26, (0, 0, 0))
            screen.blit(pokemon.sex_graphics, (pokemon.sex_x, pokemon.sex_y))

            b_info.draw(360, 235)
            type_text(battle_pkm.name, 400, 240, 26, (0, 0, 0))
            type_text(str(battle_pkm.level), 586, 240, 26, (0, 0, 0))
            screen.blit(battle_pkm.sex_graphics, (526, 246))
            if battle_pkm.current_hp > 0:
                battle_pkm.hp_bar_graphics = health_bar_status(battle_pkm.current_hp, battle_pkm.hp, path_hp_bar)
                battle_pkm.draw_hp_bar(437, 272)
            battle_pkm.draw_exp_bar(400, 310)
            type_text(str(battle_pkm.current_hp), 518, 286, 23, (0, 0, 0))
            type_text("/", 550, 286, 23, (0, 0, 0))
            type_text(str(battle_pkm.hp), 572, 286, 23, (0, 0, 0))

        elif window_state == "gain_exp":
            if gain_exp_counter < gained_exp:
                if sound_exp_counter == 0:
                    exp_effect = pygame.mixer.Sound(os.path.join(path_audio, 'exp_sound_2.wav'))
                    exp_effect.play()
                gained_exp = gain_exp(pokemon.exp_value, pokemon.level, battle_pokemon_list)
                battle_pkm.exp = battle_pkm.exp + 1
                battle_pkm.exp_bar_graphics = exp_bar_status(battle_pkm.exp, battle_pkm.to_next_level, exp_bar_status)
                battle_pkm.draw_exp_bar(400, 310)
                if battle_pkm.battle_count < 65535:
                    battle_pkm.battle_count = battle_pkm.battle_count + 100
                battle_pkm.to_next_level_exp = battle_pkm.to_next_level - battle_pkm.exp

            sound_exp_counter = sound_exp_counter + 1
            gain_exp_counter = gain_exp_counter + 1

            if gain_exp_counter2 == 0:
                for k in range(0, len(battle_pokemon_list)):
                    if battle_pokemon_list[k] != battle_pkm:
                        battle_pokemon_list[k].exp = battle_pokemon_list[k].exp + gained_exp
                        battle_pokemon_list[k].exp_bar_graphics = exp_bar_status(battle_pokemon_list[k].exp,
                                                                                 battle_pokemon_list[k].to_next_level,
                                                                                 exp_bar_status)
                        if battle_pokemon_list[k].battle_count < 65535:
                            battle_pokemon_list[k].battle_count = battle_pokemon_list[k].battle_count + 100
                        battle_pokemon_list[k].to_next_level_exp = battle_pokemon_list[k].to_next_level - \
                                                                   battle_pokemon_list[k].exp

                for i in range(0, len(battle_pokemon_list)):
                    if battle_pokemon_list[i].to_next_level_exp <= 0:
                        level_up_counter = 0
                        leveling_pokemon = battle_pokemon_list[i]
                        window_state = "level_up"

            gain_exp_counter2 = gain_exp_counter2 + 1
            catch_bg.draw(screen)
            battle_pkm.draw_battle()
            pokemon.draw(398, 90)
            type_text(str(battle_pkm.name) + " gained " + str(gained_exp) + " EXP. Points!", 40, 350, 32,
                      (255, 255, 255))
            if pokemon.current_hp > 0:
                pokemon.hp_bar_graphics = health_bar_status(pokemon.current_hp, pokemon.hp, path_hp_bar)
                pokemon.draw_hp_bar(100, 112)
            else:
                pokemon.hp_bar_graphics = health_bar_status(0, pokemon.hp, path_hp_bar)
                pokemon.draw_hp_bar(100, 112)
            type_text(pokemon.name, 56, 78, 26, (0, 0, 0))
            type_text(str(pokemon.level), 251, 78, 26, (0, 0, 0))
            screen.blit(pokemon.sex_graphics, (pokemon.sex_x, pokemon.sex_y))

            b_info.draw(360, 235)
            type_text(battle_pkm.name, 400, 240, 26, (0, 0, 0))
            type_text(str(battle_pkm.level), 586, 240, 26, (0, 0, 0))
            screen.blit(battle_pkm.sex_graphics, (526, 246))
            if battle_pkm.current_hp > 0:
                battle_pkm.hp_bar_graphics = health_bar_status(battle_pkm.current_hp, battle_pkm.hp, path_hp_bar)
                battle_pkm.draw_hp_bar(437, 272)
            battle_pkm.draw_exp_bar(400, 310)
            type_text(str(battle_pkm.current_hp), 518, 286, 23, (0, 0, 0))
            type_text("/", 550, 286, 23, (0, 0, 0))
            type_text(str(battle_pkm.hp), 572, 286, 23, (0, 0, 0))

        elif window_state == "level_up":
            if level_up_counter == 0:
                revive_effect = pygame.mixer.Sound(os.path.join(path_audio, 'level_sound.wav'))
                revive_effect.play()

                previous_hp = leveling_pokemon.hp
                previous_attack = leveling_pokemon.attack
                previous_defense = leveling_pokemon.defense
                previous_sp_atk = leveling_pokemon.sp_atk
                previous_sp_def = leveling_pokemon.sp_def
                previous_speed = leveling_pokemon.speed

                leveling_pokemon.level = leveling_pokemon.level + 1
                leveling_pokemon.hp, leveling_pokemon.current_hp, leveling_pokemon.attack, leveling_pokemon.current_attack, leveling_pokemon.defense, leveling_pokemon.current_defense, leveling_pokemon.sp_atk, leveling_pokemon.current_sp_atk, leveling_pokemon.sp_def, leveling_pokemon.current_sp_def, leveling_pokemon.speed, leveling_pokemon.current_speed = level_up(
                    leveling_pokemon.level, leveling_pokemon.base_hp, leveling_pokemon.IV_hp, leveling_pokemon.EV_hp,
                    leveling_pokemon.base_attack, leveling_pokemon.IV_attack, leveling_pokemon.EV_attack,
                    leveling_pokemon.base_defense, leveling_pokemon.IV_defense, leveling_pokemon.EV_defense,
                    leveling_pokemon.base_sp_atk, leveling_pokemon.IV_sp_atk, leveling_pokemon.EV_sp_atk,
                    leveling_pokemon.base_sp_def, leveling_pokemon.IV_sp_def, leveling_pokemon.EV_sp_def,
                    leveling_pokemon.base_speed, leveling_pokemon.IV_speed, leveling_pokemon.EV_speed)
                leveling_pokemon.total_exp, leveling_pokemon.next_level, leveling_pokemon.to_next_level = leveling(
                    leveling_pokemon.level)
                leveling_pokemon.exp = 0
                leveling_pokemon.to_next_level_exp = leveling_pokemon.to_next_level - leveling_pokemon.exp
                level_up_counter = level_up_counter + 1

                leveling_pokemon.exp_bar_graphics = exp_bar_status(leveling_pokemon.exp, leveling_pokemon.to_next_level,
                                                                   exp_bar_status)

                new_hp = leveling_pokemon.hp - previous_hp
                new_attack = leveling_pokemon.attack - previous_attack
                new_defense = leveling_pokemon.defense - previous_defense
                new_sp_atk = leveling_pokemon.sp_atk - previous_sp_atk
                new_sp_def = leveling_pokemon.sp_def - previous_sp_def
                new_speed = leveling_pokemon.speed - previous_speed

                pokemon_exist = False

            catch_bg.draw(screen)
            battle_pkm.draw_battle()
            pokemon.draw(398, 90)
            type_text(str(leveling_pokemon.name) + " grew to LV. " + str(leveling_pokemon.level), 40, 350, 32,
                      (255, 255, 255))
            if pokemon.current_hp > 0:
                pokemon.hp_bar_graphics = health_bar_status(pokemon.current_hp, pokemon.hp, path_hp_bar)
                pokemon.draw_hp_bar(100, 112)
            else:
                pokemon.hp_bar_graphics = health_bar_status(0, pokemon.hp, path_hp_bar)
                pokemon.draw_hp_bar(100, 112)
            type_text(pokemon.name, 56, 78, 26, (0, 0, 0))
            type_text(str(pokemon.level), 251, 78, 26, (0, 0, 0))
            screen.blit(pokemon.sex_graphics, (pokemon.sex_x, pokemon.sex_y))

            b_info.draw(360, 235)
            type_text(battle_pkm.name, 400, 240, 26, (0, 0, 0))
            type_text(str(battle_pkm.level), 586, 240, 26, (0, 0, 0))
            screen.blit(battle_pkm.sex_graphics, (526, 246))
            if battle_pkm.current_hp > 0:
                battle_pkm.hp_bar_graphics = health_bar_status(battle_pkm.current_hp, battle_pkm.hp, path_hp_bar)
                battle_pkm.draw_hp_bar(437, 272)
            battle_pkm.draw_exp_bar(400, 310)
            type_text(str(battle_pkm.current_hp), 518, 286, 23, (0, 0, 0))
            type_text("/", 550, 286, 23, (0, 0, 0))
            type_text(str(battle_pkm.hp), 572, 286, 23, (0, 0, 0))

            level_up_menu.draw(screen)
            type_text("MAX. HP", 400, 235, 25, (0, 0, 0))
            type_text("+", 550, 230, 30, (0, 0, 0))
            type_text(str(new_hp), 590, 230, 30, (0, 0, 0))
            type_text("ATTACK", 400, 270, 25, (0, 0, 0))
            type_text("+", 550, 265, 30, (0, 0, 0))
            type_text(str(new_attack), 590, 265, 30, (0, 0, 0))
            type_text("DEFENSE", 400, 305, 25, (0, 0, 0))
            type_text("+", 550, 300, 30, (0, 0, 0))
            type_text(str(new_defense), 590, 300, 30, (0, 0, 0))
            type_text("SP. ATK", 400, 340, 25, (0, 0, 0))
            type_text("+", 550, 335, 30, (0, 0, 0))
            type_text(str(new_sp_atk), 590, 335, 30, (0, 0, 0))
            type_text("SP. DEF", 400, 375, 25, (0, 0, 0))
            type_text("+", 550, 370, 30, (0, 0, 0))
            type_text(str(new_sp_def), 590, 370, 30, (0, 0, 0))
            type_text("SPEED", 400, 410, 25, (0, 0, 0))
            type_text("+", 550, 405, 30, (0, 0, 0))
            type_text(str(new_speed), 590, 405, 30, (0, 0, 0))

        elif window_state == "level_up2":
            catch_bg.draw(screen)
            battle_pkm.draw_battle()
            pokemon.draw(398, 90)
            type_text(str(leveling_pokemon.name) + " grew to LV. " + str(leveling_pokemon.level), 40, 350, 32,
                      (255, 255, 255))
            if pokemon.current_hp > 0:
                pokemon.hp_bar_graphics = health_bar_status(pokemon.current_hp, pokemon.hp, path_hp_bar)
                pokemon.draw_hp_bar(100, 112)
            else:
                pokemon.hp_bar_graphics = health_bar_status(0, pokemon.hp, path_hp_bar)
                pokemon.draw_hp_bar(100, 112)
            type_text(pokemon.name, 56, 78, 26, (0, 0, 0))
            type_text(str(pokemon.level), 251, 78, 26, (0, 0, 0))
            screen.blit(pokemon.sex_graphics, (pokemon.sex_x, pokemon.sex_y))

            b_info.draw(360, 235)
            type_text(battle_pkm.name, 400, 240, 26, (0, 0, 0))
            type_text(str(battle_pkm.level), 586, 240, 26, (0, 0, 0))
            screen.blit(battle_pkm.sex_graphics, (526, 246))
            if battle_pkm.current_hp > 0:
                battle_pkm.hp_bar_graphics = health_bar_status(battle_pkm.current_hp, battle_pkm.hp, path_hp_bar)
                battle_pkm.draw_hp_bar(437, 272)
            battle_pkm.draw_exp_bar(400, 310)
            type_text(str(battle_pkm.current_hp), 518, 286, 23, (0, 0, 0))
            type_text("/", 550, 286, 23, (0, 0, 0))
            type_text(str(battle_pkm.hp), 572, 286, 23, (0, 0, 0))

            level_up_menu.draw(screen)
            type_text("MAX. HP", 400, 235, 25, (0, 0, 0))
            type_text(str(leveling_pokemon.hp), 590, 230, 30, (0, 0, 0))
            type_text("ATTACK", 400, 270, 25, (0, 0, 0))
            type_text(str(leveling_pokemon.attack), 590, 265, 30, (0, 0, 0))
            type_text("DEFENSE", 400, 305, 25, (0, 0, 0))
            type_text(str(leveling_pokemon.defense), 590, 300, 30, (0, 0, 0))
            type_text("SP. ATK", 400, 340, 25, (0, 0, 0))
            type_text(str(leveling_pokemon.sp_atk), 590, 335, 30, (0, 0, 0))
            type_text("SP. DEF", 400, 375, 25, (0, 0, 0))
            type_text(str(leveling_pokemon.sp_def), 590, 370, 30, (0, 0, 0))
            type_text("SPEED", 400, 410, 25, (0, 0, 0))
            type_text(str(leveling_pokemon.speed), 590, 405, 30, (0, 0, 0))

            learning_counter = 0
            for a in range(0, len(leveling_pokemon.new_attack_level)):
                if leveling_pokemon.new_attack_level[a] == leveling_pokemon.level:
                    if len(leveling_pokemon.moves) < 4:
                        new_attack = leveling_pokemon.new_attack[a]
                        window_state = "attack_learning_1"
                    elif len(leveling_pokemon.moves) == 4:
                        new_attack = leveling_pokemon.new_attack[a]
                        window_state = "attack_learning_2_1"

        elif window_state == "attack_learning_1":
            if learning_counter == 0:
                leveling_pokemon.moves.append(Moves(new_attack, path_audio, path_moves_animations))
            learning_counter = learning_counter + 1
            catch_bg.draw(screen)
            battle_pkm.draw_battle()
            pokemon.draw(398, 90)
            type_text(str(leveling_pokemon.name) + " learned " + str(new_attack) + "!", 40, 350, 32, (255, 255, 255))
            if pokemon.current_hp > 0:
                pokemon.hp_bar_graphics = health_bar_status(pokemon.current_hp, pokemon.hp, path_hp_bar)
                pokemon.draw_hp_bar(100, 112)
            else:
                pokemon.hp_bar_graphics = health_bar_status(0, pokemon.hp, path_hp_bar)
                pokemon.draw_hp_bar(100, 112)
            type_text(pokemon.name, 56, 78, 26, (0, 0, 0))
            type_text(str(pokemon.level), 251, 78, 26, (0, 0, 0))
            screen.blit(pokemon.sex_graphics, (pokemon.sex_x, pokemon.sex_y))

            b_info.draw(360, 235)
            type_text(battle_pkm.name, 400, 240, 26, (0, 0, 0))
            type_text(str(battle_pkm.level), 586, 240, 26, (0, 0, 0))
            screen.blit(battle_pkm.sex_graphics, (526, 246))
            if battle_pkm.current_hp > 0:
                battle_pkm.hp_bar_graphics = health_bar_status(battle_pkm.current_hp, battle_pkm.hp, path_hp_bar)
                battle_pkm.draw_hp_bar(437, 272)
            battle_pkm.draw_exp_bar(400, 310)
            type_text(str(battle_pkm.current_hp), 518, 286, 23, (0, 0, 0))
            type_text("/", 550, 286, 23, (0, 0, 0))
            type_text(str(battle_pkm.hp), 572, 286, 23, (0, 0, 0))

        elif window_state == "attack_learning_2_1":
            change_skill_bg.draw(screen)
            leveling_pokemon.draw(270, 130)
            type_text(str(leveling_pokemon.name) + " is trying to learn " + str(new_attack) + ".", 40, 350, 32,
                      (255, 255, 255))
        elif window_state == "attack_learning_2_2":
            change_skill_bg.draw(screen)
            leveling_pokemon.draw(270, 130)
            type_text("But " + str(leveling_pokemon.name) + " can't learn", 40, 350, 32, (255, 255, 255))
            type_text("more than four moves.", 40, 390, 32, (255, 255, 255))
        elif window_state == "attack_learning_2_3":
            change_skill_bg.draw(screen)
            leveling_pokemon.draw(270, 130)
            type_text("Delate a move to make", 40, 350, 32, (255, 255, 255))
            type_text("room for " + str(new_attack) + "?", 40, 390, 32, (255, 255, 255))
            change_skill_m.draw(screen)
            type_text("Yes", 560, 230, 32, (0, 0, 0))
            type_text("No", 560, 270, 32, (0, 0, 0))
            change_skill_c.draw()
        elif window_state == "attack_learning_2_4":
            screen.fill((0, 0, 0))
            move_counter = 0
            pkm_summary.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_summary_5.png"))
            pkm_summary.draw()
            pkm_summary.type_text_summary("KNOWN MOVES")
            type_text("PICK", 464, 34, 20, (255, 255, 255))
            type_text("SWITCH", 552, 34, 20, (255, 255, 255))
            type_text(str(leveling_pokemon.name), 110, 74, 30, (255, 255, 255))
            screen.blit(leveling_pokemon.sex_graphics, (264, 84))
            leveling_pokemon.draw_menu(44, 100)
            moves_learn_cursor.draw()
            if len(leveling_pokemon.type) == 1:
                pkm_type = PokemonType(leveling_pokemon.type[0], path_visual_elements)
                pkm_type.graphics = pygame.transform.scale(pkm_type.graphics, (83, 31))
                pkm_type.draw(140, 114)
            else:
                pkm_type_1 = PokemonType(leveling_pokemon.type[0], path_visual_elements)
                pkm_type_2 = PokemonType(leveling_pokemon.type[1], path_visual_elements)
                pkm_type_1.graphics = pygame.transform.scale(pkm_type_1.graphics, (83, 31))
                pkm_type_2.graphics = pygame.transform.scale(pkm_type_2.graphics, (83, 31))
                pkm_type_1.draw(110, 114)
                pkm_type_2.draw(200, 114)

            learning_move = Moves(new_attack, path_audio, path_moves_animations)

            if len(leveling_pokemon.moves) == 4:
                for m in range(len(leveling_pokemon.moves)):
                    type_text(str(leveling_pokemon.moves[m].name), 430, 83 + (move_counter * 74), 32, (0, 0, 0))
                    type_text("pp", 536, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text(str(leveling_pokemon.moves[m].current_pp), 560, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text("/", 590, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text(str(leveling_pokemon.moves[m].pp), 600, 116 + (move_counter * 74), 25, (0, 0, 0))
                    move_type = PokemonType(leveling_pokemon.moves[m].type, path_visual_elements)
                    move_type.graphics = pygame.transform.scale(move_type.graphics, (83, 31))
                    move_type.draw(330, 85 + (move_counter * 74))
                    move_counter = move_counter + 1

            type_text(str(learning_move.name), 430, 83 + (4 * 74), 32, (0, 0, 0))
            type_text("pp", 536, 116 + (4 * 74), 25, (0, 0, 0))
            type_text(str(learning_move.current_pp), 560, 116 + (4 * 74), 25, (0, 0, 0))
            type_text("/", 590, 116 + (4 * 74), 25, (0, 0, 0))
            type_text(str(learning_move.pp), 600, 116 + (4 * 74), 25, (0, 0, 0))
            move_type = PokemonType(learning_move.type, path_visual_elements)
            move_type.graphics = pygame.transform.scale(move_type.graphics, (83, 31))
            move_type.draw(330, 85 + (4 * 74))

            if moves_learn_cursor.y == 75 and len(leveling_pokemon.moves) >= 1:
                type_text(str(leveling_pokemon.moves[0].power), 170, 175, 32, (0, 0, 0))
                type_text(str(leveling_pokemon.moves[0].accuracy), 156, 214, 32, (0, 0, 0))
                type_text(str(leveling_pokemon.moves[0].effect[0:25]), 24, 288, 25, (0, 0, 0))
                type_text(str(leveling_pokemon.moves[0].effect[25:50]), 24, 328, 25, (0, 0, 0))
                type_text(str(leveling_pokemon.moves[0].effect[50:len(leveling_pokemon.moves[0].effect)]), 24, 368, 25,
                          (0, 0, 0))
            elif moves_learn_cursor.y == 149 and len(leveling_pokemon.moves) >= 2:
                type_text(str(leveling_pokemon.moves[1].power), 170, 175, 32, (0, 0, 0))
                type_text(str(leveling_pokemon.moves[1].accuracy), 156, 214, 32, (0, 0, 0))
                type_text(str(leveling_pokemon.moves[1].effect[0:25]), 24, 288, 25, (0, 0, 0))
                type_text(str(leveling_pokemon.moves[1].effect[25:50]), 24, 328, 25, (0, 0, 0))
                type_text(str(leveling_pokemon.moves[1].effect[50:len(leveling_pokemon.moves[1].effect)]), 24, 368, 25,
                          (0, 0, 0))
            elif moves_learn_cursor.y == 223 and len(leveling_pokemon.moves) >= 3:
                type_text(str(leveling_pokemon.moves[2].power), 170, 175, 32, (0, 0, 0))
                type_text(str(leveling_pokemon.moves[2].accuracy), 156, 214, 32, (0, 0, 0))
                type_text(str(leveling_pokemon.moves[2].effect[0:25]), 24, 288, 25, (0, 0, 0))
                type_text(str(leveling_pokemon.moves[2].effect[25:50]), 24, 328, 25, (0, 0, 0))
                type_text(str(leveling_pokemon.moves[2].effect[50:len(leveling_pokemon.moves[2].effect)]), 24, 368, 25,
                          (0, 0, 0))
            elif moves_learn_cursor.y == 297 and len(leveling_pokemon.moves) >= 4:
                type_text(str(leveling_pokemon.moves[3].power), 170, 175, 32, (0, 0, 0))
                type_text(str(leveling_pokemon.moves[3].accuracy), 156, 214, 32, (0, 0, 0))
                type_text(str(leveling_pokemon.moves[3].effect[0:25]), 24, 288, 25, (0, 0, 0))
                type_text(str(leveling_pokemon.moves[3].effect[25:50]), 24, 328, 25, (0, 0, 0))
                type_text(str(leveling_pokemon.moves[3].effect[50:len(leveling_pokemon.moves[3].effect)]), 24, 368, 25,
                          (0, 0, 0))
            elif moves_learn_cursor.y == 371:
                type_text(str(learning_move.power), 170, 175, 32, (0, 0, 0))
                type_text(str(learning_move.accuracy), 156, 214, 32, (0, 0, 0))
                type_text(str(learning_move.effect[0:25]), 24, 288, 25, (0, 0, 0))
                type_text(str(learning_move.effect[25:50]), 24, 328, 25, (0, 0, 0))
                type_text(str(learning_move.effect[50:len(learning_move.effect)]), 24, 368, 25, (0, 0, 0))

        elif window_state == "attack_learning_2_5":
            change_skill_bg.draw(screen)
            leveling_pokemon.draw(270, 130)
            type_text("1, 2, and ... ... ... Poof!", 40, 350, 32, (255, 255, 255))
        elif window_state == "attack_learning_2_6":
            change_skill_bg.draw(screen)
            leveling_pokemon.draw(270, 130)
            type_text(str(leveling_pokemon.name) + " forgot " + str(move_to_change.name) + ".", 40, 350, 32,
                      (255, 255, 255))
        elif window_state == "attack_learning_2_7":
            change_skill_bg.draw(screen)
            leveling_pokemon.draw(270, 130)
            type_text("And...", 40, 350, 32, (255, 255, 255))
        elif window_state == "attack_learning_2_8":
            change_skill_bg.draw(screen)
            leveling_pokemon.draw(270, 130)
            type_text(str(leveling_pokemon.name) + " learned " + str(learning_move.name) + ".", 40, 350, 32,
                      (255, 255, 255))
        elif window_state == "stop_attack_learning":
            change_skill_bg.draw(screen)
            leveling_pokemon.draw(270, 130)
            type_text("Stop learning", 40, 350, 32, (255, 255, 255))
            type_text(str(new_attack) + "?", 40, 390, 32, (255, 255, 255))
            change_skill_m.draw(screen)
            type_text("Yes", 560, 230, 32, (0, 0, 0))
            type_text("No", 560, 270, 32, (0, 0, 0))
            change_skill_c_2.draw()
        elif window_state == "stop_attack_learning_2":
            change_skill_bg.draw(screen)
            leveling_pokemon.draw(270, 130)
            type_text(str(leveling_pokemon.name) + " did not learn", 40, 350, 32, (255, 255, 255))
            type_text(str(new_attack) + ".", 40, 390, 32, (255, 255, 255))

        elif window_state == "enter_menu":
            menu.draw()
            type_text("POKEDEX", 50, 30, 20, (0, 0, 0))
            type_text("POKEMON", 50, 70, 20, (0, 0, 0))
            type_text("BAG", 50, 110, 20, (0, 0, 0))
            type_text("PLAYER", 50, 150, 20, (0, 0, 0))
            type_text("SAVE", 50, 190, 20, (0, 0, 0))
            type_text("OPTION", 50, 230, 20, (0, 0, 0))
            type_text("EXIT", 50, 270, 20, (0, 0, 0))

            cursor_menu.draw()

        elif window_state == "option":
            screen.fill((0, 0, 0))
            o1.draw()
            o2.draw()
            o3.draw()
            type_text("PICK", 340, 34, 20, (255, 255, 255))
            type_text("SWITCH", 420, 34, 20, (255, 255, 255))
            type_text("CANCEL", 552, 34, 20, (255, 255, 255))
            type_text("OPTION", 80, 100, 30, (0, 0, 0))

            o_cursor.draw()

            type_text("TEXT SPEED", 80, 194, 24, (0, 0, 0))
            type_text("MID", 400, 194, 24, (255, 0, 0))
            type_text("BATTLE SCENE", 80, 228, 24, (0, 0, 0))
            type_text("ON", 400, 228, 24, (255, 0, 0))
            type_text("BATTLE STYLE", 80, 262, 24, (0, 0, 0))
            type_text("SHIFT", 400, 262, 24, (255, 0, 0))
            type_text("SOUND", 80, 296, 24, (0, 0, 0))
            type_text("MONO", 400, 296, 24, (255, 0, 0))
            type_text("BUTTON MODE", 80, 330, 24, (0, 0, 0))
            type_text("HELP", 400, 330, 24, (255, 0, 0))
            type_text("FRAME", 80, 364, 24, (0, 0, 0))
            type_text("TYPE 1", 400, 364, 24, (255, 0, 0))
            type_text("CANCLE", 80, 398, 24, (0, 0, 0))

        elif window_state == "bag_items":
            screen.fill((0, 0, 0))
            inv.draw()
            bag.graphics = pygame.image.load(os.path.join(path_visual_elements, "b1.png"))
            bag.draw()
            bag.type_text_backpack("ITEMS")
            if len(player.items) != 0:
                for p in range(0, len(player.items)):
                    if player.items[p].quantity != 0:
                        type_text(str(player.items[p].name), 265, (p + 1) * 50, 20, (0, 0, 0))
                        type_text("x " + str(player.items[p].quantity), 530, (p + 1) * 50, 20, (0, 0, 0))
            cursor_bag.draw()
            if cursor_bag.y == 53 and window_state == "bag_items" and player.items[0].quantity != 0 and len(
                    player.items) > 0:
                type_text(str(player.items[0].description[0:50]), 110, 355, 26, (255, 255, 255))
                type_text(str(player.items[0].description[50:len(player.items[0].description)]), 110, 390, 26,
                          (255, 255, 255))
                player.items[0].draw()
            elif len(player.items) > 1 and cursor_bag.y == 98 and window_state == "bag_items" and player.items[
                1].quantity != 0:
                type_text(str(player.items[1].description[0:50]), 110, 355, 26, (255, 255, 255))
                type_text(str(player.items[1].description[50:len(player.items[1].description)]), 110, 390, 26,
                          (255, 255, 255))
                player.items[1].draw()
            elif len(player.items) > 2 and cursor_bag.y == 143 and window_state == "bag_items" and player.items[
                2].quantity != 0:
                type_text(str(player.items[2].description[0:50]), 110, 355, 26, (255, 255, 255))
                type_text(str(player.items[2].description[50:len(player.items[2].description)]), 110, 390, 26,
                          (255, 255, 255))
                player.items[2].draw()
            elif len(player.items) > 3 and cursor_bag.y == 188 and window_state == "bag_items" and player.items[
                3].quantity != 0:
                type_text(str(player.items[3].description[0:50]), 110, 355, 26, (255, 255, 255))
                type_text(str(player.items[3].description[50:len(player.items[3].description)]), 110, 390, 26,
                          (255, 255, 255))
                player.items[3].draw()
            elif len(player.items) > 4 and cursor_bag.y == 233 and window_state == "bag_items" and player.items[
                4].quantity != 0:
                type_text(str(player.items[4].description[0:50]), 110, 355, 26, (255, 255, 255))
                type_text(str(player.items[4].description[50:len(player.items[3].description)]), 110, 390, 26,
                          (255, 255, 255))
                player.items[4].draw()

        elif window_state == "bag_key_items":
            screen.fill((0, 0, 0))
            inv.draw()
            bag.graphics = pygame.image.load(os.path.join(path_visual_elements, "b2.png"))
            bag.draw()
            bag.type_text_backpack("KEY ITEMS")
            if len(player.key_items) != 0:
                for p in range(0, len(player.key_items)):
                    if player.key_items[p].quantity != 0:
                        type_text(str(player.key_items[p].name), 265, (p + 1) * 50, 20, (0, 0, 0))
                        type_text("x " + str(player.key_items[p].quantity), 530, (p + 1) * 50, 20, (0, 0, 0))
                        if player.key_items[p] == player.registered_item:
                            register_item.draw(530, (p + 1) * 50)
            cursor_bag.draw()
            if len(player.key_items) > 0 and cursor_bag.y == 53 and window_state == "bag_key_items" and \
                    player.key_items[
                        0].quantity != 0:
                type_text(str(player.key_items[0].description[0:50]), 110, 355, 26, (255, 255, 255))
                type_text(str(player.key_items[0].description[50:len(player.key_items[0].description)]), 110, 390, 26,
                          (255, 255, 255))
                player.key_items[0].draw()
            elif len(player.key_items) > 1 and cursor_bag.y == 98 and window_state == "bag_key_items" and \
                    player.key_items[
                        1].quantity != 0:
                type_text(str(player.key_items[1].description[0:50]), 110, 355, 26, (255, 255, 255))
                type_text(str(player.key_items[1].description[50:len(player.key_items[1].description)]), 110, 390, 26,
                          (255, 255, 255))
                player.key_items[1].draw()
            elif len(player.key_items) > 2 and cursor_bag.y == 143 and window_state == "bag_key_items" and \
                    player.key_items[
                        2].quantity != 0:
                type_text(str(player.key_items[2].description[0:50]), 110, 355, 26, (255, 255, 255))
                type_text(str(player.key_items[2].description[50:len(player.key_items[2].description)]), 110, 390, 26,
                          (255, 255, 255))
                player.key_items[2].draw()
            elif len(player.key_items) > 3 and cursor_bag.y == 188 and window_state == "bag_key_items" and \
                    player.key_items[
                        3].quantity != 0:
                type_text(str(player.key_items[3].description[0:50]), 110, 355, 26, (255, 255, 255))
                type_text(str(player.key_items[3].description[50:len(player.key_items[3].description)]), 110, 390, 26,
                          (255, 255, 255))
                player.key_items[3].draw()
            elif len(player.key_items) > 4 and cursor_bag.y == 233 and window_state == "bag_key_items" and \
                    player.key_items[
                        4].quantity != 0:
                type_text(str(player.key_items[4].description[0:50]), 110, 355, 26, (255, 255, 255))
                type_text(str(player.key_items[4].description[50:len(player.key_items[3].description)]), 110, 390, 26,
                          (255, 255, 255))
                player.key_items[4].draw()

        elif window_state == "bag_pokeballs":
            screen.fill((0, 0, 0))
            inv.draw()
            bag.graphics = pygame.image.load(os.path.join(path_visual_elements, "b3.png"))
            bag.draw()
            bag.type_text_backpack("POKE BALLS")
            if len(player.pokeballs) != 0:
                for p in range(0, len(player.pokeballs)):
                    if player.pokeballs[p].quantity != 0:
                        type_text(str(player.pokeballs[p].name), 265, (p + 1) * 50, 20, (0, 0, 0))
                        type_text("x " + str(player.pokeballs[p].quantity), 530, (p + 1) * 50, 20, (0, 0, 0))
            cursor_bag.draw()
            if len(player.pokeballs) > 0 and cursor_bag.y == 53 and window_state == "bag_pokeballs" and \
                    player.pokeballs[
                        0].quantity != 0:
                type_text(str(player.pokeballs[0].description[0:50]), 110, 350, 24, (255, 255, 255))
                type_text(str(player.pokeballs[0].description[50:100]), 110, 375, 24, (255, 255, 255))
                type_text(str(player.pokeballs[0].description[100:len(player.pokeballs[0].description)]), 110, 400, 24,
                          (255, 255, 255))
                player.pokeballs[0].draw()
            elif len(player.pokeballs) > 1 and cursor_bag.y == 98 and window_state == "bag_pokeballs" and \
                    player.pokeballs[
                        1].quantity != 0:
                type_text(str(player.pokeballs[1].description[0:50]), 110, 350, 24, (255, 255, 255))
                type_text(str(player.pokeballs[1].description[50:100]), 110, 375, 24, (255, 255, 255))
                type_text(str(player.pokeballs[1].description[100:len(player.pokeballs[1].description)]), 110, 400, 24,
                          (255, 255, 255))
                player.pokeballs[1].draw()
            elif len(player.pokeballs) > 2 and cursor_bag.y == 143 and window_state == "bag_pokeballs" and \
                    player.pokeballs[
                        2].quantity != 0:
                type_text(str(player.pokeballs[2].description[0:50]), 110, 350, 24, (255, 255, 255))
                type_text(str(player.pokeballs[2].description[50:100]), 110, 375, 24, (255, 255, 255))
                type_text(str(player.pokeballs[2].description[100:len(player.pokeballs[2].description)]), 110, 400, 24,
                          (255, 255, 255))
                player.pokeballs[2].draw()
            elif len(player.pokeballs) > 3 and cursor_bag.y == 188 and window_state == "bag_pokeballs" and \
                    player.pokeballs[
                        3].quantity != 0:
                type_text(str(player.pokeballs[3].description[0:50]), 110, 350, 24, (255, 255, 255))
                type_text(str(player.pokeballs[3].description[50:100]), 110, 375, 24, (255, 255, 255))
                type_text(str(player.pokeballs[3].description[100:len(player.pokeballs[3].description)]), 110, 400, 24,
                          (255, 255, 255))
                player.pokeballs[3].draw()
            elif len(player.pokeballs) > 4 and cursor_bag.y == 233 and window_state == "bag_pokeballs" and \
                    player.pokeballs[
                        4].quantity != 0:
                type_text(str(player.pokeballs[4].description[0:50]), 110, 350, 24, (255, 255, 255))
                type_text(str(player.pokeballs[4].description[50:100]), 110, 375, 24, (255, 255, 255))
                type_text(str(player.pokeballs[4].description[100:len(player.pokeballs[4].description)]), 110, 400, 24,
                          (255, 255, 255))
                player.pokeballs[4].draw()

        elif window_state == "pokemon_menu":
            screen.fill((0, 0, 0))
            pokemon_selection_menu.draw()
            type_text("Choose a POKEMON.", 50, 394, 28, (0, 0, 0))
            if pkm_menu_cursor.x == 482 and pkm_menu_cursor.y == 401:
                pokemon_menu_d1.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_d3.png"))
                menu_d1_x = 488
                menu_d1_y = 378
            else:
                pokemon_menu_d1.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_d1.png"))
                menu_d1_x = 488
                menu_d1_y = 384
            pokemon_menu_d1.draw(menu_d1_x, menu_d1_y)
            type_text("CANCEL", 544, 396, 26, (255, 255, 255))
            poke_counter = 1
            pkm_menu_cursor.draw()

            if len(player.main_pokemon) == 1:
                if pkm_menu_cursor.x == 8 and pkm_menu_cursor.y == 150:
                    selection.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s4.png"))
                    selection.x = 7
                    selection.y = 75
                else:
                    selection.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s3.png"))
                    selection.x = 6
                    selection.y = 80
                selection.draw()
                player.main_pokemon[0].draw_menu(40, 125)
                type_text(str(player.main_pokemon[0].level), 134, 146, 25, (255, 255, 255))
                type_text(str(player.main_pokemon[0].current_hp), 130, 190, 25, (255, 255, 255))
                type_text(str(player.main_pokemon[0].hp), 180, 190, 25, (255, 255, 255))
                screen.blit(player.main_pokemon[0].sex_graphics, (185, 152))
                type_text(str(player.main_pokemon[0].name), 100, 120, 25, (255, 255, 255))
                player.main_pokemon[0].draw_hp_bar(47, 177)
                if player.main_pokemon[0].holding_item != "none":
                    held_item_icon.draw(66, 160, screen)

            show_pokemons_in_menu_if_more_than_one(player, pkm_menu_cursor, pkm_menu_1, pkm_menu_2, pkm_menu_3,
                                                   pkm_menu_4, pkm_menu_5, screen, held_item_icon, path_visual_elements)

        elif window_state == "selected_pokemon":
            selected_pokemon_script = pygame.image.load(os.path.join(path_visual_elements, "selected_pokemon_1.png"))
            selected_pokemon_menu = pygame.image.load(os.path.join(path_visual_elements, "selected_pokemon_2.png"))
            screen.blit(selected_pokemon_script, (4, 373))
            screen.blit(selected_pokemon_menu, (440, 252))
            type_text("Do what with this POKEMON?", 50, 394, 28, (0, 0, 0))
            type_text("SUMMARY", 500, 280, 20, (0, 0, 0))  # 40
            type_text("SWITCH", 500, 320, 20, (0, 0, 0))
            type_text("ITEM", 500, 360, 20, (0, 0, 0))
            type_text("CANCEL", 500, 400, 20, (0, 0, 0))
            selected_pkm_cursor_1.draw()

        elif window_state == "pokemon_item":
            screen.fill((0, 0, 0))
            pokemon_selection_menu.draw()
            type_text("Choose a POKEMON.", 50, 394, 28, (0, 0, 0))
            if pkm_menu_cursor.x == 482 and pkm_menu_cursor.y == 401:
                pokemon_menu_d1.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_d3.png"))
                menu_d1_x = 488
                menu_d1_y = 378
            else:
                pokemon_menu_d1.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_d1.png"))
                menu_d1_x = 488
                menu_d1_y = 384
            pokemon_menu_d1.draw(menu_d1_x, menu_d1_y)
            type_text("CANCEL", 544, 396, 26, (255, 255, 255))
            poke_counter = 1
            pkm_menu_cursor.draw()

            if len(player.main_pokemon) == 1:
                if pkm_menu_cursor.x == 8 and pkm_menu_cursor.y == 150:
                    selection.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s4.png"))
                    selection.x = 7
                    selection.y = 75
                else:
                    selection.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s3.png"))
                    selection.x = 6
                    selection.y = 80
                selection.draw()
                player.main_pokemon[0].draw_menu(40, 125)
                type_text(str(player.main_pokemon[0].level), 134, 146, 25, (255, 255, 255))
                type_text(str(player.main_pokemon[0].current_hp), 130, 190, 25, (255, 255, 255))
                type_text(str(player.main_pokemon[0].hp), 180, 190, 25, (255, 255, 255))
                screen.blit(player.main_pokemon[0].sex_graphics, (185, 152))
                type_text(str(player.main_pokemon[0].name), 100, 120, 25, (255, 255, 255))
                player.main_pokemon[0].draw_hp_bar(47, 177)
                if player.main_pokemon[0].holding_item != "none":
                    held_item_icon.draw(66, 160, screen)

            show_pokemons_in_menu_if_more_than_one(player, pkm_menu_cursor, pkm_menu_1, pkm_menu_2, pkm_menu_3,
                                                   pkm_menu_4, pkm_menu_5, screen, held_item_icon, path_visual_elements)

            pkm_item_menu.draw(488, 292)

            type_text("GIVE", 528, 315, 25, (0, 0, 0))
            type_text("TAKE", 528, 355, 25, (0, 0, 0))
            type_text("CANCEL", 528, 395, 25, (0, 0, 0))
            pokemon_item_cursor.draw()

        elif window_state == "pokemon_item_take":
            screen.fill((0, 0, 0))
            pokemon_selection_menu.draw()
            type_text("Choose a POKEMON.", 50, 394, 28, (0, 0, 0))
            if pkm_menu_cursor.x == 482 and pkm_menu_cursor.y == 401:
                pokemon_menu_d1.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_d3.png"))
                menu_d1_x = 488
                menu_d1_y = 378
            else:
                pokemon_menu_d1.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_d1.png"))
                menu_d1_x = 488
                menu_d1_y = 384
            pokemon_menu_d1.draw(menu_d1_x, menu_d1_y)
            type_text("CANCEL", 544, 396, 26, (255, 255, 255))
            poke_counter = 1
            pkm_menu_cursor.draw()

            if len(player.main_pokemon) == 1:
                if pkm_menu_cursor.x == 8 and pkm_menu_cursor.y == 150:
                    selection.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s4.png"))
                    selection.x = 7
                    selection.y = 75
                else:
                    selection.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s3.png"))
                    selection.x = 6
                    selection.y = 80
                selection.draw()
                player.main_pokemon[0].draw_menu(40, 125)
                type_text(str(player.main_pokemon[0].level), 134, 146, 25, (255, 255, 255))
                type_text(str(player.main_pokemon[0].current_hp), 130, 190, 25, (255, 255, 255))
                type_text(str(player.main_pokemon[0].hp), 180, 190, 25, (255, 255, 255))
                screen.blit(player.main_pokemon[0].sex_graphics, (185, 152))
                type_text(str(player.main_pokemon[0].name), 100, 120, 25, (255, 255, 255))
                player.main_pokemon[0].draw_hp_bar(47, 177)
                if player.main_pokemon[0].holding_item != "none":
                    held_item_icon.draw(66, 160, screen)

            show_pokemons_in_menu_if_more_than_one(player, pkm_menu_cursor, pkm_menu_1, pkm_menu_2, pkm_menu_3,
                                                   pkm_menu_4, pkm_menu_5, screen, held_item_icon, path_visual_elements)

            c_use_item.draw(0, 320)
            type_text("Recived the " + str(tmp_holding_item.name), 24, 340, 30, (0, 0, 0))
            type_text("from " + str(selected_pkm.name) + ".", 24, 380, 30, (0, 0, 0))

        elif window_state == "pokemon_cannot_take_item":
            screen.fill((0, 0, 0))
            pokemon_selection_menu.draw()
            type_text("Choose a POKEMON.", 50, 394, 28, (0, 0, 0))
            if pkm_menu_cursor.x == 482 and pkm_menu_cursor.y == 401:
                pokemon_menu_d1.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_d3.png"))
                menu_d1_x = 488
                menu_d1_y = 378
            else:
                pokemon_menu_d1.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_d1.png"))
                menu_d1_x = 488
                menu_d1_y = 384
            pokemon_menu_d1.draw(menu_d1_x, menu_d1_y)
            type_text("CANCEL", 544, 396, 26, (255, 255, 255))
            poke_counter = 1
            pkm_menu_cursor.draw()

            if len(player.main_pokemon) == 1:
                if pkm_menu_cursor.x == 8 and pkm_menu_cursor.y == 150:
                    selection.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s4.png"))
                    selection.x = 7
                    selection.y = 75
                else:
                    selection.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s3.png"))
                    selection.x = 6
                    selection.y = 80
                selection.draw()
                player.main_pokemon[0].draw_menu(40, 125)
                type_text(str(player.main_pokemon[0].level), 134, 146, 25, (255, 255, 255))
                type_text(str(player.main_pokemon[0].current_hp), 130, 190, 25, (255, 255, 255))
                type_text(str(player.main_pokemon[0].hp), 180, 190, 25, (255, 255, 255))
                screen.blit(player.main_pokemon[0].sex_graphics, (185, 152))
                type_text(str(player.main_pokemon[0].name), 100, 120, 25, (255, 255, 255))
                player.main_pokemon[0].draw_hp_bar(47, 177)
                if player.main_pokemon[0].holding_item != "none":
                    held_item_icon.draw(66, 160, screen)

            show_pokemons_in_menu_if_more_than_one(player, pkm_menu_cursor, pkm_menu_1, pkm_menu_2, pkm_menu_3,
                                                   pkm_menu_4, pkm_menu_5, screen, held_item_icon, path_visual_elements)

            c_use_item.draw(0, 320)
            type_text(str(selected_pkm.name) + " isn't holding", 24, 340, 30, (0, 0, 0))
            type_text("anything.", 24, 380, 30, (0, 0, 0))

        elif window_state == "switch_pokemon":
            screen.fill((0, 0, 0))
            pokemon_selection_menu.draw()
            type_text("Move to where?", 50, 394, 28, (0, 0, 0))
            if pkm_menu_cursor.x == 482 and pkm_menu_cursor.y == 401:
                pokemon_menu_d1.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_d3.png"))
                menu_d1_x = 488
                menu_d1_y = 378
            else:
                pokemon_menu_d1.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_d1.png"))
                menu_d1_x = 488
                menu_d1_y = 384
            pokemon_menu_d1.draw(menu_d1_x, menu_d1_y)
            type_text("CANCEL", 544, 396, 26, (255, 255, 255))
            poke_counter = 1
            pkm_menu_cursor.draw()

            if len(player.main_pokemon) == 1:
                if pkm_menu_cursor.x == 8 and pkm_menu_cursor.y == 150 and selected_pkm == player.main_pokemon[0]:
                    selection.graphics = pygame.image.load(
                        os.path.join(path_visual_elements, "pokemon_menu_switch_1.png"))
                    selection.x = 7
                    selection.y = 75
                elif pkm_menu_cursor.x == 8 and pkm_menu_cursor.y == 150 and selected_pkm != player.main_pokemon[0]:
                    selection.graphics = pygame.image.load(
                        os.path.join(path_visual_elements, "pokemon_menu_switch_1.png"))
                    selection.x = 7
                    selection.y = 75
                elif pkm_menu_cursor.x != 8 and pkm_menu_cursor.y != 150 and selected_pkm != player.main_pokemon[0]:
                    selection.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s3.png"))
                    selection.x = 6
                    selection.y = 80
                elif pkm_menu_cursor.x != 8 and pkm_menu_cursor.y != 150 and selected_pkm == player.main_pokemon[0]:
                    selection.graphics = pygame.image.load(
                        os.path.join(path_visual_elements, "pokemon_menu_switch_1_2.png"))
                    selection.x = 6
                    selection.y = 80
                selection.draw()
                player.main_pokemon[0].draw_menu(40, 125)
                type_text(str(player.main_pokemon[0].level), 134, 146, 25, (255, 255, 255))
                type_text(str(player.main_pokemon[0].current_hp), 130, 190, 25, (255, 255, 255))
                type_text(str(player.main_pokemon[0].hp), 180, 190, 25, (255, 255, 255))
                screen.blit(player.main_pokemon[0].sex_graphics, (185, 152))
                type_text(str(player.main_pokemon[0].name), 100, 120, 25, (255, 255, 255))
                player.main_pokemon[0].draw_hp_bar(47, 177)
                if player.main_pokemon[0].holding_item != "none":
                    held_item_icon.draw(66, 160, screen)

            show_pokemons_in_menu_if_more_than_one(player, pkm_menu_cursor, pkm_menu_1, pkm_menu_2, pkm_menu_3,
                                                   pkm_menu_4, pkm_menu_5, screen, held_item_icon, path_visual_elements)

        elif window_state == "player_card_1":
            badge_counter = 0
            screen.fill((0, 0, 0))
            player_card_1.draw()
            type_text("NAME:   " + str(player.name), 60, 118, 30, (0, 0, 0))
            type_text("IDNo." + str(player_card_1.id), 380, 62, 30, (0, 0, 0))
            type_text("MONEY                   " + "$" + str(player.blance), 60, 194, 30, (0, 0, 0))
            type_text("POKEDEX                 " + str(player.pokedex), 60, 240, 30, (0, 0, 0))
            type_text("TIME             " + str(time), 60, 286, 30, (0, 0, 0))
            for b in range(0, len(player.badges)):
                player.badges[b].draw(85 + (badge_counter * 68), 385, screen)
                badge_counter = badge_counter + 1

        elif window_state == "player_card_2":
            screen.fill((0, 0, 0))
            player_card_2.draw()
            type_text(str(player.name), 372, 68, 30, (0, 0, 0))

        elif window_state == "pokemon_summary_info":
            screen.fill((0, 0, 0))
            pkm_summary.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_summary_1.png"))
            pkm_summary.draw()
            pkm_summary.type_text_summary("POKEMON INFO")
            selected_pkm.draw(106, 130)
            type_text("PAGE", 464, 34, 20, (255, 255, 255))
            type_text("CANCEL", 552, 34, 20, (255, 255, 255))
            type_text(str(selected_pkm.name), 110, 74, 30, (255, 255, 255))
            type_text("Lv " + str(selected_pkm.level), 9, 74, 30, (255, 255, 255))
            screen.blit(selected_pkm.sex_graphics, (264, 84))
            if selected_pkm.number < 10:
                type_text("00" + str(selected_pkm.number), 450, 78, 30, (0, 0, 0))
            elif selected_pkm.number < 100:
                type_text("0" + str(selected_pkm.number), 450, 78, 30, (0, 0, 0))
            else:
                type_text(str(selected_pkm.number), 450, 78, 30, (0, 0, 0))
            type_text(str(selected_pkm.name), 450, 117, 30, (0, 0, 0))
            if len(selected_pkm.type) == 1:
                pkm_type = PokemonType(selected_pkm.type[0], path_visual_elements)
                pkm_type.graphics = pygame.transform.scale(pkm_type.graphics, (64, 24))
                pkm_type.draw(446, 164)
            else:
                pkm_type_1 = PokemonType(selected_pkm.type[0], path_visual_elements)
                pkm_type_2 = PokemonType(selected_pkm.type[1], path_visual_elements)
                pkm_type_1.graphics = pygame.transform.scale(pkm_type_1.graphics, (64, 24))
                pkm_type_2.graphics = pygame.transform.scale(pkm_type_2.graphics, (64, 24))
                pkm_type_1.draw(446, 164)
                pkm_type_2.draw(520, 164)
            type_text(str(player.name), 450, 197, 30, (0, 0, 0))
            type_text(str(player_card_1.id), 450, 237, 30, (0, 0, 0))
            if selected_pkm.holding_item == "none":
                type_text("NONE", 450, 277, 30, (0, 0, 0))
            else:
                type_text(str(selected_pkm.holding_item.name), 450, 277, 30, (0, 0, 0))

            type_text(str(selected_pkm.nature) + " nature.", 30, 334, 30, (0, 0, 0))
            type_text("Met in " + str(selected_pkm.location) + " at Lv  " + str(selected_pkm.starting_level) + ".", 30,
                      370,
                      30, (0, 0, 0))

        elif window_state == "pokemon_summary_skills":
            screen.fill((0, 0, 0))
            pkm_summary.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_summary_2.png"))
            pkm_summary.draw()
            pkm_summary.type_text_summary("POKEMON SKILLS")
            selected_pkm.draw(106, 130)
            type_text("PAGE", 464, 34, 20, (255, 255, 255))
            type_text("CANCEL", 552, 34, 20, (255, 255, 255))
            type_text(str(selected_pkm.name), 110, 74, 30, (255, 255, 255))
            type_text("Lv " + str(selected_pkm.level), 9, 74, 30, (255, 255, 255))
            screen.blit(selected_pkm.sex_graphics, (264, 84))
            type_text(str(selected_pkm.current_hp), 560, 78, 30, (0, 0, 0))
            type_text("/", 590, 78, 30, (0, 0, 0))
            type_text(str(selected_pkm.hp), 600, 78, 30, (0, 0, 0))
            if selected_pkm.attack >= 10:
                type_text(str(selected_pkm.attack), 600, 124, 30, (0, 0, 0))
            else:
                type_text("0" + str(selected_pkm.attack), 602, 124, 30, (0, 0, 0))
            if selected_pkm.defense >= 10:
                type_text(str(selected_pkm.defense), 600, 160, 30, (0, 0, 0))
            else:
                type_text("0" + str(selected_pkm.defense), 602, 160, 30, (0, 0, 0))
            if selected_pkm.sp_atk >= 10:
                type_text(str(selected_pkm.sp_atk), 600, 195, 30, (0, 0, 0))
            else:
                type_text("0" + str(selected_pkm.sp_atk), 602, 195, 30, (0, 0, 0))
            if selected_pkm.sp_def >= 10:
                type_text(str(selected_pkm.sp_def), 600, 230, 30, (0, 0, 0))
            else:
                type_text("0" + str(selected_pkm.sp_def), 602, 230, 30, (0, 0, 0))
            if selected_pkm.speed >= 10:
                type_text(str(selected_pkm.speed), 600, 265, 30, (0, 0, 0))
            else:
                type_text("0" + str(selected_pkm.speed), 602, 265, 30, (0, 0, 0))

            if selected_pkm.total_exp < 100:
                type_text(str(selected_pkm.total_exp), 594, 300, 30, (0, 0, 0))
            else:
                type_text(str(selected_pkm.total_exp), 590, 300, 30, (0, 0, 0))
            if selected_pkm.to_next_level < 100:
                type_text(str(selected_pkm.to_next_level_exp), 594, 332, 30, (0, 0, 0))
            else:
                type_text(str(selected_pkm.to_next_level_exp), 590, 332, 30, (0, 0, 0))

            selected_pkm.draw_exp_bar(410, 370)
            type_text(str(selected_pkm.ability), 200, 370, 30, (0, 0, 0))

        elif window_state == "pokemon_summary_moves":
            screen.fill((0, 0, 0))
            move_counter = 0
            pkm_summary.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_summary_3.png"))
            pkm_summary.draw()
            pkm_summary.type_text_summary("KNOWN MOVES")
            selected_pkm.draw(106, 130)
            type_text("PAGE", 464, 34, 20, (255, 255, 255))
            type_text("DETAIL", 552, 34, 20, (255, 255, 255))
            type_text(str(selected_pkm.name), 110, 74, 30, (255, 255, 255))
            type_text("Lv " + str(selected_pkm.level), 9, 74, 30, (255, 255, 255))
            screen.blit(selected_pkm.sex_graphics, (264, 84))
            if len(selected_pkm.moves) == 1:
                for m in range(len(selected_pkm.moves)):
                    type_text(str(selected_pkm.moves[m].name), 430, 83 + (move_counter * 74), 32, (0, 0, 0))
                    type_text("pp", 536, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text(str(selected_pkm.moves[m].current_pp), 560, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text("/", 590, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text(str(selected_pkm.moves[m].pp), 600, 116 + (move_counter * 74), 25, (0, 0, 0))
                    move_type = PokemonType(selected_pkm.moves[m].type, path_visual_elements)
                    move_type.graphics = pygame.transform.scale(move_type.graphics, (83, 31))
                    move_type.draw(330, 85 + (move_counter * 74))
                    move_counter = move_counter + 1
                type_text("-", 430, 83 + (1 * 74), 32, (0, 0, 0))
                type_text("pp", 536, 116 + (1 * 74), 25, (0, 0, 0))
                type_text("--", 560, 116 + (1 * 74), 25, (0, 0, 0))
                type_text("-", 430, 83 + (2 * 74), 32, (0, 0, 0))
                type_text("pp", 536, 116 + (2 * 74), 25, (0, 0, 0))
                type_text("--", 560, 116 + (2 * 74), 25, (0, 0, 0))
                type_text("-", 430, 83 + (3 * 74), 32, (0, 0, 0))
                type_text("pp", 536, 116 + (3 * 74), 25, (0, 0, 0))
                type_text("--", 560, 116 + (3 * 74), 25, (0, 0, 0))
            if len(selected_pkm.moves) == 2:
                for m in range(len(selected_pkm.moves)):
                    type_text(str(selected_pkm.moves[m].name), 430, 83 + (move_counter * 74), 32, (0, 0, 0))
                    type_text("pp", 536, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text(str(selected_pkm.moves[m].current_pp), 560, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text("/", 590, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text(str(selected_pkm.moves[m].pp), 600, 116 + (move_counter * 74), 25, (0, 0, 0))
                    move_type = PokemonType(selected_pkm.moves[m].type, path_visual_elements)
                    move_type.graphics = pygame.transform.scale(move_type.graphics, (83, 31))
                    move_type.draw(330, 85 + (move_counter * 74))
                    move_counter = move_counter + 1
                type_text("-", 430, 83 + (2 * 74), 32, (0, 0, 0))
                type_text("pp", 536, 116 + (2 * 74), 25, (0, 0, 0))
                type_text("--", 560, 116 + (2 * 74), 25, (0, 0, 0))
                type_text("-", 430, 83 + (3 * 74), 32, (0, 0, 0))
                type_text("pp", 536, 116 + (3 * 74), 25, (0, 0, 0))
                type_text("--", 560, 116 + (3 * 74), 25, (0, 0, 0))
            if len(selected_pkm.moves) == 3:
                for m in range(len(selected_pkm.moves)):
                    type_text(str(selected_pkm.moves[m].name), 430, 83 + (move_counter * 74), 32, (0, 0, 0))
                    type_text("pp", 536, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text(str(selected_pkm.moves[m].current_pp), 560, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text("/", 590, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text(str(selected_pkm.moves[m].pp), 600, 116 + (move_counter * 74), 25, (0, 0, 0))
                    move_type = PokemonType(selected_pkm.moves[m].type, path_visual_elements)
                    move_type.graphics = pygame.transform.scale(move_type.graphics, (83, 31))
                    move_type.draw(330, 85 + (move_counter * 74))
                    move_counter = move_counter + 1
                type_text("-", 430, 83 + (3 * 74), 32, (0, 0, 0))
                type_text("pp", 536, 116 + (3 * 74), 25, (0, 0, 0))
                type_text("--", 560, 116 + (3 * 74), 25, (0, 0, 0))
            if len(selected_pkm.moves) == 4:
                for m in range(len(selected_pkm.moves)):
                    type_text(str(selected_pkm.moves[m].name), 430, 83 + (move_counter * 74), 32, (0, 0, 0))
                    type_text("pp", 536, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text(str(selected_pkm.moves[m].current_pp), 560, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text("/", 590, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text(str(selected_pkm.moves[m].pp), 600, 116 + (move_counter * 74), 25, (0, 0, 0))
                    move_type = PokemonType(selected_pkm.moves[m].type, path_visual_elements)
                    move_type.graphics = pygame.transform.scale(move_type.graphics, (83, 31))
                    move_type.draw(330, 85 + (move_counter * 74))
                    move_counter = move_counter + 1

        elif window_state == "pokemon_summary_moves_2":
            screen.fill((0, 0, 0))
            move_counter = 0
            pkm_summary.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_summary_4.png"))
            pkm_summary.draw()
            pkm_summary.type_text_summary("KNOWN MOVES")
            type_text("PAGE", 464, 34, 20, (255, 255, 255))
            type_text("SWITCH", 552, 34, 20, (255, 255, 255))
            type_text(str(selected_pkm.name), 110, 74, 30, (255, 255, 255))
            screen.blit(selected_pkm.sex_graphics, (264, 84))
            selected_pkm.draw_menu(44, 100)
            moves_cursor.draw()
            if len(selected_pkm.type) == 1:
                pkm_type = PokemonType(selected_pkm.type[0], path_visual_elements)
                pkm_type.graphics = pygame.transform.scale(pkm_type.graphics, (83, 31))
                pkm_type.draw(140, 114)
            else:
                pkm_type_1 = PokemonType(selected_pkm.type[0], path_visual_elements)
                pkm_type_2 = PokemonType(selected_pkm.type[1], path_visual_elements)
                pkm_type_1.graphics = pygame.transform.scale(pkm_type_1.graphics, (83, 31))
                pkm_type_2.graphics = pygame.transform.scale(pkm_type_2.graphics, (83, 31))
                pkm_type_1.draw(110, 114)
                pkm_type_2.draw(200, 114)

            if len(selected_pkm.moves) == 1:
                for m in range(len(selected_pkm.moves)):
                    type_text(str(selected_pkm.moves[m].name), 430, 83 + (move_counter * 74), 32, (0, 0, 0))
                    type_text("pp", 536, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text(str(selected_pkm.moves[m].current_pp), 560, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text("/", 590, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text(str(selected_pkm.moves[m].pp), 600, 116 + (move_counter * 74), 25, (0, 0, 0))
                    move_type = PokemonType(selected_pkm.moves[m].type, path_visual_elements)
                    move_type.graphics = pygame.transform.scale(move_type.graphics, (83, 31))
                    move_type.draw(330, 85 + (move_counter * 74))
                    move_counter = move_counter + 1
                type_text("-", 430, 83 + (1 * 74), 32, (0, 0, 0))
                type_text("pp", 536, 116 + (1 * 74), 25, (0, 0, 0))
                type_text("--", 560, 116 + (1 * 74), 25, (0, 0, 0))
                type_text("-", 430, 83 + (2 * 74), 32, (0, 0, 0))
                type_text("pp", 536, 116 + (2 * 74), 25, (0, 0, 0))
                type_text("--", 560, 116 + (2 * 74), 25, (0, 0, 0))
                type_text("-", 430, 83 + (3 * 74), 32, (0, 0, 0))
                type_text("pp", 536, 116 + (3 * 74), 25, (0, 0, 0))
                type_text("--", 560, 116 + (3 * 74), 25, (0, 0, 0))
            if len(selected_pkm.moves) == 2:
                for m in range(len(selected_pkm.moves)):
                    type_text(str(selected_pkm.moves[m].name), 430, 83 + (move_counter * 74), 32, (0, 0, 0))
                    type_text("pp", 536, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text(str(selected_pkm.moves[m].current_pp), 560, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text("/", 590, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text(str(selected_pkm.moves[m].pp), 600, 116 + (move_counter * 74), 25, (0, 0, 0))
                    move_type = PokemonType(selected_pkm.moves[m].type, path_visual_elements)
                    move_type.graphics = pygame.transform.scale(move_type.graphics, (83, 31))
                    move_type.draw(330, 85 + (move_counter * 74))
                    move_counter = move_counter + 1
                type_text("-", 430, 83 + (2 * 74), 32, (0, 0, 0))
                type_text("pp", 536, 116 + (2 * 74), 25, (0, 0, 0))
                type_text("--", 560, 116 + (2 * 74), 25, (0, 0, 0))
                type_text("-", 430, 83 + (3 * 74), 32, (0, 0, 0))
                type_text("pp", 536, 116 + (3 * 74), 25, (0, 0, 0))
                type_text("--", 560, 116 + (3 * 74), 25, (0, 0, 0))
            if len(selected_pkm.moves) == 3:
                for m in range(len(selected_pkm.moves)):
                    type_text(str(selected_pkm.moves[m].name), 430, 83 + (move_counter * 74), 32, (0, 0, 0))
                    type_text("pp", 536, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text(str(selected_pkm.moves[m].current_pp), 560, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text("/", 590, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text(str(selected_pkm.moves[m].pp), 600, 116 + (move_counter * 74), 25, (0, 0, 0))
                    move_type = PokemonType(selected_pkm.moves[m].type, path_visual_elements)
                    move_type.graphics = pygame.transform.scale(move_type.graphics, (83, 31))
                    move_type.draw(330, 85 + (move_counter * 74))
                    move_counter = move_counter + 1
                type_text("-", 430, 83 + (3 * 74), 32, (0, 0, 0))
                type_text("pp", 536, 116 + (3 * 74), 25, (0, 0, 0))
                type_text("--", 560, 116 + (3 * 74), 25, (0, 0, 0))
            if len(selected_pkm.moves) == 4:
                for m in range(len(selected_pkm.moves)):
                    type_text(str(selected_pkm.moves[m].name), 430, 83 + (move_counter * 74), 32, (0, 0, 0))
                    type_text("pp", 536, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text(str(selected_pkm.moves[m].current_pp), 560, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text("/", 590, 116 + (move_counter * 74), 25, (0, 0, 0))
                    type_text(str(selected_pkm.moves[m].pp), 600, 116 + (move_counter * 74), 25, (0, 0, 0))
                    move_type = PokemonType(selected_pkm.moves[m].type, path_visual_elements)
                    move_type.graphics = pygame.transform.scale(move_type.graphics, (83, 31))
                    move_type.draw(330, 85 + (move_counter * 74))
                    move_counter = move_counter + 1

            if moves_cursor.y == 75 and len(selected_pkm.moves) >= 1:
                type_text(str(selected_pkm.moves[0].power), 170, 175, 32, (0, 0, 0))
                type_text(str(selected_pkm.moves[0].accuracy), 156, 214, 32, (0, 0, 0))
                type_text(str(selected_pkm.moves[0].effect[0:25]), 24, 288, 25, (0, 0, 0))
                type_text(str(selected_pkm.moves[0].effect[25:50]), 24, 328, 25, (0, 0, 0))
                type_text(str(selected_pkm.moves[0].effect[50:len(selected_pkm.moves[0].effect)]), 24, 368, 25,
                          (0, 0, 0))
            elif moves_cursor.y == 149 and len(selected_pkm.moves) >= 2:
                type_text(str(selected_pkm.moves[1].power), 170, 175, 32, (0, 0, 0))
                type_text(str(selected_pkm.moves[1].accuracy), 156, 214, 32, (0, 0, 0))
                type_text(str(selected_pkm.moves[1].effect[0:25]), 24, 288, 25, (0, 0, 0))
                type_text(str(selected_pkm.moves[1].effect[25:50]), 24, 328, 25, (0, 0, 0))
                type_text(str(selected_pkm.moves[1].effect[50:len(selected_pkm.moves[1].effect)]), 24, 368, 25,
                          (0, 0, 0))
            elif moves_cursor.y == 223 and len(selected_pkm.moves) >= 3:
                type_text(str(selected_pkm.moves[2].power), 170, 175, 32, (0, 0, 0))
                type_text(str(selected_pkm.moves[2].accuracy), 156, 214, 32, (0, 0, 0))
                type_text(str(selected_pkm.moves[2].effect[0:25]), 24, 288, 25, (0, 0, 0))
                type_text(str(selected_pkm.moves[2].effect[25:50]), 24, 328, 25, (0, 0, 0))
                type_text(str(selected_pkm.moves[2].effect[50:len(selected_pkm.moves[2].effect)]), 24, 368, 25,
                          (0, 0, 0))
            elif moves_cursor.y == 297 and len(selected_pkm.moves) >= 4:
                type_text(str(selected_pkm.moves[3].power), 170, 175, 32, (0, 0, 0))
                type_text(str(selected_pkm.moves[3].accuracy), 156, 214, 32, (0, 0, 0))
                type_text(str(selected_pkm.moves[3].effect[0:25]), 24, 288, 25, (0, 0, 0))
                type_text(str(selected_pkm.moves[3].effect[25:50]), 24, 328, 25, (0, 0, 0))
                type_text(str(selected_pkm.moves[3].effect[50:len(selected_pkm.moves[3].effect)]), 24, 368, 25,
                          (0, 0, 0))

        elif window_state == "pokemon_catching":
            if pokemon_catching_animation < len(pkm_caught.graphics_list):
                screen.fill((0, 0, 0))
                catch_bg.draw(screen)
                if pokemon_catching_animation < 7:
                    pokemon.draw(398, 90)
                if pokemon_catching_animation < (len(pkm_caught.graphics_list) - 1):
                    type_text(str(player.name) + " used POKEBALL !", 40, 350, 32, (255, 255, 255))
                else:
                    type_text("Gotcha! " + str(pokemon.name) + " was caught!", 40, 350, 32, (255, 255, 255))
                if pokemon.current_hp > 0:
                    pokemon.hp_bar_graphics = health_bar_status(pokemon.current_hp, pokemon.hp, path_hp_bar)
                    pokemon.draw_hp_bar(100, 112)
                else:
                    pokemon.hp_bar_graphics = health_bar_status(0, pokemon.hp, path_hp_bar)
                    pokemon.draw_hp_bar(100, 112)
                type_text(pokemon.name, 56, 78, 26, (0, 0, 0))
                type_text(str(pokemon.level), 251, 78, 26, (0, 0, 0))
                screen.blit(pokemon.sex_graphics, (pokemon.sex_x, pokemon.sex_y))

                graphics = pkm_caught.graphics_list[pokemon_catching_animation]
                pkm_caught.draw(graphics, screen)
                pokemon_catching_animation = pokemon_catching_animation + 1

            if pokemon_catching_animation == len(pkm_caught.graphics_list):
                if pokemon_catching_counter == 0:
                    pokemonCounter = pokemonCounter + 1
                    pokemon_exist = False
                    if len(player.pokemons) <= 4:
                        player.pokemons.append(pokemon)
                    else:
                        player.pokemon_storage.append(pokemon)
                    pokemon_catching_counter = pokemon_catching_counter + 1

            pygame.time.wait(100)

        elif window_state == "pokemon_uncatching":
            if pokemon_catching_animation < len(pkm_uncaught.graphics_list):
                screen.fill((0, 0, 0))
                catch_bg.draw(screen)
                if pokemon_catching_animation < 7:
                    pokemon.draw(398, 90)
                if pokemon_catching_animation > 33:
                    pokemon.draw(398, 90)
                if pokemon_catching_animation < (len(pkm_uncaught.graphics_list) - 1):
                    type_text(str(player.name) + " used POKEBALL !", 40, 350, 32, (255, 255, 255))
                else:
                    type_text("Oh no! It was too close!", 40, 350, 32, (255, 255, 255))
                if pokemon.current_hp > 0:
                    pokemon.hp_bar_graphics = health_bar_status(pokemon.current_hp, pokemon.hp, path_hp_bar)
                    pokemon.draw_hp_bar(100, 112)
                else:
                    pokemon.hp_bar_graphics = health_bar_status(0, pokemon.hp, path_hp_bar)
                    pokemon.draw_hp_bar(100, 112)
                type_text(pokemon.name, 56, 78, 26, (0, 0, 0))
                type_text(str(pokemon.level), 251, 78, 26, (0, 0, 0))
                screen.blit(pokemon.sex_graphics, (pokemon.sex_x, pokemon.sex_y))

                graphics = pkm_uncaught.graphics_list[pokemon_catching_animation]
                pkm_uncaught.draw(graphics, screen)
                pokemon_catching_animation = pokemon_catching_animation + 1

            if pokemon_catching_animation == len(pkm_uncaught.graphics_list):
                turn = "enemy"
                pkm_attack_2 = "True"
                animation_counter2 = 0
                window_state = "enemy_turn"

            pygame.time.wait(100)

        elif window_state == "selected_bag_items":
            screen.fill((0, 0, 0))
            inv.draw()
            bag.graphics = pygame.image.load(os.path.join(path_visual_elements, "b1.png"))
            bag.draw()
            bag.type_text_backpack("ITEMS")
            if len(player.items) != 0:
                for p in range(0, len(player.items)):
                    if player.items[p].quantity != 0:
                        type_text(str(player.items[p].name), 265, (p + 1) * 50, 20, (0, 0, 0))
                        type_text("x " + str(player.items[p].quantity), 530, (p + 1) * 50, 20, (0, 0, 0))
            cursor_bag.draw()
            if cursor_bag.y == 53 and window_state == "selected_bag_items" and player.items[0].quantity != 0 and len(
                    player.items) > 0:
                player.items[0].draw()
            elif len(player.items) > 1 and cursor_bag.y == 98 and window_state == "selected_bag_items" and player.items[
                1].quantity != 0:
                player.items[1].draw()
            elif len(player.items) > 2 and cursor_bag.y == 143 and window_state == "selected_bag_items" and \
                    player.items[
                        2].quantity != 0:
                player.items[2].draw()
            elif len(player.items) > 3 and cursor_bag.y == 188 and window_state == "selected_bag_items" and \
                    player.items[
                        3].quantity != 0:
                player.items[3].draw()
            elif len(player.items) > 4 and cursor_bag.y == 233 and window_state == "selected_bag_items" and \
                    player.items[
                        4].quantity != 0:
                player.items[4].draw()

            selected_item_m1.draw(106, 336)
            selected_item_m2.draw(453, 248)
            type_text(str(selected_item.name) + " is ", 130, 352, 30, (0, 0, 0))
            type_text("selected.", 130, 387, 30, (0, 0, 0))

            type_text("USE", 494, 275, 25, (0, 0, 0))
            type_text("GIVE", 494, 315, 25, (0, 0, 0))
            type_text("TOSS", 494, 355, 25, (0, 0, 0))
            type_text("CANCEL", 494, 395, 25, (0, 0, 0))
            cursor_bag_items.draw()

        elif window_state == "selected_bag_key_items":
            screen.fill((0, 0, 0))
            inv.draw()
            bag.graphics = pygame.image.load(os.path.join(path_visual_elements, "b2.png"))
            bag.draw()
            bag.type_text_backpack("KEY ITEMS")
            if len(player.key_items) != 0:
                for p in range(0, len(player.key_items)):
                    if player.key_items[p].quantity != 0:
                        type_text(str(player.key_items[p].name), 265, (p + 1) * 50, 20, (0, 0, 0))
                        type_text("x " + str(player.key_items[p].quantity), 530, (p + 1) * 50, 20, (0, 0, 0))
            cursor_bag.draw()
            if len(player.key_items) > 0 and cursor_bag.y == 53 and window_state == "selected_bag_key_items" and \
                    player.key_items[0].quantity != 0:
                player.key_items[0].draw()
                if player.key_items[0] == player.registered_item:
                    register_item.draw(530, 1 * 50)
            elif len(player.key_items) > 1 and cursor_bag.y == 98 and window_state == "selected_bag_key_items" and \
                    player.key_items[1].quantity != 0:
                player.key_items[1].draw()
                if player.key_items[1] == player.registered_item:
                    register_item.draw(530, 2 * 50)
            elif len(player.key_items) > 2 and cursor_bag.y == 143 and window_state == "selected_bag_key_items" and \
                    player.key_items[2].quantity != 0:
                player.key_items[2].draw()
                if player.key_items[2] == player.registered_item:
                    register_item.draw(530, 3 * 50)
            elif len(player.key_items) > 3 and cursor_bag.y == 188 and window_state == "selected_bag_key_items" and \
                    player.key_items[3].quantity != 0:
                player.key_items[3].draw()
                if player.key_items[3] == player.registered_item:
                    register_item.draw(530, 4 * 50)
            elif len(player.key_items) > 4 and cursor_bag.y == 233 and window_state == "selected_bag_key_items" and \
                    player.key_items[4].quantity != 0:
                player.key_items[4].draw()
                if player.key_items[4] == player.registered_item:
                    register_item.draw(530, 5 * 50)

            selected_item_m1.draw(106, 336)
            selected_item_m3.draw(453, 289)
            type_text(str(selected_item.name) + " is ", 130, 352, 30, (0, 0, 0))
            type_text("selected.", 130, 387, 30, (0, 0, 0))

            if selected_item != player.registered_item:
                type_text("USE", 494, 315, 25, (0, 0, 0))
                type_text("REGISTER", 494, 355, 25, (0, 0, 0))
                type_text("CANCEL", 494, 395, 25, (0, 0, 0))

            elif selected_item == player.registered_item:
                type_text("USE", 494, 315, 25, (0, 0, 0))
                type_text("DESELECT", 494, 355, 25, (0, 0, 0))
                type_text("CANCEL", 494, 395, 25, (0, 0, 0))
            cursor_bag_key_items.draw()

        elif window_state == "selected_bag_pokeballs":
            screen.fill((0, 0, 0))
            inv.draw()
            bag.graphics = pygame.image.load(os.path.join(path_visual_elements, "b3.png"))
            bag.draw()
            bag.type_text_backpack("POKE BALLS")
            if len(player.pokeballs) != 0:
                for p in range(0, len(player.pokeballs)):
                    if player.pokeballs[p].quantity != 0:
                        type_text(str(player.pokeballs[p].name), 265, (p + 1) * 50, 20, (0, 0, 0))
                        type_text("x " + str(player.pokeballs[p].quantity), 530, (p + 1) * 50, 20, (0, 0, 0))
            cursor_bag.draw()
            if len(player.pokeballs) > 0 and cursor_bag.y == 53 and window_state == "selected_bag_pokeballs" and \
                    player.pokeballs[0].quantity != 0:
                player.pokeballs[0].draw()
            elif len(player.pokeballs) > 1 and cursor_bag.y == 98 and window_state == "selected_bag_pokeballs" and \
                    player.pokeballs[1].quantity != 0:
                player.pokeballs[1].draw()
            elif len(player.pokeballs) > 2 and cursor_bag.y == 143 and window_state == "selected_bag_pokeballs" and \
                    player.pokeballs[2].quantity != 0:
                player.pokeballs[2].draw()
            elif len(player.pokeballs) > 3 and cursor_bag.y == 188 and window_state == "selected_bag_pokeballs" and \
                    player.pokeballs[3].quantity != 0:
                player.pokeballs[3].draw()
            elif len(player.pokeballs) > 4 and cursor_bag.y == 233 and window_state == "selected_bag_pokeballs" and \
                    player.pokeballs[4].quantity != 0:
                player.pokeballs[4].draw()

            selected_item_m1.draw(106, 336)
            selected_item_m3.draw(453, 289)
            type_text(str(selected_item.name) + " is ", 130, 352, 30, (0, 0, 0))
            type_text("selected.", 130, 387, 30, (0, 0, 0))

            type_text("GIVE", 494, 315, 25, (0, 0, 0))
            type_text("TOSS", 494, 355, 25, (0, 0, 0))
            type_text("CANCEL", 494, 395, 25, (0, 0, 0))
            cursor_bag_pokeballs.draw()

        elif window_state == "use_bag_items":
            screen.fill((0, 0, 0))
            pokemon_selection_menu.draw()
            type_text("Use on which POKEMON?", 50, 394, 28, (0, 0, 0))
            if use_bag_items_cursor.x == 482 and use_bag_items_cursor.y == 401:
                pokemon_menu_d1.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_d3.png"))
                menu_d1_x = 488
                menu_d1_y = 378
            else:
                pokemon_menu_d1.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_d1.png"))
                menu_d1_x = 488
                menu_d1_y = 384
            pokemon_menu_d1.draw(menu_d1_x, menu_d1_y)
            type_text("CANCEL", 544, 396, 26, (255, 255, 255))
            poke_counter = 1
            use_bag_items_cursor.draw()

            if len(player.main_pokemon) == 1:
                if use_bag_items_cursor.x == 8 and use_bag_items_cursor.y == 150:
                    selection.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s4.png"))
                    selection.x = 7
                    selection.y = 75
                else:
                    selection.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s3.png"))
                    selection.x = 6
                    selection.y = 80
                selection.draw()
                player.main_pokemon[0].draw_menu(40, 125)
                type_text(str(player.main_pokemon[0].level), 134, 146, 25, (255, 255, 255))
                type_text(str(player.main_pokemon[0].current_hp), 130, 190, 25, (255, 255, 255))
                type_text(str(player.main_pokemon[0].hp), 180, 190, 25, (255, 255, 255))
                screen.blit(player.main_pokemon[0].sex_graphics, (185, 152))
                type_text(str(player.main_pokemon[0].name), 100, 120, 25, (255, 255, 255))
                player.main_pokemon[0].draw_hp_bar(47, 177)
                if player.main_pokemon[0].holding_item != "none":
                    held_item_icon.draw(66, 160, screen)

            show_pokemons_in_menu_if_more_than_one(player, pkm_menu_cursor, pkm_menu_1, pkm_menu_2, pkm_menu_3,
                                                   pkm_menu_4, pkm_menu_5, screen, held_item_icon, path_visual_elements)

        elif window_state == "cannot_use_items":
            screen.fill((0, 0, 0))
            pokemon_selection_menu.draw()
            type_text("Use on which POKEMON?", 50, 394, 28, (0, 0, 0))
            if use_bag_items_cursor.x == 482 and use_bag_items_cursor.y == 401:
                pokemon_menu_d1.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_d3.png"))
                menu_d1_x = 488
                menu_d1_y = 378
            else:
                pokemon_menu_d1.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_d1.png"))
                menu_d1_x = 488
                menu_d1_y = 384
            pokemon_menu_d1.draw(menu_d1_x, menu_d1_y)
            type_text("CANCEL", 544, 396, 26, (255, 255, 255))
            poke_counter = 1
            use_bag_items_cursor.draw()

            if len(player.main_pokemon) == 1:
                if use_bag_items_cursor.x == 8 and use_bag_items_cursor.y == 150:
                    selection.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s4.png"))
                    selection.x = 7
                    selection.y = 75
                else:
                    selection.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s3.png"))
                    selection.x = 6
                    selection.y = 80
                selection.draw()
                player.main_pokemon[0].draw_menu(40, 125)
                type_text(str(player.main_pokemon[0].level), 134, 146, 25, (255, 255, 255))
                type_text(str(player.main_pokemon[0].current_hp), 130, 190, 25, (255, 255, 255))
                type_text(str(player.main_pokemon[0].hp), 180, 190, 25, (255, 255, 255))
                screen.blit(player.main_pokemon[0].sex_graphics, (185, 152))
                type_text(str(player.main_pokemon[0].name), 100, 120, 25, (255, 255, 255))
                player.main_pokemon[0].draw_hp_bar(47, 177)
                if player.main_pokemon[0].holding_item != "none":
                    held_item_icon.draw(66, 160, screen)

            show_pokemons_in_menu_if_more_than_one(player, pkm_menu_cursor, pkm_menu_1, pkm_menu_2, pkm_menu_3,
                                                   pkm_menu_4, pkm_menu_5, screen, held_item_icon, path_visual_elements)
            c_use_item.draw(0, 320)
            type_text("It won't have any effect.", 24, 340, 30, (0, 0, 0))

        elif window_state == "toss_bag_items_1":
            screen.fill((0, 0, 0))
            inv.draw()
            bag.graphics = pygame.image.load(os.path.join(path_visual_elements, "b1.png"))
            bag.draw()
            bag.type_text_backpack("ITEMS")
            if len(player.items) != 0:
                for p in range(0, len(player.items)):
                    if player.items[p].quantity != 0:
                        type_text(str(player.items[p].name), 265, (p + 1) * 50, 20, (0, 0, 0))
                        type_text("x " + str(player.items[p].quantity), 530, (p + 1) * 50, 20, (0, 0, 0))
            cursor_bag.draw()
            if cursor_bag.y == 53 and window_state == "toss_bag_items_1" and player.items[0].quantity != 0 and len(
                    player.items) > 0:
                player.items[0].draw()
            elif len(player.items) > 1 and cursor_bag.y == 98 and window_state == "toss_bag_items_1" and player.items[
                1].quantity != 0:
                player.items[1].draw()
            elif len(player.items) > 2 and cursor_bag.y == 143 and window_state == "toss_bag_items_1" and player.items[
                2].quantity != 0:
                player.items[2].draw()
            elif len(player.items) > 3 and cursor_bag.y == 188 and window_state == "toss_bag_items_1" and player.items[
                3].quantity != 0:
                player.items[3].draw()
            elif len(player.items) > 4 and cursor_bag.y == 233 and window_state == "toss_bag_items_1" and player.items[
                4].quantity != 0:
                player.items[4].draw()

            selected_item_m1.draw(106, 336)
            selected_item_m4.draw(453, 336)
            type_text("Throw away " + str(toss_number) + " of ", 130, 352, 30, (0, 0, 0))
            type_text("this item?", 130, 387, 30, (0, 0, 0))

            type_text("YES", 494, 358, 25, (0, 0, 0))
            type_text("NO", 494, 392, 25, (0, 0, 0))

            cursor_toss_bag_items.draw()

        elif window_state == "toss_bag_items_1_2":
            screen.fill((0, 0, 0))
            inv.draw()
            bag.graphics = pygame.image.load(os.path.join(path_visual_elements, "b1.png"))
            bag.draw()
            bag.type_text_backpack("ITEMS")
            if len(player.items) != 0:
                for p in range(0, len(player.items)):
                    if player.items[p].quantity != 0:
                        type_text(str(player.items[p].name), 265, (p + 1) * 50, 20, (0, 0, 0))
                        type_text("x " + str(player.items[p].quantity), 530, (p + 1) * 50, 20, (0, 0, 0))
            cursor_bag.draw()
            if cursor_bag.y == 53 and window_state == "toss_bag_items_1_2" and player.items[0].quantity != 0 and len(
                    player.items) > 0:
                player.items[0].draw()
            elif len(player.items) > 1 and cursor_bag.y == 98 and window_state == "toss_bag_items_1_2" and player.items[
                1].quantity != 0:
                player.items[1].draw()
            elif len(player.items) > 2 and cursor_bag.y == 143 and window_state == "toss_bag_items_1_2" and \
                    player.items[
                        2].quantity != 0:
                player.items[2].draw()
            elif len(player.items) > 3 and cursor_bag.y == 188 and window_state == "toss_bag_items_1_2" and \
                    player.items[
                        3].quantity != 0:
                player.items[3].draw()
            elif len(player.items) > 4 and cursor_bag.y == 233 and window_state == "toss_bag_items_1_2" and \
                    player.items[
                        4].quantity != 0:
                player.items[4].draw()

            selected_item_m1.draw(106, 336)
            type_text("Threw away " + str(toss_number), 130, 352, 30, (0, 0, 0))
            type_text(str(selected_item.name) + "(s).", 130, 387, 30, (0, 0, 0))

            if toss_times == 0:
                selected_item.quantity = selected_item.quantity - toss_number

            toss_times = toss_times + 1

        elif window_state == "toss_bag_items_2":
            screen.fill((0, 0, 0))
            inv.draw()
            bag.graphics = pygame.image.load(os.path.join(path_visual_elements, "b1.png"))
            bag.draw()
            bag.type_text_backpack("ITEMS")
            if len(player.items) != 0:
                for p in range(0, len(player.items)):
                    if player.items[p].quantity != 0:
                        type_text(str(player.items[p].name), 265, (p + 1) * 50, 20, (0, 0, 0))
                        type_text("x " + str(player.items[p].quantity), 530, (p + 1) * 50, 20, (0, 0, 0))
            cursor_bag.draw()
            if cursor_bag.y == 53 and window_state == "toss_bag_items_2" and player.items[0].quantity != 0 and len(
                    player.items) > 0:
                player.items[0].draw()
            elif len(player.items) > 1 and cursor_bag.y == 98 and window_state == "toss_bag_items_2" and player.items[
                1].quantity != 0:
                player.items[1].draw()
            elif len(player.items) > 2 and cursor_bag.y == 143 and window_state == "toss_bag_items_2" and player.items[
                2].quantity != 0:
                player.items[2].draw()
            elif len(player.items) > 3 and cursor_bag.y == 188 and window_state == "toss_bag_items_2" and player.items[
                3].quantity != 0:
                player.items[3].draw()
            elif len(player.items) > 4 and cursor_bag.y == 233 and window_state == "toss_bag_items_2" and player.items[
                4].quantity != 0:
                player.items[4].draw()

            selected_item_m1.draw(106, 336)
            selected_item_m4.draw(453, 336)
            type_text("Toss out how many", 130, 352, 30, (0, 0, 0))
            type_text(str(selected_item.name) + "(s)?", 130, 387, 30, (0, 0, 0))

            if toss_number < 10:
                type_text("x00" + str(toss_number), 520, 375, 25, (0, 0, 0))
            elif 10 <= toss_number < 100:
                type_text("x0" + str(toss_number), 520, 375, 25, (0, 0, 0))
            elif toss_number >= 100:
                type_text("x" + str(toss_number), 520, 375, 25, (0, 0, 0))

            cursor_up.draw()
            if cursor_up.y != 336:
                cursor_up.y = 336
            elif cursor_up.y == 336:
                cursor_up.y = 340
            cursor_down.draw()
            if cursor_down.y != 418:
                cursor_down.y = 418
            elif cursor_down.y == 418:
                cursor_down.y = 414

        elif window_state == "toss_bag_pokeballs_1":
            screen.fill((0, 0, 0))
            inv.draw()
            bag.graphics = pygame.image.load(os.path.join(path_visual_elements, "b3.png"))
            bag.draw()
            bag.type_text_backpack("POKE BALLS")
            if len(player.pokeballs) != 0:
                for p in range(0, len(player.pokeballs)):
                    if player.pokeballs[p].quantity != 0:
                        type_text(str(player.pokeballs[p].name), 265, (p + 1) * 50, 20, (0, 0, 0))
                        type_text("x " + str(player.pokeballs[p].quantity), 530, (p + 1) * 50, 20, (0, 0, 0))
            cursor_bag.draw()
            if len(player.pokeballs) > 0 and cursor_bag.y == 53 and window_state == "toss_bag_pokeballs_1" and \
                    player.pokeballs[0].quantity != 0:
                player.pokeballs[0].draw()
            elif len(player.pokeballs) > 1 and cursor_bag.y == 98 and window_state == "toss_bag_pokeballs_1" and \
                    player.pokeballs[1].quantity != 0:
                player.pokeballs[1].draw()
            elif len(player.pokeballs) > 2 and cursor_bag.y == 143 and window_state == "toss_bag_pokeballs_1" and \
                    player.pokeballs[2].quantity != 0:
                player.pokeballs[2].draw()
            elif len(player.pokeballs) > 3 and cursor_bag.y == 188 and window_state == "toss_bag_pokeballs_1" and \
                    player.pokeballs[3].quantity != 0:
                player.pokeballs[3].draw()
            elif len(player.pokeballs) > 4 and cursor_bag.y == 233 and window_state == "toss_bag_pokeballs_1" and \
                    player.pokeballs[4].quantity != 0:
                player.pokeballs[4].draw()

            selected_item_m1.draw(106, 336)
            selected_item_m4.draw(453, 336)
            type_text("Throw away " + str(toss_number) + " of ", 130, 352, 30, (0, 0, 0))
            type_text("this item?", 130, 387, 30, (0, 0, 0))

            type_text("YES", 494, 358, 25, (0, 0, 0))
            type_text("NO", 494, 392, 25, (0, 0, 0))

            cursor_toss_bag_pokeballs.draw()

        elif window_state == "toss_bag_pokeballs_1_2":
            screen.fill((0, 0, 0))
            inv.draw()
            bag.graphics = pygame.image.load(os.path.join(path_visual_elements, "b3.png"))
            bag.draw()
            bag.type_text_backpack("POKE BALLS")
            if len(player.pokeballs) != 0:
                for p in range(0, len(player.pokeballs)):
                    if player.pokeballs[p].quantity != 0:
                        type_text(str(player.pokeballs[p].name), 265, (p + 1) * 50, 20, (0, 0, 0))
                        type_text("x " + str(player.pokeballs[p].quantity), 530, (p + 1) * 50, 20, (0, 0, 0))
            cursor_bag.draw()
            if len(player.pokeballs) > 0 and cursor_bag.y == 53 and window_state == "toss_bag_pokeballs_1" and \
                    player.pokeballs[0].quantity != 0:
                player.pokeballs[0].draw()
            elif len(player.pokeballs) > 1 and cursor_bag.y == 98 and window_state == "toss_bag_pokeballs_1" and \
                    player.pokeballs[1].quantity != 0:
                player.pokeballs[1].draw()
            elif len(player.pokeballs) > 2 and cursor_bag.y == 143 and window_state == "toss_bag_pokeballs_1" and \
                    player.pokeballs[2].quantity != 0:
                player.pokeballs[2].draw()
            elif len(player.pokeballs) > 3 and cursor_bag.y == 188 and window_state == "toss_bag_pokeballs_1" and \
                    player.pokeballs[3].quantity != 0:
                player.pokeballs[3].draw()
            elif len(player.pokeballs) > 4 and cursor_bag.y == 233 and window_state == "toss_bag_pokeballs_1" and \
                    player.pokeballs[4].quantity != 0:
                player.pokeballs[4].draw()

            selected_item_m1.draw(106, 336)
            type_text("Threw away " + str(toss_number), 130, 352, 30, (0, 0, 0))
            type_text(str(selected_item.name) + "(s).", 130, 387, 30, (0, 0, 0))

            if toss_times == 0:
                selected_item.quantity = selected_item.quantity - toss_number

            toss_times = toss_times + 1

        elif window_state == "toss_bag_pokeballs_2":
            screen.fill((0, 0, 0))
            inv.draw()
            bag.graphics = pygame.image.load(os.path.join(path_visual_elements, "b3.png"))
            bag.draw()
            bag.type_text_backpack("POKE BALLS")
            if len(player.pokeballs) != 0:
                for p in range(0, len(player.pokeballs)):
                    if player.pokeballs[p].quantity != 0:
                        type_text(str(player.pokeballs[p].name), 265, (p + 1) * 50, 20, (0, 0, 0))
                        type_text("x " + str(player.pokeballs[p].quantity), 530, (p + 1) * 50, 20, (0, 0, 0))
            cursor_bag.draw()
            if len(player.pokeballs) > 0 and cursor_bag.y == 53 and window_state == "toss_bag_pokeballs_2" and \
                    player.pokeballs[0].quantity != 0:
                player.pokeballs[0].draw()
            elif len(player.pokeballs) > 1 and cursor_bag.y == 98 and window_state == "toss_bag_pokeballs_2" and \
                    player.pokeballs[1].quantity != 0:
                player.pokeballs[1].draw()
            elif len(player.pokeballs) > 2 and cursor_bag.y == 143 and window_state == "toss_bag_pokeballs_2" and \
                    player.pokeballs[2].quantity != 0:
                player.pokeballs[2].draw()
            elif len(player.pokeballs) > 3 and cursor_bag.y == 188 and window_state == "toss_bag_pokeballs_2" and \
                    player.pokeballs[3].quantity != 0:
                player.pokeballs[3].draw()
            elif len(player.pokeballs) > 4 and cursor_bag.y == 233 and window_state == "toss_bag_pokeballs_2" and \
                    player.pokeballs[4].quantity != 0:
                player.pokeballs[4].draw()

            selected_item_m1.draw(106, 336)
            selected_item_m4.draw(453, 336)
            type_text("Toss out how many", 130, 352, 30, (0, 0, 0))
            type_text(str(selected_item.name) + "(s)?", 130, 387, 30, (0, 0, 0))

            if toss_number < 10:
                type_text("x00" + str(toss_number), 520, 375, 25, (0, 0, 0))
            elif 10 <= toss_number < 100:
                type_text("x0" + str(toss_number), 520, 375, 25, (0, 0, 0))
            elif toss_number >= 100:
                type_text("x" + str(toss_number), 520, 375, 25, (0, 0, 0))

            cursor_up.draw()
            if cursor_up.y != 336:
                cursor_up.y = 336
            elif cursor_up.y == 336:
                cursor_up.y = 340
            cursor_down.draw()
            if cursor_down.y != 418:
                cursor_down.y = 418
            elif cursor_down.y == 418:
                cursor_down.y = 414

        elif window_state == "give_items":
            screen.fill((0, 0, 0))
            pokemon_selection_menu.draw()
            type_text("Give to which POKEMON?", 50, 394, 28, (0, 0, 0))
            if give_items_cursor.x == 482 and give_items_cursor.y == 401:
                pokemon_menu_d1.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_d3.png"))
                menu_d1_x = 488
                menu_d1_y = 378
            else:
                pokemon_menu_d1.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_d1.png"))
                menu_d1_x = 488
                menu_d1_y = 384
            pokemon_menu_d1.draw(menu_d1_x, menu_d1_y)
            type_text("CANCEL", 544, 396, 26, (255, 255, 255))
            poke_counter = 1
            give_items_cursor.draw()

            if len(player.main_pokemon) == 1:
                if give_items_cursor.x == 8 and give_items_cursor.y == 150:
                    selection.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s4.png"))
                    selection.x = 7
                    selection.y = 75
                else:
                    selection.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s3.png"))
                    selection.x = 6
                    selection.y = 80
                selection.draw()
                player.main_pokemon[0].draw_menu(40, 125)
                type_text(str(player.main_pokemon[0].level), 134, 146, 25, (255, 255, 255))
                type_text(str(player.main_pokemon[0].current_hp), 130, 190, 25, (255, 255, 255))
                type_text(str(player.main_pokemon[0].hp), 180, 190, 25, (255, 255, 255))
                screen.blit(player.main_pokemon[0].sex_graphics, (185, 152))
                type_text(str(player.main_pokemon[0].name), 100, 120, 25, (255, 255, 255))
                player.main_pokemon[0].draw_hp_bar(47, 177)
                if player.main_pokemon[0].holding_item != "none":
                    held_item_icon.draw(66, 160, screen)

            show_pokemons_in_menu_if_more_than_one(player, pkm_menu_cursor, pkm_menu_1, pkm_menu_2, pkm_menu_3,
                                                   pkm_menu_4, pkm_menu_5, screen, held_item_icon, path_visual_elements)

        elif window_state == "give_items2":
            giving_item = "False"
            screen.fill((0, 0, 0))
            pokemon_selection_menu.draw()
            type_text("Give to which POKEMON?", 50, 394, 28, (0, 0, 0))
            if give_items_cursor.x == 482 and give_items_cursor.y == 401:
                pokemon_menu_d1.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_d3.png"))
                menu_d1_x = 488
                menu_d1_y = 378
            else:
                pokemon_menu_d1.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_d1.png"))
                menu_d1_x = 488
                menu_d1_y = 384
            pokemon_menu_d1.draw(menu_d1_x, menu_d1_y)
            type_text("CANCEL", 544, 396, 26, (255, 255, 255))
            poke_counter = 1
            give_items_cursor.draw()

            if len(player.main_pokemon) == 1:
                if give_items_cursor.x == 8 and give_items_cursor.y == 150:
                    selection.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s4.png"))
                    selection.x = 7
                    selection.y = 75
                else:
                    selection.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s3.png"))
                    selection.x = 6
                    selection.y = 80
                selection.draw()
                player.main_pokemon[0].draw_menu(40, 125)
                type_text(str(player.main_pokemon[0].level), 134, 146, 25, (255, 255, 255))
                type_text(str(player.main_pokemon[0].current_hp), 130, 190, 25, (255, 255, 255))
                type_text(str(player.main_pokemon[0].hp), 180, 190, 25, (255, 255, 255))
                screen.blit(player.main_pokemon[0].sex_graphics, (185, 152))
                type_text(str(player.main_pokemon[0].name), 100, 120, 25, (255, 255, 255))
                player.main_pokemon[0].draw_hp_bar(47, 177)
                if player.main_pokemon[0].holding_item != "none":
                    held_item_icon.draw(66, 160, screen)

            show_pokemons_in_menu_if_more_than_one(player, pkm_menu_cursor, pkm_menu_1, pkm_menu_2, pkm_menu_3,
                                                   pkm_menu_4, pkm_menu_5, screen, held_item_icon, path_visual_elements)

            c_use_item.draw(0, 320)
            type_text(str(selected_pkm.name) + " was given the", 24, 340, 30, (0, 0, 0))
            type_text(str(selected_item.name) + " to hold.", 24, 380, 30, (0, 0, 0))

        elif window_state == "give_items3":
            screen.fill((0, 0, 0))
            pokemon_selection_menu.draw()
            type_text("Give to which POKEMON?", 50, 394, 28, (0, 0, 0))
            if give_items_cursor.x == 482 and give_items_cursor.y == 401:
                pokemon_menu_d1.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_d3.png"))
                menu_d1_x = 488
                menu_d1_y = 378
            else:
                pokemon_menu_d1.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_d1.png"))
                menu_d1_x = 488
                menu_d1_y = 384
            pokemon_menu_d1.draw(menu_d1_x, menu_d1_y)
            type_text("CANCEL", 544, 396, 26, (255, 255, 255))
            poke_counter = 1
            give_items_cursor.draw()

            if len(player.main_pokemon) == 1:
                if give_items_cursor.x == 8 and give_items_cursor.y == 150:
                    selection.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s4.png"))
                    selection.x = 7
                    selection.y = 75
                else:
                    selection.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s3.png"))
                    selection.x = 6
                    selection.y = 80
                selection.draw()
                player.main_pokemon[0].draw_menu(40, 125)
                type_text(str(player.main_pokemon[0].level), 134, 146, 25, (255, 255, 255))
                type_text(str(player.main_pokemon[0].current_hp), 130, 190, 25, (255, 255, 255))
                type_text(str(player.main_pokemon[0].hp), 180, 190, 25, (255, 255, 255))
                screen.blit(player.main_pokemon[0].sex_graphics, (185, 152))
                type_text(str(player.main_pokemon[0].name), 100, 120, 25, (255, 255, 255))
                player.main_pokemon[0].draw_hp_bar(47, 177)
                if player.main_pokemon[0].holding_item != "none":
                    held_item_icon.draw(66, 160, screen)

            if len(player.pokemons) > 0:
                for poke in player.pokemons:
                    if give_items_cursor.x == 245 and give_items_cursor.y == 67:
                        pkm_menu_1.graphics = pygame.image.load(
                            os.path.join(path_visual_elements, "pokemon_menu_s2.png"))
                    elif give_items_cursor.y != 67:
                        pkm_menu_1.graphics = pygame.image.load(
                            os.path.join(path_visual_elements, "pokemon_menu_s1.png"))
                    if give_items_cursor.x == 245 and give_items_cursor.y == 133:
                        pkm_menu_2.graphics = pygame.image.load(
                            os.path.join(path_visual_elements, "pokemon_menu_s2.png"))
                    elif give_items_cursor.y != 133:
                        pkm_menu_2.graphics = pygame.image.load(
                            os.path.join(path_visual_elements, "pokemon_menu_s1.png"))
                    if give_items_cursor.x == 245 and give_items_cursor.y == 199:
                        pkm_menu_3.graphics = pygame.image.load(
                            os.path.join(path_visual_elements, "pokemon_menu_s2.png"))
                    elif give_items_cursor.y != 199:
                        pkm_menu_3.graphics = pygame.image.load(
                            os.path.join(path_visual_elements, "pokemon_menu_s1.png"))
                    if give_items_cursor.x == 245 and give_items_cursor.y == 265:
                        pkm_menu_4.graphics = pygame.image.load(
                            os.path.join(path_visual_elements, "pokemon_menu_s2.png"))
                    elif give_items_cursor.y != 265:
                        pkm_menu_4.graphics = pygame.image.load(
                            os.path.join(path_visual_elements, "pokemon_menu_s1.png"))
                    if give_items_cursor.x == 245 and give_items_cursor.y == 331:
                        pkm_menu_5.graphics = pygame.image.load(
                            os.path.join(path_visual_elements, "pokemon_menu_s2.png"))
                    elif give_items_cursor.y != 331:
                        pkm_menu_5.graphics = pygame.image.load(
                            os.path.join(path_visual_elements, "pokemon_menu_s1.png"))

                    if len(player.pokemons) == 1:
                        pkm_menu_1.draw(234, 53)
                        player.pokemons[0].draw_menu(285, 62)
                        type_text(str(player.pokemons[0].level), 370, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].current_hp), 544, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].hp), 584, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].name), 338, 58, 23, (255, 255, 255))
                        screen.blit(player.pokemons[0].sex_graphics, (420, 88))
                        player.pokemons[0].draw_hp_bar(454, 68)
                        if player.pokemons[0].holding_item != "none":
                            held_item_icon.draw(315, 94, screen)
                    elif len(player.pokemons) == 2:
                        pkm_menu_1.draw(234, 53)
                        player.pokemons[0].draw_menu(285, 62)
                        type_text(str(player.pokemons[0].level), 370, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].current_hp), 544, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].hp), 584, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].name), 338, 58, 23, (255, 255, 255))
                        screen.blit(player.pokemons[0].sex_graphics, (420, 88))
                        player.pokemons[0].draw_hp_bar(454, 68)
                        if player.pokemons[0].holding_item != "none":
                            held_item_icon.draw(315, 94, screen)
                        pkm_menu_2.draw(234, 53 + 64)
                        player.pokemons[1].draw_menu(285, 62 + 64)
                        type_text(str(player.pokemons[1].level), 370, 88 + 64, 20, (255, 255, 255))
                        type_text(str(player.pokemons[1].current_hp), 544, 88 + 64, 20, (255, 255, 255))
                        type_text(str(player.pokemons[1].hp), 584, 88 + 64, 20, (255, 255, 255))
                        type_text(str(player.pokemons[1].name), 338, 58 + 64, 23, (255, 255, 255))
                        screen.blit(player.pokemons[1].sex_graphics, (420, 88 + 64))
                        player.pokemons[1].draw_hp_bar(454, 68 + 67)
                        if player.pokemons[1].holding_item != "none":
                            held_item_icon.draw(315, 157, screen)
                    elif len(player.pokemons) == 3:
                        pkm_menu_1.draw(234, 53)
                        player.pokemons[0].draw_menu(285, 62)
                        type_text(str(player.pokemons[0].level), 370, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].current_hp), 544, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].hp), 584, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].name), 338, 58, 23, (255, 255, 255))
                        screen.blit(player.pokemons[0].sex_graphics, (420, 88))
                        player.pokemons[0].draw_hp_bar(454, 68)
                        if player.pokemons[0].holding_item != "none":
                            held_item_icon.draw(315, 94, screen)
                        pkm_menu_2.draw(234, 53 + 64)
                        player.pokemons[1].draw_menu(285, 62 + 64)
                        type_text(str(player.pokemons[1].level), 370, 88 + 64, 20, (255, 255, 255))
                        type_text(str(player.pokemons[1].current_hp), 544, 88 + 64, 20, (255, 255, 255))
                        type_text(str(player.pokemons[1].hp), 584, 88 + 64, 20, (255, 255, 255))
                        type_text(str(player.pokemons[1].name), 338, 58 + 64, 23, (255, 255, 255))
                        screen.blit(player.pokemons[1].sex_graphics, (420, 88 + 64))
                        player.pokemons[1].draw_hp_bar(454, 68 + 67)
                        if player.pokemons[1].holding_item != "none":
                            held_item_icon.draw(315, 157, screen)
                        pkm_menu_3.draw(234, 53 + (2 * 64))
                        player.pokemons[2].draw_menu(285, 62 + (2 * 64))
                        type_text(str(player.pokemons[2].level), 370, 88 + (2 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[2].current_hp), 544, 88 + (2 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[2].hp), 584, 88 + (2 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[2].name), 338, 58 + (2 * 64), 23, (255, 255, 255))
                        screen.blit(player.pokemons[2].sex_graphics, (420, 88 + (2 * 64)))
                        player.pokemons[2].draw_hp_bar(454, 68 + (2 * 64))
                        if player.pokemons[2].holding_item != "none":
                            held_item_icon.draw(315, 220, screen)
                    elif len(player.pokemons) == 4:
                        pkm_menu_1.draw(234, 53)
                        player.pokemons[0].draw_menu(285, 62)
                        type_text(str(player.pokemons[0].level), 370, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].current_hp), 544, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].hp), 584, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].name), 338, 58, 23, (255, 255, 255))
                        screen.blit(player.pokemons[0].sex_graphics, (420, 88))
                        player.pokemons[0].draw_hp_bar(454, 94)
                        if player.pokemons[0].holding_item != "none":
                            held_item_icon.draw(315, 62, screen)
                        pkm_menu_2.draw(234, 53 + 64)
                        player.pokemons[1].draw_menu(285, 62 + 64)
                        type_text(str(player.pokemons[1].level), 370, 88 + 64, 20, (255, 255, 255))
                        type_text(str(player.pokemons[1].current_hp), 544, 88 + 64, 20, (255, 255, 255))
                        type_text(str(player.pokemons[1].hp), 584, 88 + 64, 20, (255, 255, 255))
                        type_text(str(player.pokemons[1].name), 338, 58 + 64, 23, (255, 255, 255))
                        screen.blit(player.pokemons[1].sex_graphics, (420, 88 + 64))
                        player.pokemons[1].draw_hp_bar(454, 68 + 67)
                        if player.pokemons[1].holding_item != "none":
                            held_item_icon.draw(315, 157, screen)
                        pkm_menu_3.draw(234, 53 + (2 * 64))
                        player.pokemons[2].draw_menu(285, 62 + (2 * 64))
                        type_text(str(player.pokemons[2].level), 370, 88 + (2 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[2].current_hp), 544, 88 + (2 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[2].hp), 584, 88 + (2 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[2].name), 338, 58 + (2 * 64), 23, (255, 255, 255))
                        screen.blit(player.pokemons[2].sex_graphics, (420, 88 + (2 * 64)))
                        player.pokemons[2].draw_hp_bar(454, 68 + (2 * 64))
                        if player.pokemons[2].holding_item != "none":
                            held_item_icon.draw(315, 220, screen)
                        pkm_menu_4.draw(234, 53 + (3 * 64))
                        player.pokemons[3].draw_menu(285, 62 + (3 * 64))
                        type_text(str(player.pokemons[3].level), 370, 88 + (3 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[3].current_hp), 544, 88 + (3 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[3].hp), 584, 88 + (3 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[3].name), 338, 58 + (3 * 64), 23, (255, 255, 255))
                        screen.blit(player.pokemons[3].sex_graphics, (420, 88 + (3 * 64)))
                        player.pokemons[3].draw_hp_bar(454, 68 + (3 * 64))
                        if player.pokemons[3].holding_item != "none":
                            held_item_icon.draw(315, 286, screen)
                    elif len(player.pokemons) == 5:
                        pkm_menu_1.draw(234, 53)
                        player.pokemons[0].draw_menu(285, 62)
                        type_text(str(player.pokemons[0].level), 370, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].current_hp), 544, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].hp), 584, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].name), 338, 58, 23, (255, 255, 255))
                        screen.blit(player.pokemons[0].sex_graphics, (420, 88))
                        player.pokemons[0].draw_hp_bar(454, 68)
                        if player.pokemons[0].holding_item != "none":
                            held_item_icon.draw(315, 94, screen)
                        pkm_menu_2.draw(234, 53 + 64)
                        player.pokemons[1].draw_menu(285, 62 + 64)
                        type_text(str(player.pokemons[1].level), 370, 88 + 64, 20, (255, 255, 255))
                        type_text(str(player.pokemons[1].current_hp), 544, 88 + 64, 20, (255, 255, 255))
                        type_text(str(player.pokemons[1].hp), 584, 88 + 64, 20, (255, 255, 255))
                        type_text(str(player.pokemons[1].name), 338, 58 + 64, 23, (255, 255, 255))
                        screen.blit(player.pokemons[1].sex_graphics, (420, 88 + 64))
                        player.pokemons[1].draw_hp_bar(454, 68 + 67)
                        if player.pokemons[1].holding_item != "none":
                            held_item_icon.draw(315, 157, screen)
                        pkm_menu_3.draw(234, 53 + (2 * 64))
                        player.pokemons[2].draw_menu(285, 62 + (2 * 64))
                        type_text(str(player.pokemons[2].level), 370, 88 + (2 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[2].current_hp), 544, 88 + (2 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[2].hp), 584, 88 + (2 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[2].name), 338, 58 + (2 * 64), 23, (255, 255, 255))
                        screen.blit(player.pokemons[2].sex_graphics, (420, 88 + (2 * 64)))
                        player.pokemons[2].draw_hp_bar(454, 68 + (2 * 64))
                        if player.pokemons[2].holding_item != "none":
                            held_item_icon.draw(315, 220, screen)
                        pkm_menu_4.draw(234, 53 + (3 * 64))
                        player.pokemons[3].draw_menu(285, 62 + (3 * 64))
                        type_text(str(player.pokemons[3].level), 370, 88 + (3 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[3].current_hp), 544, 88 + (3 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[3].hp), 584, 88 + (3 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[3].name), 338, 58 + (3 * 64), 23, (255, 255, 255))
                        screen.blit(player.pokemons[3].sex_graphics, (420, 88 + (3 * 64)))
                        player.pokemons[3].draw_hp_bar(454, 68 + (3 * 64))
                        if player.pokemons[3].holding_item != "none":
                            held_item_icon.draw(315, 286, screen)
                        pkm_menu_5.draw(234, 53 + (4 * 64))
                        player.pokemons[4].draw_menu(285, 62 + (4 * 64))
                        type_text(str(player.pokemons[4].level), 370, 88 + (4 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[4].current_hp), 544, 88 + (4 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[4].hp), 584, 88 + (4 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[4].name), 338, 58 + (4 * 64), 23, (255, 255, 255))
                        screen.blit(player.pokemons[4].sex_graphics, (420, 88 + (4 * 64)))
                        player.pokemons[4].draw_hp_bar(454, 68 + (4 * 64))
                        if player.pokemons[4].holding_item != "none":
                            held_item_icon.draw(315, 350, screen)

            c_use_item.draw(0, 320)
            type_text(str(selected_pkm.name) + " is already holding", 24, 340, 30, (0, 0, 0))
            type_text("one " + str(selected_pkm.holding_item.name) + ".", 24, 380, 30, (0, 0, 0))

        elif window_state == "give_items4":
            c_use_item.draw(0, 320)
            type_text("Would you like to switch the", 24, 340, 30, (0, 0, 0))
            type_text("two items?", 24, 380, 30, (0, 0, 0))
            selected_item_m4.draw(398, 210)
            type_text("YES", 439, 232, 25, (0, 0, 0))
            type_text("NO", 439, 266, 25, (0, 0, 0))

            cursor_switch_items.draw()

        elif window_state == "give_items5":
            screen.fill((0, 0, 0))
            pokemon_selection_menu.draw()
            type_text("Give to which POKEMON?", 50, 394, 28, (0, 0, 0))
            if give_items_cursor.x == 482 and give_items_cursor.y == 401:
                pokemon_menu_d1.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_d3.png"))
                menu_d1_x = 488
                menu_d1_y = 378
            else:
                pokemon_menu_d1.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_d1.png"))
                menu_d1_x = 488
                menu_d1_y = 384
            pokemon_menu_d1.draw(menu_d1_x, menu_d1_y)
            type_text("CANCEL", 544, 396, 26, (255, 255, 255))
            poke_counter = 1
            give_items_cursor.draw()

            if len(player.main_pokemon) == 1:
                if give_items_cursor.x == 8 and give_items_cursor.y == 150:
                    selection.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s4.png"))
                    selection.x = 7
                    selection.y = 75
                else:
                    selection.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s3.png"))
                    selection.x = 6
                    selection.y = 80
                selection.draw()
                player.main_pokemon[0].draw_menu(40, 125)
                type_text(str(player.main_pokemon[0].level), 134, 146, 25, (255, 255, 255))
                type_text(str(player.main_pokemon[0].current_hp), 130, 190, 25, (255, 255, 255))
                type_text(str(player.main_pokemon[0].hp), 180, 190, 25, (255, 255, 255))
                screen.blit(player.main_pokemon[0].sex_graphics, (185, 152))
                type_text(str(player.main_pokemon[0].name), 100, 120, 25, (255, 255, 255))
                player.main_pokemon[0].draw_hp_bar(47, 177)
                if player.main_pokemon[0].holding_item != "none":
                    held_item_icon.draw(66, 160, screen)

            if len(player.pokemons) > 0:
                for poke in player.pokemons:
                    if give_items_cursor.x == 245 and give_items_cursor.y == 67:
                        pkm_menu_1.graphics = pygame.image.load(
                            os.path.join(path_visual_elements, "pokemon_menu_s2.png"))
                    elif give_items_cursor.y != 67:
                        pkm_menu_1.graphics = pygame.image.load(
                            os.path.join(path_visual_elements, "pokemon_menu_s1.png"))
                    if give_items_cursor.x == 245 and give_items_cursor.y == 133:
                        pkm_menu_2.graphics = pygame.image.load(
                            os.path.join(path_visual_elements, "pokemon_menu_s2.png"))
                    elif give_items_cursor.y != 133:
                        pkm_menu_2.graphics = pygame.image.load(
                            os.path.join(path_visual_elements, "pokemon_menu_s1.png"))
                    if give_items_cursor.x == 245 and give_items_cursor.y == 199:
                        pkm_menu_3.graphics = pygame.image.load(
                            os.path.join(path_visual_elements, "pokemon_menu_s2.png"))
                    elif give_items_cursor.y != 199:
                        pkm_menu_3.graphics = pygame.image.load(
                            os.path.join(path_visual_elements, "pokemon_menu_s1.png"))
                    if give_items_cursor.x == 245 and give_items_cursor.y == 265:
                        pkm_menu_4.graphics = pygame.image.load(
                            os.path.join(path_visual_elements, "pokemon_menu_s2.png"))
                    elif give_items_cursor.y != 265:
                        pkm_menu_4.graphics = pygame.image.load(
                            os.path.join(path_visual_elements, "pokemon_menu_s1.png"))
                    if give_items_cursor.x == 245 and give_items_cursor.y == 331:
                        pkm_menu_5.graphics = pygame.image.load(
                            os.path.join(path_visual_elements, "pokemon_menu_s2.png"))
                    elif give_items_cursor.y != 331:
                        pkm_menu_5.graphics = pygame.image.load(
                            os.path.join(path_visual_elements, "pokemon_menu_s1.png"))

                    if len(player.pokemons) == 1:
                        pkm_menu_1.draw(234, 53)
                        player.pokemons[0].draw_menu(285, 62)
                        type_text(str(player.pokemons[0].level), 370, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].current_hp), 544, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].hp), 584, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].name), 338, 58, 23, (255, 255, 255))
                        screen.blit(player.pokemons[0].sex_graphics, (420, 88))
                        player.pokemons[0].draw_hp_bar(454, 68)
                        if player.pokemons[0].holding_item != "none":
                            held_item_icon.draw(315, 94, screen)
                    elif len(player.pokemons) == 2:
                        pkm_menu_1.draw(234, 53)
                        player.pokemons[0].draw_menu(285, 62)
                        type_text(str(player.pokemons[0].level), 370, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].current_hp), 544, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].hp), 584, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].name), 338, 58, 23, (255, 255, 255))
                        screen.blit(player.pokemons[0].sex_graphics, (420, 88))
                        player.pokemons[0].draw_hp_bar(454, 68)
                        if player.pokemons[0].holding_item != "none":
                            held_item_icon.draw(315, 94, screen)
                        pkm_menu_2.draw(234, 53 + 64)
                        player.pokemons[1].draw_menu(285, 62 + 64)
                        type_text(str(player.pokemons[1].level), 370, 88 + 64, 20, (255, 255, 255))
                        type_text(str(player.pokemons[1].current_hp), 544, 88 + 64, 20, (255, 255, 255))
                        type_text(str(player.pokemons[1].hp), 584, 88 + 64, 20, (255, 255, 255))
                        type_text(str(player.pokemons[1].name), 338, 58 + 64, 23, (255, 255, 255))
                        screen.blit(player.pokemons[1].sex_graphics, (420, 88 + 64))
                        player.pokemons[1].draw_hp_bar(454, 68 + 67)
                        if player.pokemons[1].holding_item != "none":
                            held_item_icon.draw(315, 157, screen)
                    elif len(player.pokemons) == 3:
                        pkm_menu_1.draw(234, 53)
                        player.pokemons[0].draw_menu(285, 62)
                        type_text(str(player.pokemons[0].level), 370, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].current_hp), 544, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].hp), 584, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].name), 338, 58, 23, (255, 255, 255))
                        screen.blit(player.pokemons[0].sex_graphics, (420, 88))
                        player.pokemons[0].draw_hp_bar(454, 68)
                        if player.pokemons[0].holding_item != "none":
                            held_item_icon.draw(315, 94, screen)
                        pkm_menu_2.draw(234, 53 + 64)
                        player.pokemons[1].draw_menu(285, 62 + 64)
                        type_text(str(player.pokemons[1].level), 370, 88 + 64, 20, (255, 255, 255))
                        type_text(str(player.pokemons[1].current_hp), 544, 88 + 64, 20, (255, 255, 255))
                        type_text(str(player.pokemons[1].hp), 584, 88 + 64, 20, (255, 255, 255))
                        type_text(str(player.pokemons[1].name), 338, 58 + 64, 23, (255, 255, 255))
                        screen.blit(player.pokemons[1].sex_graphics, (420, 88 + 64))
                        player.pokemons[1].draw_hp_bar(454, 68 + 67)
                        if player.pokemons[1].holding_item != "none":
                            held_item_icon.draw(315, 157, screen)
                        pkm_menu_3.draw(234, 53 + (2 * 64))
                        player.pokemons[2].draw_menu(285, 62 + (2 * 64))
                        type_text(str(player.pokemons[2].level), 370, 88 + (2 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[2].current_hp), 544, 88 + (2 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[2].hp), 584, 88 + (2 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[2].name), 338, 58 + (2 * 64), 23, (255, 255, 255))
                        screen.blit(player.pokemons[2].sex_graphics, (420, 88 + (2 * 64)))
                        player.pokemons[2].draw_hp_bar(454, 68 + (2 * 64))
                        if player.pokemons[2].holding_item != "none":
                            held_item_icon.draw(315, 220, screen)
                    elif len(player.pokemons) == 4:
                        pkm_menu_1.draw(234, 53)
                        player.pokemons[0].draw_menu(285, 62)
                        type_text(str(player.pokemons[0].level), 370, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].current_hp), 544, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].hp), 584, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].name), 338, 58, 23, (255, 255, 255))
                        screen.blit(player.pokemons[0].sex_graphics, (420, 88))
                        player.pokemons[0].draw_hp_bar(454, 94)
                        if player.pokemons[0].holding_item != "none":
                            held_item_icon.draw(315, 62, screen)
                        pkm_menu_2.draw(234, 53 + 64)
                        player.pokemons[1].draw_menu(285, 62 + 64)
                        type_text(str(player.pokemons[1].level), 370, 88 + 64, 20, (255, 255, 255))
                        type_text(str(player.pokemons[1].current_hp), 544, 88 + 64, 20, (255, 255, 255))
                        type_text(str(player.pokemons[1].hp), 584, 88 + 64, 20, (255, 255, 255))
                        type_text(str(player.pokemons[1].name), 338, 58 + 64, 23, (255, 255, 255))
                        screen.blit(player.pokemons[1].sex_graphics, (420, 88 + 64))
                        player.pokemons[1].draw_hp_bar(454, 68 + 67)
                        if player.pokemons[1].holding_item != "none":
                            held_item_icon.draw(315, 157, screen)
                        pkm_menu_3.draw(234, 53 + (2 * 64))
                        player.pokemons[2].draw_menu(285, 62 + (2 * 64))
                        type_text(str(player.pokemons[2].level), 370, 88 + (2 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[2].current_hp), 544, 88 + (2 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[2].hp), 584, 88 + (2 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[2].name), 338, 58 + (2 * 64), 23, (255, 255, 255))
                        screen.blit(player.pokemons[2].sex_graphics, (420, 88 + (2 * 64)))
                        player.pokemons[2].draw_hp_bar(454, 68 + (2 * 64))
                        if player.pokemons[2].holding_item != "none":
                            held_item_icon.draw(315, 220, screen)
                        pkm_menu_4.draw(234, 53 + (3 * 64))
                        player.pokemons[3].draw_menu(285, 62 + (3 * 64))
                        type_text(str(player.pokemons[3].level), 370, 88 + (3 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[3].current_hp), 544, 88 + (3 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[3].hp), 584, 88 + (3 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[3].name), 338, 58 + (3 * 64), 23, (255, 255, 255))
                        screen.blit(player.pokemons[3].sex_graphics, (420, 88 + (3 * 64)))
                        player.pokemons[3].draw_hp_bar(454, 68 + (3 * 64))
                        if player.pokemons[3].holding_item != "none":
                            held_item_icon.draw(315, 286, screen)
                    elif len(player.pokemons) == 5:
                        pkm_menu_1.draw(234, 53)
                        player.pokemons[0].draw_menu(285, 62)
                        type_text(str(player.pokemons[0].level), 370, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].current_hp), 544, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].hp), 584, 88, 20, (255, 255, 255))
                        type_text(str(player.pokemons[0].name), 338, 58, 23, (255, 255, 255))
                        screen.blit(player.pokemons[0].sex_graphics, (420, 88))
                        player.pokemons[0].draw_hp_bar(454, 68)
                        if player.pokemons[0].holding_item != "none":
                            held_item_icon.draw(315, 94, screen)
                        pkm_menu_2.draw(234, 53 + 64)
                        player.pokemons[1].draw_menu(285, 62 + 64)
                        type_text(str(player.pokemons[1].level), 370, 88 + 64, 20, (255, 255, 255))
                        type_text(str(player.pokemons[1].current_hp), 544, 88 + 64, 20, (255, 255, 255))
                        type_text(str(player.pokemons[1].hp), 584, 88 + 64, 20, (255, 255, 255))
                        type_text(str(player.pokemons[1].name), 338, 58 + 64, 23, (255, 255, 255))
                        screen.blit(player.pokemons[1].sex_graphics, (420, 88 + 64))
                        player.pokemons[1].draw_hp_bar(454, 68 + 67)
                        if player.pokemons[1].holding_item != "none":
                            held_item_icon.draw(315, 157, screen)
                        pkm_menu_3.draw(234, 53 + (2 * 64))
                        player.pokemons[2].draw_menu(285, 62 + (2 * 64))
                        type_text(str(player.pokemons[2].level), 370, 88 + (2 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[2].current_hp), 544, 88 + (2 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[2].hp), 584, 88 + (2 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[2].name), 338, 58 + (2 * 64), 23, (255, 255, 255))
                        screen.blit(player.pokemons[2].sex_graphics, (420, 88 + (2 * 64)))
                        player.pokemons[2].draw_hp_bar(454, 68 + (2 * 64))
                        if player.pokemons[2].holding_item != "none":
                            held_item_icon.draw(315, 220)
                        pkm_menu_4.draw(234, 53 + (3 * 64))
                        player.pokemons[3].draw_menu(285, 62 + (3 * 64))
                        type_text(str(player.pokemons[3].level), 370, 88 + (3 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[3].current_hp), 544, 88 + (3 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[3].hp), 584, 88 + (3 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[3].name), 338, 58 + (3 * 64), 23, (255, 255, 255))
                        screen.blit(player.pokemons[3].sex_graphics, (420, 88 + (3 * 64)))
                        player.pokemons[3].draw_hp_bar(454, 68 + (3 * 64))
                        if player.pokemons[3].holding_item != "none":
                            held_item_icon.draw(315, 286, screen)
                        pkm_menu_5.draw(234, 53 + (4 * 64))
                        player.pokemons[4].draw_menu(285, 62 + (4 * 64))
                        type_text(str(player.pokemons[4].level), 370, 88 + (4 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[4].current_hp), 544, 88 + (4 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[4].hp), 584, 88 + (4 * 64), 20, (255, 255, 255))
                        type_text(str(player.pokemons[4].name), 338, 58 + (4 * 64), 23, (255, 255, 255))
                        screen.blit(player.pokemons[4].sex_graphics, (420, 88 + (4 * 64)))
                        player.pokemons[4].draw_hp_bar(454, 68 + (4 * 64))
                        if player.pokemons[4].holding_item != "none":
                            held_item_icon.draw(315, 350, screen)

            c_use_item.draw(0, 320)
            type_text("The " + str(tmp_item.name) + " was taken and", 24, 340, 30, (0, 0, 0))
            type_text("replaced with the " + str(selected_item.name) + ".", 24, 380, 30, (0, 0, 0))

        elif window_state == "use_bag_key_items":
            if selected_item.name == "Town Map":
                screen.fill((0, 0, 0))
                world_map.draw()
                if map_c == 1 or map_c == 2 or map_c == 3:
                    m_cursor.graphics = pygame.image.load(os.path.join(path_visual_elements, "map_cursor1.png"))
                elif map_c == 4 or map_c == 5 or map_c == 6:
                    m_cursor.graphics = pygame.image.load(os.path.join(path_visual_elements, "map_cursor2.png"))
                m_cursor.draw()
                m_cursor.move_y(Map_dy)
                m_cursor.move_x(Map_dx)
                if map_c == 1:
                    map_c = 2
                elif map_c == 2:
                    map_c = 3
                elif map_c == 3:
                    map_c = 4
                elif map_c == 4:
                    map_c = 5
                elif map_c == 5:
                    map_c = 6
                elif map_c == 6:
                    map_c = 1

                type_text("x:" + str(m_cursor.x) + " " + "y:" + str(m_cursor.y), 500, 28, 30, (255, 255, 255))
                if m_cursor.x == 123 and m_cursor.y == 167:
                    type_text("Indigo Plateau", 70, 28, 30, (255, 255, 255))
                elif m_cursor.x == 123 and m_cursor.y == 191:
                    type_text("Route 23", 70, 28, 30, (255, 255, 255))
                    type_text("Victory Road", 190, 28, 30, (255, 10, 10))
                elif m_cursor.x == 123 and 167 < m_cursor.y <= 263:
                    type_text("Route 23", 70, 28, 30, (255, 255, 255))
                elif 123 <= m_cursor.x <= 151 and m_cursor.y == 275:
                    type_text("Route 22", 70, 28, 30, (255, 255, 255))
                elif m_cursor.x == 165 and m_cursor.y == 275:
                    type_text("Viridian City", 70, 28, 30, (255, 255, 255))
                elif m_cursor.x == 165 and 323 >= m_cursor.y > 275:
                    type_text("Route 1", 70, 28, 30, (255, 255, 255))
                elif m_cursor.x == 165 and m_cursor.y == 335:
                    type_text("Pallet Town", 70, 28, 30, (255, 255, 255))
                elif m_cursor.x == 165 and m_cursor.y == 407:
                    type_text("Cannibar Island", 70, 28, 30, (255, 255, 255))
                    type_text("Pokemon Mansion", 250, 28, 30, (255, 10, 10))
                elif m_cursor.x == 165 and 395 >= m_cursor.y > 335:
                    type_text("Route 21", 70, 28, 30, (255, 255, 255))
                elif m_cursor.x == 249 and m_cursor.y == 407:
                    type_text("Route 20", 70, 28, 30, (255, 255, 255))
                    type_text("Seaform Island", 190, 28, 30, (255, 10, 10))
                elif 169 < m_cursor.x <= 319 and m_cursor.y == 407 and m_cursor.x != 249:
                    type_text("Route 20", 70, 28, 30, (255, 255, 255))
                elif m_cursor.x == 333 and m_cursor.y == 359:
                    type_text("Fuchsia City", 70, 28, 30, (255, 255, 255))
                    type_text("Safari Zone", 220, 28, 30, (255, 10, 10))
                elif m_cursor.x == 333 and 407 >= m_cursor.y > 359:
                    type_text("Route 19", 70, 28, 30, (255, 255, 255))
                elif 221 < m_cursor.x <= 319 and m_cursor.y == 359:
                    type_text("Route 18", 70, 28, 30, (255, 255, 255))
                elif m_cursor.x == 235 and 347 >= m_cursor.y > 239:
                    type_text("Route 17", 70, 28, 30, (255, 255, 255))
                elif m_cursor.x == 319 and m_cursor.y == 239:
                    type_text("Celdon City", 70, 28, 30, (255, 255, 255))
                elif 221 < m_cursor.x <= 305 and m_cursor.y == 239:
                    type_text("Route 16", 70, 28, 30, (255, 255, 255))
                elif m_cursor.x == 375 and m_cursor.y == 239:
                    type_text("Saffron City", 70, 28, 30, (255, 255, 255))
                elif 319 < m_cursor.x <= 361 and m_cursor.y == 239:
                    type_text("Route 7", 70, 28, 30, (255, 255, 255))
                elif m_cursor.x == 459 and m_cursor.y == 239:
                    type_text("Lavender Town", 70, 28, 30, (255, 255, 255))
                    type_text("Pokemon Tower", 260, 28, 30, (255, 10, 10))
                elif 375 < m_cursor.x <= 445 and m_cursor.y == 239:
                    type_text("Route 8", 70, 28, 30, (255, 255, 255))
                elif m_cursor.x == 165 and m_cursor.y == 191:
                    type_text("Peter City", 70, 28, 30, (255, 255, 255))
                elif m_cursor.x == 165 and 263 >= m_cursor.y > 191 and m_cursor.y != 215 and m_cursor.y != 239:
                    type_text("Route 2", 70, 28, 30, (255, 255, 255))
                elif m_cursor.x == 165 and m_cursor.y == 215:
                    type_text("Route 2", 70, 28, 30, (255, 255, 255))
                    type_text("Diglette's Cave Tower", 190, 28, 30, (255, 10, 10))
                elif m_cursor.x == 165 and m_cursor.y == 239:
                    type_text("Route 2", 70, 28, 30, (255, 255, 255))
                    type_text("Viridian Forest", 190, 28, 30, (10, 255, 10))
                elif 165 < m_cursor.x <= 249 and m_cursor.y == 191:
                    type_text("Route 3", 70, 28, 30, (255, 255, 255))
                elif m_cursor.x == 249 and 191 >= m_cursor.y > 167:
                    type_text("Route 3", 70, 28, 30, (255, 255, 255))
                elif m_cursor.x == 375 and m_cursor.y == 167:
                    type_text("Cerulean City", 70, 28, 30, (255, 255, 255))
                elif 235 < m_cursor.x <= 361 and m_cursor.y == 167 and m_cursor.x != 277:
                    type_text("Route 4", 70, 28, 30, (255, 255, 255))
                elif m_cursor.x == 277 and m_cursor.y == 167:
                    type_text("Route 4", 70, 28, 30, (255, 255, 255))
                    type_text("Mt. Moon", 190, 28, 30, (255, 10, 10))
                elif m_cursor.x == 375 and 155 >= m_cursor.y > 119:
                    type_text("Route 24", 70, 28, 30, (255, 255, 255))
                elif 375 < m_cursor.x <= 417 and m_cursor.y == 131:
                    type_text("Route 25", 70, 28, 30, (255, 255, 255))
                elif 375 < m_cursor.x <= 445 and m_cursor.y == 167:
                    type_text("Route 9", 70, 28, 30, (255, 255, 255))
                elif m_cursor.x == 459 and 227 >= m_cursor.y > 155 and m_cursor.y != 167 and m_cursor.y != 191:
                    type_text("Route 10", 70, 28, 30, (255, 255, 255))
                elif m_cursor.x == 459 and m_cursor.y == 167:
                    type_text("Route 10", 70, 28, 30, (255, 255, 255))
                    type_text("Rock Tunnel", 190, 28, 30, (255, 10, 10))
                elif m_cursor.x == 459 and m_cursor.y == 191:
                    type_text("Route 10", 70, 28, 30, (255, 255, 255))
                    type_text("Power Plant", 190, 28, 30, (255, 10, 10))
                elif m_cursor.x == 375 and m_cursor.y == 299:
                    type_text("Vermilion City", 70, 28, 30, (255, 255, 255))
                elif m_cursor.x == 375 and 287 >= m_cursor.y > 239 and m_cursor.y != 167 and m_cursor.y != 191:
                    type_text("Route 6", 70, 28, 30, (255, 255, 255))
                elif 375 < m_cursor.x <= 445 and m_cursor.y == 299 and m_cursor.x != 403:
                    type_text("Route 11", 70, 28, 30, (255, 255, 255))
                elif m_cursor.x == 403 and m_cursor.y == 299:
                    type_text("Route 11", 70, 28, 30, (255, 255, 255))
                    type_text("Diglette's Cave", 190, 28, 30, (255, 10, 10))
                elif m_cursor.x == 459 and 335 >= m_cursor.y > 239:
                    type_text("Route 12", 70, 28, 30, (255, 255, 255))
                elif 403 < m_cursor.x <= 445 and m_cursor.y == 335:
                    type_text("Route 13", 70, 28, 30, (255, 255, 255))
                elif m_cursor.x == 403 and 403 >= m_cursor.y > 323:
                    type_text("Route 14", 70, 28, 30, (255, 255, 255))
                elif 333 < m_cursor.x <= 389 and m_cursor.y == 359:
                    type_text("Route 15", 70, 28, 30, (255, 255, 255))

        elif window_state == "pokedex_table":
            screen.fill((0, 0, 0))
            pkd_table.draw()
            type_text("POKEDEX          TABLE OF CONTENTS", 100, 31, 30, (255, 255, 255))
            type_text("PICK", 518, 421, 25, (255, 255, 255))
            type_text("OK", 605, 421, 25, (255, 255, 255))

            type_text("Seen:", 430, 100, 25, (0, 0, 0))
            type_text(str(player.seen), 540, 130, 25, (255, 10, 10))
            type_text("Owned:", 430, 160, 25, (0, 0, 0))
            type_text(str(player.owned), 540, 190, 25, (255, 10, 10))

            type_text("POKEMON LIST", 30, 80, 30, (255, 10, 10))
            type_text("NUMERICAL MODE", 70, 120, 25, (0, 0, 0))
            type_text("POKEMON HABITATS", 30, 155, 30, (255, 10, 10))
            type_text("Grassland POKEMON", 70, 190, 25, (0, 0, 0))
            type_text("Forest POKEMON", 70, 225, 25, (0, 0, 0))
            type_text("Water's-edge POKEMON", 70, 264, 25, (0, 0, 0))
            type_text("Sea POKEMON", 70, 301, 25, (0, 0, 0))
            type_text("Cave POKEMON", 70, 338, 25, (0, 0, 0))
            type_text("Mountain POKEMON", 70, 375, 25, (0, 0, 0))

            pokedex_table_c.draw()

            if pokedex_table_c.y == 125:
                pokedex_icon.graphics = pygame.image.load(os.path.join(path_visual_elements, "pkd_icon1.png"))
                pokedex_icon.draw()
            elif pokedex_table_c.y == 195:
                pokedex_icon.graphics = pygame.image.load(os.path.join(path_visual_elements, "pkd_icon2.png"))
                pokedex_icon.draw()
            elif pokedex_table_c.y == 232:
                pokedex_icon.graphics = pygame.image.load(os.path.join(path_visual_elements, "pkd_icon3.png"))
                pokedex_icon.draw()
            elif pokedex_table_c.y == 269:
                pokedex_icon.graphics = pygame.image.load(os.path.join(path_visual_elements, "pkd_icon4.png"))
                pokedex_icon.draw()
            elif pokedex_table_c.y == 306:
                pokedex_icon.graphics = pygame.image.load(os.path.join(path_visual_elements, "pkd_icon5.png"))
                pokedex_icon.draw()
            elif pokedex_table_c.y == 343:
                pokedex_icon.graphics = pygame.image.load(os.path.join(path_visual_elements, "pkd_icon6.png"))
                pokedex_icon.draw()
            elif pokedex_table_c.y == 380:
                pokedex_icon.graphics = pygame.image.load(os.path.join(path_visual_elements, "pkd_icon7.png"))
                pokedex_icon.draw()

            cursor_up_dex.draw()
            if cursor_up_dex.y == 66:
                cursor_up_dex.y = 64
            elif cursor_up_dex.y == 64:
                cursor_up_dex.y = 62
            elif cursor_up_dex.y == 62:
                cursor_up_dex.y = 64
            elif cursor_up_dex.y == 64:
                cursor_up_dex.y = 66

            cursor_down_dex.draw()
            if cursor_down_dex.y == 386:
                cursor_down_dex.y = 388
            elif cursor_down_dex.y == 388:
                cursor_down_dex.y = 390
            elif cursor_down_dex.y == 390:
                cursor_down_dex.y = 388
            elif cursor_down_dex.y == 388:
                cursor_down_dex.y = 386

        elif window_state == "pokedex_table2":
            screen.fill((0, 0, 0))
            pkd_table.draw()
            type_text("POKEDEX          TABLE OF CONTENTS", 100, 31, 30, (255, 255, 255))
            type_text("PICK", 518, 421, 25, (255, 255, 255))
            type_text("OK", 605, 421, 25, (255, 255, 255))

            type_text("Seen:", 430, 100, 25, (0, 0, 0))
            type_text(str(player.seen), 540, 130, 25, (255, 10, 10))
            type_text("Owned:", 430, 160, 25, (0, 0, 0))
            type_text(str(player.owned), 540, 190, 25, (255, 10, 10))

            type_text("Rough-terrain POKEMON", 70, 80, 25, (0, 0, 0))
            type_text("Urban POKEMON", 70, 117, 25, (0, 0, 0))
            type_text("Rare POKEMON", 70, 154, 25, (0, 0, 0))

            type_text("SEARCH", 30, 186, 30, (255, 10, 10))

            type_text("A TO Z MODE", 70, 221, 25, (0, 0, 0))
            type_text("TYPE MODE", 70, 258, 25, (0, 0, 0))
            type_text("LIGHTEST MODE", 70, 295, 25, (0, 0, 0))
            type_text("SMALLEST MODE", 70, 332, 25, (0, 0, 0))

            type_text("CLOSE POKEDEX", 70, 375, 25, (255, 10, 10))

            pokedex_table_c2.draw()

            if pokedex_table_c2.y == 85:
                pokedex_icon.graphics = pygame.image.load(os.path.join(path_visual_elements, "pkd_icon8.png"))
                pokedex_icon.draw()
            elif pokedex_table_c2.y == 122:
                pokedex_icon.graphics = pygame.image.load(os.path.join(path_visual_elements, "pkd_icon9.png"))
                pokedex_icon.draw()
            elif pokedex_table_c2.y == 159:
                pokedex_icon.graphics = pygame.image.load(os.path.join(path_visual_elements, "pkd_icon10.png"))
                pokedex_icon.draw()
            elif pokedex_table_c2.y == 225:
                pokedex_icon.graphics = pygame.image.load(os.path.join(path_visual_elements, "pkd_icon11.png"))
                pokedex_icon.draw()
            elif pokedex_table_c2.y == 262:
                pokedex_icon.graphics = pygame.image.load(os.path.join(path_visual_elements, "pkd_icon12.png"))
                pokedex_icon.draw()
            elif pokedex_table_c2.y == 299:
                pokedex_icon.graphics = pygame.image.load(os.path.join(path_visual_elements, "pkd_icon13.png"))
                pokedex_icon.draw()
            elif pokedex_table_c2.y == 336:
                pokedex_icon.graphics = pygame.image.load(os.path.join(path_visual_elements, "pkd_icon14.png"))
                pokedex_icon.draw()
            elif pokedex_table_c2.y == 378:
                pokedex_icon.graphics = pygame.image.load(os.path.join(path_visual_elements, "pkd_icon15.png"))
                pokedex_icon.draw()

            cursor_up_dex.draw()
            if cursor_up_dex.y == 66:
                cursor_up_dex.y = 64
            elif cursor_up_dex.y == 64:
                cursor_up_dex.y = 62
            elif cursor_up_dex.y == 62:
                cursor_up_dex.y = 64
            elif cursor_up_dex.y == 64:
                cursor_up_dex.y = 66

            cursor_down_dex.draw()
            if cursor_down_dex.y == 386:
                cursor_down_dex.y = 388
            elif cursor_down_dex.y == 388:
                cursor_down_dex.y = 390
            elif cursor_down_dex.y == 390:
                cursor_down_dex.y = 388
            elif cursor_down_dex.y == 388:
                cursor_down_dex.y = 386

        elif window_state == "game":
            pallet_town.draw_and_update(screen, player)
            for grass in pallet_town.grasses:
                if grass.collide(player.shape) and (up or down or right or left):
                    player.pokemon_steps = player.pokemon_steps + 1
                    if random.randint(0, 100) > 95 and player.pokemon_steps > 50 and player.pokeballs[0].quantity > 0:
                        if random.randint(1, 4) == 1:
                            pokemon = Pokemon(1, path_pokemons, path_audio, path_moves_animations, path_exp_bar,
                                              path_hp_bar)
                        elif random.randint(1, 4) == 2:
                            pokemon = Pokemon(2, path_pokemons, path_audio, path_moves_animations, path_exp_bar,
                                              path_hp_bar)
                        elif random.randint(1, 4) == 3:
                            pokemon = Pokemon(3, path_pokemons, path_audio, path_moves_animations, path_exp_bar,
                                              path_hp_bar)
                        elif random.randint(1, 4) == 4:
                            pokemon = Pokemon(4, path_pokemons, path_audio, path_moves_animations, path_exp_bar,
                                              path_hp_bar)

                        player.pokemon_steps = 0
                        pokemon_exist = True
                if pokemon_exist:
                    battle_pokemon_counter = 0
                    window_state = "encounter_1"
                    pygame.mixer.music.load(os.path.join(path_audio, 'pokemon_battle.wav'))
                    pygame.mixer.music.play(-1)

            player.draw(screen)
            player.move_y(dy)
            player.move_x(dx)
            type_text("x:" + str(player.tmp_x) + " " + "y:" + str(player.tmp_y), 540, 20, 20, (255, 255, 255))
            type_text("Steps:" + str(player.pokemon_steps), 450, 20, 20, (255, 255, 255))
            type_text("Pokeballs:" + str(player.pokeballs[0].quantity), 20, 20, 20, (255, 255, 255))
            type_text("Pokemony:" + str(pokemonCounter + 1), 140, 20, 20, (255, 255, 255))
            type_text("Time:" + str(time), 500, 400, 20, (255, 255, 255))

        steps = redrawGameWindow(path_boy_player_animations, window_state, player, up, down, right, left, steps)