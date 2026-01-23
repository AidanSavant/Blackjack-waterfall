from .config import Config

import pygame
from pygame import Surface, time

class Game:
    def __init__(self, config: Config) -> None:
        pygame.init()
        pygame.display.set_caption("Waterfall blackjack game")

        self.fps = config.fps
        self.clock: time.Clock = pygame.time.Clock()

        self.screen: Surface = pygame.display.set_mode((config.width, config.height))
        self.screen.fill(config.background_rgb)

    def start_game_loop(self) -> None:
        while True:
            self.clock.tick(self.fps)
            pygame.display.flip() 

