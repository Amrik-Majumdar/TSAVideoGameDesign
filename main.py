"""
The Last Broadcast - Bootstrap loader.

This file serves as the entry point and simply delegates to the
modular src package. All game logic has been moved to src/.

To run the game: python main.py
"""

from src.main import main

if __name__ == "__main__":
    main()
