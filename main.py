import pygame
import sys
import random
from dataclasses import dataclass

# ==============================
# CONFIG
# ==============================
WIDTH, HEIGHT = 960, 540
FPS = 60

CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (240, 240, 240)
DARK = (10, 10, 10)

# ==============================
# DATA MODELS
# ==============================
@dataclass
class Record:
    title: str
    mood: str
    era: str
    genre: str
    used: bool = False

@dataclass
class Caller:
    name: str
    text: str
    desired_mood: str

# ==============================
# GAME DATA
# ==============================
RECORDS = [
    Record("Neon Dreams", "upbeat", "80s", "synth"),
    Record("Late Night Static", "sad", "80s", "rock"),
    Record("Midnight Drive", "nostalgic", "70s", "soft rock"),
    Record("Heart on Hold", "sad", "80s", "pop"),
    Record("Last Dance FM", "upbeat", "80s", "disco"),
    Record("Rain on Vinyl", "calm", "70s", "jazz"),
]

CALLER_POOL = [
    Caller("Mark", "I just got laid off. Drove around for an hour before calling.", "nostalgic"),
    Caller("Angela", "My mom used to listen to this station every night.", "calm"),
    Caller("Tom", "Everyone else is asleep. Feels like I'm the only one left.", "sad"),
    Caller("Lisa", "I don't want this night to end.", "upbeat"),
]

# ==============================
# INIT
# ==============================
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Last Broadcast")
clock = pygame.time.Clock()

FONT = pygame.font.SysFont("consolas", 18)
BIG_FONT = pygame.font.SysFont("consolas", 28)

# Load background
background = pygame.image.load("/Users/dineshkaarthick/Documents/TSA 2026/sprites/Background.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# ==============================
# GAME STATE
# ==============================
hour = 1
listeners = 5
transmitter = 100
perfect_moments = []

callers = CALLER_POOL.copy()
random.shuffle(callers)
current_caller = callers.pop()

mode = "CALL"  # CALL, RECORD_SELECT, GAME_OVER

# ==============================
# HELPERS
# ==============================
def draw_text(text, x, y, color=CYAN, font=FONT):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

def draw_wrapped_text(text, x, y, max_width, color=CYAN):
    words = text.split(" ")
    line = ""
    for word in words:
        test = line + word + " "
        if FONT.size(test)[0] > max_width:
            draw_text(line, x, y, color)
            y += 22
            line = word + " "
        else:
            line = test
    draw_text(line, x, y, color)

def next_caller():
    global current_caller, mode
    if not callers:
        end_game()
    else:
        current_caller = callers.pop()
        mode = "CALL"

def end_game():
    global mode
    mode = "GAME_OVER"

# ==============================
# RECORD SELECTION LOGIC
# ==============================
def handle_record_selection(record):
    global transmitter, listeners, hour

    record.used = True
    hour += 1
    transmitter -= 10

    if record.mood == current_caller.desired_mood:
        listeners += 2
        transmitter += 5
        perfect_moments.append((current_caller.name, record.title))
    else:
        listeners = max(0, listeners - 1)

    if hour > 12 or transmitter <= 0:
        end_game()
    else:
        next_caller()

# ==============================
# MAIN LOOP
# ==============================
running = True
while running:
    clock.tick(FPS)
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if mode == "CALL" and event.key == pygame.K_RETURN:
                mode = "RECORD_SELECT"

            elif mode == "RECORD_SELECT":
                if pygame.K_1 <= event.key <= pygame.K_9:
                    idx = event.key - pygame.K_1
                    if idx < len(RECORDS) and not RECORDS[idx].used:
                        handle_record_selection(RECORDS[idx])

            elif mode == "GAME_OVER" and event.key == pygame.K_ESCAPE:
                running = False

    # ==============================
    # HUD
    # ==============================
    pygame.draw.rect(screen, DARK, (20, 20, 260, 90))
    pygame.draw.rect(screen, CYAN, (20, 20, 260, 90), 2)
    draw_text(f"HOUR {hour}/12", 30, 30)
    draw_text(f"LISTENERS: {listeners}", 30, 55)
    draw_text(f"TRANSMITTER: {transmitter}%", 30, 80)

    # ==============================
    # MODES
    # ==============================
    if mode == "CALL":
        # Dialogue box bottom
        box_rect = pygame.Rect(40, HEIGHT - 160, WIDTH - 80, 120)
        pygame.draw.rect(screen, DARK, box_rect)
        pygame.draw.rect(screen, CYAN, box_rect, 3)

        draw_text(f"CALLER: {current_caller.name}", box_rect.x + 15, box_rect.y + 10, MAGENTA, BIG_FONT)
        draw_wrapped_text(
            current_caller.text,
            box_rect.x + 15,
            box_rect.y + 45,
            box_rect.width - 30
        )

        draw_text("Press ENTER to select a record", WIDTH - 330, HEIGHT - 30, YELLOW)

    elif mode == "RECORD_SELECT":
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(230)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))

        draw_text("SELECT A RECORD (1–9)", 40, 40, MAGENTA, BIG_FONT)

        y = 100
        for i, record in enumerate(RECORDS):
            color = WHITE if not record.used else (120, 120, 120)
            status = "[USED]" if record.used else ""
            draw_text(
                f"{i+1}. {record.title} | {record.mood} | {record.era} | {record.genre} {status}",
                60,
                y,
                color,
            )
            y += 30

    elif mode == "GAME_OVER":
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(240)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))

        draw_text("SUNRISE", WIDTH // 2 - 80, 40, CYAN, BIG_FONT)
        draw_text(f"Final Listeners: {listeners}", 100, 120)
        draw_text(f"Perfect Moments: {len(perfect_moments)}", 100, 150)

        y = 220
        draw_text("MEMORY WALL", 100, y, MAGENTA)
        y += 30
        for caller, song in perfect_moments:
            draw_text(f"{caller} — {song}", 120, y)
            y += 24

        draw_text("ESC to Quit", 100, HEIGHT - 40, YELLOW)

    pygame.display.flip()

pygame.quit()
sys.exit()
