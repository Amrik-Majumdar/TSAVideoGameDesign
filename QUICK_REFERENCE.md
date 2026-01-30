# Quick Reference - Enhanced GameState

## GameState Fields

```python
# Time
state.hour                 # Current hour (1-12)
state.time_progress       # Sub-hour progress (0.0-1.0)

# Resources
state.transmitter         # Transmitter health (0-100%)
state.listeners          # Listener count (int)
state.listener_map       # List[ListenerLocation]

# Records
state.records            # List[Record]
state.records_used       # Count of used records
state.get_unused_records()  # Get available records

# Callers
state.current_caller     # Active Caller object
state.callers           # Remaining callers queue
state.has_callers_remaining()  # Check if more callers

# Score & Memory
state.score             # Points earned
state.perfect_moments   # List[(caller, song)]

# Flags
state.emergency_used    # Emergency power boost used
state.game_over        # Game over flag

# Mode
state.mode             # "CALL", "RECORD_SELECT", "GAME_OVER"

# Debug
state.debug_mode       # Debug toggle
state.snapshot_count   # Number of snapshots taken
```

## Key Methods

```python
# Listener Management
state.add_listener(name=None)      # Add listener to map
state.remove_listener()            # Remove listener from map

# Game State
state.is_game_over()              # Check game over conditions

# Debug
state.get_snapshot()              # Get state dict
state.print_snapshot(label="")    # Print formatted snapshot
```

## Debug Mode

### Enable
- Command line: `python main.py --debug`
- In-game: Press `F3`

### Snapshot Triggers
- Game start
- Mode transitions
- Before/after record selection
- Game exit

## System Architecture

### All Systems Follow Pattern:
```python
def system_function(state: GameState, ...) -> None:
    """
    System description.
    
    Args:
        state: GameState (modified in place)
        ...
        
    NO GLOBALS - All mutations through state parameter.
    """
    # Read state
    value = state.some_field
    
    # Modify state
    state.some_field = new_value
    
    # Optional: Debug snapshot
    state.print_snapshot("Event description")
```

## Testing

```bash
# Run game normally
python main.py

# Run with debug
python main.py --debug

# Run tests
python test_gamestate.py
```

## Common Operations

### Check for Perfect Match
```python
if record.mood == state.current_caller.desired_mood:
    state.score += 100
    state.perfect_moments.append((caller.name, record.title))
```

### Update Listeners
```python
# Add listeners
for _ in range(count):
    state.add_listener()

# Remove listeners
for _ in range(count):
    state.remove_listener()
```

### Check Game Over
```python
if state.is_game_over():
    state.mode = "GAME_OVER"
    state.game_over = True
```

## Fixed-Step Loop Constants

```python
FIXED_TIMESTEP = 1.0 / 60.0  # 60 Hz
MAX_FRAME_TIME = 0.25        # 250ms cap
```

## No-Global Guarantee

✅ All state in GameState object  
✅ No module-level mutables  
✅ Systems receive state explicitly  
✅ Independent instances possible  

## File Structure

```
/src
├── game_state.py        # GameState class + models
├── main.py              # Fixed-step loop + debug
├── config.py            # Constants only
├── /systems             # State modifiers
│   ├── records.py       # Record selection logic
│   ├── time.py          # Time management
│   ├── callers.py       # Caller utilities
│   ├── listeners.py     # Listener utilities
│   ├── transmitter.py   # Transmitter checks
│   └── audio.py         # Audio (stubbed)
└── /ui                  # State renderers
    ├── hud.py           # HUD with score
    ├── phone.py         # Caller dialogue
    ├── record_shelf.py  # Record selection
    ├── game_over.py     # End screen
    ├── booth.py         # Background
    └── city_map.py      # Map (stubbed)
```
