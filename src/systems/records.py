"""
Record selection system.

Handles the logic of selecting records and evaluating matches with caller moods.
Modifies game state based on the player's choice.
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
        state: The current game state
        record: The record being played for the caller
        
    Side effects:
        - Marks record as used
        - Advances hour
        - Drains transmitter
        - Updates listeners based on mood match
        - Records perfect moments
        - Triggers game over if conditions met
        - Advances to next caller or ends game
    """
    # Mark record as used
    record.used = True
    
    # Time passes
    state.hour += 1
    
    # Transmitter drains every hour
    state.transmitter -= TRANSMITTER_DRAIN_PER_HOUR
    
    # Check if mood matches caller's desired mood
    if record.mood == state.current_caller.desired_mood:
        # Perfect match!
        state.listeners += LISTENERS_GAIN_ON_MATCH
        state.transmitter += TRANSMITTER_GAIN_ON_MATCH
        state.perfect_moments.append((state.current_caller.name, record.title))
    else:
        # Mismatch - lose listeners
        state.listeners = max(0, state.listeners - LISTENERS_LOSS_ON_MISMATCH)
    
    # Check game over conditions
    if state.is_game_over():
        state.mode = "GAME_OVER"
    else:
        advance_to_next_caller(state)


def advance_to_next_caller(state: GameState) -> None:
    """
    Move to the next caller or end the game if none remain.
    
    Args:
        state: The current game state
        
    Side effects:
        - Pops next caller from queue
        - Sets mode to CALL or GAME_OVER
    """
    if state.has_callers_remaining():
        state.current_caller = state.callers.pop()
        state.mode = "CALL"
    else:
        state.mode = "GAME_OVER"
