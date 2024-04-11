// // variables for time
// const hoursElement = document.getElementById('hours');
// const minutesElement = document.getElementById('minutes');
// const secondsElement = document.getElementById('seconds');

// // variables for buttons
// const startBtn = document.getElementById('startBtn');
// const stopBtn = document.getElementById('stopBtn');
// const resetBtn = document.getElementById('resetBtn');

// let timerInterval;
// let totalSeconds = 0;

// // function for start button
// function startTimer() {
//     timerInterval = setInterval(updateTimer, 1000);
// }

// // function for stop button
// function stopTimer() {
//     clearInterval(timerInterval);
// }

// // function for reset button
// function resetTimer() {
//     stopTimer();
//     totalSeconds = 0;
//     updateTimer();
// }

// function updateTimer() {
//     const hours = Math.floor(totalSeconds / 3600);
//     const minutes = Math.floor((totalSeconds % 3600) / 60);
//     const seconds = totalSeconds % 60;

//     hoursElement.textContent = padZero(hours);
//     minutesElement.textContent = padZero(minutes);
//     secondsElement.textContent = padZero(seconds);

//     totalSeconds++;
// }

// function padZero(value) {
//     return String(value).padStart(2, '0');
// }

// startBtn.addEventListener('click', startTimer);
// stopBtn.addEventListener('click', stopTimer);
// resetBtn.addEventListener('click', resetTimer);
// Get the necessary DOM elements
const hoursDisplay = document.getElementById('hours'); // Element to display hours
const minutesDisplay = document.getElementById('minutes'); // Element to display minutes
const secondsDisplay = document.getElementById('seconds'); // Element to display seconds
const startBtn = document.getElementById('startBtn'); // Start button
const stopBtn = document.getElementById('stopBtn'); // Stop button
const resetBtn = document.getElementById('resetBtn'); // Reset button

let timer; // Variable to store the setInterval function

// Function to start the stopwatch
function startTimer() {
    let hours = 0;
    let minutes = 0;
    let seconds = 0;

    timer = setInterval(() => {
        seconds++;

        // Update the display with the new time values
        secondsDisplay.textContent = padNumber(seconds % 60);
        minutesDisplay.textContent = padNumber(parseInt(seconds / 60, 10) % 60);
        hoursDisplay.textContent = padNumber(parseInt(seconds / 3600, 10));

    }, 1000); // Update the time every second
}

// Function to stop the stopwatch
function stopTimer() {
    clearInterval(timer); // Clear the setInterval function
}

// Function to reset the stopwatch
function resetTimer() {
    stopTimer(); // Stop the stopwatch
    secondsDisplay.textContent = '00'; // Reset seconds display
    minutesDisplay.textContent = '00'; // Reset minutes display
    hoursDisplay.textContent = '00'; // Reset hours display
}

// Function to pad single-digit numbers with leading zeros
function padNumber(num) {
    return num < 10 ? `0${num}` : num;
}

// Event listeners for the buttons
startBtn.addEventListener('click', startTimer); // Start button
stopBtn.addEventListener('click', stopTimer); // Stop button
resetBtn.addEventListener('click', resetTimer); // Reset button
