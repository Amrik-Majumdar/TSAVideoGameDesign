# THE LAST BROADCAST - DJ BOOTH PIXEL ART REFERENCE
## Canvas: 640x480 pixels | Palette: Cyan (#0ff), Magenta (#f0f), Black (#000), Dark Cyan (#088)

---

## SCENE LAYOUT (Isometric View - 3/4 Perspective)

```
┌─────────────────────────────────────────────────────────┐
│                    TRANSMITTER TOWER                    │ ← Top 80px
│                   (background element)                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│     BACK WALL                                           │ ← 120-280px
│     (Cork board, posters, window)                       │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│     DESK SURFACE (Isometric)                            │ ← 280-380px
│     (Mixer, turntable, phone, clutter)                  │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                 FOREGROUND                              │ ← 380-480px
│           (Chair legs, carpet texture)                  │
└─────────────────────────────────────────────────────────┘
```

---

## ESSENTIAL OBJECTS TO DRAW (40 Total)

### DESK LEVEL (Main Interaction Zone)

#### **1. MIXING BOARD** [150x80px] - CENTER FOCAL POINT
- Position: (240, 300)
- Clickable: YES
- Story: *"Channel 3 has been stuck at 7dB since 1982. You stopped trying to fix it in 1984."*
- Visual Elements:
  - 6 vertical fader slots (simple rectangles)
  - VU meters (2 horizontal bars with cyan/magenta gradient)
  - 12 rotary knobs (circles with indicator line)
  - Power LED (pulsing cyan dot)
  - Worn labels (barely visible text)
  - Coffee ring stain (top-right corner)

#### **2. TURNTABLE** [100x60px] - LEFT SIDE
- Position: (100, 320)
- Clickable: YES
- Story: *"A Technics SL-1200. Same model as every club in America. Yours has initials carved in the dust cover: 'S+J 1982'."*
- Visual Elements:
  - Circular platter (concentric circles)
  - Tonearm (thin diagonal line with cartridge)
  - Speed selector buttons (33/45)
  - Power button (glowing cyan when active)
  - Dust cover (semi-transparent overlay)
  - Currently playing record (if active - spinning animation)

#### **3. ROTARY PHONE** [60x50px] - RIGHT SIDE
- Position: (480, 310)
- Clickable: YES
- Story: *"The cord is 12 feet long from pacing. You've had 4,783 conversations on this phone. Tonight is the last."*
- Visual Elements:
  - Curved handset (resting in cradle or floating off-hook)
  - Rotary dial (circle with finger holes)
  - Coiled cord (dynamic - stretches during calls)
  - Blinking light when caller waiting (magenta pulse)
  - Worn number labels (faded text)

#### **4. COFFEE MUG** [20x25px] - NEAR MIXER
- Position: (370, 295)
- Clickable: YES
- Story: *"'World's Okayest DJ' - a gift from Sarah in 1983. The handle broke in 1985. You still use it."*
- Visual Elements:
  - Cylindrical body
  - Handle broken off (jagged edge visible)
  - Steam rising (when "fresh" - wavy lines)
  - Coffee level (changes throughout night - drops over time)
  - Text barely visible on side

#### **5. ASHTRAY** [30x15px] - LEFT OF PHONE
- Position: (440, 320)
- Clickable: YES
- Story: *"You quit smoking in 1985. You keep it for guests. Nobody's visited in three years."*
- Visual Elements:
  - Circular dish
  - Single cigarette butt (from last visitor)
  - Hotel logo on bottom (barely visible)
  - Ash residue (gray pixels)

#### **6. NOTEPAD** [40x30px] - CENTER-RIGHT
- Position: (400, 330)
- Clickable: YES
- Story: *"Caller names, song requests, phone numbers. The last page just says 'Remember to say goodbye.'"*
- Visual Elements:
  - Spiral binding (left edge)
  - Scribbled notes (illegible lines)
  - Pen resting on top
  - Corner pages curled
  - Coffee stain (bottom-right)

#### **7. RECORD CRATE** [80x100px] - FLOOR LEFT
- Position: (40, 350)
- Clickable: YES
- Story: *"347 records. You know every scratch, every skip. After tonight, they'll sell for 50 cents each at Goodwill."*
- Visual Elements:
  - Wooden milk crate
  - Record sleeves visible (vertical lines)
  - Dividers (alphabetical tabs barely visible)
  - One record leaning against side
  - Dust accumulated on edges

#### **8. DESK LAMP** [30x60px] - TOP RIGHT
- Position: (540, 260)
- Clickable: YES
- Story: *"Adjustable arm from a drafting table. The bulb flickers when the transmitter peaks. Always has."*
- Visual Elements:
  - Articulated arm (3 segments)
  - Cone shade
  - Light glow (cyan radial gradient)
  - Base clamped to desk edge
  - On/off switch (visible)
  - Occasional flicker (animation)

---

### BACK WALL (Environmental Storytelling)

#### **9. CORK BOARD** [200x150px] - CENTER BACK
- Position: (220, 130)
- Clickable: YES
- Story: *"Every photo tells the same story: people who used to work here. You're the last one left."*
- Sub-elements (each individually clickable):
  - **9a. Station photo (1979)** - Group shot, 8 people
  - **9b. Concert ticket stub** - "Springsteen, 1981"
  - **9c. Polaroid (Sarah)** - Woman smiling, dated "6/14/82"
  - **9d. FCC license** - Official document, yellowed
  - **9e. Postcard** - "Wish you were here" (faded)
  - **9f. Newspaper clipping** - "Local Radio Thrives"
  - Pushpins holding everything (cyan dots)

#### **10. WINDOW** [120x100px] - TOP LEFT
- Position: (80, 120)
- Clickable: YES
- Story: *"The city used to glow at night. Now half the streetlights are out. Budget cuts."*
- Visual Elements:
  - 4-pane window frame
  - Night sky (black)
  - City lights (distant yellow/cyan pixels - sparse)
  - Venetian blinds (partially open - horizontal lines)
  - Slight glow from transmitter tower reflection

#### **11. POSTER (Station Logo)** [80x120px] - RIGHT WALL
- Position: (500, 140)
- Clickable: YES
- Story: *"WKLS-AM: 'The Voice of the Valley' - Serving our community since 1967. Sold to MediaCorp for $1.2 million."*
- Visual Elements:
  - Bold "WKLS" text
  - Frequency "1340 AM"
  - Stylized radio waves (concentric arcs)
  - Faded colors (was vibrant, now dull)
  - Curling corner (top-right)

#### **12. CLOCK** [40x40px] - TOP CENTER
- Position: (300, 100)
- Clickable: YES
- Story: *"Runs three minutes fast. You've never fixed it. If you're early, you're on time."*
- Visual Elements:
  - Circular face
  - Hour/minute hands (actual working time)
  - Second hand (optional - ticking animation)
  - Numbers (12, 3, 6, 9 visible)
  - Slight glow (cyan backlight)
  - Shows current hour of game

---

### ATMOSPHERIC DETAILS (Non-Interactive Background)

#### **13. SOUNDPROOFING FOAM** - WALLS (TEXTURE)
- Scattered pyramid-shaped foam panels
- Cyan highlights on peaks
- Creates depth on back wall

#### **14. CABLES** - FLOOR/DESK (VISUAL NOISE)
- XLR cables snaking across floor
- Tangled near mixer
- Some connected, some loose
- Cyan/black striped pattern

#### **15. CARPET** - FLOOR (TEXTURE)
- Industrial carpet (dark with cyan flecks)
- Stains visible (coffee, wear patterns)
- Path worn from chair to door

#### **16. AIR VENT** - BACK WALL TOP
- Horizontal slats
- Slight dust accumulation
- Barely visible (dark)

#### **17. TRANSMITTER TOWER** - VISIBLE THROUGH WINDOW/BACKGROUND
- Distant red light blinking (safety beacon)
- Antenna structure silhouette
- Symbol of the station dying

---

## ADDITIONAL CLICKABLE OBJECTS (Smaller Details)

#### **18. MICROPHONE** [25x60px] - Desk center-left
*"Neumann U47. Worth more than three months' salary. You've never dropped it. Not once."*

#### **19. HEADPHONES** [50x40px] - Hanging on mixer
*"Sennheiser HD 414s. The foam disintegrated in 1984. You taped it back together."*

#### **20. BROADCAST LOG** [60x40px] - Desk right edge
*"FCC requirement. Every song, every announcement, logged by hand. Tonight's page is blank."*

#### **21. EMPTY BEER BOTTLE** [15x35px] - Floor near crate
*"From the last staff party. December 1984. Nobody remembers what you were celebrating."*

#### **22. STAPLER** [25x15px] - Desk left
*"Swingline 747. Appears in every office scene in every movie. This one actually works."*

#### **23. RUBBER BAND BALL** [20x20px] - Desk edge
*"Started in 1981. Now the size of a baseball. You add one every time you think about quitting."*

#### **24. CASSETTE TAPE** [30x20px] - Near turntable
*"Mix tape. Label says 'Emergency Use Only' in Sarah's handwriting. You've never played it."*

#### **25. SCISSORS** [20x30px] - In cup with pens
*"For cutting reel-to-reel tape. You haven't used reel-to-reel since 1983."*

#### **26. ROLL OF TAPE** [20x20px] - Desk clutter
*"Scotch tape. Half gone. Used for everything except taping things together."*

#### **27. PAPERWEIGHT** [25x30px] - On loose papers
*"A rock. Literally just a rock. Found it in the parking lot in 1979."*

#### **28. DEAD PLANT** [30x40px] - Corner of desk
*"It was a cactus. You managed to kill a cactus. That's impressive."*

#### **29. CALENDAR** [60x50px] - Wall right side
*"Still shows March 1987. Nobody bothered to flip it. What's the point?"*

#### **30. FIRE EXTINGUISHER** [25x50px] - Floor corner
*"Inspection sticker expired 1985. If there's a fire, you're calling the fire department."*

#### **31. COAT HOOK** [15x30px] - Wall left
*"Your jacket. The one Sarah said made you look 'like a real DJ.' You wear it every shift."*

#### **32. LIGHT SWITCH** [15x25px] - Wall by door
*"Controls the overhead fluorescents. You keep them off. Desk lamp is enough."*

#### **33. EXTENSION CORD** [roping across floor]
*"Connects the turntable. The outlet is on the wrong wall. Has been since 1972."*

#### **34. DESK DRAWER** [40x20px] - Visible under desk
*"Locked since 1983. You lost the key in 1984. You don't remember what's inside."*

#### **35. TRASH CAN** [30x40px] - Floor right
*"Full of crumpled papers. Drafts of tonight's final speech. None felt right."*

#### **36. MOUSE TRAP** [20x15px] - Floor back corner
*"Set in 1986. Never caught anything. Maybe the mice moved out with everyone else."*

#### **37. SPARE FUSE** [10x15px] - Taped to wall
*"For the transmitter. Last replacement fuse in the building. When this blows, it's over."*

#### **38. STATION MANUAL** [50x35px] - Shelf under desk
*"'WKLS Operations Manual - 1967.' Mimeographed. Smells like a library basement."*

#### **39. FIRST AID KIT** [40x30px] - Mounted on wall
*"Hasn't been opened since 1981 when Derek cut his hand on a razor blade splice."*

#### **40. DUST BUNNY** [15x10px] - Corner floor
*"You meant to sweep this week. And last week. And the week before."*

---

## COLOR PALETTE & USAGE

### Primary Colors:
- **Cyan (#00ffff)** - UI elements, highlights, active equipment, glowing lights
- **Magenta (#ff00ff)** - Secondary highlights, caller indicator, special items
- **Black (#000000)** - Background, shadows, dead space
- **Dark Cyan (#008888)** - Mid-tones, inactive equipment, depth

### Accent Colors (sparingly):
- **Yellow (#ffff00)** - Warning lights, transmitter alerts
- **Dark Gray (#333333)** - Wood, metal surfaces
- **Red (#ff0000)** - Emergency indicators, power lights

---

## ANIMATION NOTES

### Continuous Loops:
1. **Clock second hand** - Ticks every second
2. **VU Meters** - Bounce during dialogue/music
3. **Phone light** - Pulses when caller waiting
4. **Lamp flicker** - Occasional (when transmitter stressed)
5. **Turntable spin** - During music playback
6. **Coffee steam** - Gentle wavy lines
7. **Transmitter tower beacon** - Slow blink (distant)

### Interactive Feedback:
1. **Object hover** - Slight cyan glow outline
2. **Object click** - Brief magenta flash
3. **Record selection** - Slides from crate to turntable
4. **Phone rings** - Handset vibrates, bell animation

---

## ISOMETRIC PERSPECTIVE GUIDE

```
     TOP VIEW                    ISOMETRIC VIEW
   
   ╔═══════╗                      ╱╲╱╲╱╲╱╲
   ║ DESK  ║                     ╱  DESK  ╲
   ║       ║                    ╱          ╲
   ╚═══════╝                   ╱____________╲
```

**Depth Rules:**
- Objects further back are higher on screen (Y position)
- All horizontal lines should angle 30° left or right
- Vertical lines stay vertical
- Objects in foreground overlap background
- Desk surface tilted ~15° toward viewer

**Scale Reference:**
- 1 grid unit = 20px
- Desk surface: 400px wide × 80px deep
- Character would be ~100px tall (never shown, just for scale)

---

## RENDERING ORDER (Back to Front)

1. Background (black)
2. Window/night sky
3. Back wall (soundproofing texture)
4. Cork board + posters
5. Clock
6. Desk surface (isometric plane)
7. Cables (floor)
8. Large equipment (crate, trash can)
9. Desk equipment (mixer, turntable)
10. Small objects (mug, ashtray, notepad)
11. Desk lamp (top layer for glow effect)
12. Hover effects/UI overlays

---

## SPRITE SHEET ORGANIZATION RECOMMENDATION

```
booth-sprites.png (1024x1024)

┌────────────────────────────────┐
│ MIXER    TURNTABLE    PHONE    │  Row 1: Large equipment
├────────────────────────────────┤
│ LAMP     CRATE       BOARD     │  Row 2: Medium objects
├────────────────────────────────┤
│ MUG ASHTRAY PAD  [small objs]  │  Row 3: Small clutter
├────────────────────────────────┤
│ [Background textures]          │  Row 4: Tileable textures
└────────────────────────────────┘
```

**OR** 

Individual PNGs per object for easier editing:
- `mixer.png`, `turntable.png`, `phone.png`, etc.
- Transparent backgrounds
- Consistent naming convention

---

## TECHNICAL SPECIFICATIONS

**Canvas Resolution:** 640×480 (4:3 aspect ratio)
**Pixel Scale:** 1:1 (no anti-aliasing in pixel art)
**Export Format:** PNG with transparency
**Coordinate System:** Top-left origin (0,0)

**Clickable Regions:**
```javascript
const BOOTH_OBJECTS = [
  { id: 1, name: "Mixer", x: 240, y: 300, w: 150, h: 80, story: "..." },
  { id: 2, name: "Turntable", x: 100, y: 320, w: 100, h: 60, story: "..." },
  // ... etc
];
```

---

## MOOD & ATMOSPHERE NOTES

**Lighting Philosophy:**
- Single source (desk lamp) creates dramatic shadows
- Equipment glows provide secondary light (cyan)
- Window provides minimal ambient (dark blue)
- Overall darkness = isolation, finality

**Wear & Tear:**
- Everything should look USED
- Dust, coffee rings, worn labels
- Cables have kinks and loops
- Nothing is pristine

**Emotional Subtext:**
- Objects tell story of abandonment
- Each item is a memory frozen in time
- Clutter = accumulated years
- Emptiness = everyone left

---

## FINAL CHECKLIST FOR ARTIST

- [ ] All 40 objects drawn and positioned
- [ ] Isometric perspective consistent
- [ ] Clickable regions clearly defined
- [ ] Color palette adhered to (cyan/magenta/black)
- [ ] Atmospheric depth (back to front layering)
- [ ] Animation frames prepared (clock, VU meters, etc.)
- [ ] Interactive feedback states (hover/click)
- [ ] Sprite sheet organized OR individual PNGs exported
- [ ] Coordinates documented for code integration
- [ ] Test render at 640×480 to verify pixel clarity

---

## INTEGRATION WITH EXISTING CODE

Your `game-final.js` has this structure waiting:
```javascript
const BOOTH_OBJECTS = [
  { id: 1, x: 240, y: 300, w: 150, h: 80, story: "...", special: null },
  // Add all 40 objects here with exact coordinates
];

function renderBooth() {
  // Draw background
  // Draw all objects from BOOTH_OBJECTS array
  // Apply hover effects
  // Render animations
}
```

Once you have the pixel art, I can code the full rendering system.
