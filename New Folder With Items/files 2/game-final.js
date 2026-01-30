/**
 * THE LAST BROADCAST
 * Clean, object-oriented game architecture
 * Following strict UI/UX and retro design principles
 */

// =============================================================================
// GAME STATE (Single Source of Truth)
// =============================================================================

const GameState = {
    phase: 'LANDING', // LANDING, INTRO, WAITING, DIALOGUE, SELECTING, PLAYING, GAME_OVER
    hour: 1,
    transmitterPower: 100,
    listeners: [],
    totalListenerSeconds: 0,
    perfectMatches: [],
    goodMatches: [],
    records: [],
    availableCallers: [],
    currentCaller: null,
    usedRecords: new Set(),
    gameTime: 0,
    timePerHour: 12, // seconds per game hour
    discoveredObjects: new Set(),
    audioContext: null,
    callsAnswered: 0
};

// =============================================================================
// DATA: RECORDS
// =============================================================================

const RECORDS_DATA = [
    { id: 1, title: "Rebel Heart", genre: "Rock", mood: "Defiant", era: "1980s" },
    { id: 2, title: "Blue Monday", genre: "Blues", mood: "Melancholy", era: "1970s" },
    { id: 3, title: "Starlight Serenade", genre: "Jazz", mood: "Tender", era: "1960s" },
    { id: 4, title: "Summer Drive", genre: "Pop", mood: "Upbeat", era: "1980s" },
    { id: 5, title: "Yesterday's Song", genre: "Folk", mood: "Nostalgic", era: "1970s" },
    { id: 6, title: "Neon Dreams", genre: "Ambient", mood: "Contemplative", era: "1980s" },
    { id: 7, title: "Factory Floor", genre: "Rock", mood: "Upbeat", era: "1980s" },
    { id: 8, title: "Moonlit Waltz", genre: "Jazz", mood: "Nostalgic", era: "1960s" },
    { id: 9, title: "Highway 61", genre: "Blues", mood: "Defiant", era: "1970s" },
    { id: 10, title: "Sarah's Song", genre: "Folk", mood: "Tender", era: "1980s", special: "sarah" },
    { id: 11, title: "Cityscape", genre: "Ambient", mood: "Melancholy", era: "1980s" },
    { id: 12, title: "Morning Light", genre: "Pop", mood: "Upbeat", era: "1980s" }
];

// =============================================================================
// DATA: CALLERS
// =============================================================================

const CALLERS_DATA = [
    {
        id: 1, name: "Bill", minHour: 2,
        text: "Just got laid off. Twenty years at the plant. They gave me a Casio watch. I don't know who I am if I'm not building things.",
        needs: { genre: "Rock", mood: "Defiant", era: "1980s" },
        relationship: "factory_father",
        responses: {
            perfect: "Yeah... you're right. We built this town. We're not done yet. Thank you.",
            good: "Appreciate it. Helps to know someone's listening.",
            poor: "Not what I needed. Goodnight."
        }
    },
    {
        id: 2, name: "Marie", minHour: 2,
        text: "My daughter turns sixteen tomorrow. I remember holding her the day she was born. Where did the time go?",
        needs: { genre: "Folk", mood: "Nostalgic", era: "1970s" },
        responses: {
            perfect: "That's it. That's exactly it. Time moves, but love stays. Thank you.",
            good: "That's nice. Thank you.",
            poor: "I should go wrap her present."
        }
    },
    {
        id: 3, name: "Tommy", minHour: 3,
        text: "Driving to the coast. Left at midnight. If I stop, I'll turn around. I can't turn around.",
        needs: { genre: "Pop", mood: "Upbeat", era: "1980s" },
        responses: {
            perfect: "This is it. This is the soundtrack for starting over. Thank you!",
            good: "Okay. Yeah. I can do this.",
            poor: "That's making me sadder. I gotta go."
        }
    },
    {
        id: 4, name: "Lisa", minHour: 4,
        text: "Dad came home and just sat there. Wouldn't talk. Wouldn't look at me. I've never seen him cry.",
        needs: { genre: "Blues", mood: "Tender", era: "1970s" },
        relationship: "factory_daughter",
        relatedTo: "factory_father",
        responses: {
            perfect: "Wait... is this for him too? Tell him I love him. Please.",
            good: "Thank you. That's beautiful.",
            poor: "I need to check on him. Goodnight."
        }
    },
    {
        id: 5, name: "James", minHour: 5,
        text: "Mom used to sing me this song. Can't remember the words. She's in the hospital. They say I should prepare myself.",
        needs: { genre: "Jazz", mood: "Nostalgic", era: "1960s" },
        relationship: "hospital_son",
        responses: {
            perfect: "That's the one. How did you know? Thank you. I'm going to sit with her now.",
            good: "That's close. Really close. Thanks.",
            poor: "No, that's not it. Sorry."
        }
    },
    {
        id: 6, name: "Angela", minHour: 6,
        text: "I own the factory. Had to let thirty people go today. Known these families for decades. Some won't look at me now.",
        needs: { genre: "Jazz", mood: "Melancholy", era: "1960s" },
        relationship: "factory_owner",
        relatedTo: "factory_father",
        responses: {
            perfect: "I thought someone would yell at me. But you just listened. Thank you.",
            good: "I appreciate that. Really.",
            poor: "I understand. Thanks."
        }
    },
    {
        id: 7, name: "Daniel", minHour: 7,
        text: "At the hospital. Mom's not going to make it. Nurses say I should talk to her, but what do you say?",
        needs: { genre: "Jazz", mood: "Tender", era: "1960s" },
        relationship: "hospital_son_return",
        relatedTo: "hospital_son",
        responses: {
            perfect: "That song. She sang that to me. You remembered. Thank you.",
            good: "That's beautiful. Thank you.",
            poor: "I need to get back to her."
        }
    },
    {
        id: 8, name: "Rebecca", minHour: 3,
        text: "My husband and I used to dance in the kitchen. Three years ago today, he died. I can still feel his hand on my back.",
        needs: { genre: "Jazz", mood: "Nostalgic", era: "1960s" },
        responses: {
            perfect: "That's our song. Thank you so much.",
            good: "He would have liked that.",
            poor: "Not quite right, but thanks."
        }
    },
    {
        id: 9, name: "Carlos", minHour: 2,
        text: "Night shift just ended. Factory closes next month. Thirty years. Don't know how to be anything else.",
        needs: { genre: "Blues", mood: "Defiant", era: "1970s" },
        responses: {
            perfect: "That's right. We're not done yet. Not by a long shot.",
            good: "Appreciate it, friend.",
            poor: "Yeah. Maybe. Goodnight."
        }
    },
    {
        id: 10, name: "Sarah", minHour: 9,
        text: "I don't know if you remember me. I used to call in, years ago. You played our song. I said I'd wait for the morning show. I did.",
        needs: { genre: "Folk", mood: "Tender", era: "1980s" },
        special: "sarah",
        responses: {
            perfect: "You remembered. After all these years. Thank you for keeping the morning show alive.",
            good: "That's close. Thank you for trying.",
            poor: "It's okay. It was a long time ago."
        }
    },
    {
        id: 11, name: "Michelle", minHour: 8,
        text: "I'm a nurse. Double shift just ended. Lost someone tonight—young kid. I keep seeing his mother's face.",
        needs: { genre: "Ambient", mood: "Contemplative", era: "1980s" },
        responses: {
            perfect: "Sometimes we need the quiet. Thank you for understanding.",
            good: "Thank you. That helps.",
            poor: "I need something else. Thanks."
        }
    },
    {
        id: 12, name: "Frank", minHour: 2,
        text: "Son's getting married tomorrow. Giving a speech. How do you tell your kid you're proud without crying?",
        needs: { genre: "Folk", mood: "Tender", era: "1970s" },
        responses: {
            perfect: "Perfect. You always know just what we need.",
            good: "That's nice. Really nice.",
            poor: "Not quite right, but thanks."
        }
    },
    {
        id: 13, name: "Jennifer", minHour: 5,
        text: "Just broke up with my boyfriend. Five years. He said I work too much. Maybe he's right. Don't know who I am without the work.",
        needs: { genre: "Pop", mood: "Upbeat", era: "1980s" },
        responses: {
            perfect: "Maybe this IS the start of something good. Thank you.",
            good: "Okay. That helps.",
            poor: "Can't do upbeat right now. Sorry."
        }
    },
    {
        id: 14, name: "Robert", minHour: 6,
        text: "Truck driver. Been on the road three weeks. Haven't seen my family. Sometimes forget what my daughter's voice sounds like.",
        needs: { genre: "Folk", mood: "Nostalgic", era: "1970s" },
        responses: {
            perfect: "That's the one. Makes me remember. Thank you, friend.",
            good: "Appreciate that. Gets lonely.",
            poor: "Thanks for trying."
        }
    },
    {
        id: 15, name: "David", minHour: 4,
        text: "Just retired. Forty years teaching. Walked out today for the last time. Now what? Just... now what?",
        needs: { genre: "Jazz", mood: "Contemplative", era: "1960s" },
        responses: {
            perfect: "Maybe this is the beginning, not the end. Thank you for that.",
            good: "That's thoughtful. Thanks.",
            poor: "Not sure that's what I needed."
        }
    },
    {
        id: 16, name: "Marcus", minHour: 9,
        text: "My band broke up tonight. We were supposed to make it big. Now I'm thirty-five with a guitar and nothing else.",
        needs: { genre: "Rock", mood: "Defiant", era: "1980s" },
        responses: {
            perfect: "You're right. It's not over. Not if I don't let it be. Thank you.",
            good: "Thanks, man. Needed that.",
            poor: "Maybe it IS over."
        }
    },
    {
        id: 17, name: "Paul", minHour: 10,
        text: "Daughter just called. She's having a baby. I'm going to be a grandfather. Never thought I'd make it this far.",
        needs: { genre: "Pop", mood: "Upbeat", era: "1980s" },
        responses: {
            perfect: "That's PERFECT! That's exactly how I feel! Thank you!",
            good: "That's great. Really great.",
            poor: "Not quite the celebration I hoped for."
        }
    },
    {
        id: 18, name: "Helen", minHour: 8,
        text: "Wedding anniversary. He's been gone five years. I still set a place for him at dinner. Is that crazy?",
        needs: { genre: "Jazz", mood: "Tender", era: "1960s" },
        responses: {
            perfect: "That's beautiful. Love doesn't end. Thank you for reminding me.",
            good: "That's sweet. Thank you.",
            poor: "Not quite right, but thanks."
        }
    }
];

// =============================================================================
// DATA: BOOTH OBJECTS
// =============================================================================

const BOOTH_OBJECTS = [
    // DESK LEVEL - Main Equipment
    { id: "mixer", x: 240, y: 300, w: 150, h: 80, 
      story: "Channel 3 has been stuck at 7dB since 1982. You stopped trying to fix it in 1984.", 
      color: "#0ff", type: "equipment" },
    { id: "turntable", x: 100, y: 320, w: 100, h: 60, 
      story: "A Technics SL-1200. Same model as every club in America. Yours has initials carved in the dust cover: 'S+J 1982'.", 
      color: "#0ff", type: "equipment" },
    { id: "phone", x: 480, y: 310, w: 60, h: 50, 
      story: "The cord is 12 feet long from pacing. You've had 4,783 conversations on this phone. Tonight is the last.", 
      color: "#f0f", type: "equipment" },
    { id: "coffee", x: 370, y: 295, w: 20, h: 25, 
      story: "'World's Okayest DJ' - a gift from Sarah in 1983. The handle broke in 1985. You still use it.", 
      color: "#ff0", type: "small" },
    { id: "ashtray", x: 440, y: 320, w: 30, h: 15, 
      story: "You quit smoking in 1985. You keep it for guests. Nobody's visited in three years.", 
      color: "#888", type: "small" },
    { id: "notepad", x: 400, y: 330, w: 40, h: 30, 
      story: "Caller names, song requests, phone numbers. The last page just says 'Remember to say goodbye.'", 
      color: "#ff0", type: "small" },
    { id: "crate", x: 40, y: 350, w: 80, h: 100, 
      story: "347 records. You know every scratch, every skip. After tonight, they'll sell for 50 cents each at Goodwill.", 
      color: "#0ff", type: "equipment" },
    { id: "lamp", x: 540, y: 260, w: 30, h: 60, 
      story: "Adjustable arm from a drafting table. The bulb flickers when the transmitter peaks. Always has.", 
      color: "#ff0", type: "equipment" },
    
    // BACK WALL - Environmental
    { id: "corkboard", x: 220, y: 130, w: 200, h: 150, 
      story: "Every photo tells the same story: people who used to work here. You're the last one left.", 
      color: "#0ff", type: "wall" },
    { id: "window", x: 80, y: 120, w: 120, h: 100, 
      story: "The city used to glow at night. Now half the streetlights are out. Budget cuts.", 
      color: "#088", type: "wall" },
    { id: "poster", x: 500, y: 140, w: 80, h: 120, 
      story: "WKLS-AM: 'The Voice of the Valley' - Serving our community since 1967. Sold to MediaCorp for $1.2 million.", 
      color: "#0ff", type: "wall" },
    { id: "clock", x: 300, y: 100, w: 40, h: 40, 
      story: "Runs three minutes fast. You've never fixed it. If you're early, you're on time.", 
      color: "#0ff", type: "wall" },
    
    // SMALLER DETAILS
    { id: "microphone", x: 340, y: 265, w: 25, h: 60, 
      story: "Neumann U47. Worth more than three months' salary. You've never dropped it. Not once.", 
      color: "#0ff", type: "equipment" },
    { id: "headphones", x: 320, y: 305, w: 50, h: 40, 
      story: "Sennheiser HD 414s. The foam disintegrated in 1984. You taped it back together.", 
      color: "#0ff", type: "small" },
    { id: "log", x: 520, y: 330, w: 60, h: 40, 
      story: "FCC requirement. Every song, every announcement, logged by hand. Tonight's page is blank.", 
      color: "#ff0", type: "small" },
    { id: "beer", x: 65, y: 420, w: 15, h: 35, 
      story: "From the last staff party. December 1984. Nobody remembers what you were celebrating.", 
      color: "#0f8", type: "small" },
    { id: "stapler", x: 200, y: 340, w: 25, h: 15, 
      story: "Swingline 747. Appears in every office scene in every movie. This one actually works.", 
      color: "#888", type: "small" },
    { id: "rubberband", x: 230, y: 335, w: 20, h: 20, 
      story: "Started in 1981. Now the size of a baseball. You add one every time you think about quitting.", 
      color: "#f80", type: "small" },
    { id: "cassette", x: 150, y: 340, w: 30, h: 20, 
      story: "Mix tape. Label says 'Emergency Use Only' in Sarah's handwriting. You've never played it.", 
      special: "sarah", color: "#f0f", type: "small" },
    { id: "scissors", x: 415, y: 300, w: 20, h: 30, 
      story: "For cutting reel-to-reel tape. You haven't used reel-to-reel since 1983.", 
      color: "#888", type: "small" },
    { id: "tape_roll", x: 390, y: 310, w: 20, h: 20, 
      story: "Scotch tape. Half gone. Used for everything except taping things together.", 
      color: "#ff0", type: "small" },
    { id: "paperweight", x: 425, y: 335, w: 25, h: 30, 
      story: "A rock. Literally just a rock. Found it in the parking lot in 1979.", 
      color: "#666", type: "small" },
    { id: "plant", x: 560, y: 320, w: 30, h: 40, 
      story: "It was a cactus. You managed to kill a cactus. That's impressive.", 
      color: "#0a0", type: "small" },
    { id: "calendar", x: 460, y: 200, w: 60, h: 50, 
      story: "Still shows March 1987. Nobody bothered to flip it. What's the point?", 
      color: "#f00", type: "wall" },
    { id: "extinguisher", x: 590, y: 350, w: 25, h: 50, 
      story: "Inspection sticker expired 1985. If there's a fire, you're calling the fire department.", 
      color: "#f00", type: "small" },
    { id: "jacket", x: 50, y: 250, w: 35, h: 60, 
      story: "Your jacket. The one Sarah said made you look 'like a real DJ.' You wear it every shift.", 
      color: "#088", type: "wall" },
    { id: "switch", x: 60, y: 180, w: 15, h: 25, 
      story: "Controls the overhead fluorescents. You keep them off. Desk lamp is enough.", 
      color: "#ff0", type: "wall" },
    { id: "drawer", x: 200, y: 380, w: 40, h: 20, 
      story: "Locked since 1983. You lost the key in 1984. You don't remember what's inside.", 
      color: "#333", type: "small" },
    { id: "trash", x: 560, y: 380, w: 30, h: 40, 
      story: "Full of crumpled papers. Drafts of tonight's final speech. None felt right.", 
      color: "#333", type: "small" },
    { id: "mousetrap", x: 580, y: 450, w: 20, h: 15, 
      story: "Set in 1986. Never caught anything. Maybe the mice moved out with everyone else.", 
      color: "#888", type: "small" },
    { id: "fuse", x: 540, y: 200, w: 10, h: 15, 
      story: "For the transmitter. Last replacement fuse in the building. When this blows, it's over.", 
      color: "#ff0", type: "wall" },
    { id: "manual", x: 180, y: 390, w: 50, h: 35, 
      story: "'WKLS Operations Manual - 1967.' Mimeographed. Smells like a library basement.", 
      color: "#0ff", type: "small" },
    { id: "firstaid", x: 120, y: 180, w: 40, h: 30, 
      story: "Hasn't been opened since 1981 when Derek cut his hand on a razor blade splice.", 
      color: "#f00", type: "wall" },
    
    // SPECIAL OBJECTS
    { id: "sarah_photo", x: 250, y: 150, w: 40, h: 40, 
      story: "Sarah, June 14, 1982. She said she'd wait for the morning show. She did.", 
      special: "sarah_photo", color: "#f0f", type: "wall" },
    { id: "station_photo", x: 310, y: 150, w: 60, h: 45, 
      story: "Staff photo, 1979. Eight people. You recognize six. Two you've forgotten.", 
      color: "#0ff", type: "wall" },
    { id: "concert_stub", x: 370, y: 160, w: 30, h: 20, 
      story: "Springsteen, 1981. You interviewed him in the parking lot. He remembered your name.", 
      color: "#ff0", type: "wall" },
    { id: "postcard", x: 250, y: 200, w: 35, h: 25, 
      story: "'Wish you were here' - from Marie, 1980. She never came back from California.", 
      color: "#0ff", type: "wall" },
    { id: "newspaper", x: 320, y: 210, w: 50, h: 35, 
      story: "'Local Radio Thrives' - headline from 1978. The optimism hurts to read.", 
      color: "#ff0", type: "wall" },
    { id: "fcc_license", x: 370, y: 195, w: 40, h: 50, 
      story: "Your broadcast license. Signed by you in 1975. Expires tomorrow.", 
      color: "#0ff", type: "wall" },
    { id: "vinyl_special", x: 55, y: 375, w: 12, h: 40, 
      story: "Sarah's Song. The record you played the morning she called. Keep it for last.", 
      special: "sarah_vinyl", color: "#f0f", type: "small" }
];

// =============================================================================
// CANVAS & RENDERING
// =============================================================================

let canvas, ctx;
let canvasScale = 1;

function initCanvas() {
    canvas = document.getElementById('game-canvas');
    ctx = canvas.getContext('2d');
    ctx.imageSmoothingEnabled = false;
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);
}

function resizeCanvas() {
    const container = canvas.parentElement;
    const containerW = container.clientWidth - 40;
    const containerH = container.clientHeight - 40;
    
    const scaleX = containerW / 640;
    const scaleY = containerH / 480;
    canvasScale = Math.min(scaleX, scaleY, 2); // Max 2x scale
    
    canvas.style.width = (640 * canvasScale) + 'px';
    canvas.style.height = (480 * canvasScale) + 'px';
}

function renderBooth() {
    // Clear
    ctx.fillStyle = '#000';
    ctx.fillRect(0, 0, 640, 480);
    
    // Background gradient
    const grad = ctx.createLinearGradient(0, 0, 640, 480);
    grad.addColorStop(0, '#001a1a');
    grad.addColorStop(0.5, '#000814');
    grad.addColorStop(1, '#000');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, 640, 480);
    
    // BACK WALL - Soundproofing texture
    ctx.fillStyle = '#0a1a1a';
    ctx.fillRect(60, 40, 520, 280);
    
    // Soundproofing foam pattern
    for (let x = 70; x < 570; x += 40) {
        for (let y = 50; y < 310; y += 40) {
            ctx.fillStyle = '#0d1d1d';
            ctx.fillRect(x + 5, y + 5, 30, 30);
        }
    }
    
    // WINDOW with city lights
    ctx.fillStyle = '#000814';
    ctx.fillRect(80, 120, 120, 100);
    ctx.strokeStyle = '#0ff';
    ctx.lineWidth = 2;
    ctx.strokeRect(80, 120, 120, 100);
    // Window panes
    ctx.strokeRect(80, 120, 60, 50);
    ctx.strokeRect(140, 120, 60, 50);
    ctx.strokeRect(80, 170, 60, 50);
    ctx.strokeRect(140, 170, 60, 50);
    
    // City lights (sparse)
    for (let i = 0; i < 25; i++) {
        const x = 85 + Math.random() * 110;
        const y = 125 + Math.random() * 90;
        ctx.fillStyle = `rgba(0, 255, 255, ${0.2 + Math.random() * 0.6})`;
        ctx.fillRect(x, y, 2, 2);
    }
    
    // Transmitter tower in distance
    ctx.strokeStyle = 'rgba(255, 0, 0, 0.3)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(150, 130);
    ctx.lineTo(150, 110);
    ctx.lineTo(145, 115);
    ctx.lineTo(155, 115);
    ctx.lineTo(150, 110);
    ctx.stroke();
    // Blinking beacon
    if (Math.floor(Date.now() / 1000) % 2 === 0) {
        ctx.fillStyle = '#f00';
        ctx.fillRect(149, 109, 3, 3);
    }
    
    // CORK BOARD area
    ctx.fillStyle = '#8B4513';
    ctx.fillRect(220, 130, 200, 150);
    
    // Pushpin pattern
    const pins = [
        [240, 145], [270, 145], [300, 145], [330, 145],
        [240, 190], [300, 190], [350, 190],
        [240, 235], [290, 235], [340, 235]
    ];
    pins.forEach(([x, y]) => {
        ctx.fillStyle = '#0ff';
        ctx.fillRect(x, y, 3, 3);
    });
    
    // POSTER on right
    ctx.fillStyle = '#003a3a';
    ctx.fillRect(500, 140, 80, 120);
    ctx.strokeStyle = '#0ff';
    ctx.lineWidth = 2;
    ctx.strokeRect(500, 140, 80, 120);
    ctx.fillStyle = '#0ff';
    ctx.font = 'bold 16px monospace';
    ctx.fillText('WKLS', 515, 170);
    ctx.font = '10px monospace';
    ctx.fillText('1340 AM', 515, 190);
    ctx.fillText('Est.1967', 515, 240);
    
    // CLOCK
    drawClock(300, 100, 40);
    
    // FLOOR - Carpet texture
    ctx.fillStyle = '#0a0a0a';
    ctx.fillRect(0, 400, 640, 80);
    // Carpet specks
    for (let i = 0; i < 200; i++) {
        ctx.fillStyle = `rgba(0, 255, 255, ${Math.random() * 0.1})`;
        ctx.fillRect(Math.random() * 640, 400 + Math.random() * 80, 1, 1);
    }
    
    // DESK SURFACE (Isometric)
    ctx.fillStyle = '#1a2a2a';
    ctx.fillRect(80, 290, 480, 120);
    // Desk edge highlight
    ctx.fillStyle = '#0ff';
    ctx.globalAlpha = 0.1;
    ctx.fillRect(80, 290, 480, 4);
    ctx.globalAlpha = 1;
    
    // CABLES on floor
    ctx.strokeStyle = '#333';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(110, 380);
    ctx.quadraticCurveTo(200, 420, 350, 380);
    ctx.stroke();
    
    // Draw all interactive objects
    drawDetailedObjects();
    
    // LISTENER MAP (bottom-left corner overlay)
    drawListenerMap(20, 430, 100, 40);
    
    // DESK LAMP (top layer for glow)
    drawLamp(540, 260);
}

function drawClock(x, y, size) {
    // Clock face
    ctx.fillStyle = '#1a1a1a';
    ctx.beginPath();
    ctx.arc(x + size/2, y + size/2, size/2, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#0ff';
    ctx.lineWidth = 2;
    ctx.stroke();
    
    // Hour marks
    ctx.fillStyle = '#0ff';
    const marks = [0, 3, 6, 9];
    marks.forEach(hour => {
        const angle = (hour * 30 - 90) * Math.PI / 180;
        const markX = x + size/2 + Math.cos(angle) * (size/2 - 6);
        const markY = y + size/2 + Math.sin(angle) * (size/2 - 6);
        ctx.fillRect(markX - 1, markY - 1, 2, 2);
    });
    
    // Time based on game hour
    const hour = GameState.hour % 12;
    const hourAngle = (hour * 30 - 90) * Math.PI / 180;
    const minuteAngle = ((GameState.gameTime % 60) * 6 - 90) * Math.PI / 180;
    
    // Hour hand
    ctx.strokeStyle = '#0ff';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(x + size/2, y + size/2);
    ctx.lineTo(
        x + size/2 + Math.cos(hourAngle) * (size/3),
        y + size/2 + Math.sin(hourAngle) * (size/3)
    );
    ctx.stroke();
    
    // Minute hand
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(x + size/2, y + size/2);
    ctx.lineTo(
        x + size/2 + Math.cos(minuteAngle) * (size/2 - 5),
        y + size/2 + Math.sin(minuteAngle) * (size/2 - 5)
    );
    ctx.stroke();
}

function drawLamp(x, y) {
    // Lamp arm (articulated)
    ctx.strokeStyle = '#444';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(x + 15, y + 60);
    ctx.lineTo(x + 15, y + 40);
    ctx.lineTo(x + 25, y + 20);
    ctx.lineTo(x + 15, y + 5);
    ctx.stroke();
    
    // Lamp shade
    ctx.fillStyle = '#ff0';
    ctx.beginPath();
    ctx.moveTo(x, y);
    ctx.lineTo(x + 10, y + 15);
    ctx.lineTo(x + 40, y + 15);
    ctx.lineTo(x + 30, y);
    ctx.closePath();
    ctx.fill();
    
    // Light glow
    const lampGlow = ctx.createRadialGradient(x + 15, y + 10, 5, x + 15, y + 10, 80);
    lampGlow.addColorStop(0, 'rgba(255, 255, 0, 0.3)');
    lampGlow.addColorStop(0.5, 'rgba(255, 255, 0, 0.1)');
    lampGlow.addColorStop(1, 'rgba(255, 255, 0, 0)');
    ctx.fillStyle = lampGlow;
    ctx.fillRect(x - 50, y - 50, 150, 150);
    
    // Flicker effect if transmitter low
    if (GameState.transmitterPower < 30 && Math.random() > 0.7) {
        ctx.globalAlpha = 0.5;
        ctx.fillStyle = '#000';
        ctx.fillRect(x, y, 40, 20);
        ctx.globalAlpha = 1;
    }
}

function drawDetailedObjects() {
    BOOTH_OBJECTS.forEach(obj => {
        const discovered = GameState.discoveredObjects.has(obj.special);
        const isSpecial = obj.special !== undefined;
        
        ctx.save();
        
        // Draw based on object type
        switch(obj.id) {
            case 'mixer':
                drawMixer(obj.x, obj.y, obj.w, obj.h);
                break;
            case 'turntable':
                drawTurntable(obj.x, obj.y, obj.w, obj.h);
                break;
            case 'phone':
                drawPhone(obj.x, obj.y, obj.w, obj.h);
                break;
            case 'crate':
                drawRecordCrate(obj.x, obj.y, obj.w, obj.h);
                break;
            case 'microphone':
                drawMicrophone(obj.x, obj.y, obj.w, obj.h);
                break;
            default:
                // Simple representation for other objects
                ctx.fillStyle = obj.color;
                ctx.globalAlpha = discovered ? 1 : 0.7;
                ctx.fillRect(obj.x, obj.y, obj.w, obj.h);
                
                // Border
                ctx.globalAlpha = 1;
                ctx.strokeStyle = discovered ? obj.color : 'rgba(0, 255, 255, 0.3)';
                ctx.lineWidth = discovered ? 2 : 1;
                ctx.strokeRect(obj.x, obj.y, obj.w, obj.h);
                
                // Special glow
                if (isSpecial) {
                    ctx.shadowBlur = discovered ? 15 : 5;
                    ctx.shadowColor = '#f0f';
                    ctx.strokeStyle = '#f0f';
                    ctx.strokeRect(obj.x - 1, obj.y - 1, obj.w + 2, obj.h + 2);
                    ctx.shadowBlur = 0;
                }
        }
        
        ctx.restore();
    });
}

function drawMixer(x, y, w, h) {
    // Mixer body
    ctx.fillStyle = '#2a3a3a';
    ctx.fillRect(x, y, w, h);
    ctx.strokeStyle = '#0ff';
    ctx.lineWidth = 2;
    ctx.strokeRect(x, y, w, h);
    
    // Faders (vertical sliders)
    for (let i = 0; i < 6; i++) {
        const faderX = x + 10 + i * 23;
        const faderY = y + 15;
        
        // Slot
        ctx.fillStyle = '#000';
        ctx.fillRect(faderX, faderY, 8, 40);
        
        // Fader position (random heights for visual variety)
        const faderPos = faderY + 5 + (i * 6) % 30;
        ctx.fillStyle = '#0ff';
        ctx.fillRect(faderX - 2, faderPos, 12, 8);
    }
    
    // VU Meters
    ctx.fillStyle = '#000';
    ctx.fillRect(x + 10, y + 60, 130, 12);
    
    // VU meter bars (animated if playing)
    const vuLevel = GameState.phase === 'PLAYING' ? Math.random() * 100 : 20;
    const gradient = ctx.createLinearGradient(x + 10, 0, x + 140, 0);
    gradient.addColorStop(0, '#0ff');
    gradient.addColorStop(0.7, '#ff0');
    gradient.addColorStop(1, '#f00');
    ctx.fillStyle = gradient;
    ctx.fillRect(x + 10, y + 60, vuLevel * 1.3, 12);
    
    // Coffee ring stain
    ctx.strokeStyle = 'rgba(139, 69, 19, 0.3)';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(x + w - 20, y + 15, 10, 0, Math.PI * 2);
    ctx.stroke();
}

function drawTurntable(x, y, w, h) {
    // Turntable base
    ctx.fillStyle = '#1a1a1a';
    ctx.fillRect(x, y, w, h);
    ctx.strokeStyle = '#0ff';
    ctx.lineWidth = 2;
    ctx.strokeRect(x, y, w, h);
    
    // Platter
    ctx.fillStyle = '#000';
    ctx.beginPath();
    ctx.arc(x + w/2, y + h/2, 30, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#0ff';
    ctx.stroke();
    
    // Spindle
    ctx.fillStyle = '#0ff';
    ctx.fillRect(x + w/2 - 2, y + h/2 - 2, 4, 4);
    
    // Tonearm
    ctx.strokeStyle = '#888';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(x + w - 15, y + 10);
    ctx.lineTo(x + w/2 + 15, y + h/2 - 10);
    ctx.stroke();
    
    // Cartridge
    ctx.fillStyle = '#0ff';
    ctx.fillRect(x + w/2 + 13, y + h/2 - 12, 6, 6);
    
    // Record if playing
    if (GameState.phase === 'PLAYING') {
        ctx.strokeStyle = '#f0f';
        for (let r = 20; r < 30; r += 3) {
            ctx.beginPath();
            ctx.arc(x + w/2, y + h/2, r, 0, Math.PI * 2);
            ctx.stroke();
        }
    }
}

function drawPhone(x, y, w, h) {
    // Phone base
    ctx.fillStyle = '#2a2a2a';
    ctx.fillRect(x, y, w, h);
    ctx.strokeStyle = '#f0f';
    ctx.lineWidth = 2;
    ctx.strokeRect(x, y, w, h);
    
    // Rotary dial
    ctx.beginPath();
    ctx.arc(x + w/2, y + h/2 + 5, 18, 0, Math.PI * 2);
    ctx.stroke();
    
    // Finger holes
    for (let i = 0; i < 10; i++) {
        const angle = (i * 36 - 90) * Math.PI / 180;
        const holeX = x + w/2 + Math.cos(angle) * 12;
        const holeY = y + h/2 + 5 + Math.sin(angle) * 12;
        ctx.fillStyle = '#000';
        ctx.fillRect(holeX - 2, holeY - 2, 4, 4);
    }
    
    // Handset
    ctx.fillStyle = '#333';
    ctx.fillRect(x + 5, y - 15, 50, 10);
    ctx.strokeStyle = '#f0f';
    ctx.strokeRect(x + 5, y - 15, 50, 10);
    
    // Blinking light when caller waiting
    if (GameState.currentCaller && Math.floor(Date.now() / 500) % 2 === 0) {
        ctx.fillStyle = '#f0f';
        ctx.shadowBlur = 10;
        ctx.shadowColor = '#f0f';
        ctx.fillRect(x + w - 10, y + 5, 6, 6);
        ctx.shadowBlur = 0;
    }
}

function drawRecordCrate(x, y, w, h) {
    // Crate body
    ctx.fillStyle = '#654321';
    ctx.fillRect(x, y, w, h);
    ctx.strokeStyle = '#0ff';
    ctx.lineWidth = 2;
    ctx.strokeRect(x, y, w, h);
    
    // Wooden slats
    for (let i = 0; i < 4; i++) {
        ctx.strokeStyle = '#3a2010';
        ctx.beginPath();
        ctx.moveTo(x, y + i * 25);
        ctx.lineTo(x + w, y + i * 25);
        ctx.stroke();
    }
    
    // Records visible
    for (let i = 0; i < 12; i++) {
        const recordX = x + 8 + i * 6;
        const recordY = y + 5;
        const used = GameState.usedRecords.size > i;
        
        ctx.fillStyle = used ? '#333' : (i % 2 === 0 ? '#f0f' : '#0ff');
        ctx.fillRect(recordX, recordY, 4, 85);
    }
}

function drawMicrophone(x, y, w, h) {
    // Mic stand
    ctx.fillStyle = '#444';
    ctx.fillRect(x + w/2 - 2, y + 20, 4, h - 20);
    
    // Mic body
    ctx.fillStyle = '#0ff';
    ctx.fillRect(x, y, w, 25);
    ctx.strokeStyle = '#0ff';
    ctx.lineWidth = 2;
    ctx.strokeRect(x, y, w, 25);
    
    // Grille lines
    ctx.strokeStyle = '#000';
    ctx.lineWidth = 1;
    for (let i = 0; i < 5; i++) {
        ctx.beginPath();
        ctx.moveTo(x + 3, y + 5 + i * 4);
        ctx.lineTo(x + w - 3, y + 5 + i * 4);
        ctx.stroke();
    }
    
    // Glow if active
    if (GameState.phase === 'DIALOGUE') {
        ctx.shadowBlur = 15;
        ctx.shadowColor = '#0ff';
        ctx.strokeRect(x - 2, y - 2, w + 4, 29);
        ctx.shadowBlur = 0;
    }
}

function drawListenerMap(x, y, w, h) {
    // Map background
    ctx.fillStyle = 'rgba(0, 0, 0, 0.8)';
    ctx.fillRect(x, y, w, h);
    ctx.strokeStyle = '#0ff';
    ctx.lineWidth = 1;
    ctx.strokeRect(x, y, w, h);
    
    // Title
    ctx.fillStyle = '#0ff';
    ctx.font = '8px monospace';
    ctx.fillText('LISTENERS', x + 3, y + 8);
    
    // Grid (100x100 scaled down)
    const gridSize = 36;
    const gridX = x + (w - gridSize) / 2;
    const gridY = y + 12;
    
    ctx.fillStyle = '#001a1a';
    ctx.fillRect(gridX, gridY, gridSize, gridSize);
    
    // Draw listener pixels
    GameState.listeners.forEach(listener => {
        const px = gridX + (listener.x / 100) * gridSize;
        const py = gridY + (listener.y / 100) * gridSize;
        
        // Glow effect
        const alpha = 0.6 + Math.sin(Date.now() / 500 + listener.x) * 0.4;
        ctx.fillStyle = `rgba(0, 255, 255, ${alpha})`;
        ctx.fillRect(Math.floor(px), Math.floor(py), 2, 2);
    });
    
    // Grid lines (subtle)
    ctx.strokeStyle = 'rgba(0, 255, 255, 0.1)';
    ctx.lineWidth = 1;
    for (let i = 0; i <= 4; i++) {
        const offset = (i * gridSize) / 4;
        ctx.beginPath();
        ctx.moveTo(gridX + offset, gridY);
        ctx.lineTo(gridX + offset, gridY + gridSize);
        ctx.stroke();
        
        ctx.beginPath();
        ctx.moveTo(gridX, gridY + offset);
        ctx.lineTo(gridX + gridSize, gridY + offset);
        ctx.stroke();
    }
}

// =============================================================================
// GAME LOGIC
// =============================================================================

function initGame() {
    // Initialize audio context on user interaction
    document.getElementById('start-btn').addEventListener('click', () => {
        if (!GameState.audioContext) {
            GameState.audioContext = new (window.AudioContext || window.webkitAudioContext)();
        }
        if (GameState.audioContext.state === 'suspended') {
            GameState.audioContext.resume();
        }
        
        startGame();
    });
    
    // Canvas interaction
    canvas.addEventListener('click', handleCanvasClick);
    
    // UI buttons
    document.getElementById('select-record-btn').addEventListener('click', showRecordSelection);
    document.getElementById('station-id-btn').addEventListener('click', playStationID);
    document.getElementById('cancel-selection-btn').addEventListener('click', hideRecordSelection);
    document.getElementById('restart-btn').addEventListener('click', () => location.reload());
    
    // Initialize data
    GameState.records = [...RECORDS_DATA];
    GameState.availableCallers = shuffle([...CALLERS_DATA]).slice(0, 15);
    
    // Initialize listeners
    for (let i = 0; i < 5; i++) {
        addListener();
    }
    
    // Build record grid
    buildRecordGrid();
    
    // Start render loop
    requestAnimationFrame(renderLoop);
}

function startGame() {
    // Hide landing, show game
    document.getElementById('landing-page').style.display = 'none';
    document.getElementById('game-container').classList.add('active');
    
    GameState.phase = 'INTRO';
    
    // Show intro dialogue
    showDialogue({
        name: "STATION MANAGER",
        text: "Alright. Last night. Keep it professional, play some hits, hand over the keys at sunrise. The board's made up their minds. Just make it through the night."
    });
    
    setTimeout(() => {
        hideDialogue();
        GameState.phase = 'WAITING';
        startGameLoop();
        scheduleNextCaller(5);
    }, 5000);
}

function startGameLoop() {
    setInterval(() => {
        if (GameState.phase === 'WAITING' || GameState.phase === 'DIALOGUE' || GameState.phase === 'SELECTING') {
            updateGameTime();
        }
    }, 100);
}

function updateGameTime() {
    GameState.gameTime += 0.1;
    
    // Update hour
    const newHour = Math.min(Math.floor(GameState.gameTime / GameState.timePerHour) + 1, 12);
    if (newHour !== GameState.hour) {
        GameState.hour = newHour;
        updateUI();
    }
    
    // Drop transmitter
    const dropPerTick = (100 / 12) / (GameState.timePerHour * 10);
    GameState.transmitterPower = Math.max(0, GameState.transmitterPower - dropPerTick);
    updateUI();
    
    // Update listeners
    GameState.listeners.forEach(l => {
        l.duration += 0.1;
        GameState.totalListenerSeconds += 0.1;
    });
    
    // Check end conditions
    if (GameState.hour >= 12 && GameState.gameTime >= GameState.timePerHour * 12) {
        endGame('SUNRISE');
    } else if (GameState.transmitterPower <= 0) {
        endGame('SIGNAL_LOST');
    }
}

function updateUI() {
    document.getElementById('hour-display').textContent = GameState.hour;
    document.getElementById('listener-display').textContent = GameState.listeners.length;
    document.getElementById('records-display').textContent = 12 - GameState.usedRecords.size;
    document.getElementById('transmitter-fill').style.height = GameState.transmitterPower + '%';
}

// =============================================================================
// CALLER SYSTEM
// =============================================================================

function scheduleNextCaller(delay = 10) {
    if (GameState.phase === 'GAME_OVER') return;
    
    setTimeout(() => {
        if (GameState.phase === 'WAITING') {
            triggerCall();
        } else {
            scheduleNextCaller(5);
        }
    }, delay * 1000);
}

function triggerCall() {
    const available = GameState.availableCallers.filter(c => 
        !c.called && c.minHour <= GameState.hour
    );
    
    if (available.length === 0) {
        scheduleNextCaller(8);
        return;
    }
    
    const caller = available[Math.floor(Math.random() * available.length)];
    caller.called = true;
    GameState.currentCaller = caller;
    GameState.callsAnswered++;
    
    showDialogue(caller);
    GameState.phase = 'DIALOGUE';
}

function showDialogue(entity) {
    document.getElementById('caller-name').textContent = entity.name.toUpperCase();
    document.getElementById('dialogue-text').textContent = entity.text;
    document.getElementById('dialogue-box').classList.add('visible');
}

function hideDialogue() {
    document.getElementById('dialogue-box').classList.remove('visible');
}

// =============================================================================
// RECORD SELECTION
// =============================================================================

function buildRecordGrid() {
    const grid = document.getElementById('record-grid');
    grid.innerHTML = '';
    
    GameState.records.forEach(record => {
        const card = document.createElement('div');
        card.className = 'record-card';
        card.dataset.id = record.id;
        
        card.innerHTML = `
            <div class="record-title">${record.title}</div>
            <div class="record-tags">
                <span class="tag genre">${record.genre}</span>
                <span class="tag mood">${record.mood}</span>
                <span class="tag era">${record.era}</span>
            </div>
        `;
        
        card.addEventListener('click', () => selectRecord(record));
        grid.appendChild(card);
    });
}

function showRecordSelection() {
    if (GameState.phase !== 'DIALOGUE') return;
    GameState.phase = 'SELECTING';
    document.getElementById('record-selection').classList.add('visible');
}

function hideRecordSelection() {
    document.getElementById('record-selection').classList.remove('visible');
    if (GameState.currentCaller) {
        GameState.phase = 'DIALOGUE';
    }
}

function selectRecord(record) {
    if (GameState.usedRecords.has(record.id)) return;
    
    GameState.usedRecords.add(record.id);
    
    // Mark as used
    const card = document.querySelector(`[data-id="${record.id}"]`);
    card.classList.add('used');
    
    hideRecordSelection();
    hideDialogue();
    playRecord(record);
}

function playRecord(record) {
    GameState.phase = 'PLAYING';
    const caller = GameState.currentCaller;
    
    // Calculate match
    let score = 0;
    if (record.genre === caller.needs.genre) score++;
    if (record.mood === caller.needs.mood) score++;
    if (record.era === caller.needs.era) score++;
    
    // Special Sarah handling
    if (caller.special === 'sarah' && record.special === 'sarah' &&
        GameState.discoveredObjects.has('sarah_photo')) {
        score = 3;
    }
    
    let response, listenerChange;
    
    if (score === 3) {
        response = caller.responses.perfect;
        listenerChange = 2;
        GameState.perfectMatches.push({
            caller: caller.name,
            song: record.title,
            response: response
        });
    } else if (score >= 2) {
        response = caller.responses.good;
        listenerChange = 0;
        GameState.goodMatches.push({ caller: caller.name, song: record.title });
    } else {
        response = caller.responses.poor;
        listenerChange = -1;
    }
    
    // Boost transmitter if upbeat
    if (record.mood === 'Upbeat') {
        GameState.transmitterPower = Math.min(100, GameState.transmitterPower + 10);
    }
    
    updateUI();
    
    // Show response
    setTimeout(() => {
        showResponse(caller.name, response, record.title, score);
        updateListeners(listenerChange);
        
        setTimeout(() => {
            hideDialogue();
            GameState.phase = 'WAITING';
            scheduleNextCaller(8);
        }, 4000);
    }, 2000);
}

function showResponse(callerName, response, songTitle, score) {
    const symbol = score === 3 ? '✓' : score >= 2 ? '○' : '✗';
    document.getElementById('caller-name').innerHTML = `${callerName.toUpperCase()} [${symbol}]`;
    document.getElementById('dialogue-text').innerHTML = `
        <div style="color: #f0f; margin-bottom: 12px;">♪ ${songTitle} ♪</div>
        <div>${response}</div>
    `;
    document.querySelector('.dialogue-actions').style.display = 'none';
    document.getElementById('dialogue-box').classList.add('visible');
    
    setTimeout(() => {
        document.querySelector('.dialogue-actions').style.display = 'flex';
    }, 4000);
}

function playStationID() {
    GameState.transmitterPower = Math.min(100, GameState.transmitterPower + 5);
    updateUI();
    hideDialogue();
    GameState.phase = 'WAITING';
    scheduleNextCaller(6);
}

// =============================================================================
// LISTENER MANAGEMENT
// =============================================================================

function addListener() {
    GameState.listeners.push({
        x: Math.random() * 100,
        y: Math.random() * 100,
        duration: 0
    });
    updateUI();
}

function removeListener() {
    if (GameState.listeners.length > 0) {
        GameState.listeners.pop();
        updateUI();
    }
}

function updateListeners(change) {
    if (change > 0) {
        for (let i = 0; i < change; i++) addListener();
    } else if (change < 0) {
        for (let i = 0; i < Math.abs(change); i++) removeListener();
    }
}

// =============================================================================
// BOOTH INTERACTION
// =============================================================================

function handleCanvasClick(e) {
    if (GameState.phase !== 'WAITING') return;
    
    const rect = canvas.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / canvasScale);
    const y = ((e.clientY - rect.top) / canvasScale);
    
    for (const obj of BOOTH_OBJECTS) {
        if (x >= obj.x && x <= obj.x + obj.w && 
            y >= obj.y && y <= obj.y + obj.h) {
            showObjectStory(obj);
            if (obj.special) {
                GameState.discoveredObjects.add(obj.special);
            }
            break;
        }
    }
}

function showObjectStory(obj) {
    showDialogue({
        name: "MEMORY",
        text: obj.story
    });
    
    setTimeout(() => {
        hideDialogue();
    }, 3000);
}

// =============================================================================
// GAME OVER
// =============================================================================

function endGame(reason) {
    GameState.phase = 'GAME_OVER';
    
    document.getElementById('ending-title').textContent = 
        reason === 'SUNRISE' ? 'SUNRISE' : 'SIGNAL LOST';
    
    document.getElementById('final-listeners').textContent = GameState.listeners.length;
    document.getElementById('total-calls').textContent = GameState.callsAnswered;
    document.getElementById('perfect-count').textContent = GameState.perfectMatches.length;
    document.getElementById('listener-hours').textContent = 
        Math.floor(GameState.totalListenerSeconds / 60);
    
    // Memory wall
    const memoryList = document.getElementById('memory-list');
    if (GameState.perfectMatches.length > 0) {
        memoryList.innerHTML = '';
        GameState.perfectMatches.forEach(match => {
            const item = document.createElement('div');
            item.className = 'memory-item';
            item.innerHTML = `
                <div class="memory-caller">${match.caller}</div>
                <div class="memory-response">"${match.response}"</div>
            `;
            memoryList.appendChild(item);
        });
        
        // Special Sarah ending
        if (GameState.perfectMatches.some(m => m.caller === 'Sarah')) {
            const special = document.createElement('div');
            special.style.textAlign = 'center';
            special.style.marginTop = '25px';
            special.style.fontSize = '20px';
            special.style.color = '#f0f';
            special.style.fontWeight = 'bold';
            special.textContent = '★ YOU KEPT THE MORNING SHOW ALIVE ★';
            memoryList.appendChild(special);
        }
    } else {
        memoryList.innerHTML = '<p style="text-align: center; color: #0ff; opacity: 0.6;">No perfect connections were made tonight.</p>';
    }
    
    document.getElementById('game-over').classList.add('visible');
}

// =============================================================================
// RENDER LOOP
// =============================================================================

function renderLoop() {
    if (GameState.phase !== 'LANDING') {
        renderBooth();
    }
    requestAnimationFrame(renderLoop);
}

// =============================================================================
// UTILITIES
// =============================================================================

function shuffle(arr) {
    const shuffled = [...arr];
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    return shuffled;
}

// =============================================================================
// INITIALIZE
// =============================================================================

window.addEventListener('load', () => {
    initCanvas();
    initGame();
});
