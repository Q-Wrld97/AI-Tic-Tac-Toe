function makeMove(position) {
    // Get the selected AI type from the radio buttons
    var aiType = document.querySelector('input[name="ai_type"]:checked').value;
    
    // Send a POST request to the server to make a move
    fetch("/make_move", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: "position=" + position + "&ai_type=" + aiType
    })
    .then(response => response.text())
    .then(data => {
        // Update the HTML content with the response data
        document.documentElement.innerHTML = data;
        
        // Show or hide the reset button based on the winner message
        var resetButton = document.getElementById("reset-button");
        var winnerMessage = document.querySelector(".winner").textContent;
        if (winnerMessage !== "") {
            resetButton.style.display = "block";
        } else {
            resetButton.style.display = "none";
        }
    });
}

function resetGame() {
    // Get the selected AI type from the radio buttons
    var aiType = document.querySelector('input[name="ai_type"]:checked').value;
    
    // Send a POST request to the server to reset the game
    fetch('/reset_game', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `ai_type=${aiType}`
    })
    .then(response => response.text())
    .then(data => {
        // Update the HTML content with the response data
        document.documentElement.innerHTML = data;
        
        // Hide the reset button
        var resetButton = document.querySelector(".reset-btn");
        resetButton.style.display = "none";
        
    });
}
