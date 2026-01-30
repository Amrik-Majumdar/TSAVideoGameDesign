"""
Record selection system.

Handles the logic of selecting records and evaluating matches with caller moods.
Modifies game state based on the player's choice.

NO GLOBALS - All state is passed explicitly via GameState parameter.
"""

from src.game_state import GameState, Record
from src.config import (
    TRANSMITTER_DRAIN_PER_HOUR,
    LISTENERS_GAIN_ON_MATCH,
    LISTENERS_LOSS_ON_MISMATCH,
    TRANSMITTER_GAIN_ON_MATCH
)


def handle_record_selection(state: GameState, record: Record) -> None:
    """
    Process a record selection and update game state.
    
    Args:
        state: The current game state (modified in place)
        record: The record being played for the caller
        
    Side effects:
        - Marks record as used
        - Increments records_used counter
        - Advances hour
        - Drains transmitter
        - Updates listeners based on mood match
        - Updates score on perfect match
        - Records perfect moments
        - Triggers game over if conditions met
        - Advances to next caller or ends game
        
    NO GLOBALS - All state mutations happen through the state parameter.
    """
    # Debug snapshot before processing
    state.print_snapshot("BEFORE record selection")
    
    # Mark record as used
    record.used = True
    state.records_used += 1
    
    # Time passes
    state.hour += 1
    state.time_progress = 0.0  # Reset time progress for new hour
    
    # Transmitter drains every hour
    state.transmitter -= TRANSMITTER_DRAIN_PER_HOUR
    
    # Check if mood matches caller's desired mood
    if record.mood == state.current_caller.desired_mood:
        # Perfect match!
        state.listeners += LISTENERS_GAIN_ON_MATCH
        # Add listeners to the map
        for _ in range(LISTENERS_GAIN_ON_MATCH):
            state.add_listener()
        
        state.transmitter += TRANSMITTER_GAIN_ON_MATCH
        state.score += 100  # Award points for perfect match
        state.perfect_moments.append((state.current_caller.name, record.title))
    else:
        # Mismatch - lose listeners
        old_count = state.listeners
        state.listeners = max(0, state.listeners - LISTENERS_LOSS_ON_MISMATCH)
        # Remove listeners from map
        for _ in range(old_count - state.listeners):
            state.remove_listener()
    
    # Debug snapshot after processing
    state.print_snapshot("AFTER record selection")
    
    # Check game over conditions
    if state.is_game_over():
        state.mode = "GAME_OVER"
        state.game_over = True
    else:
        advance_to_next_caller(state)


def advance_to_next_caller(state: GameState) -> None:
    """
    Move to the next caller or end the game if none remain.
    
    Args:
        state: The current game state (modified in place)
        
    Side effects:
        - Pops next caller from queue
        - Sets mode to CALL or GAME_OVER
        - Sets game_over flag if no callers remain
        
    NO GLOBALS - All state mutations happen through the state parameter.
    """
    if state.has_callers_remaining():
        state.current_caller = state.callers.pop()
        state.mode = "CALL"
    else:
        state.mode = "GAME_OVER"
        state.game_over = True
