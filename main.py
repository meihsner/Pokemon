from PokemonMechanics import *

path_NPC = "C:/Users/Admin/PycharmProjects/Pokemon/NPCs/"
path_audio = "C:/Users/Admin/PycharmProjects/Pokemon/audio/"
path_moves_animation = "C:/Users/Admin/PycharmProjects/Pokemon/moves_animation/"
path_items = "C:/Users/Admin/PycharmProjects/Pokemon/Items/"
path_pokemons = "C:/Users/Admin/PycharmProjects/Pokemon/Pokemons/"
path_exp_bar = "C:/Users/Admin/PycharmProjects/Pokemon/exp_bar/"
path_hp_bar = "C:/Users/Admin/PycharmProjects/Pokemon/hp_bar/"
path_structures = "C:/Users/Admin/PycharmProjects/Pokemon/structures/"
path_moves_animations = "C:/Users/Admin/PycharmProjects/Pokemon/moves_animations/"
path_boy_player_animations = "C:/Users/Admin/PycharmProjects/Pokemon/boy/"
path_visual_elements = "C:/Users/Admin/PycharmProjects/Pokemon/visual_elements/"

pygame.init()
size = width, height = 640, 480
pygame.display.set_caption('Pokemon')
background_color = (255, 255, 255)
screen = pygame.display.set_mode(size)

pygame.mixer.init()
pygame.mixer.music.load(os.path.join(path_audio, 'intro.wav'))
pygame.mixer.music.play(-1)

player = Player(250, 275, path_boy_player_animations)

game(player, screen, path_NPC, path_audio, path_moves_animation, path_items, path_pokemons, path_exp_bar, path_hp_bar,
     path_structures, path_moves_animations, path_boy_player_animations, path_visual_elements)
