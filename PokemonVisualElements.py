import random
from PokemonMechanics import *


def show_pokemons_in_menu_if_more_than_one(player, pkm_menu_cursor, pkm_menu_1, pkm_menu_2, pkm_menu_3,
                                           pkm_menu_4, pkm_menu_5, screen, held_item_icon, path_visual_elements):
    if len(player.pokemons) > 0:
        for poke in player.pokemons:
            if pkm_menu_cursor.x == 245 and pkm_menu_cursor.y == 67:
                pkm_menu_1.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s2.png"))
            elif pkm_menu_cursor.y != 67:
                pkm_menu_1.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s1.png"))
            if pkm_menu_cursor.x == 245 and pkm_menu_cursor.y == 133:
                pkm_menu_2.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s2.png"))
            elif pkm_menu_cursor.y != 133:
                pkm_menu_2.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s1.png"))
            if pkm_menu_cursor.x == 245 and pkm_menu_cursor.y == 199:
                pkm_menu_3.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s2.png"))
            elif pkm_menu_cursor.y != 199:
                pkm_menu_3.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s1.png"))
            if pkm_menu_cursor.x == 245 and pkm_menu_cursor.y == 265:
                pkm_menu_4.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s2.png"))
            elif pkm_menu_cursor.y != 265:
                pkm_menu_4.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s1.png"))
            if pkm_menu_cursor.x == 245 and pkm_menu_cursor.y == 331:
                pkm_menu_5.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s2.png"))
            elif pkm_menu_cursor.y != 331:
                pkm_menu_5.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s1.png"))

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


def load_images(number_of_images, path_man_player_animations, name, extension, version):
    images_list = []
    if version == 1:
        for i in range(0, number_of_images):
            images_list.append(pygame.image.load(os.path.join(path_man_player_animations + name +
                                                              "_" + str(i) + "." + extension)))
    elif version == 2:
        for i in range(0, number_of_images):
            if i <= 9:
                images_list.append(pygame.image.load(os.path.join(path_man_player_animations + name +
                                                                  "_" + "0" + str(i) + "." + extension)))
            else:
                images_list.append(pygame.image.load(os.path.join(path_man_player_animations + name +
                                                                  "_" + str(i) + "." + extension)))

    return images_list


def type_text(text, text_x, text_y, size, color):
    font = pygame.font.SysFont("Arial", size)
    rend = font.render(text, True, color)
    screen.blit(rend, (text_x, text_y))


class HeldItemIcon:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "held_item_icon.png"))

    def draw(self, x, y, screen):
        screen.blit(self.graphics, (x, y))


class BackgroundCatching:
    def __init__(self, path_visual_elements):
        self.height = 640
        self.width = 480
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "catching_screen.png"))

    def draw(self, screen):
        screen.blit(self.graphics, (0, 30))


class ChangeSkillBackground:
    def __init__(self, path_visual_elements):
        self.height = 640
        self.width = 480
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "change_move_screen.png"))

    def draw(self, screen):
        screen.blit(self.graphics, (0, 30))


class ChangeSkillMenu:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "change_move_screen_2.png"))

    def draw(self, screen):
        screen.blit(self.graphics, (512, 210))


class PokemonCaught:
    def __init__(self, path_man_player_animations):
        self.graphics_list = load_images(36, path_man_player_animations, "caught", "png", 2)

    def draw(self, graphics, screen):
        screen.blit(graphics, (0, 30))


class PokemonUncaught:
    def __init__(self, path_man_player_animations):
        self.graphics_list = load_images(37, path_man_player_animations, "uncaught", "png", 2)

    def draw(self, graphics, screen):
        screen.blit(graphics, (0, 30))


class EncounterMenu:
    def __init__(self, path_visual_elements):
        self.height = 100
        self.width = 100
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "encounter_menu.png"))

    def draw(self, screen):
        screen.blit(self.graphics, (350, 326))


class LevelUpInfo:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "level_up_info.png"))

    def draw(self, screen):
        screen.blit(self.graphics, (380, 212))


class BattleMenu:
    def __init__(self, number, path_visual_elements):
        if number == 1:
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "battle_interface_1.png"))
        elif number == 2:
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "battle_interface_2.png"))

    def draw(self, x, y, screen):
        screen.blit(self.graphics, (x, y))


class EffectMenu:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "effect_screen.png"))

    def draw(self, screen):
        screen.blit(self.graphics, (1, 329))


class MenuCursor:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "menu_cursor.png"))
        self.x = 385
        self.y = 356
        self.height = 40
        self.width = 25
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))


class CursorUpDown:
    def __init__(self, position, path_visual_elements):
        if position == "up":
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "cursor_up.png"))
        elif position == "down":
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "cursor_down.png"))
        self.x = 385
        self.y = 356

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))


class ChangeSkillCursor:
    def __init__(self, path_visual_elements):
        self.x = 540
        self.y = 240
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "menu_cursor.png"))

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))


class MoveCursor:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "moves_cursor.png"))
        self.x = 325
        self.y = 75

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))


class MapCursor:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "map_cursor1.png"))
        self.x = 123
        self.y = 167

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))

    def move_y(self, v):
        self.y = self.y + v

    def move_x(self, c):
        self.x = self.x + c


class BattleCursor:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "menu_cursor.png"))
        self.x = 36
        self.y = 357

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))


class EnterMenu:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "enter_menu.png"))
        self.x = 0
        self.y = 0
        self.height = 300
        self.width = 162
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))


class PokemonMenu:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_selection_menu.png"))
        self.x = 0
        self.y = 25
        self.height = 300
        self.width = 162
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))


class PokemonMenuMain:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s3.png"))
        self.x = 6
        self.y = 80

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))


class RegisterItem:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "registered_item.png"))

    def draw(self, x, y):
        screen.blit(self.graphics, (x, y))


class Options1:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "options_1.png"))
        self.x = 30
        self.y = 80

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))


class Options2:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "options_2.png"))
        self.x = 30
        self.y = 160

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))


class Options3:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "options_3.png"))
        self.x = 0
        self.y = 25

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))


class OptionCursor:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "option_cursor.png"))
        self.x = 67
        self.y = 196

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))


class PokemonMenuCancel:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_d1.png"))

    def draw(self, x, y):
        screen.blit(self.graphics, (x, y))


class PokemonMenuMain2:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_menu_s1.png"))

    def draw(self, x, y):
        screen.blit(self.graphics, (x, y))


class BattleInfo:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "battle_info.png"))

    def draw(self, x, y):
        screen.blit(self.graphics, (x, y))


class Inventory:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "bag_interface.png"))
        self.x = 0
        self.y = 26
        self.height = 480
        self.width = 320
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))


class MapItem:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "KantoTownMap.png"))
        self.x = 0
        self.y = 26

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))


class Backpack:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "b1.png"))
        self.x = 6
        self.y = 110
        self.height = 50
        self.width = 50
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))

    def type_text_backpack(self, text):
        type_text(text, 50, 50, 20, (0, 0, 0))


class PokemonSummary:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_summary_1.png"))
        self.x = 0
        self.y = 25

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))

    def type_text_summary(self, text):
        type_text(text, 26, 28, 30, (255, 255, 255))


class PokedexTable:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokedex_table.png"))
        self.x = 0
        self.y = 26

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))


class TrainerCard:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "trainer_card_1.png"))
        self.x = 0
        self.y = 30
        self.id = random.randint(10000, 99999)

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))


class PokemonMenuCursor:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "menu_cursor.png"))
        self.x = 8
        self.y = 150
        self.height = 40
        self.width = 25
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))


class PokedexTableCursor:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "menu_cursor.png"))
        self.x = 54
        self.y = 125

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))


class PokedexIcon:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "pkd_icon1.png"))
        self.x = 400
        self.y = 240

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))


class SelectedPokemonCursor:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "menu_cursor.png"))
        self.x = 480
        self.y = 280
        self.height = 40
        self.width = 25
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        screen.blit(self.graphics, (self.x, self.y))


class SelectedItemMenu:
    def __init__(self, number, path_visual_elements):
        if number == 1:
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "item_interface_1.png"))
        elif number == 2:
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "item_interface_2.png"))
        elif number == 3:
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "item_interface_3.png"))
        elif number == 4:
            self.graphics = pygame.image.load(os.path.join(path_visual_elements, "item_interface_4.png"))

    def draw(self, x, y):
        screen.blit(self.graphics, (x, y))


class PokemonItemMenu:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "pokemon_item_interface1.png"))

    def draw(self, x, y):
        screen.blit(self.graphics, (x, y))


class CannotUseItem:
    def __init__(self, path_visual_elements):
        self.graphics = pygame.image.load(os.path.join(path_visual_elements, "cannot_use_item.png"))

    def draw(self, x, y):
        screen.blit(self.graphics, (x, y))
