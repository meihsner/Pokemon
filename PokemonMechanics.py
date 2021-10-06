import pygame
import os
import math


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
