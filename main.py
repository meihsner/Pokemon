from PokemonMechanics import *

def main():
     path_NPC = "NPCs/"
     path_audio = "audio/"
     path_moves_animation = "moves_animation/"
     path_items = "Items/"
     path_pokemons = "Pokemons/"
     path_exp_bar = "exp_bar/"
     path_hp_bar = "hp_bar/"
     path_structures = "structures/"
     path_moves_animations = "moves_animations/"
     path_boy_player_animations = "boy/"
     path_visual_elements = "visual_elements/"

     pygame.init()
     size = width, height = 640, 480
     pygame.display.set_caption('Pokemon')
     screen = pygame.display.set_mode(size)

     pygame.mixer.init()
     pygame.mixer.music.load(os.path.join(path_audio, 'intro.wav'))
     pygame.mixer.music.play(-1)

     player = Player(250, 275, path_boy_player_animations)

     game(player, screen, path_NPC, path_audio, path_moves_animation, path_items, path_pokemons, path_exp_bar, path_hp_bar,
          path_structures, path_moves_animations, path_boy_player_animations, path_visual_elements)


if __name__ == "__main__":
     main()

