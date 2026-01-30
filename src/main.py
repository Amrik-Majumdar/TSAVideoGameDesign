"""
The Last Broadcast - Main entry point.

This module orchestrates the game loop and delegates to systems and UI.
It contains NO game logic - only initialization and coordination.

Game flow:
1. Initialize pygame, load assets
2. Create GameState (with optional debug mode)
3. Fixed-step main loop:
   - Accumulate delta time
   - Update systems at fixed timestep
   - Handle input events
   - Render UI based on current mode
4. Cleanup and exit

FIXED-STEP LOOP: Accumulates delta time and updates at consistent intervals
DEBUG MODE: Enable with --debug flag to see GameState snapshots
"""

import pygame
import sys

# Import configuration
from src.config import WIDTH, HEIGHT, FPS

# Import game state
from src.game_state import GameState

# Import systems
from src.systems import audio
from src.systems.time import TimeSystem
from src.systems.records import handle_record_selection

# Import UI modules
from src.ui.booth import render_booth_background
from src.ui.hud import render_hud
from src.ui.phone import render_call_mode
from src.ui.record_shelf import render_record_select_mode
from src.ui.game_over import render_game_over_mode


# Fixed timestep configuration
FIXED_TIMESTEP = 1.0 / 60.0  # 60 updates per second
MAX_FRAME_TIME = 0.25  # Cap delta time to prevent spiral of death


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
        state: Current game state (modified in place)
        
    Returns:
        bool: True to continue running, False to quit
        
    NO GLOBALS - All state mutations happen through the state parameter.
    """
    if event.type == pygame.QUIT:
        return False
    
    if event.type == pygame.KEYDOWN:
        # Debug mode toggle (F3)
        if event.key == pygame.K_F3:
            state.debug_mode = not state.debug_mode
            print(f"Debug mode: {'ON' if state.debug_mode else 'OFF'}")
            if state.debug_mode:
                state.print_snapshot("DEBUG MODE ENABLED")
            return True
        
        # Handle input based on current mode
        if state.mode == "CALL":
            if event.key == pygame.K_RETURN:
                # Move to record selection
                state.mode = "RECORD_SELECT"
                state.print_snapshot("Entering record selection")
        
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
    Main game loop with fixed timestep.
    
    Initializes the game, runs the fixed-step main loop, and handles cleanup.
    
    Features:
    - Fixed timestep updates (60 Hz)
    - Delta time accumulation
    - Frame time capping to prevent spiral of death
    - Debug mode support (toggle with F3 or --debug flag)
    
    NO GLOBALS - All state is contained in GameState object.
    """
    # Check for debug mode flag
    debug_mode = "--debug" in sys.argv
    
    # Initialize
    screen, clock, fonts, background = initialize_pygame()
    audio.initialize_audio()
    
    # Create game state with debug mode
    state = GameState(debug_mode=debug_mode)
    time_system = TimeSystem(total_night_length_seconds=state.night_length_seconds)
    
    if debug_mode:
        print("\n" + "="*60)
        print("DEBUG MODE ENABLED")
        print("Press F3 to toggle debug mode during gameplay")
        print("="*60 + "\n")
        state.print_snapshot("GAME START")
    
    # Fixed timestep accumulator
    accumulator = 0.0
    
    # Main loop
    running = True
    while running:
        # Calculate frame delta time
        frame_time = clock.tick(FPS) / 1000.0
        
        # Cap frame time to prevent spiral of death
        if frame_time > MAX_FRAME_TIME:
            frame_time = MAX_FRAME_TIME
        
        # Accumulate time for fixed updates
        accumulator += frame_time
        
        # Fixed timestep updates
        while accumulator >= FIXED_TIMESTEP:
            # Update systems at fixed rate
            time_system.update(state, FIXED_TIMESTEP)
            accumulator -= FIXED_TIMESTEP
        
        # Handle events (variable rate, but that's fine for input)
        for event in pygame.event.get():
            if not handle_input(event, state):
                running = False
                if state.debug_mode:
                    state.print_snapshot("GAME EXIT")
        
        # Render (variable rate, interpolation could go here)
        render(screen, state, fonts, background)
        pygame.display.flip()
    
    # Cleanup
    audio.stop_audio()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
