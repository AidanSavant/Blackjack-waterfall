from .config import Config

from .models.deck import Deck
from .models.player import Player
from .models.dealer import Dealer

import pygame
from pygame import Surface, time

class Game:
    def __init__(self, config: Config) -> None:
        self._init_pygame(config.fps, config.width, config.height, config.background_rgb)

        self.deck = Deck()
        self._init_players()

    def _init_pygame(self, fps, width, height, background_rgb) -> None:
        pygame.init()
        pygame.display.set_caption("Blackjack game (waterfall implementation)")

        self.fps: int = fps
        self.clock: time.Clock = pygame.time.Clock()

        self.screen: Surface = pygame.display.set_mode((width, height))
        self.screen.fill(background_rgb)

    def _init_players(self) -> None:
        self.dealer: Dealer = Dealer(self.deck)
        self.player: Player = Player(self.deck)

    def start_game_loop(self) -> None:
        # TODO: Start drawing the player/dealer hand, the deck, and the hit/stand buttons
        # Daniel is working on the individual screens

        while True:
            self.clock.tick(self.fps)
            pygame.display.flip()


