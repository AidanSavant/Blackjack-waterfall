import pygame
pygame.init()

# Window
W, H = 1000, 700
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Blackjack UI Mock")

# Colors
GREEN = (0, 120, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
DARK = (50, 50, 50)

# Fonts
FONT = pygame.font.SysFont("arial", 24)
BIG = pygame.font.SysFont("arial", 36)

# Keeps track of fps
clock = pygame.time.Clock()

# ---- Mock State (replace later with backend.get_state()) ----
state = {
    "player_hand": ["A♠", "10♦"],
    "dealer_hand": ["K♣", "??"],
    "player_total": 21,
    "dealer_total": 10,
    "player_score": 2,
    "dealer_score": 1,
    "deck_count": 42,
    "game_over": False,
    "message": "Your turn"
}

# ---- Simple Button ----
class Button:
    def __init__(self, text, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

    def draw(self, surf):
        pygame.draw.rect(surf, GRAY, self.rect, border_radius=10)
        pygame.draw.rect(surf, DARK, self.rect, 2, border_radius=10)
        t = FONT.render(self.text, True, BLACK)
        surf.blit(t, t.get_rect(center=self.rect.center))

    def clicked(self, pos):
        return self.rect.collidepoint(pos)

hit_btn = Button("Hit", 350, 610, 120, 50)
stand_btn = Button("Stand", 530, 610, 120, 50)
again_btn = Button("Play Again", 420, 610, 160, 50)

# ---- Drawing helpers ----
def draw_text(text, x, y, big=False):
    f = BIG if big else FONT
    img = f.render(text, True, WHITE)
    screen.blit(img, (x, y))

def draw_hand(cards, y, label):
    # Draws label
    if cards == state["dealer_hand"]:
        draw_text(label, 400, y - 55, big=True)
    elif cards == state["player_hand"]:
        draw_text(label, 400, y + 130, big=True)
    # Draws cards
    x = 400
    for c in cards:
        rect = pygame.Rect(x, y, 80, 120)
        pygame.draw.rect(screen, WHITE, rect, border_radius=8)
        pygame.draw.rect(screen, BLACK, rect, 2, border_radius=8)
        t = FONT.render(c, True, BLACK)
        screen.blit(t, (x + 12, y + 10))
        x += 95

def draw_deck():
    rect = pygame.Rect(50, H//2 - 60, 80, 120)
    rect_back1 = pygame.Rect(52.5, H//2 - 57.5, 80, 120)
    rect_back2 = pygame.Rect(55, H//2 - 55, 80, 120)
    
    # 3rd layer of the deck design
    pygame.draw.rect(screen, DARK, rect_back2, border_radius=8)
    pygame.draw.rect(screen, BLACK, rect_back2, 2, border_radius=8)
    # 2nd layer of the deck design
    pygame.draw.rect(screen, DARK, rect_back1, border_radius=8)
    pygame.draw.rect(screen, BLACK, rect_back1, 2, border_radius=8)
    # Top layer of the deck design
    pygame.draw.rect(screen, DARK, rect, border_radius=8)
    pygame.draw.rect(screen, BLACK, rect, 2, border_radius=8)
    t = FONT.render("Deck", True, WHITE)
    screen.blit(t, (65, H//2 - 20))
    # Deck count just for testing purposes (Can stay if needed)
    t = FONT.render(f"Deck: {state['deck_count']}", True, WHITE)
    screen.blit(t, (40, H//2 + 70))

# Draw score in the middle of the screen
# TODO: Follow up with backend to get actual scores
def draw_score():
    s = f"Player {state['player_score']}  -  Dealer {state['dealer_score']}"
    draw_text(s, W//2 - 120, 300)

# ---- Main Loop ----
running = True
while running:
    screen.fill(GREEN)

    # Areas
    # Dealer area (Dark green background)
    pygame.draw.rect(screen, (0, 90, 0), (180, 50, W-350, 250), border_radius=20)
    # Player area (Dark green background)
    pygame.draw.rect(screen, (0, 90, 0), (180, 340, W-350, 250), border_radius=20)

    # Draw hands
    draw_hand(state["dealer_hand"], 120, "Dealer's Hand")
    draw_hand(state["player_hand"], 400, "Player's Hand")

    # Deck
    draw_deck()

    # Totals + message
    draw_text(f"Dealer: {state['dealer_total']}", 430, 250)
    draw_text(f"Player: {state['player_total']}", 430, 355)
    draw_text(state["message"], W//2 - 80, 10, big=True)

    # Score
    draw_score()

    # Buttons
    if not state["game_over"]:
        hit_btn.draw(screen)
        stand_btn.draw(screen)
    else:
        again_btn.draw(screen)

    # Events (mock behavior only)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if hit_btn.clicked(pos) and not state["game_over"]:
                state["player_hand"].append("5♥")
                state["player_total"] += 5
                state["message"] = "You hit!"
                if state["player_total"] > 21:
                    state["message"] = "Bust!"
                    state["game_over"] = True
            if stand_btn.clicked(pos) and not state["game_over"]:
                state["message"] = "Dealer's turn..."
                state["game_over"] = True
            if again_btn.clicked(pos) and state["game_over"]:
                # reset mock
                state.update({
                    "player_hand": ["A♠", "10♦"],
                    "dealer_hand": ["K♣", "??"],
                    "player_total": 21,
                    "dealer_total": 10,
                    "game_over": False,
                    "message": "Your turn"
                })

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
