"""
Transmitter health system.

Manages the transmitter health mechanic and related checks.
The transmitter degrades over time and can be repaired by matching moods.
"""

from src.game_state import GameState


def check_transmitter_failure(state: GameState) -> bool:
    """
    Check if transmitter has failed (reached 0%).
    
    Args:
        state: The current game state
        
    Returns:
        True if transmitter has failed
    """
    return state.transmitter <= 0


def get_transmitter_status(state: GameState) -> str:
    """
    Get a descriptive status of the transmitter.
    
    Args:
        state: The current game state
        
    Returns:
        Status string like "CRITICAL", "LOW", "GOOD", "EXCELLENT"
    """
    if state.transmitter <= 0:
        return "FAILED"
    elif state.transmitter <= 25:
        return "CRITICAL"
    elif state.transmitter <= 50:
        return "LOW"
    elif state.transmitter <= 75:
        return "GOOD"
    else:
        return "EXCELLENT"
