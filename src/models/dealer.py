from .player import Player

from dataclasses import dataclass

@dataclass(slots=True)
class Dealer(Player):
    def has_to_hit(self) -> bool:
        return self.hand.highest_value < 17

