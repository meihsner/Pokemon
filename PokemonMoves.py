import os
import pygame

size = width, height = 640, 480
pygame.display.set_caption('Pokemon')
background_color = (255, 255, 255)
screen = pygame.display.set_mode(size)


def load_images(number_of_images, path_moves_animations, name, extension, version):
    images_list = []
    if version == 1:
        for i in range(0, number_of_images):
            images_list.append(pygame.image.load(os.path.join(path_moves_animations +
                                                              name + "_" + str(i) + "." + extension)))
    elif version == 2:
        for i in range(0, number_of_images):
            if i <= 9:
                images_list.append(pygame.image.load(os.path.join(path_moves_animations +
                                                                  name + "_" + "0" + str(i) + "." + extension)))
            else:
                images_list.append(pygame.image.load(os.path.join(path_moves_animations +
                                                                  name + "_" + str(i) + "." + extension)))

    return images_list


class Moves:
    def __init__(self, name, path_audio, path_moves_animations):
        self.x = 0
        self.y = 25
        if name == "Scratch":
            self.name = "Scratch"
            self.number = 1
            self.type = "normal"
            self.category = "physical"
            self.max_pp = 56
            self.pp = 35
            self.current_pp = 35
            self.power = 40
            self.accuracy = 100
            self.atk_debuff = 0
            self.def_debuff = 0
            self.spd_debuff = 0
            self.acc_debuff = 0
            self.atk_buff = 0
            self.def_buff = 0
            self.spd_buff = 0
            self.acc_buff = 0
            self.effect = "Scratch inflicts damage and has no secondary effect."
            self.can_learn = ["Charmander", "Charmeleon", "Charizard", "Sandshrew", "Sandslash", "Nidoran_f",
                              "Nidorina", "Nidoqueen", "Paras", "Parasect", "Diglett", "Dugtrio", "Meowth", "Persian",
                              "Psyduck", "Golduck", "Mankey", "Primeape", "Kabuto", "Kabutops"]
            self.graphics_list = load_images(5, path_moves_animations, "scratch", "png", 1)
            self.graphics_list_enemy = load_images(5, path_moves_animations, "scratch_enemy", "png", 1)
            self.sound = os.path.join(path_audio, "scratch_sound.wav")
        elif name == "Growl":
            self.name = "Growl"
            self.number = 2
            self.type = "normal"
            self.category = "status"
            self.max_pp = 64
            self.pp = 40
            self.current_pp = 40
            self.power = 0
            self.accuracy = 100
            self.atk_debuff = 1
            self.def_debuff = 0
            self.spd_debuff = 0
            self.acc_debuff = 0
            self.atk_buff = 0
            self.def_buff = 0
            self.spd_buff = 0
            self.acc_buff = 0
            self.effect = "Growl decreases the Attack stat of all adjacent opponents by one stage."
            self.can_learn = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Spearow",
                              "Fearow", "Pikachu", "Raichu", "Nidoran_f", "Nidorina", "Nidoqueen", "Clefairy",
                              "Clefable", "Diglett", "Dugtrio", "Meowth", "Persian", "Ponyta", "Rapidash", "Slowpoke",
                              "Slowbro", "Doduo", "Dodrio", "Seel", "Dewgong", "Cubone", "Marowak", "Chansey",
                              "Kangaskhan", "Lapras", "Eevee", "Vaporeon", "Jolteon", "Flareon"]
            self.graphics_list = load_images(6, path_moves_animations, "growl", "png", 1)
            self.graphics_list_enemy = load_images(6, path_moves_animations, "growl_enemy", "png", 1)
            self.sound = os.path.join(path_audio, 'growl_sound.wav')
        elif name == "Ember":
            self.name = "Ember"
            self.number = 3
            self.type = "fire"
            self.category = "special"
            self.max_pp = 40
            self.pp = 25
            self.current_pp = 25
            self.power = 40
            self.accuracy = 100
            self.atk_debuff = 0
            self.def_debuff = 0
            self.spd_debuff = 0
            self.acc_debuff = 0
            self.atk_buff = 0
            self.def_buff = 0
            self.spd_buff = 0
            self.acc_buff = 0
            self.effect = "Ember deals damage and has a 10% chance of burning the target."
            self.can_learn = ["Charmander", "Charmeleon", "Charizard", "Vulpix", "Ninetales", "Growlithe", "Arcanine",
                              "Ponyta", "Rapidash", "Magmar", "Flareon", "Moltres"]
            self.graphics_list = load_images(12, path_moves_animations, "ember", "png", 2)
            self.graphics_list_enemy = load_images(12, path_moves_animations, "ember_enemy", "png", 2)
            self.sound = os.path.join(path_audio, 'ember_sound.wav')
        elif name == "Smokescreen":
            self.name = "Smokescreen"
            self.number = 4
            self.type = "normal"
            self.category = "status"
            self.max_pp = 32
            self.pp = 20
            self.current_pp = 20
            self.power = 0
            self.accuracy = 100
            self.atk_debuff = 0
            self.def_debuff = 0
            self.spd_debuff = 0
            self.acc_debuff = 1
            self.atk_buff = 0
            self.def_buff = 0
            self.spd_buff = 0
            self.acc_buff = 0
            self.effect = "Smokescreen lowers the target's accuracy stat by one stage."
            self.can_learn = ["Charmander", "Charmeleon", "Charizard", "Koffing", "Weezing", "Horsea", "Seadra",
                              "Magmar"]
            self.graphics_list = load_images(12, path_moves_animations, "smokescreen", "png", 2)
            self.graphics_list_enemy = load_images(12, path_moves_animations, "smokescreen_enemy", "png", 2)
            self.sound = os.path.join(path_audio, 'smokescreen_sound.wav')
        elif name == "Tackle":
            self.name = "Tackle"
            self.number = 5
            self.type = "normal"
            self.category = "physical"
            self.max_pp = 56
            self.pp = 35
            self.current_pp = 35
            self.power = 40
            self.accuracy = 100
            self.atk_debuff = 0
            self.def_debuff = 0
            self.spd_debuff = 0
            self.acc_debuff = 0
            self.atk_buff = 0
            self.def_buff = 0
            self.spd_buff = 0
            self.acc_buff = 0
            self.effect = "Tackle deals damage and has no secondary effect."
            self.can_learn = ["Bulbasaur", "Ivysaur", "Venusaur", "Squirtle", "Wartortle", "Blastoise", "Caterpie",
                              "Butterfree", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Nidoran_f",
                              "Nidorina", "Nidoqueen", "Nidoran_m", "Nidorino", "Nidoking", "Vulpix", "Ninetales",
                              "Venonat", "Venomoth", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke",
                              "Slowbro", "Magnemite", "Magneton", "Shellder", "Cloyster", "Onix", "Voltorb",
                              "Electrode", "Hitmonlee", "Hitmonchan", "Koffing", "Weezing", "Rhyhorn", "Rhydon",
                              "Staryu", "Starmie", "Tauros", "Magikarp", "Gyardos", "Eevee", "Vaporeon", "Jolteon",
                              "Flareon", "Porygon",
                              "Snorlax"]
            self.graphics_list = load_images(5, path_moves_animations, "tackle", "png", 1)
            self.graphics_list_enemy = load_images(5, path_moves_animations, "tackle_enemy", "png", 1)
            self.sound = os.path.join(path_audio, 'tackle_sound.wav')
        elif name == "Tail Whip":
            self.name = "Tail Whip"
            self.number = 6
            self.type = "normal"
            self.category = "status"
            self.max_pp = 48
            self.pp = 30
            self.current_pp = 30
            self.power = 0
            self.accuracy = 100
            self.atk_debuff = 0
            self.def_debuff = 1
            self.spd_debuff = 0
            self.acc_debuff = 0
            self.atk_buff = 0
            self.def_buff = 0
            self.spd_buff = 0
            self.acc_buff = 0
            self.effect = "Tail Whip decreases the Defense stat of all adjacent opponents by one stage."
            self.can_learn = ["Squirtle", "Wartortle", "Blastoise", "Rattata", "Raticate", "Pikachu", "Raichu",
                              "Nidoran_f", "Nidorina", "Nidoqueen", "Vulpix", "Ninetales", "Psyduck", "Golduck",
                              "Ponyta", "Rapidash", "Cubone", "Marowak", "Rhyhorn", "Rhydon", "Chansey", "Kangaskhan",
                              "Goldeen", "Seaking", "Tauros", "Eevee", "Vaporeon", "Jolteon", "Flareon"]
            self.graphics_list = load_images(8, path_moves_animations, "tail_whip", "png", 1)
            self.graphics_list_enemy = load_images(8, path_moves_animations, "tail_whip_enemy", "png", 1)
            self.sound = os.path.join(path_audio, 'tail_whip_sound.wav')
        elif name == "Withdraw":
            self.name = "Withdraw"
            self.number = 7
            self.type = "water"
            self.category = "status"
            self.max_pp = 64
            self.pp = 40
            self.current_pp = 40
            self.power = 0
            self.accuracy = 100
            self.atk_debuff = 0
            self.def_debuff = 0
            self.spd_debuff = 0
            self.acc_debuff = 0
            self.atk_buff = 0
            self.def_buff = 1
            self.spd_buff = 0
            self.acc_buff = 0
            self.effect = "Withdraw increases the user's Defense by one stage."
            self.can_learn = ["Squirtle", "Wartortle", "Blastoise", "Slowbro", "Shellder", "Cloyster", "Omanyte",
                              "Omastar"]
            self.graphics_list = load_images(5, path_moves_animations, "withdraw", "png", 1)
            self.graphics_list_enemy = load_images(5, path_moves_animations, "withdraw_enemy", "png", 1)
            self.sound = os.path.join(path_audio, 'withdraw_sound.wav')
        elif name == "Water gun":
            self.name = "Water gun"
            self.number = 8
            self.type = "water"
            self.category = "special"
            self.max_pp = 40
            self.pp = 25
            self.current_pp = 25
            self.power = 40
            self.accuracy = 100
            self.atk_debuff = 0
            self.def_debuff = 0
            self.spd_debuff = 0
            self.acc_debuff = 0
            self.atk_buff = 0
            self.def_buff = 0
            self.spd_buff = 0
            self.acc_buff = 0
            self.effect = "Water Gun inflicts damage and has no secondary effect."
            self.can_learn = ["Squirtle", "Wartortle", "Blastoise", "Psyduck", "Golduck", "Poliwag", "Poliwhirl",
                              "Poliwrath", "Tentacool", "Tentacruel", "Slowpoke", "Slowbro", "Shellder", "Cloyster",
                              "Krabby", "Kingler", "Horsea", "Seadra", "Staryu", "Starmie", "Lapras", "Vaporeon",
                              "Omanyte", "Omastar"]
            self.graphics_list = load_images(9, path_moves_animations, "water_gun", "png", 1)
            self.graphics_list_enemy = load_images(9, path_moves_animations, "water_gun_enemy", "png", 1)
            self.sound = os.path.join(path_audio, 'water_gun_sound.wav')
        elif name == "Sand attack":
            self.name = "Sand attack"
            self.number = 9
            self.type = "ground"
            self.category = "status"
            self.max_pp = 24
            self.pp = 15
            self.current_pp = 15
            self.power = 0
            self.accuracy = 100
            self.atk_debuff = 0
            self.def_debuff = 0
            self.spd_debuff = 0
            self.acc_debuff = 1
            self.atk_buff = 0
            self.def_buff = 0
            self.spd_buff = 0
            self.acc_buff = 0
            self.effect = "Sand Attack decreases the target's accuracy stat by one stage."
            self.can_learn = ["Pidgey", "Pidgeotto", "Pidgeot", "Sandshrew", "Sandslash", "Diglett", "Dugtrio",
                              "Geodude", "Gravler", "Golem", "Farfetch'd", "Rhyhorn", "Rhydon", "Eevee", "Vaporeon",
                              "Jolteon", "Flareon", "Kabuto", "Kabutops"]
            self.graphics_list = load_images(9, path_moves_animations, "sand_attack", "png", 1)
            self.graphics_list_enemy = load_images(9, path_moves_animations, "sand_attack_enemy", "png", 1)
            self.sound = os.path.join(path_audio, 'sand_attack_sound.wav')

    def draw(self, grafika):
        screen.blit(grafika, (self.x, self.y))
