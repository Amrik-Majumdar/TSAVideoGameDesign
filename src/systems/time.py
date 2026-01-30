"""
Time management system.

Handles time progression and checks for time-based game over conditions.
Implements smooth time progression using delta time accumulation.

NO GLOBALS - All state is passed explicitly via GameState parameter.
"""

from src.game_state import GameState


def update_time(state: GameState, delta_time: float) -> None:
    """
    Update time-based game state with smooth progression.
    
    Args:
        state: The current game state (modified in place)
        delta_time: Time elapsed since last frame in seconds
        
    Side effects:
        - Accumulates time_progress (0.0 to 1.0 within each hour)
        - Could trigger time-based events in the future
        
    NO GLOBALS - All state mutations happen through the state parameter.
    
    Future features might include:
    - Real-time countdown timers
    - Time pressure mechanics
    - Day/night cycle visual effects
    - Automatic hour advancement if time_progress reaches certain threshold
    """
    # Currently time only advances when records are selected
    # This accumulates sub-hour time for potential future mechanics
    
    # Accumulate time progress (could be used for animations, etc.)
    # Note: We don't auto-advance hours here - that's driven by record selection
    # But we track smooth time for potential visual effects
    pass  # Time advancement is event-driven, not real-time


def get_time_of_night(state: GameState) -> str:
    """
    Get a descriptive string for the current time of night.
    
    Args:
        state: The current game state
        
    Returns:
        String describing time period like "Late Night", "Midnight", etc.
    """
    hour = state.hour
    if hour <= 2:
        return "Late Night"
    elif hour <= 4:
        return "Midnight"
    elif hour <= 6:
        return "Early Morning"
    elif hour <= 8:
        return "Pre-Dawn"
    elif hour <= 10:
        return "Dawn"
    else:
        return "Sunrise"
