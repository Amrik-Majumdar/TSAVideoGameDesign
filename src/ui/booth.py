"""
Booth view (stubbed).

Placeholder for the radio booth visual environment.
Could render the DJ booth, equipment, window view of the city, etc.
"""

import pygame
from src.game_state import GameState


def render_booth_background(screen: pygame.Surface, background_image: pygame.Surface) -> None:
    """
    Render the booth environment background.
    
    Args:
        screen: Pygame surface to render to
        background_image: Pre-loaded background image
        
    Currently just draws the background image.
    Future: Could add animated elements, time-of-day effects, etc.
    """
    screen.blit(background_image, (0, 0))
