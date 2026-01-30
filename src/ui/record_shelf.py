"""
Record shelf view.

Renders the record selection interface showing all available records.
Player selects a record by pressing number keys.
"""

import pygame
from src.game_state import GameState
from src.config import (
    WIDTH, HEIGHT,
    BLACK, WHITE, MAGENTA, GRAY
)


def render_record_select_mode(screen: pygame.Surface, state: GameState,
                               small_font: pygame.font.Font, big_font: pygame.font.Font) -> None:
    """
    Render the record selection screen.
    
    Args:
        screen: Pygame surface to render to
        state: Current game state
        small_font: Regular font for record details
        big_font: Larger font for title
    """
    # Dark overlay
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(230)
    overlay.fill(BLACK)
    screen.blit(overlay, (0, 0))
    
    # Title
    title_text = big_font.render("SELECT A RECORD (1–9)", True, MAGENTA)
    screen.blit(title_text, (40, 40))
    
    # List all records
    y = 100
    for i, record in enumerate(state.records):
        # Gray out used records
        color = WHITE if not record.used else GRAY
        
        # Show [USED] marker
        status = "[USED]" if record.used else ""
        
        # Format: "1. Title | mood | era | genre [USED]"
        record_text = (
            f"{i+1}. {record.title} | {record.mood} | "
            f"{record.era} | {record.genre} {status}"
        )
        
        text_surface = small_font.render(record_text, True, color)
        screen.blit(text_surface, (60, y))
        y += 30
