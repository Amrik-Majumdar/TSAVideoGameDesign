"""
Caller dialogue view (phone UI).

Renders the caller's dialogue box when in CALL mode.
Shows caller name and their story/request.
"""

import pygame
from src.game_state import GameState
from src.config import (
    WIDTH, HEIGHT,
    DIALOGUE_BOX_MARGIN, DIALOGUE_BOX_HEIGHT, DIALOGUE_BOX_PADDING,
    DARK, CYAN, MAGENTA, YELLOW
)


def draw_wrapped_text(screen: pygame.Surface, text: str, x: int, y: int, 
                      max_width: int, color: tuple, font: pygame.font.Font) -> None:
    """
    Draw text with word wrapping.
    
    Args:
        screen: Surface to draw on
        text: Text to wrap and draw
        x, y: Starting position
        max_width: Maximum width before wrapping
        color: Text color
        font: Font to use
    """
    words = text.split(" ")
    line = ""
    for word in words:
        test = line + word + " "
        if font.size(test)[0] > max_width:
            surface = font.render(line, True, color)
            screen.blit(surface, (x, y))
            y += 22
            line = word + " "
        else:
            line = test
    # Draw remaining text
    surface = font.render(line, True, color)
    screen.blit(surface, (x, y))


def render_call_mode(screen: pygame.Surface, state: GameState, 
                     small_font: pygame.font.Font, big_font: pygame.font.Font) -> None:
    """
    Render the caller dialogue interface.
    
    Args:
        screen: Pygame surface to render to
        state: Current game state
        small_font: Regular font for body text
        big_font: Larger font for caller name
    """
    # Dialogue box at bottom of screen
    box_rect = pygame.Rect(
        DIALOGUE_BOX_MARGIN,
        HEIGHT - DIALOGUE_BOX_HEIGHT,
        WIDTH - (DIALOGUE_BOX_MARGIN * 2),
        DIALOGUE_BOX_HEIGHT - DIALOGUE_BOX_MARGIN
    )
    
    # Draw box background and border
    pygame.draw.rect(screen, DARK, box_rect)
    pygame.draw.rect(screen, CYAN, box_rect, 3)
    
    # Draw caller name
    caller_name_text = big_font.render(
        f"CALLER: {state.current_caller.name}", 
        True, 
        MAGENTA
    )
    screen.blit(caller_name_text, (box_rect.x + DIALOGUE_BOX_PADDING, box_rect.y + 10))
    
    # Draw caller's story with word wrapping
    draw_wrapped_text(
        screen,
        state.current_caller.text,
        box_rect.x + DIALOGUE_BOX_PADDING,
        box_rect.y + 45,
        box_rect.width - (DIALOGUE_BOX_PADDING * 2),
        CYAN,
        small_font
    )
    
    # Draw prompt to continue
    prompt_text = small_font.render("Press ENTER to select a record", True, YELLOW)
    screen.blit(prompt_text, (WIDTH - 330, HEIGHT - 30))
