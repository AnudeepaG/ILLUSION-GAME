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
        // Set a funky background color with random RGB values
        background(random(255), random(255), random(255));

        // Loop through the canvas in a grid pattern
        for (let x = 0; x < width; x += 50) {
            for (let y = 0; y < height; y += 50) {
                // Randomize the color for each shape
                fill(random(255), random(255), random(255));

                // Randomly select a shape to draw
                let shapeType = random(['circle', 'rectangle', 'triangle', 'line', 'arc']);

                // Draw the selected shape
                if (shapeType === 'circle') {
                    // Draw a circle
                    ellipse(x, y, random(10, 30), random(10, 30));
                } else if (shapeType === 'rectangle') {
                    // Draw a rectangle
                    rect(x, y, random(10, 30), random(10, 30));
                } else if (shapeType === 'triangle') {
                    // Draw a triangle
                    let x1 = x + random(-10, 10);
                    let y1 = y + random(-10, 10);
                    let x2 = x + random(-10, 10);
                    let y2 = y + random(-10, 10);
                    let x3 = x + random(-10, 10);
                    let y3 = y + random(-10, 10);
                    triangle(x1, y1, x2, y2, x3, y3);
                } else if (shapeType === 'line') {
                    // Draw a line
                    let x2 = x + random(10, 50);
                    let y2 = y + random(10, 50);
                    line(x, y, x2, y2);
                } else if (shapeType === 'arc') {
                    // Draw an arc
                    let arcStart = random(TWO_PI);
                    let arcEnd = arcStart + random(PI);
                    arc(x, y, random(10, 30), random(10, 30), arcStart, arcEnd);
                }
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
