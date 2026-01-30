"""
Global game state container.

This module defines the GameState class which holds all mutable game state:
- Current hour and game mode
- Listener count and transmitter health
- Active callers and records
- Perfect moments memory

GameState is passed to systems and UI modules but they should not
import each other - only interact through this shared state object.
"""

import random
from dataclasses import dataclass, field
from typing import List
from src.config import (
    STARTING_LISTENERS,
    STARTING_TRANSMITTER,
    MAX_HOURS
)


@dataclass
class Record:
    """Represents a vinyl record that can be played for a caller."""
    title: str
    mood: str
    era: str
    genre: str
    used: bool = False


@dataclass
class Caller:
    """Represents a caller with a story and desired mood."""
    name: str
    text: str
    desired_mood: str


class GameState:
    """
    Central state container for the entire game.
    
    Holds all mutable game state and provides access to systems.
    Systems should query and modify this state, not maintain their own.
    """
    
    def __init__(self):
        # Time progression
        self.hour: int = 1
        
        # Resources
        self.listeners: int = STARTING_LISTENERS
        self.transmitter: int = STARTING_TRANSMITTER
        
        # Game mode: "CALL", "RECORD_SELECT", "GAME_OVER"
        self.mode: str = "CALL"
        
        # Records pool
        self.records: List[Record] = [
            Record("Neon Dreams", "upbeat", "80s", "synth"),
            Record("Late Night Static", "sad", "80s", "rock"),
            Record("Midnight Drive", "nostalgic", "70s", "soft rock"),
            Record("Heart on Hold", "sad", "80s", "pop"),
            Record("Last Dance FM", "upbeat", "80s", "disco"),
            Record("Rain on Vinyl", "calm", "70s", "jazz"),
        ]
        
        # Caller queue
        caller_pool = [
            Caller("Mark", "I just got laid off. Drove around for an hour before calling.", "nostalgic"),
            Caller("Angela", "My mom used to listen to this station every night.", "calm"),
            Caller("Tom", "Everyone else is asleep. Feels like I'm the only one left.", "sad"),
            Caller("Lisa", "I don't want this night to end.", "upbeat"),
        ]
        random.shuffle(caller_pool)
        self.callers: List[Caller] = caller_pool
        self.current_caller: Caller = self.callers.pop()
        
        # Memory/achievements
        self.perfect_moments: List[tuple] = []
    
    def is_game_over(self) -> bool:
        """Check if game over conditions are met."""
        return self.hour > MAX_HOURS or self.transmitter <= 0
    
    def has_callers_remaining(self) -> bool:
        """Check if there are more callers in the queue."""
        return len(self.callers) > 0
