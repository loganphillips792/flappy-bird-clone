import pygame, sys, time
from settings import *

# https://www.pygame.org/docs/
# https://www.youtube.com/watch?v=VUFvY349ess 6:42 timestamp

class Game:
    def __init__(self):
        pygame.init()
        # creates a new Surface object that represents the actual displayed graphics. Any drawing you do to this Surface will become visible on the monitor
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Flappy Bird')
        self.clock = pygame.time.Clock()

        # sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
    
    def run(self):
        last_time = time.time()
        while True:
            # delta time
            dt = time.time() - last_time
            last_time = time.time()

            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # game logic
            pygame.display.update()
            self.clock.tick(FRAMERATE)

def main():
    game = Game()
    game.run()

main()