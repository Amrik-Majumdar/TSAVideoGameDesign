"""
Game over / end screen.

Displays final statistics and the memory wall of perfect moments.
"""

import pygame
from src.game_state import GameState
from src.config import (
    WIDTH, HEIGHT,
    BLACK, CYAN, MAGENTA, YELLOW
)


def render_game_over_mode(screen: pygame.Surface, state: GameState,
                          small_font: pygame.font.Font, big_font: pygame.font.Font) -> None:
    """
    Render the game over screen with final stats.
    
    Args:
        screen: Pygame surface to render to
        state: Current game state
        small_font: Regular font for body text
        big_font: Larger font for title
    """
    # Dark overlay
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(240)
    overlay.fill(BLACK)
    screen.blit(overlay, (0, 0))
    
    # Title
    title_text = big_font.render("SUNRISE", True, CYAN)
    screen.blit(title_text, (WIDTH // 2 - 80, 40))
    
    # Final stats
    score_text = small_font.render(f"Final Score: {state.score}", True, MAGENTA)
    screen.blit(score_text, (100, 100))
    
    listeners_text = small_font.render(f"Final Listeners: {state.listeners}", True, CYAN)
    screen.blit(listeners_text, (100, 130))
    
    perfect_count_text = small_font.render(
        f"Perfect Moments: {len(state.perfect_moments)}", 
        True, 
        CYAN
    )
    screen.blit(perfect_count_text, (100, 160))
    
    records_text = small_font.render(f"Records Played: {state.records_used}", True, CYAN)
    screen.blit(records_text, (100, 190))
    
    # Memory wall
    y = 240
    memory_title = small_font.render("MEMORY WALL", True, MAGENTA)
    screen.blit(memory_title, (100, y))
    y += 30
    
    # List all perfect moments
    for caller_name, song_title in state.perfect_moments:
        memory_text = small_font.render(f"{caller_name} — {song_title}", True, CYAN)
        screen.blit(memory_text, (120, y))
        y += 24
    
    # Exit prompt
    exit_text = small_font.render("ESC to Quit", True, YELLOW)
    screen.blit(exit_text, (100, HEIGHT - 40))
