from dataclasses import dataclass

@dataclass
class Card:
    rank: str
    rank_path: str = f"assets/{rank}_card"
