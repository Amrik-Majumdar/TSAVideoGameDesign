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
    { id: "sarah_photo", x: 500, y: 70, w: 40, h: 40, 
      story: "Sarah, 1982. She said she'd wait for the morning show.", 
      special: "sarah_photo", color: "#f0f" },
    { id: "coffee", x: 150, y: 300, w: 30, h: 30, 
      story: "Cold coffee from six hours ago. You've stopped tasting it.", 
      color: "#0f0" },
    { id: "playlist", x: 220, y: 90, w: 45, h: 35, 
      story: "Tomorrow's playlist. You won't need it.", 
      color: "#ff0" },
    { id: "drawing", x: 420, y: 180, w: 50, h: 40, 
      story: "Your daughter drew you at the station. You're smiling.", 
      color: "#0ff" },
    { id: "old_mic", x: 280, y: 230, w: 35, h: 55, 
      story: "The microphone from your first broadcast, 1975.", 
      color: "#f80" }
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
    grad.addColorStop(1, '#000');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, 640, 480);
    
    // Walls
    ctx.fillStyle = '#0a1a1a';
    ctx.fillRect(80, 50, 480, 320);
    
    // Window
    ctx.fillStyle = '#000033';
    ctx.fillRect(420, 80, 120, 100);
    
    // City lights
    ctx.fillStyle = '#0ff';
    for (let i = 0; i < 40; i++) {
        const x = 425 + Math.random() * 110;
        const y = 85 + Math.random() * 90;
        const brightness = 0.3 + Math.random() * 0.7;
        ctx.globalAlpha = brightness;
        ctx.fillRect(x, y, 2, 2);
    }
    ctx.globalAlpha = 1;
    
    // Desk
    ctx.fillStyle = '#1a2a2a';
    ctx.fillRect(100, 300, 440, 100);
    
    // Soundboard
    ctx.fillStyle = '#2a3a3a';
    ctx.fillRect(130, 320, 180, 60);
    
    // Soundboard details
    ctx.fillStyle = '#0ff';
    for (let i = 0; i < 8; i++) {
        ctx.fillRect(140 + i * 20, 330, 8, 30);
    }
    ctx.fillStyle = '#f0f';
    for (let i = 0; i < 6; i++) {
        ctx.fillRect(145 + i * 25, 365, 3, 10);
    }
    
    // Microphone stand
    ctx.fillStyle = '#3a4a4a';
    ctx.fillRect(340, 280, 40, 80);
    
    // Microphone
    ctx.fillStyle = '#0ff';
    ctx.fillRect(345, 260, 30, 30);
    ctx.strokeStyle = '#0ff';
    ctx.lineWidth = 2;
    ctx.strokeRect(345, 260, 30, 30);
    
    // Record shelves
    ctx.fillStyle = '#0a0a0a';
    for (let i = 0; i < 3; i++) {
        ctx.fillRect(90, 80 + i * 70, 100, 50);
    }
    
    // Records on shelves
    for (let row = 0; row < 3; row++) {
        for (let col = 0; col < 8; col++) {
            const used = GameState.usedRecords.size > (row * 8 + col);
            ctx.fillStyle = used ? '#333' : (col % 2 === 0 ? '#f0f' : '#0ff');
            ctx.fillRect(95 + col * 11, 85 + row * 70, 9, 40);
        }
    }
    
    // Phone
    ctx.fillStyle = '#2a2a2a';
    ctx.fillRect(450, 320, 60, 40);
    ctx.strokeStyle = '#0ff';
    ctx.lineWidth = 2;
    ctx.strokeRect(450, 320, 60, 40);
    
    // Draw clickable objects
    drawObjects();
    
    // Grid overlay (subtle)
    ctx.strokeStyle = 'rgba(0, 255, 255, 0.05)';
    ctx.lineWidth = 1;
    for (let x = 0; x < 640; x += 80) {
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, 480);
        ctx.stroke();
    }
    for (let y = 0; y < 480; y += 60) {
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(640, y);
        ctx.stroke();
    }
}

function drawObjects() {
    BOOTH_OBJECTS.forEach(obj => {
        const discovered = GameState.discoveredObjects.has(obj.special);
        
        ctx.fillStyle = obj.color;
        ctx.globalAlpha = discovered ? 1 : 0.6;
        ctx.fillRect(obj.x, obj.y, obj.w, obj.h);
        
        if (discovered) {
            ctx.shadowBlur = 10;
            ctx.shadowColor = obj.color;
            ctx.strokeStyle = obj.color;
            ctx.lineWidth = 2;
            ctx.strokeRect(obj.x - 2, obj.y - 2, obj.w + 4, obj.h + 4);
            ctx.shadowBlur = 0;
        } else {
            ctx.strokeStyle = 'rgba(0, 255, 255, 0.3)';
            ctx.lineWidth = 1;
            ctx.strokeRect(obj.x, obj.y, obj.w, obj.h);
        }
        
        ctx.globalAlpha = 1;
    });
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
