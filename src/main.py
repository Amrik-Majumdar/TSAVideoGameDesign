"""
The Last Broadcast - Main entry point.

This module orchestrates the game loop and delegates to systems and UI.
It contains NO game logic - only initialization and coordination.

Game flow:
1. Initialize pygame, load assets
2. Create GameState
3. Main loop:
   - Handle input events
   - Update systems
   - Render UI based on current mode
4. Cleanup and exit
"""

import pygame
import sys

# Import configuration
from src.config import WIDTH, HEIGHT, FPS

# Import game state
from src.game_state import GameState

# Import systems
from src.systems import audio, time
from src.systems.records import handle_record_selection

# Import UI modules
from src.ui.booth import render_booth_background
from src.ui.hud import render_hud
from src.ui.phone import render_call_mode
from src.ui.record_shelf import render_record_select_mode
from src.ui.game_over import render_game_over_mode


def initialize_pygame():
    """
    Initialize pygame and create the game window.
    
    Returns:
        tuple: (screen, clock, fonts, background)
    """
    pygame.init()
    
    # Create window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("The Last Broadcast")
    
    # Create clock for framerate control
    clock = pygame.time.Clock()
    
    # Load fonts
    small_font = pygame.font.SysFont("consolas", 18)
    big_font = pygame.font.SysFont("consolas", 28)
    fonts = {"small": small_font, "big": big_font}
    
    # Load background image
    background = pygame.image.load("sprites/Background.png").convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    
    return screen, clock, fonts, background


def handle_input(event: pygame.event.Event, state: GameState) -> bool:
    """
    Handle a single input event.
    
    Args:
        event: Pygame event to process
        state: Current game state
        
    Returns:
        bool: True to continue running, False to quit
    """
    if event.type == pygame.QUIT:
        return False
    
    if event.type == pygame.KEYDOWN:
        # Handle input based on current mode
        if state.mode == "CALL":
            if event.key == pygame.K_RETURN:
                # Move to record selection
                state.mode = "RECORD_SELECT"
        
        elif state.mode == "RECORD_SELECT":
            # Check for number key press (1-9)
            if pygame.K_1 <= event.key <= pygame.K_9:
                idx = event.key - pygame.K_1
                if idx < len(state.records) and not state.records[idx].used:
                    # Valid selection - process it
                    handle_record_selection(state, state.records[idx])
        
        elif state.mode == "GAME_OVER":
            if event.key == pygame.K_ESCAPE:
                # Quit game
                return False
    
    return True


def render(screen: pygame.Surface, state: GameState, fonts: dict, background: pygame.Surface) -> None:
    """
    Render the current game state.
    
    Args:
        screen: Pygame surface to render to
        state: Current game state
        fonts: Dictionary of loaded fonts
        background: Background image
    """
    # Draw background (booth environment)
    render_booth_background(screen, background)
    
    # Draw HUD (always visible except game over)
    if state.mode != "GAME_OVER":
        render_hud(screen, state, fonts["small"])
    
    # Draw mode-specific UI
    if state.mode == "CALL":
        render_call_mode(screen, state, fonts["small"], fonts["big"])
    
    elif state.mode == "RECORD_SELECT":
        render_record_select_mode(screen, state, fonts["small"], fonts["big"])
    
    elif state.mode == "GAME_OVER":
        render_game_over_mode(screen, state, fonts["small"], fonts["big"])


def main():
    """
    Main game loop.
    
    Initializes the game, runs the main loop, and handles cleanup.
    """
    # Initialize
    screen, clock, fonts, background = initialize_pygame()
    audio.initialize_audio()
    
    # Create game state
    state = GameState()
    
    # Main loop
    running = True
    while running:
        # Calculate delta time
        delta_time = clock.tick(FPS) / 1000.0
        
        # Handle events
        for event in pygame.event.get():
            if not handle_input(event, state):
                running = False
        
        # Update systems
        time.update_time(state, delta_time)
        
        # Render
        render(screen, state, fonts, background)
        pygame.display.flip()
    
    # Cleanup
    audio.stop_audio()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
