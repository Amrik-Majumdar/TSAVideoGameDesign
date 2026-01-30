# """
# The Last Broadcast - Bootstrap loader.

# This file serves as the entry point and simply delegates to the
# modular src package. All game logic has been moved to src/.

# To run the game: python main.py
# """

# from src.main import main

# if __name__ == "__main__":
#     main()
# above is used for the old version (ignore for now)

# import pygame
# import sys
# import random
# from dataclasses import dataclass, field

# # ==============================
# # CONFIG
# # ==============================
# WIDTH, HEIGHT = 960, 540
# FPS = 60

# CYAN = (0, 255, 255)
# MAGENTA = (255, 0, 255)
# YELLOW = (255, 255, 0)
# BLACK = (0, 0, 0)
# WHITE = (240, 240, 240)
# DARK = (10, 10, 10)

# # ==============================
# # DATA MODELS
# # ==============================
# @dataclass
# class Record:
#     title: str
#     genre: str
#     mood: str
#     era: str
#     used: bool = False

# @dataclass
# class Caller:
#     name: str
#     text: str
#     needs: dict
#     minHour: int
#     used: bool = False
#     hint_lines: list = None
#     responses: dict = None
#     relationship: str = None
#     relatedTo: str = None
#     special: str = None

# # ==============================
# # RECORDS
# # ==============================
# RECORDS = [
#     Record("Rebel Heart", "Rock", "Defiant", "1980s"),
#     Record("Blue Monday", "Blues", "Melancholy", "1970s"),
#     Record("Starlight Serenade", "Jazz", "Tender", "1960s"),
#     Record("Summer Drive", "Pop", "Upbeat", "1980s"),
#     Record("Yesterday's Song", "Folk", "Nostalgic", "1970s"),
#     Record("Neon Dreams", "Ambient", "Contemplative", "1980s"),
#     Record("Factory Floor", "Rock", "Upbeat", "1980s"),
#     Record("Moonlit Waltz", "Jazz", "Nostalgic", "1960s"),
#     Record("Highway 61", "Blues", "Defiant", "1970s"),
#     Record("Sarah's Song", "Folk", "Tender", "1980s"),
#     Record("Cityscape", "Ambient", "Melancholy", "1980s"),
#     Record("Morning Light", "Pop", "Upbeat", "1980s"),
# ]

# # ==============================
# # CALLERS WITH HINTS
# # ==============================
# CALLERS = [
#     Caller(
#         "Bill", minHour=2,
#         text="Just got laid off. Twenty years at the plant. They gave me a Casio watch. I don't know who I am if I'm not building things.",
#         needs={"genre": "Rock", "mood": "Defiant", "era": "1980s"},
#         relationship="factory_father",
#         hint_lines=["I need something strong, something to get me back up!", "Maybe something from the 80s?"],
#         responses={
#             "perfect": "Yeah... you're right. We built this town. We're not done yet. Thank you.",
#             "good": "Appreciate it. Helps to know someone's listening.",
#             "poor": "Not what I needed. Goodnight."
#         }
#     ),
#     Caller(
#         "Marie", minHour=2,
#         text="My daughter turns sixteen tomorrow. I remember holding her the day she was born. Where did the time go?",
#         needs={"genre": "Folk", "mood": "Nostalgic", "era": "1970s"},
#         hint_lines=["Something gentle, perhaps with memories.", "I miss the old songs..."],
#         responses={
#             "perfect": "That's it. That's exactly it. Time moves, but love stays. Thank you.",
#             "good": "That's nice. Thank you.",
#             "poor": "I should go wrap her present."
#         }
#     ),
#     Caller(
#         "Tommy", minHour=3,
#         text="Driving to the coast. Left at midnight. If I stop, I'll turn around. I can't turn around.",
#         needs={"genre": "Pop", "mood": "Upbeat", "era": "1980s"},
#         hint_lines=["Keep me moving with something fast.", "A song with energy, you know?"],
#         responses={
#             "perfect": "This is it. This is the soundtrack for starting over. Thank you!",
#             "good": "Okay. Yeah. I can do this.",
#             "poor": "That's making me sadder. I gotta go."
#         }
#     ),
#     Caller(
#         "Lisa", minHour=4,
#         text="Dad came home and just sat there. Wouldn't talk. Wouldn't look at me. I've never seen him cry.",
#         needs={"genre": "Blues", "mood": "Tender", "era": "1970s"},
#         relationship="factory_daughter",
#         relatedTo="factory_father",
#         hint_lines=["Something gentle, for when words won't come.", "Maybe something that speaks for us?"],
#         responses={
#             "perfect": "Wait... is this for him too? Tell him I love him. Please.",
#             "good": "Thank you. That's beautiful.",
#             "poor": "I need to check on him. Goodnight."
#         }
#     ),
#     Caller(
#         "James", minHour=5,
#         text="Mom used to sing me this song. Can't remember the words. She's in the hospital. They say I should prepare myself.",
#         needs={"genre": "Jazz", "mood": "Nostalgic", "era": "1960s"},
#         relationship="hospital_son",
#         hint_lines=["Something from the 60s, I think.", "It was jazz... she loved jazz."],
#         responses={
#             "perfect": "That's the one. How did you know? Thank you. I'm going to sit with her now.",
#             "good": "That's close. Really close. Thanks.",
#             "poor": "No, that's not it. Sorry."
#         }
#     ),
#     Caller(
#         "Angela", minHour=6,
#         text="I own the factory. Had to let thirty people go today. Known these families for decades. Some won't look at me now.",
#         needs={"genre": "Jazz", "mood": "Melancholy", "era": "1960s"},
#         relationship="factory_owner",
#         relatedTo="factory_father",
#         hint_lines=["Something that understands regret.", "From a simpler time... the 60s."],
#         responses={
#             "perfect": "I thought someone would yell at me. But you just listened. Thank you.",
#             "good": "I appreciate that. Really.",
#             "poor": "I understand. Thanks."
#         }
#     ),
#     Caller(
#         "Daniel", minHour=7,
#         text="At the hospital. Mom's not going to make it. Nurses say I should talk to her, but what do you say?",
#         needs={"genre": "Jazz", "mood": "Tender", "era": "1960s"},
#         relationship="hospital_son_return",
#         relatedTo="hospital_son",
#         hint_lines=["Something soft, tender.", "She loved the old standards..."],
#         responses={
#             "perfect": "That song. She sang that to me. You remembered. Thank you.",
#             "good": "That's beautiful. Thank you.",
#             "poor": "I need to get back to her."
#         }
#     ),
#     Caller(
#         "Rebecca", minHour=3,
#         text="My husband and I used to dance in the kitchen. Three years ago today, he died. I can still feel his hand on my back.",
#         needs={"genre": "Jazz", "mood": "Nostalgic", "era": "1960s"},
#         hint_lines=["Something we danced to...", "From the 60s, when we were young."],
#         responses={
#             "perfect": "That's our song. Thank you so much.",
#             "good": "He would have liked that.",
#             "poor": "Not quite right, but thanks."
#         }
#     ),
#     Caller(
#         "Carlos", minHour=2,
#         text="Night shift just ended. Factory closes next month. Thirty years. Don't know how to be anything else.",
#         needs={"genre": "Blues", "mood": "Defiant", "era": "1970s"},
#         hint_lines=["Something with fight in it.", "Blues from the 70s, maybe?"],
#         responses={
#             "perfect": "That's right. We're not done yet. Not by a long shot.",
#             "good": "Appreciate it, friend.",
#             "poor": "Yeah. Maybe. Goodnight."
#         }
#     ),
#     Caller(
#         "Sarah", minHour=9,
#         text="I don't know if you remember me. I used to call in, years ago. You played our song. I said I'd wait for the morning show. I did.",
#         needs={"genre": "Folk", "mood": "Tender", "era": "1980s"},
#         special="sarah",
#         hint_lines=["Do you remember? Folk... tender...", "It was our song, from the 80s."],
#         responses={
#             "perfect": "You remembered. After all these years. Thank you for keeping the morning show alive.",
#             "good": "That's close. Thank you for trying.",
#             "poor": "It's okay. It was a long time ago."
#         }
#     ),
#     Caller(
#         "Michelle", minHour=8,
#         text="I'm a nurse. Double shift just ended. Lost someone tonight—young kid. I keep seeing his mother's face.",
#         needs={"genre": "Ambient", "mood": "Contemplative", "era": "1980s"},
#         hint_lines=["I need quiet. Something contemplative.", "Something modern, ambient..."],
#         responses={
#             "perfect": "Sometimes we need the quiet. Thank you for understanding.",
#             "good": "Thank you. That helps.",
#             "poor": "I need something else. Thanks."
#         }
#     ),
#     Caller(
#         "Frank", minHour=2,
#         text="Son's getting married tomorrow. Giving a speech. How do you tell your kid you're proud without crying?",
#         needs={"genre": "Folk", "mood": "Tender", "era": "1970s"},
#         hint_lines=["Something gentle, heartfelt.", "Folk, I think. From the 70s."],
#         responses={
#             "perfect": "Perfect. You always know just what we need.",
#             "good": "That's nice. Really nice.",
#             "poor": "Not quite right, but thanks."
#         }
#     ),
#     Caller(
#         "Jennifer", minHour=5,
#         text="Just broke up with my boyfriend. Five years. He said I work too much. Maybe he's right. Don't know who I am without the work.",
#         needs={"genre": "Pop", "mood": "Upbeat", "era": "1980s"},
#         hint_lines=["Something to lift me up.", "Pop, upbeat, 80s vibes."],
#         responses={
#             "perfect": "Maybe this IS the start of something good. Thank you.",
#             "good": "Okay. That helps.",
#             "poor": "Can't do upbeat right now. Sorry."
#         }
#     ),
#     Caller(
#         "Robert", minHour=6,
#         text="Truck driver. Been on the road three weeks. Haven't seen my family. Sometimes forget what my daughter's voice sounds like.",
#         needs={"genre": "Folk", "mood": "Nostalgic", "era": "1970s"},
#         hint_lines=["Something that reminds me of home.", "Folk from the old days..."],
#         responses={
#             "perfect": "That's the one. Makes me remember. Thank you, friend.",
#             "good": "Appreciate that. Gets lonely.",
#             "poor": "Thanks for trying."
#         }
#     ),
#     Caller(
#         "David", minHour=4,
#         text="Just retired. Forty years teaching. Walked out today for the last time. Now what? Just... now what?",
#         needs={"genre": "Jazz", "mood": "Contemplative", "era": "1960s"},
#         hint_lines=["Something thoughtful, reflective.", "Jazz, something to think to."],
#         responses={
#             "perfect": "Maybe this is the beginning, not the end. Thank you for that.",
#             "good": "That's thoughtful. Thanks.",
#             "poor": "Not sure that's what I needed."
#         }
#     ),
#     Caller(
#         "Marcus", minHour=9,
#         text="My band broke up tonight. We were supposed to make it big. Now I'm thirty-five with a guitar and nothing else.",
#         needs={"genre": "Rock", "mood": "Defiant", "era": "1980s"},
#         hint_lines=["Something that fights back.", "Rock. 80s rock."],
#         responses={
#             "perfect": "You're right. It's not over. Not if I don't let it be. Thank you.",
#             "good": "Thanks, man. Needed that.",
#             "poor": "Maybe it IS over."
#         }
#     ),
#     Caller(
#         "Paul", minHour=10,
#         text="Daughter just called. She's having a baby. I'm going to be a grandfather. Never thought I'd make it this far.",
#         needs={"genre": "Pop", "mood": "Upbeat", "era": "1980s"},
#         hint_lines=["I'm celebrating! Something joyful!", "Pop, upbeat, 80s!"],
#         responses={
#             "perfect": "That's PERFECT! That's exactly how I feel! Thank you!",
#             "good": "That's great. Really great.",
#             "poor": "Not quite the celebration I hoped for."
#         }
#     ),
#     Caller(
#         "Helen", minHour=8,
#         text="Wedding anniversary. He's been gone five years. I still set a place for him at dinner. Is that crazy?",
#         needs={"genre": "Jazz", "mood": "Tender", "era": "1960s"},
#         hint_lines=["Something tender, loving.", "Jazz from when we were young..."],
#         responses={
#             "perfect": "That's beautiful. Love doesn't end. Thank you for reminding me.",
#             "good": "That's sweet. Thank you.",
#             "poor": "Not quite right, but thanks."
#         }
#     ),
# ]

# # ==============================
# # INIT PYGAME
# # ==============================
# pygame.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("The Last Broadcast")
# clock = pygame.time.Clock()

# FONT = pygame.font.SysFont("consolas", 18)
# BIG_FONT = pygame.font.SysFont("consolas", 28)

# # Try to load background, if it fails use a solid color
# try:
#     background = pygame.image.load("/Users/dineshkaarthick/Documents/TSA 2026/sprites/Background.png").convert()
#     background = pygame.transform.scale(background, (WIDTH, HEIGHT))
# except:
#     background = pygame.Surface((WIDTH, HEIGHT))
#     background.fill((20, 20, 30))

# # ==============================
# # GAME STATE
# # ==============================
# hour = 1
# listeners = 5
# transmitter = 100
# perfect_moments = []

# mode = "DELAY_BEFORE_NEXT_CALL"
# dialogue_lines = []
# dialogue_index = 0
# current_appreciation = ""
# appreciation_timer = 0
# next_caller_timer = 0
# current_caller = None
# perfect_dialogue_active = False

# # ==============================
# # HELPERS
# # ==============================
# def draw_text(text, x, y, color=CYAN, font=FONT):
#     surface = font.render(text, True, color)
#     screen.blit(surface, (x, y))

# def draw_wrapped_text(text, x, y, max_width, color=CYAN):
#     words = text.split(" ")
#     line = ""
#     current_y = y
#     for word in words:
#         test = line + word + " "
#         if FONT.size(test)[0] > max_width:
#             draw_text(line, x, current_y, color)
#             current_y += 22
#             line = word + " "
#         else:
#             line = test
#     draw_text(line, x, current_y, color)

# def end_game():
#     global mode
#     mode = "GAME_OVER"

# def start_caller():
#     """Pick a new caller and build dialogue sequence."""
#     global current_caller, mode, dialogue_lines, dialogue_index, perfect_dialogue_active
#     global current_appreciation, hour

#     available = [c for c in CALLERS if not c.used and c.minHour <= hour]
    
#     if not available:
#         # No callers available at current hour, advance to next hour
#         if hour < 12:
#             hour += 1
#             available = [c for c in CALLERS if not c.used and c.minHour <= hour]
        
#         if not available or hour > 12:
#             end_game()
#             return

#     current_caller = random.choice(available)
#     current_caller.used = True

#     # Build dialogue sequence
#     dialogue_lines = [f"DJ: Hello, {current_caller.name}. How are you tonight?"]
    
#     # Add hint if available
#     if current_caller.hint_lines:
#         dialogue_lines.append(f"{current_caller.name}: {random.choice(current_caller.hint_lines)}")
    
#     # Add main story
#     dialogue_lines.append(f"{current_caller.name}: {current_caller.text}")
    
#     dialogue_index = 0
#     perfect_dialogue_active = False
#     current_appreciation = ""
#     mode = "CALL"

# def get_next_caller():
#     """Set delay before next caller appears."""
#     global mode, next_caller_timer, dialogue_lines, dialogue_index, current_appreciation, perfect_dialogue_active
#     dialogue_lines = []
#     dialogue_index = 0
#     current_appreciation = ""
#     perfect_dialogue_active = False
#     delay = random.randint(1500, 3500)
#     next_caller_timer = pygame.time.get_ticks() + delay
#     mode = "DELAY_BEFORE_NEXT_CALL"

# def handle_record_selection(record):
#     global transmitter, listeners, hour, current_appreciation, perfect_dialogue_active, dialogue_lines, dialogue_index, mode

#     record.used = True
#     transmitter -= 10

#     # Check if record matches caller's needs
#     match_count = 0
#     if record.genre == current_caller.needs["genre"]:
#         match_count += 1
#     if record.mood == current_caller.needs["mood"]:
#         match_count += 1
#     if record.era == current_caller.needs["era"]:
#         match_count += 1

#     # Perfect match = all 3 attributes match
#     if match_count == 3:
#         listeners += 2
#         transmitter += 5
#         perfect_moments.append((current_caller.name, record.title))
        
#         # Get response from caller
#         if current_caller.responses:
#             current_appreciation = current_caller.responses["perfect"]
#         else:
#             current_appreciation = random.choice([
#                 "Thank you! That was perfect!",
#                 "I needed that song tonight.",
#                 "You really understand me.",
#                 "This means a lot."
#             ])
        
#         # Show thank you dialogue
#         dialogue_lines = [
#             f"DJ: *plays {record.title}*",
#             f"{current_caller.name}: {current_appreciation}"
#         ]
#         dialogue_index = 0
#         perfect_dialogue_active = True
#         mode = "CALL"
        
#     # Good match = 2 attributes match
#     elif match_count == 2:
#         listeners += 1
        
#         if current_caller.responses:
#             current_appreciation = current_caller.responses["good"]
#         else:
#             current_appreciation = "That's nice. Thank you."
        
#         dialogue_lines = [
#             f"DJ: *plays {record.title}*",
#             f"{current_caller.name}: {current_appreciation}"
#         ]
#         dialogue_index = 0
#         perfect_dialogue_active = True
#         mode = "CALL"
        
#     # Poor match = 0-1 attributes match
#     else:
#         listeners = max(0, listeners - 1)
        
#         if current_caller.responses:
#             current_appreciation = current_caller.responses["poor"]
#         else:
#             current_appreciation = "Not what I needed. Goodnight."
        
#         dialogue_lines = [
#             f"DJ: *plays {record.title}*",
#             f"{current_caller.name}: {current_appreciation}"
#         ]
#         dialogue_index = 0
#         perfect_dialogue_active = True
#         mode = "CALL"

# # ==============================
# # MAIN LOOP
# # ==============================
# running = True
# while running:
#     clock.tick(FPS)
#     current_time = pygame.time.get_ticks()
#     screen.blit(background, (0, 0))

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         if event.type == pygame.KEYDOWN:
#             # Advance dialogue
#             if mode == "CALL" and event.key == pygame.K_SPACE:
#                 dialogue_index += 1
#                 if dialogue_index >= len(dialogue_lines):
#                     if perfect_dialogue_active:
#                         # After showing response, advance hour and get next caller
#                         perfect_dialogue_active = False
#                         hour += 1
                        
#                         # Check for game over conditions
#                         if hour > 12 or transmitter <= 0 or listeners <= 0:
#                             end_game()
#                         else:
#                             get_next_caller()
#                     else:
#                         # Story told, now select record
#                         mode = "RECORD_SELECT"

#             # Record selection (1-9, 0 for 10th, Q for 11th, W for 12th)
#             elif mode == "RECORD_SELECT":
#                 idx = -1
#                 if pygame.K_1 <= event.key <= pygame.K_9:
#                     idx = event.key - pygame.K_1
#                 elif event.key == pygame.K_0:
#                     idx = 9
#                 elif event.key == pygame.K_q:
#                     idx = 10
#                 elif event.key == pygame.K_w:
#                     idx = 11
                
#                 if 0 <= idx < len(RECORDS) and not RECORDS[idx].used:
#                     handle_record_selection(RECORDS[idx])

#             elif mode == "GAME_OVER" and event.key == pygame.K_ESCAPE:
#                 running = False

#     # Delay mode before next caller
#     if mode == "DELAY_BEFORE_NEXT_CALL" and current_time >= next_caller_timer:
#         if hour <= 12 and transmitter > 0 and listeners > 0:
#             start_caller()
#         else:
#             end_game()

#     # ==============================
#     # HUD
#     # ==============================
#     pygame.draw.rect(screen, DARK, (20, 20, 260, 90))
#     pygame.draw.rect(screen, CYAN, (20, 20, 260, 90), 2)
#     draw_text(f"HOUR {hour}/12", 30, 30)
#     draw_text(f"LISTENERS: {listeners}", 30, 55)
#     draw_text(f"TRANSMITTER: {transmitter}%", 30, 80)

#     # ==============================
#     # MODES
#     # ==============================
#     if mode == "CALL":
#         box_rect = pygame.Rect(40, HEIGHT - 160, WIDTH - 80, 120)
#         pygame.draw.rect(screen, DARK, box_rect)
#         pygame.draw.rect(screen, CYAN, box_rect, 3)

#         draw_text(f"CALLER: {current_caller.name}", box_rect.x + 15, box_rect.y + 10, MAGENTA, BIG_FONT)

#         if dialogue_index < len(dialogue_lines):
#             draw_wrapped_text(dialogue_lines[dialogue_index], box_rect.x + 15, box_rect.y + 45, box_rect.width - 30)
#         draw_text("Press SPACE to continue...", WIDTH - 250, HEIGHT - 30, YELLOW)

#     elif mode == "RECORD_SELECT":
#         overlay = pygame.Surface((WIDTH, HEIGHT))
#         overlay.set_alpha(230)
#         overlay.fill(BLACK)
#         screen.blit(overlay, (0, 0))

#         draw_text("SELECT A RECORD", 40, 40, MAGENTA, BIG_FONT)
#         draw_text(f"Need: {current_caller.needs['genre']} / {current_caller.needs['mood']} / {current_caller.needs['era']}", 40, 75, YELLOW)

#         y = 120
#         for i, record in enumerate(RECORDS):
#             color = WHITE if not record.used else (120, 120, 120)
#             status = "[USED]" if record.used else ""
#             key = str((i + 1) % 10) if i < 9 else ("0" if i == 9 else ("Q" if i == 10 else "W"))
#             draw_text(f"{key}. {record.title} | {record.mood} | {record.era} | {record.genre} {status}", 60, y, color)
#             y += 30

#     elif mode == "GAME_OVER":
#         overlay = pygame.Surface((WIDTH, HEIGHT))
#         overlay.set_alpha(240)
#         overlay.fill(BLACK)
#         screen.blit(overlay, (0, 0))

#         draw_text("SUNRISE", WIDTH // 2 - 80, 40, CYAN, BIG_FONT)
#         draw_text(f"Final Hour: {hour}/12", 100, 120)
#         draw_text(f"Final Listeners: {listeners}", 100, 150)
#         draw_text(f"Perfect Moments: {len(perfect_moments)}", 100, 180)

#         y = 240
#         draw_text("MEMORY WALL", 100, y, MAGENTA)
#         y += 30
#         for caller_name, song in perfect_moments:
#             draw_text(f"{caller_name} — {song}", 120, y)
#             y += 24

#         draw_text("ESC to Quit", 100, HEIGHT - 40, YELLOW)
    
#     elif mode == "DELAY_BEFORE_NEXT_CALL":
#         # Show waiting message
#         draw_text("Waiting for next caller...", WIDTH // 2 - 120, HEIGHT // 2, YELLOW)

#     pygame.display.flip()

# pygame.quit()
# sys.exit()

import pygame
import sys
import random
from dataclasses import dataclass, field

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
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

# ==============================
# DATA MODELS
# ==============================
@dataclass
class Record:
    title: str
    genre: str
    mood: str
    era: str
    used: bool = False

@dataclass
class Caller:
    name: str
    text: str
    needs: dict
    minHour: int
    used: bool = False
    hint_lines: list = None
    responses: dict = None
    relationship: str = None
    relatedTo: str = None
    special: str = None

# ==============================
# RECORDS
# ==============================
RECORDS = [
    Record("Rebel Heart", "Rock", "Defiant", "1980s"),
    Record("Blue Monday", "Blues", "Melancholy", "1970s"),
    Record("Starlight Serenade", "Jazz", "Tender", "1960s"),
    Record("Summer Drive", "Pop", "Upbeat", "1980s"),
    Record("Yesterday's Song", "Folk", "Nostalgic", "1970s"),
    Record("Neon Dreams", "Ambient", "Contemplative", "1980s"),
    Record("Factory Floor", "Rock", "Upbeat", "1980s"),
    Record("Moonlit Waltz", "Jazz", "Nostalgic", "1960s"),
    Record("Highway 61", "Blues", "Defiant", "1970s"),
    Record("Sarah's Song", "Folk", "Tender", "1980s"),
    Record("Cityscape", "Ambient", "Melancholy", "1980s"),
    Record("Morning Light", "Pop", "Upbeat", "1980s"),
]

# ==============================
# CALLERS WITH HINTS
# ==============================
CALLERS = [
    Caller(
        "Bill", minHour=2,
        text="Just got laid off. Twenty years at the plant. They gave me a Casio watch. I don't know who I am if I'm not building things.",
        needs={"genre": "Rock", "mood": "Defiant", "era": "1980s"},
        relationship="factory_father",
        hint_lines=["I need something strong, something to get me back up!", "Maybe something from the 80s?"],
        responses={
            "perfect": "Yeah... you're right. We built this town. We're not done yet. Thank you.",
            "good": "Appreciate it. Helps to know someone's listening.",
            "poor": "Not what I needed. Goodnight."
        }
    ),
    Caller(
        "Marie", minHour=2,
        text="My daughter turns sixteen tomorrow. I remember holding her the day she was born. Where did the time go?",
        needs={"genre": "Folk", "mood": "Nostalgic", "era": "1970s"},
        hint_lines=["Something gentle, perhaps with memories.", "I miss the old songs..."],
        responses={
            "perfect": "That's it. That's exactly it. Time moves, but love stays. Thank you.",
            "good": "That's nice. Thank you.",
            "poor": "I should go wrap her present."
        }
    ),
    Caller(
        "Tommy", minHour=3,
        text="Driving to the coast. Left at midnight. If I stop, I'll turn around. I can't turn around.",
        needs={"genre": "Pop", "mood": "Upbeat", "era": "1980s"},
        hint_lines=["Keep me moving with something fast.", "A song with energy, you know?"],
        responses={
            "perfect": "This is it. This is the soundtrack for starting over. Thank you!",
            "good": "Okay. Yeah. I can do this.",
            "poor": "That's making me sadder. I gotta go."
        }
    ),
    Caller(
        "Lisa", minHour=4,
        text="Dad came home and just sat there. Wouldn't talk. Wouldn't look at me. I've never seen him cry.",
        needs={"genre": "Blues", "mood": "Tender", "era": "1970s"},
        relationship="factory_daughter",
        relatedTo="factory_father",
        hint_lines=["Something gentle, for when words won't come.", "Maybe something that speaks for us?"],
        responses={
            "perfect": "Wait... is this for him too? Tell him I love him. Please.",
            "good": "Thank you. That's beautiful.",
            "poor": "I need to check on him. Goodnight."
        }
    ),
    Caller(
        "James", minHour=5,
        text="Mom used to sing me this song. Can't remember the words. She's in the hospital. They say I should prepare myself.",
        needs={"genre": "Jazz", "mood": "Nostalgic", "era": "1960s"},
        relationship="hospital_son",
        hint_lines=["Something from the 60s, I think.", "It was jazz... she loved jazz."],
        responses={
            "perfect": "That's the one. How did you know? Thank you. I'm going to sit with her now.",
            "good": "That's close. Really close. Thanks.",
            "poor": "No, that's not it. Sorry."
        }
    ),
    Caller(
        "Angela", minHour=6,
        text="I own the factory. Had to let thirty people go today. Known these families for decades. Some won't look at me now.",
        needs={"genre": "Jazz", "mood": "Melancholy", "era": "1960s"},
        relationship="factory_owner",
        relatedTo="factory_father",
        hint_lines=["Something that understands regret.", "From a simpler time... the 60s."],
        responses={
            "perfect": "I thought someone would yell at me. But you just listened. Thank you.",
            "good": "I appreciate that. Really.",
            "poor": "I understand. Thanks."
        }
    ),
    Caller(
        "Daniel", minHour=7,
        text="At the hospital. Mom's not going to make it. Nurses say I should talk to her, but what do you say?",
        needs={"genre": "Jazz", "mood": "Tender", "era": "1960s"},
        relationship="hospital_son_return",
        relatedTo="hospital_son",
        hint_lines=["Something soft, tender.", "She loved the old standards..."],
        responses={
            "perfect": "That song. She sang that to me. You remembered. Thank you.",
            "good": "That's beautiful. Thank you.",
            "poor": "I need to get back to her."
        }
    ),
    Caller(
        "Rebecca", minHour=3,
        text="My husband and I used to dance in the kitchen. Three years ago today, he died. I can still feel his hand on my back.",
        needs={"genre": "Jazz", "mood": "Nostalgic", "era": "1960s"},
        hint_lines=["Something we danced to...", "From the 60s, when we were young."],
        responses={
            "perfect": "That's our song. Thank you so much.",
            "good": "He would have liked that.",
            "poor": "Not quite right, but thanks."
        }
    ),
    Caller(
        "Carlos", minHour=2,
        text="Night shift just ended. Factory closes next month. Thirty years. Don't know how to be anything else.",
        needs={"genre": "Blues", "mood": "Defiant", "era": "1970s"},
        hint_lines=["Something with fight in it.", "Blues from the 70s, maybe?"],
        responses={
            "perfect": "That's right. We're not done yet. Not by a long shot.",
            "good": "Appreciate it, friend.",
            "poor": "Yeah. Maybe. Goodnight."
        }
    ),
    Caller(
        "Sarah", minHour=9,
        text="I don't know if you remember me. I used to call in, years ago. You played our song. I said I'd wait for the morning show. I did.",
        needs={"genre": "Folk", "mood": "Tender", "era": "1980s"},
        special="sarah",
        hint_lines=["Do you remember? Folk... tender...", "It was our song, from the 80s."],
        responses={
            "perfect": "You remembered. After all these years. Thank you for keeping the morning show alive.",
            "good": "That's close. Thank you for trying.",
            "poor": "It's okay. It was a long time ago."
        }
    ),
    Caller(
        "Michelle", minHour=8,
        text="I'm a nurse. Double shift just ended. Lost someone tonight—young kid. I keep seeing his mother's face.",
        needs={"genre": "Ambient", "mood": "Contemplative", "era": "1980s"},
        hint_lines=["I need quiet. Something contemplative.", "Something modern, ambient..."],
        responses={
            "perfect": "Sometimes we need the quiet. Thank you for understanding.",
            "good": "Thank you. That helps.",
            "poor": "I need something else. Thanks."
        }
    ),
    Caller(
        "Frank", minHour=2,
        text="Son's getting married tomorrow. Giving a speech. How do you tell your kid you're proud without crying?",
        needs={"genre": "Folk", "mood": "Tender", "era": "1970s"},
        hint_lines=["Something gentle, heartfelt.", "Folk, I think. From the 70s."],
        responses={
            "perfect": "Perfect. You always know just what we need.",
            "good": "That's nice. Really nice.",
            "poor": "Not quite right, but thanks."
        }
    ),
    Caller(
        "Jennifer", minHour=5,
        text="Just broke up with my boyfriend. Five years. He said I work too much. Maybe he's right. Don't know who I am without the work.",
        needs={"genre": "Pop", "mood": "Upbeat", "era": "1980s"},
        hint_lines=["Something to lift me up.", "Pop, upbeat, 80s vibes."],
        responses={
            "perfect": "Maybe this IS the start of something good. Thank you.",
            "good": "Okay. That helps.",
            "poor": "Can't do upbeat right now. Sorry."
        }
    ),
    Caller(
        "Robert", minHour=6,
        text="Truck driver. Been on the road three weeks. Haven't seen my family. Sometimes forget what my daughter's voice sounds like.",
        needs={"genre": "Folk", "mood": "Nostalgic", "era": "1970s"},
        hint_lines=["Something that reminds me of home.", "Folk from the old days..."],
        responses={
            "perfect": "That's the one. Makes me remember. Thank you, friend.",
            "good": "Appreciate that. Gets lonely.",
            "poor": "Thanks for trying."
        }
    ),
    Caller(
        "David", minHour=4,
        text="Just retired. Forty years teaching. Walked out today for the last time. Now what? Just... now what?",
        needs={"genre": "Jazz", "mood": "Contemplative", "era": "1960s"},
        hint_lines=["Something thoughtful, reflective.", "Jazz, something to think to."],
        responses={
            "perfect": "Maybe this is the beginning, not the end. Thank you for that.",
            "good": "That's thoughtful. Thanks.",
            "poor": "Not sure that's what I needed."
        }
    ),
    Caller(
        "Marcus", minHour=9,
        text="My band broke up tonight. We were supposed to make it big. Now I'm thirty-five with a guitar and nothing else.",
        needs={"genre": "Rock", "mood": "Defiant", "era": "1980s"},
        hint_lines=["Something that fights back.", "Rock. 80s rock."],
        responses={
            "perfect": "You're right. It's not over. Not if I don't let it be. Thank you.",
            "good": "Thanks, man. Needed that.",
            "poor": "Maybe it IS over."
        }
    ),
    Caller(
        "Paul", minHour=10,
        text="Daughter just called. She's having a baby. I'm going to be a grandfather. Never thought I'd make it this far.",
        needs={"genre": "Pop", "mood": "Upbeat", "era": "1980s"},
        hint_lines=["I'm celebrating! Something joyful!", "Pop, upbeat, 80s!"],
        responses={
            "perfect": "That's PERFECT! That's exactly how I feel! Thank you!",
            "good": "That's great. Really great.",
            "poor": "Not quite the celebration I hoped for."
        }
    ),
    Caller(
        "Helen", minHour=8,
        text="Wedding anniversary. He's been gone five years. I still set a place for him at dinner. Is that crazy?",
        needs={"genre": "Jazz", "mood": "Tender", "era": "1960s"},
        hint_lines=["Something tender, loving.", "Jazz from when we were young..."],
        responses={
            "perfect": "That's beautiful. Love doesn't end. Thank you for reminding me.",
            "good": "That's sweet. Thank you.",
            "poor": "Not quite right, but thanks."
        }
    ),
]

# ==============================
# INIT PYGAME
# ==============================
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Last Broadcast")
clock = pygame.time.Clock()

FONT = pygame.font.SysFont("consolas", 18)
BIG_FONT = pygame.font.SysFont("consolas", 28)
SMALL_FONT = pygame.font.SysFont("consolas", 14)

# Try to load background, if it fails use a solid color
try:
    background = pygame.image.load("sprites/Background.png").convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
except:
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill((20, 20, 30))

# ==============================
# GAME STATE
# ==============================
hour = 1
listeners = 5
transmitter = 100
perfect_moments = []
total_calls = 0
streak = 0
best_streak = 0

mode = "DELAY_BEFORE_NEXT_CALL"
dialogue_lines = []
dialogue_index = 0
current_appreciation = ""
appreciation_timer = 0
next_caller_timer = 0
current_caller = None
perfect_dialogue_active = False

# Notification system
notifications = []  # List of (message, color, timestamp)

# ==============================
# HELPERS
# ==============================
def draw_text(text, x, y, color=CYAN, font=FONT):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

def draw_wrapped_text(text, x, y, max_width, color=CYAN):
    words = text.split(" ")
    line = ""
    current_y = y
    for word in words:
        test = line + word + " "
        if FONT.size(test)[0] > max_width:
            draw_text(line, x, current_y, color)
            current_y += 22
            line = word + " "
        else:
            line = test
    draw_text(line, x, current_y, color)

def add_notification(message, color=YELLOW):
    """Add a temporary notification to display"""
    notifications.append((message, color, pygame.time.get_ticks()))

def draw_notifications():
    """Draw active notifications"""
    current_time = pygame.time.get_ticks()
    y_offset = 130
    active_notifications = []
    
    for message, color, timestamp in notifications:
        age = current_time - timestamp
        if age < 3000:  # Show for 3 seconds
            alpha = 255 if age < 2500 else int(255 * (1 - (age - 2500) / 500))
            draw_text(message, 300, y_offset, color)
            y_offset += 25
            active_notifications.append((message, color, timestamp))
    
    notifications[:] = active_notifications

def end_game():
    global mode
    mode = "GAME_OVER"

def start_caller():
    """Pick a new caller and build dialogue sequence."""
    global current_caller, mode, dialogue_lines, dialogue_index, perfect_dialogue_active
    global current_appreciation, hour, total_calls

    available = [c for c in CALLERS if not c.used and c.minHour <= hour]
    
    if not available:
        # No callers available at current hour
        if hour >= 12:
            end_game()
            return
        else:
            # Skip to next hour
            hour += 1
            available = [c for c in CALLERS if not c.used and c.minHour <= hour]
        
        if not available or hour > 12:
            end_game()
            return

    current_caller = random.choice(available)
    current_caller.used = True
    total_calls += 1

    # Build dialogue sequence
    dialogue_lines = [f"DJ: Hello, {current_caller.name}. How are you tonight?"]
    
    # Add hint if available
    if current_caller.hint_lines:
        dialogue_lines.append(f"{current_caller.name}: {random.choice(current_caller.hint_lines)}")
    
    # Add main story
    dialogue_lines.append(f"{current_caller.name}: {current_caller.text}")
    
    dialogue_index = 0
    perfect_dialogue_active = False
    current_appreciation = ""
    mode = "CALL"

def get_next_caller():
    """Set delay before next caller appears."""
    global mode, next_caller_timer, dialogue_lines, dialogue_index, current_appreciation, perfect_dialogue_active
    dialogue_lines = []
    dialogue_index = 0
    current_appreciation = ""
    perfect_dialogue_active = False
    delay = random.randint(1500, 3500)
    next_caller_timer = pygame.time.get_ticks() + delay
    mode = "DELAY_BEFORE_NEXT_CALL"

def handle_record_selection(record):
    global transmitter, listeners, hour, current_appreciation, perfect_dialogue_active
    global dialogue_lines, dialogue_index, mode, streak, best_streak

    record.used = True
    transmitter -= 10

    # Check if record matches caller's needs
    match_count = 0
    if record.genre == current_caller.needs["genre"]:
        match_count += 1
    if record.mood == current_caller.needs["mood"]:
        match_count += 1
    if record.era == current_caller.needs["era"]:
        match_count += 1

    # Perfect match = all 3 attributes match
    if match_count == 3:
        listeners += 2
        transmitter += 5
        perfect_moments.append((current_caller.name, record.title))
        streak += 1
        best_streak = max(best_streak, streak)
        
        # Get response from caller
        if current_caller.responses:
            current_appreciation = current_caller.responses["perfect"]
        else:
            current_appreciation = random.choice([
                "Thank you! That was perfect!",
                "I needed that song tonight.",
                "You really understand me.",
                "This means a lot."
            ])
        
        add_notification("Perfect Match! +2 Listeners", GREEN)
        
        # Show thank you dialogue
        dialogue_lines = [
            f"DJ: *plays {record.title}*",
            f"{current_caller.name}: {current_appreciation}"
        ]
        dialogue_index = 0
        perfect_dialogue_active = True
        mode = "CALL"
        
    # Good match = 2 attributes match
    elif match_count == 2:
        listeners += 1
        streak = 0
        
        if current_caller.responses:
            current_appreciation = current_caller.responses["good"]
        else:
            current_appreciation = "That's nice. Thank you."
        
        add_notification("Good Match. +1 Listener", YELLOW)
        
        dialogue_lines = [
            f"DJ: *plays {record.title}*",
            f"{current_caller.name}: {current_appreciation}"
        ]
        dialogue_index = 0
        perfect_dialogue_active = True
        mode = "CALL"
        
    # Poor match = 0-1 attributes match
    else:
        listeners = max(0, listeners - 1)
        streak = 0
        
        if current_caller.responses:
            current_appreciation = current_caller.responses["poor"]
        else:
            current_appreciation = "Not what I needed. Goodnight."
        
        add_notification("Poor Match. -1 Listener", RED)
        
        dialogue_lines = [
            f"DJ: *plays {record.title}*",
            f"{current_caller.name}: {current_appreciation}"
        ]
        dialogue_index = 0
        perfect_dialogue_active = True
        mode = "CALL"

def draw_signal_bars():
    """Draw animated signal bars for transmitter"""
    bar_count = 5
    bar_width = 5
    bar_spacing = 2
    max_height = 25
    x_start = 220
    y_base = 85
    
    active_bars = int((transmitter / 100) * bar_count)
    
    for i in range(bar_count):
        bar_height = max_height * (i + 1) / bar_count
        if i < active_bars:
            if transmitter > 70:
                color = GREEN
            elif transmitter > 30:
                color = YELLOW
            else:
                color = RED
        else:
            color = (40, 40, 40)
        
        pygame.draw.rect(screen, color, 
                        (x_start + i * (bar_width + bar_spacing), 
                         y_base - bar_height, 
                         bar_width, 
                         bar_height))

# ==============================
# MAIN LOOP
# ==============================
running = True
while running:
    clock.tick(FPS)
    current_time = pygame.time.get_ticks()
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # Advance dialogue
            if mode == "CALL" and event.key == pygame.K_SPACE:
                dialogue_index += 1
                if dialogue_index >= len(dialogue_lines):
                    if perfect_dialogue_active:
                        # After showing response, advance hour and get next caller
                        perfect_dialogue_active = False
                        hour += 1
                        
                        # Check for game over conditions
                        if hour > 12 or transmitter <= 0 or listeners <= 0:
                            end_game()
                        else:
                            get_next_caller()
                    else:
                        # Story told, now select record
                        mode = "RECORD_SELECT"

            # Record selection (1-9, 0 for 10th, Q for 11th, W for 12th)
            elif mode == "RECORD_SELECT":
                idx = -1
                if pygame.K_1 <= event.key <= pygame.K_9:
                    idx = event.key - pygame.K_1
                elif event.key == pygame.K_0:
                    idx = 9
                elif event.key == pygame.K_q:
                    idx = 10
                elif event.key == pygame.K_w:
                    idx = 11
                
                if 0 <= idx < len(RECORDS) and not RECORDS[idx].used:
                    handle_record_selection(RECORDS[idx])

            elif mode == "GAME_OVER" and event.key == pygame.K_ESCAPE:
                running = False
            elif mode == "GAME_OVER" and event.key == pygame.K_r:
                # Restart game
                pygame.quit()
                sys.exit()

    # Delay mode before next caller
    if mode == "DELAY_BEFORE_NEXT_CALL" and current_time >= next_caller_timer:
        if hour <= 12 and transmitter > 0 and listeners > 0:
            start_caller()
        else:
            end_game()

    # ==============================
    # HUD
    # ==============================
    hud_box = pygame.Rect(10, 10, 270, 110)
    pygame.draw.rect(screen, DARK, hud_box)
    pygame.draw.rect(screen, CYAN, hud_box, 2)
    
    draw_text(f"HOUR {hour}/12", 20, 20)
    draw_text(f"LISTENERS: {listeners}", 20, 45)
    draw_text(f"TRANSMITTER: {transmitter}%", 20, 70)
    
    # Draw signal bars
    draw_signal_bars()
    
    # Streak indicator
    if streak > 0:
        draw_text(f"STREAK: {streak}", 155, 20, GREEN)
    
    # Draw notifications
    draw_notifications()

    # ==============================
    # MODES
    # ==============================
    if mode == "CALL":
        box_rect = pygame.Rect(40, HEIGHT - 160, WIDTH - 80, 120)
        pygame.draw.rect(screen, DARK, box_rect)
        pygame.draw.rect(screen, CYAN, box_rect, 3)

        draw_text(f"CALLER: {current_caller.name}", box_rect.x + 15, box_rect.y + 10, MAGENTA, BIG_FONT)

        if dialogue_index < len(dialogue_lines):
            draw_wrapped_text(dialogue_lines[dialogue_index], box_rect.x + 15, box_rect.y + 45, box_rect.width - 30)
        draw_text("Press SPACE to continue...", WIDTH - 250, HEIGHT - 30, YELLOW)

    elif mode == "RECORD_SELECT":
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(230)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))

        draw_text("SELECT A RECORD", 40, 40, MAGENTA, BIG_FONT)
        draw_text(f"Need: {current_caller.needs['genre']} / {current_caller.needs['mood']} / {current_caller.needs['era']}", 40, 75, YELLOW)

        y = 120
        for i, record in enumerate(RECORDS):
            color = WHITE if not record.used else (80, 80, 80)
            status = "[USED]" if record.used else ""
            key = str((i + 1) % 10) if i < 9 else ("0" if i == 9 else ("Q" if i == 10 else "W"))
            
            # Highlight matching attributes
            match_indicators = []
            if record.genre == current_caller.needs["genre"]:
                match_indicators.append("G")
            if record.mood == current_caller.needs["mood"]:
                match_indicators.append("M")
            if record.era == current_caller.needs["era"]:
                match_indicators.append("E")
            
            match_text = f"[{''.join(match_indicators)}]" if match_indicators else ""
            
            draw_text(f"{key}. {record.title} | {record.mood} | {record.era} | {record.genre} {match_text} {status}", 60, y, color)
            y += 30

    elif mode == "GAME_OVER":
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(240)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))

        # Calculate score
        score = (len(perfect_moments) * 100) + (listeners * 10)
        
        draw_text("SUNRISE", WIDTH // 2 - 80, 40, CYAN, BIG_FONT)
        draw_text(f"You made it to Hour {hour}/12", 100, 100, YELLOW)
        draw_text(f"Final Score: {score}", 100, 130, MAGENTA, BIG_FONT)
        
        draw_text(f"Total Calls: {total_calls}", 100, 180)
        draw_text(f"Final Listeners: {listeners}", 100, 210)
        draw_text(f"Perfect Moments: {len(perfect_moments)}", 100, 240)
        draw_text(f"Best Streak: {best_streak}", 100, 270)

        y = 320
        draw_text("MEMORY WALL", 100, y, MAGENTA)
        y += 30
        for caller_name, song in perfect_moments[:8]:  # Show first 8
            draw_text(f"{caller_name} — {song}", 120, y, CYAN, SMALL_FONT)
            y += 20
        
        if len(perfect_moments) > 8:
            draw_text(f"... and {len(perfect_moments) - 8} more", 120, y, CYAN, SMALL_FONT)

        draw_text("ESC to Quit | R to Restart", 100, HEIGHT - 40, YELLOW)
    
    elif mode == "DELAY_BEFORE_NEXT_CALL":
        # Show waiting message in caller box area
        box_rect = pygame.Rect(40, HEIGHT - 160, WIDTH - 80, 120)
        pygame.draw.rect(screen, DARK, box_rect)
        pygame.draw.rect(screen, CYAN, box_rect, 3)
        
        # Animated dots
        dots = "." * ((current_time // 500) % 4)
        draw_text(f"Waiting for next caller{dots}", box_rect.x + 15, box_rect.y + 45, YELLOW)

    pygame.display.flip()

pygame.quit()
sys.exit()


# use version given above, make sure to have sprites folder
