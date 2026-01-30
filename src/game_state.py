"""
Global game state container.

This module defines the GameState class which holds all mutable game state:
- Time progression (hour and accumulated time)
- Listener count and transmitter health
- Active callers and records
- Score and perfect moments memory
- Game flags (emergency_used, game_over)

GameState is passed to systems and UI modules but they should not
import each other - only interact through this shared state object.

NO GLOBALS - All systems receive GameState explicitly and modify it.
"""

import random
import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from src.config import (
    STARTING_LISTENERS,
    STARTING_TRANSMITTER,
    MAX_HOURS,
    NIGHT_LENGTH_SECONDS
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


@dataclass
class ListenerLocation:
    """Represents a listener at a location in the city."""
    name: str
    x: float
    y: float
    connected_at_hour: int


class GameState:
    """
    Central state container for the entire game.
    
    Holds all mutable game state and provides access to systems.
    Systems should query and modify this state, not maintain their own.
    
    ALL state mutations happen through this object - no implicit globals.
    """
    
    def __init__(self, debug_mode: bool = False):
        # ===== TIME PROGRESSION =====
        self.hour: int = 1
        self.time_progress: float = 0.0  # Accumulated night progress (0.0 to 1.0)
        self.night_elapsed: float = 0.0  # Elapsed seconds since night start
        self.night_length_seconds: float = NIGHT_LENGTH_SECONDS
        self.night_phase: str = "early_night"
        self.phase_flags: Dict[str, bool] = {
            "early_night": True,
            "deep_night": False,
            "pre_sunrise": False,
        }
        self.phase_events: List[str] = []
        
        # ===== TRANSMITTER HEALTH =====
        self.transmitter: int = STARTING_TRANSMITTER  # Also called transmitter_health
        
        # ===== LISTENER MAP =====
        # Total listener count (backward compatible)
        self.listeners: int = STARTING_LISTENERS
        # Detailed listener locations for potential map visualization
        self.listener_map: List[ListenerLocation] = self._initialize_listener_map()
        
        # ===== RECORDS USED =====
        # Records pool with usage tracking
        self.records: List[Record] = [
            Record("Neon Dreams", "upbeat", "80s", "synth"),
            Record("Late Night Static", "sad", "80s", "rock"),
            Record("Midnight Drive", "nostalgic", "70s", "soft rock"),
            Record("Heart on Hold", "sad", "80s", "pop"),
            Record("Last Dance FM", "upbeat", "80s", "disco"),
            Record("Rain on Vinyl", "calm", "70s", "jazz"),
        ]
        self.records_used: int = 0  # Count of records played
        
        # ===== CURRENT CALLER =====
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
        
        # ===== SCORE =====
        self.score: int = 0  # Points earned from perfect matches
        
        # ===== FLAGS =====
        self.emergency_used: bool = False  # Has emergency power boost been used
        self.game_over: bool = False  # Is game in terminal state
        
        # ===== GAME MODE =====
        # Game mode: "CALL", "RECORD_SELECT", "GAME_OVER"
        self.mode: str = "CALL"
        
        # ===== MEMORY/ACHIEVEMENTS =====
        self.perfect_moments: List[tuple] = []
        
        # ===== DEBUG MODE =====
        self.debug_mode: bool = debug_mode
        self.snapshot_count: int = 0
    
    def _initialize_listener_map(self) -> List[ListenerLocation]:
        """Initialize starting listener locations."""
        locations = []
        listener_names = ["Alex", "Jamie", "Sam", "Casey", "Morgan"]
        for i in range(STARTING_LISTENERS):
            name = listener_names[i] if i < len(listener_names) else f"Listener_{i+1}"
            locations.append(ListenerLocation(
                name=name,
                x=random.uniform(0.1, 0.9),
                y=random.uniform(0.1, 0.9),
                connected_at_hour=1
            ))
        return locations
    
    def add_listener(self, name: Optional[str] = None) -> None:
        """
        Add a new listener to the map.
        
        Args:
            name: Optional name for the listener
        """
        self.listeners += 1
        if name is None:
            name = f"Listener_{self.listeners}"
        self.listener_map.append(ListenerLocation(
            name=name,
            x=random.uniform(0.1, 0.9),
            y=random.uniform(0.1, 0.9),
            connected_at_hour=self.hour
        ))
    
    def remove_listener(self) -> None:
        """Remove a listener from the map."""
        if self.listeners > 0:
            self.listeners -= 1
            if self.listener_map:
                self.listener_map.pop()
    
    def is_game_over(self) -> bool:
        """Check if game over conditions are met."""
        return self.hour > MAX_HOURS or self.transmitter <= 0 or self.game_over
    
    def has_callers_remaining(self) -> bool:
        """Check if there are more callers in the queue."""
        return len(self.callers) > 0
    
    def get_unused_records(self) -> List[Record]:
        """Get list of records that haven't been played yet."""
        return [r for r in self.records if not r.used]
    
    def get_snapshot(self) -> Dict:
        """
        Get a snapshot of current game state for debugging.
        
        Returns:
            Dictionary containing key state variables
        """
        self.snapshot_count += 1
        return {
            "snapshot_id": self.snapshot_count,
            "hour": self.hour,
            "time_progress": round(self.time_progress, 3),
            "mode": self.mode,
            "transmitter_health": self.transmitter,
            "listeners": self.listeners,
            "listener_locations": len(self.listener_map),
            "records_used": self.records_used,
            "records_remaining": len(self.get_unused_records()),
            "current_caller": self.current_caller.name if self.current_caller else None,
            "callers_remaining": len(self.callers),
            "score": self.score,
            "perfect_moments": len(self.perfect_moments),
            "emergency_used": self.emergency_used,
            "game_over": self.game_over,
        }
    
    def print_snapshot(self, label: str = "") -> None:
        """
        Print a formatted snapshot of the game state.
        
        Args:
            label: Optional label to identify this snapshot
        """
        if not self.debug_mode:
            return
        
        snapshot = self.get_snapshot()
        prefix = f"[{label}] " if label else ""
        print(f"\n{'='*60}")
        print(f"{prefix}GameState Snapshot #{snapshot['snapshot_id']}")
        print(f"{'='*60}")
        print(json.dumps(snapshot, indent=2))
        print(f"{'='*60}\n")
