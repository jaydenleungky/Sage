
    // Add an event listener to capture Enter key press on inputs
    document.querySelector('.login-form').addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            // Trigger form submission when Enter is pressed
            document.querySelector('.login-form button').click();
        }
    });

