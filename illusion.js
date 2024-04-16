let canvas;
let isRunning = true; // Initially, the illusion is running

function setup() {
    // Create a canvas that fills the browser window
    canvas = createCanvas(windowWidth, windowHeight);
    canvas.position(0, 0);
    canvas.style('z-index', -1); // Set the z-index so it doesn't overlap with other content
}

function draw() {
    // Only draw the illusion if it is running
    if (isRunning) {
        // Clear the canvas
        clear();

        // Draw some shapes
        for (let x = 0; x < width; x += 50) {
            for (let y = 0; y < height; y += 50) {
                fill(random(255), random(255), random(255)); // Random colors
                ellipse(x, y, 20, 20); // Draw circles
            }
        }
    }
}

// Function to toggle the illusion on and off
function toggleIllusion() {
    isRunning = !isRunning;
}

// Resize the canvas when the window is resized
function windowResized() {
    resizeCanvas(windowWidth, windowHeight);
}
