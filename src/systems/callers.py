"""
Caller management system.

Handles caller queue management and dialogue state.
Currently minimal - could be expanded for dynamic caller generation.
"""

from src.game_state import GameState


def get_current_caller_info(state: GameState) -> dict:
    """
    Get information about the current caller.
    
    Args:
        state: The current game state
        
    Returns:
        Dictionary with caller name, text, and desired mood
    """
    return {
        "name": state.current_caller.name,
        "text": state.current_caller.text,
        "desired_mood": state.current_caller.desired_mood
    }


def has_more_callers(state: GameState) -> bool:
    """
    Check if more callers are waiting.
    
    Args:
        state: The current game state
        
    Returns:
        True if callers remain in queue
    """
    return state.has_callers_remaining()
