"""
Configuration and constants for The Last Broadcast.

This module contains all game constants including:
- Display settings (resolution, FPS)
- Color palette
- Timing constants
- Game balance tuning values

No game logic should live here - only values that might need tweaking.
"""

# ==============================
# DISPLAY SETTINGS
# ==============================
WIDTH = 960
HEIGHT = 540
FPS = 60

# ==============================
# COLOR PALETTE
# ==============================
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (240, 240, 240)
DARK = (10, 10, 10)
GRAY = (120, 120, 120)

# ==============================
# GAME BALANCE
# ==============================
MAX_HOURS = 12
STARTING_LISTENERS = 5
STARTING_TRANSMITTER = 100

TRANSMITTER_DRAIN_PER_HOUR = 10
LISTENERS_GAIN_ON_MATCH = 2
LISTENERS_LOSS_ON_MISMATCH = 1
TRANSMITTER_GAIN_ON_MATCH = 5

# ==============================
# UI LAYOUT
# ==============================
HUD_X = 20
HUD_Y = 20
HUD_WIDTH = 260
HUD_HEIGHT = 90
HUD_PADDING = 10

DIALOGUE_BOX_MARGIN = 40
DIALOGUE_BOX_HEIGHT = 160
DIALOGUE_BOX_PADDING = 15
