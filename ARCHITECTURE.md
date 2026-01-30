# The Last Broadcast - Enhanced GameState Architecture

## Overview
This refactored version features a centralized GameState object that tracks all mutable game data with NO implicit global mutations.

## GameState Features

### Core State Tracking
- **time_progress**: Sub-hour time accumulation (0.0 to 1.0)
- **transmitter_health**: Power level (0-100%)
- **listener_map**: Detailed listener locations with ListenerLocation objects
- **records_used**: Count of records played
- **current_caller**: Active caller object
- **score**: Points earned from perfect matches
- **flags**: 
  - `emergency_used`: Emergency power boost status
  - `game_over`: Terminal game state flag

### Fixed-Step Game Loop
The game uses a fixed timestep update loop:
- Updates run at consistent 60 Hz
- Delta time accumulation prevents timing issues
- Frame time capping prevents "spiral of death"

### Debug Mode

#### Enabling Debug Mode
1. **Command line**: `python main.py --debug`
2. **In-game toggle**: Press `F3` during gameplay

#### Debug Features
- **GameState Snapshots**: JSON-formatted state dumps at key moments
- **Snapshot Triggers**:
  - Game start
  - Mode changes (entering record selection)
  - Before/after record selection
  - Game exit
- **Snapshot Contents**:
  - Hour and time progress
  - Current mode
  - Transmitter health
  - Listener count and map size
  - Records used/remaining
  - Caller information
  - Score and perfect moments
  - Game flags

#### Sample Debug Output
```
============================================================
[BEFORE record selection] GameState Snapshot #5
============================================================
{
  "snapshot_id": 5,
  "hour": 3,
  "time_progress": 0.0,
  "mode": "RECORD_SELECT",
  "transmitter_health": 85,
  "listeners": 7,
  "listener_locations": 7,
  "records_used": 2,
  "records_remaining": 4,
  "current_caller": "Tom",
  "callers_remaining": 1,
  "score": 200,
  "perfect_moments": 2,
  "emergency_used": false,
  "game_over": false
}
============================================================
```

## Architecture Guarantees

### No Implicit Globals
- All systems receive `GameState` as a parameter
- All state mutations happen explicitly through `GameState` object
- No module-level mutable state in systems

### Explicit State Flow
```
main.py
  └─> Creates GameState
  └─> Passes to systems/*.py (receives, modifies explicitly)
  └─> Passes to ui/*.py (receives, reads only)
```

## Running the Game

### Normal Mode
```bash
python main.py
```

### Debug Mode
```bash
python main.py --debug
```

### Controls
- **ENTER**: Select a record (from caller screen)
- **1-9**: Choose record (in record selection mode)
- **F3**: Toggle debug mode
- **ESC**: Quit (from game over screen)

## System Architecture

### /src/systems/
All systems receive and modify `GameState` explicitly:
- `records.py`: Record selection logic with score calculation
- `time.py`: Time progression management
- `callers.py`: Caller queue management
- `listeners.py`: Listener tracking utilities
- `transmitter.py`: Transmitter health checks
- `audio.py`: Audio system (stubbed)

### /src/ui/
All UI modules receive `GameState` for read-only rendering:
- `hud.py`: Heads-up display with score
- `phone.py`: Caller dialogue view
- `record_shelf.py`: Record selection screen
- `game_over.py`: End screen with final stats
- `booth.py`: Background rendering
- `city_map.py`: City visualization (stubbed)

## Testing

The game has been tested to ensure:
✅ No global state mutations
✅ All systems receive GameState explicitly
✅ Fixed-step loop runs smoothly
✅ Debug mode snapshots work correctly
✅ Score tracking functions properly
✅ Listener map updates with additions/removals
✅ All original gameplay features preserved
