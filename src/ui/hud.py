"""
HUD (Heads-Up Display) rendering.

Renders the persistent UI elements that appear in all modes:
- Hour counter
- Listener count
- Transmitter health
"""

import pygame
from src.game_state import GameState
from src.config import (
    HUD_X, HUD_Y, HUD_WIDTH, HUD_HEIGHT,
    DARK, CYAN, HUD_PADDING
)


def render_hud(screen: pygame.Surface, state: GameState, font: pygame.font.Font) -> None:
    """
    Render the main HUD showing hour, listeners, transmitter, and score.
    
    Args:
        screen: Pygame surface to render to
        state: Current game state
        font: Font to use for text
    """
    # Draw HUD background box
    pygame.draw.rect(screen, DARK, (HUD_X, HUD_Y, HUD_WIDTH, HUD_HEIGHT))
    pygame.draw.rect(screen, CYAN, (HUD_X, HUD_Y, HUD_WIDTH, HUD_HEIGHT), 2)
    
    # Draw HUD text
    text_x = HUD_X + HUD_PADDING
    text_y = HUD_Y + HUD_PADDING
    
    hour_text = font.render(f"HOUR {state.hour}/12", True, CYAN)
    screen.blit(hour_text, (text_x, text_y))
    
    listeners_text = font.render(f"LISTENERS: {state.listeners}", True, CYAN)
    screen.blit(listeners_text, (text_x, text_y + 25))
    
    transmitter_text = font.render(f"TRANSMITTER: {state.transmitter}%", True, CYAN)
    screen.blit(transmitter_text, (text_x, text_y + 50))
    
    # Add score display in corner
    score_text = font.render(f"SCORE: {state.score}", True, CYAN)
    screen.blit(score_text, (text_x + 140, text_y))
