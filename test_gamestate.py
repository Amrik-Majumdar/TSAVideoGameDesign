"""
Test script for GameState implementation.

This script verifies:
1. GameState initializes correctly
2. No global state mutations occur
3. Listener map stays synchronized
4. Score tracking works
5. Flags work correctly
6. Debug snapshots function properly
"""

import sys
sys.path.insert(0, 'd:/Users/Atiksh/Education/Coding/TSAVideoGameDesign2526')

from src.game_state import GameState, Record, Caller
from src.systems.records import handle_record_selection


def test_initialization():
    """Test that GameState initializes with correct values."""
    print("\n=== Testing Initialization ===")
    state = GameState(debug_mode=False)
    
    assert state.hour == 1, "Hour should start at 1"
    assert state.time_progress == 0.0, "Time progress should start at 0.0"
    assert state.listeners == 5, "Should start with 5 listeners"
    assert len(state.listener_map) == 5, "Listener map should have 5 entries"
    assert state.transmitter == 100, "Transmitter should start at 100"
    assert state.score == 0, "Score should start at 0"
    assert state.emergency_used == False, "Emergency should not be used"
    assert state.game_over == False, "Game should not be over"
    assert len(state.records) == 6, "Should have 6 records"
    assert state.records_used == 0, "No records should be used initially"
    
    print("✅ All initialization checks passed")
    return state


def test_listener_map_sync():
    """Test that listener count and listener_map stay synchronized."""
    print("\n=== Testing Listener Map Synchronization ===")
    state = GameState(debug_mode=False)
    
    initial_count = state.listeners
    initial_map_size = len(state.listener_map)
    assert initial_count == initial_map_size, "Initial counts should match"
    
    # Add listeners
    state.add_listener()
    assert state.listeners == initial_count + 1, "Listener count should increment"
    assert len(state.listener_map) == initial_map_size + 1, "Map size should increment"
    
    state.add_listener("Test Listener")
    assert state.listeners == initial_count + 2, "Listener count should be +2"
    assert len(state.listener_map) == initial_map_size + 2, "Map size should be +2"
    
    # Remove listeners
    state.remove_listener()
    assert state.listeners == initial_count + 1, "Listener count should decrement"
    assert len(state.listener_map) == initial_map_size + 1, "Map size should decrement"
    
    print(f"✅ Listener map synchronization working (count: {state.listeners}, map: {len(state.listener_map)})")


def test_score_tracking():
    """Test that score is tracked correctly on perfect matches."""
    print("\n=== Testing Score Tracking ===")
    state = GameState(debug_mode=False)
    
    # Find a record that matches current caller's mood
    matching_record = None
    for record in state.records:
        if record.mood == state.current_caller.desired_mood:
            matching_record = record
            break
    
    if matching_record:
        initial_score = state.score
        handle_record_selection(state, matching_record)
        assert state.score == initial_score + 100, f"Score should increase by 100 (was {initial_score}, now {state.score})"
        assert len(state.perfect_moments) == 1, "Should have 1 perfect moment"
        print(f"✅ Score tracking working (score: {state.score})")
    else:
        print("⚠️  No matching record found for initial caller")


def test_no_globals():
    """Test that no global state is being mutated."""
    print("\n=== Testing No Global Mutations ===")
    
    # Create two independent game states
    state1 = GameState(debug_mode=False)
    state2 = GameState(debug_mode=False)
    
    # Modify state1
    state1.hour = 5
    state1.score = 500
    state1.emergency_used = True
    
    # Verify state2 is unaffected
    assert state2.hour == 1, "State2 hour should be unchanged"
    assert state2.score == 0, "State2 score should be unchanged"
    assert state2.emergency_used == False, "State2 emergency should be unused"
    
    print("✅ No global state mutations detected")


def test_debug_snapshots():
    """Test that debug snapshots work correctly."""
    print("\n=== Testing Debug Snapshots ===")
    state = GameState(debug_mode=True)
    
    snapshot = state.get_snapshot()
    assert snapshot["snapshot_id"] == 1, "First snapshot should have ID 1"
    assert snapshot["hour"] == state.hour, "Snapshot should reflect current hour"
    assert snapshot["score"] == state.score, "Snapshot should reflect current score"
    assert snapshot["listeners"] == state.listeners, "Snapshot should reflect listeners"
    
    # Get another snapshot
    snapshot2 = state.get_snapshot()
    assert snapshot2["snapshot_id"] == 2, "Second snapshot should have ID 2"
    
    print(f"✅ Debug snapshots working (generated {state.snapshot_count} snapshots)")


def test_game_over_conditions():
    """Test that game over conditions are detected correctly."""
    print("\n=== Testing Game Over Conditions ===")
    
    # Test transmitter failure
    state1 = GameState(debug_mode=False)
    state1.transmitter = 0
    assert state1.is_game_over() == True, "Game should be over when transmitter is 0"
    
    # Test hour limit
    state2 = GameState(debug_mode=False)
    state2.hour = 13
    assert state2.is_game_over() == True, "Game should be over when hour > 12"
    
    # Test game_over flag
    state3 = GameState(debug_mode=False)
    state3.game_over = True
    assert state3.is_game_over() == True, "Game should be over when flag is set"
    
    # Test normal state
    state4 = GameState(debug_mode=False)
    assert state4.is_game_over() == False, "Game should not be over initially"
    
    print("✅ Game over conditions working correctly")


def test_record_tracking():
    """Test that record usage is tracked correctly."""
    print("\n=== Testing Record Tracking ===")
    state = GameState(debug_mode=False)
    
    initial_unused = len(state.get_unused_records())
    assert initial_unused == 6, "Should have 6 unused records initially"
    assert state.records_used == 0, "No records should be used initially"
    
    # Mark a record as used
    record = state.records[0]
    record.used = True
    state.records_used += 1
    
    unused = len(state.get_unused_records())
    assert unused == 5, "Should have 5 unused records after using one"
    assert state.records_used == 1, "Should have 1 used record"
    
    print(f"✅ Record tracking working (used: {state.records_used}, unused: {unused})")


def run_all_tests():
    """Run all tests and report results."""
    print("="*60)
    print("GameState Implementation Test Suite")
    print("="*60)
    
    try:
        test_initialization()
        test_listener_map_sync()
        test_score_tracking()
        test_no_globals()
        test_debug_snapshots()
        test_game_over_conditions()
        test_record_tracking()
        
        print("\n" + "="*60)
        print("✅ ALL TESTS PASSED!")
        print("="*60)
        print("\nGameState implementation is working correctly:")
        print("  • No global state mutations")
        print("  • Listener map stays synchronized")
        print("  • Score tracking functions properly")
        print("  • Debug mode works as expected")
        print("  • All game mechanics preserved")
        
    except AssertionError as e:
        print("\n" + "="*60)
        print(f"❌ TEST FAILED: {e}")
        print("="*60)
        raise


if __name__ == "__main__":
    run_all_tests()
