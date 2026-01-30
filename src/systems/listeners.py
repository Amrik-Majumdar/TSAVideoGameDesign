"""
Listener tracking system.

Manages the listener count mechanic.
More listeners = more reach, but can be lost by poor music choices.
"""

from src.game_state import GameState


def get_listener_count(state: GameState) -> int:
    """
    Get the current listener count.
    
    Args:
        state: The current game state
        
    Returns:
        Number of current listeners
    """
    return state.listeners


def get_listener_status(state: GameState) -> str:
    """
    Get a descriptive status of the listener count.
    
    Args:
        state: The current game state
        
    Returns:
        Status string describing audience size
    """
    listeners = state.listeners
    if listeners == 0:
        return "EMPTY"
    elif listeners <= 2:
        return "LONELY"
    elif listeners <= 5:
        return "INTIMATE"
    elif listeners <= 10:
        return "GROWING"
    else:
        return "PACKED"
