# The Last Broadcast

A retro-by-design, UI/UX-first narrative game about empathy, memory, and scarcity.

## Overview

**The Last Broadcast** is a non-violent retro-inspired game set in 1987. You play as a late-night AM radio DJ hosting the final broadcast of a dying station before corporate buyout. Your goal is not to win through combat or speed, but to keep listeners connected until sunrise by making emotionally intelligent decisions under pressure.

This project intentionally combines:
- Retro aesthetics (fixed perspective, low resolution, limited palette)
- Modern usability and UI/UX discipline
- Narrative-driven gameplay focused on empathy and consequence

Retro is the aesthetic. **Usability is mandatory.**

---

## Core Gameplay Concept

- You receive calls from listeners describing their situations indirectly.
- You choose from a limited set of vinyl records to respond emotionally.
- Each record can only be played once.
- Your choices affect:
  - Listener retention
  - Audio quality
  - Visual tone
  - Interconnected narrative outcomes
- A failing transmitter acts as a global timer and tension system.

When the transmitter reaches zero, the broadcast ends.

---

## Design Pillars

### 1. No Violence
There is no combat, no enemies, and no fail-states based on reflex. The challenge is emotional judgment and resource management.

### 2. Retro by Design, Not Accident
- 320x240 internal resolution
- Strict 16-color CGA-inspired palette
- Pixel-perfect layout and alignment
- One bitmap font with high contrast

Retro limitations are intentional and disciplined.

### 3. Modern UX Standards
- Clear affordances
- Immediate feedback for every action
- Forgiving interaction zones
- Zero reliance on “retro excuses” for bad usability

---

## UI / UX Master Rules

- Clarity always beats nostalgia.
- Every interaction must produce visible and audible feedback.
- If a player is confused, the design has failed.
- Everything clickable must look clickable.
- No invisible mechanics.
- No clutter.

Bad retro = accidental limitations.  
Good retro = intentional constraints.

---

## Visual Structure

### Broadcast Booth (Primary View)
- Fixed isometric or top-down perspective
- Single-room environment:
  - Soundboard
  - Record shelf
  - Phone
  - Transmitter gauge
  - Window overlooking the city
- The transmitter gauge visually drains over time and acts as the main timer.

### Listener Map (Secondary View)
- Toggleable city grid (100x100)
- Each listener is represented by a glowing pixel
- Emotional success increases brightness and pulse
- Poor choices cause pixels to fade permanently

---

## Core Gameplay Loop

1. **The Call**
   - Text-only dialogue
   - No explicit song requests

2. **The Choice**
   - Select one vinyl record
   - Each record has:
     - Genre
     - Mood
     - Era
     - Hidden memory tag

3. **The Outcome**
   - Perfect match (3 tags): +2 listeners
   - Good match (2 tags): no change
   - Poor match (≤1 tag): −1 listener

Each record can only be used once.

---

## Transmitter System

- Drains steadily across 12 in-game hours
- When it hits zero, the game ends

Player tradeoffs:
- Boost the transmitter with high-energy music
- Read station IDs for small stabilization
- Ignore the system to prioritize emotional authenticity

This represents the core theme: **art vs survival**.

---

## Audio Design

- All audio is diegetic (exists in the game world)
- Generated in real time using Tone.js
- No pre-rendered MP3 files
- Emotional performance affects sound quality:
  - Good matches sound warmer and clearer
  - Poor matches sound filtered and constrained
- Transmitter hum rises in pitch as failure approaches

---

## Narrative Structure

- 30 total callers
  - 15 standalone
  - 15 interconnected across hidden story webs
- No quest markers
- No relationship indicators
- Players deduce connections organically through dialogue

---

## Endings

At sunrise or transmitter failure, the game presents:
- Total listeners retained
- Total listener-seconds
- A Memory Wall of perfect emotional moments

There is no “best” ending.  
Depth of connection matters more than quantity.

---

## Technical Constraints

- Canvas API only (no Phaser or game engines)
- Client-side only
- Tone.js for audio
- Single global game state
- GitHub Pages / Vercel compatible

---

## Execution Priority

1. Fix scrolling and overall site usability
2. Establish clean game architecture
3. Implement core gameplay loop
4. Add visual and audio feedback systems
5. Layer in narrative depth and polish

If any implementation detail conflicts with this README, **the README wins**.

---

## Final Principle

Retro is not an excuse.  
Retro is a discipline.

If it is retro, it must be **excellent**.
