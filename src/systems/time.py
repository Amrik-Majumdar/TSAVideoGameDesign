"""
Time system.

Manages the night-to-sunrise progression with configurable total length.
Tracks phases (early night, deep night, pre-sunrise) and emits events/flags
on phase transitions. No rendering logic.

NO GLOBALS - All state is passed explicitly via GameState parameter.
"""

from typing import Dict, List
from src.game_state import GameState
from src.config import NIGHT_LENGTH_SECONDS, NIGHT_PHASE_THRESHOLDS


class TimeSystem:
    """
    Time progression system for the night cycle.
    
    Responsibilities:
    - Advance night elapsed time
    - Compute phase based on normalized progress
    - Emit phase transition events/flags
    
    Unit-testable helpers:
    - get_phase(progress)
    - is_sunrise(progress)
    """
    
    def __init__(self, total_night_length_seconds: float = NIGHT_LENGTH_SECONDS):
        self.total_night_length_seconds = max(1.0, float(total_night_length_seconds))
    
    def update(self, state: GameState, delta_time: float) -> None:
        """
        Advance the night timer and update phase state.
        
        Args:
            state: Current game state (modified in place)
            delta_time: Time elapsed since last update in seconds
        """
        if delta_time <= 0:
            return
        
        # Advance elapsed time
        state.night_elapsed = min(
            state.night_elapsed + delta_time,
            state.night_length_seconds
        )
        
        # Normalized progress (0.0 to 1.0)
        progress = min(1.0, state.night_elapsed / state.night_length_seconds)
        state.time_progress = progress
        
        # Determine phase and emit transitions
        new_phase = self.get_phase(progress)
        if new_phase != state.night_phase:
            state.night_phase = new_phase
            self._emit_phase_event(state, new_phase)
        
        # If sunrise reached, set game_over flag (optional milestone)
        if self.is_sunrise(progress):
            state.game_over = True
    
    def get_phase(self, progress: float) -> str:
        """
        Get current night phase based on normalized progress.
        
        Args:
            progress: Normalized progress from 0.0 to 1.0
        
        Returns:
            Phase name: "early_night", "deep_night", or "pre_sunrise"
        """
        clamped = max(0.0, min(1.0, progress))
        if clamped >= NIGHT_PHASE_THRESHOLDS["pre_sunrise"]:
            return "pre_sunrise"
        if clamped >= NIGHT_PHASE_THRESHOLDS["deep_night"]:
            return "deep_night"
        return "early_night"
    
    def is_sunrise(self, progress: float) -> bool:
        """
        Determine if sunrise has been reached.
        
        Args:
            progress: Normalized progress from 0.0 to 1.0
        
        Returns:
            True if sunrise has been reached
        """
        return progress >= 1.0
    
    def _emit_phase_event(self, state: GameState, phase: str) -> None:
        """
        Emit phase transition flags/events in GameState.
        
        Args:
            state: Current game state (modified in place)
            phase: New phase name
        """
        # Reset all phase flags then set current
        for key in state.phase_flags.keys():
            state.phase_flags[key] = False
        state.phase_flags[phase] = True
        
        # Record phase event for debugging or systems to react
        state.phase_events.append(phase)


def get_phase(progress: float) -> str:
    """
    Unit-testable helper to get phase from progress.
    
    Args:
        progress: Normalized progress (0.0 to 1.0)
    
    Returns:
        Phase name
    """
    return TimeSystem().get_phase(progress)


def is_sunrise(progress: float) -> bool:
    """
    Unit-testable helper to check if sunrise reached.
    
    Args:
        progress: Normalized progress (0.0 to 1.0)
    
    Returns:
        True if sunrise reached
    """
    return TimeSystem().is_sunrise(progress)
