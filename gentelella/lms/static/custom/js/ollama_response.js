// ollama_response.js

document.addEventListener('DOMContentLoaded', function () {
    const userInput = document.getElementById('userinput');
    const details = document.getElementById('details');

    userInput.addEventListener('change', function () {
        const text = userInput.value;

        // Function to retrieve CSRF token from cookies
        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Search for the CSRF token cookie
                    if (cookie.startsWith(name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        // Retrieve CSRF token and include it in headers
        const csrftoken = getCookie('csrftoken');

        fetch("", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrftoken, // Include CSRF token in headers
            },
            body: new URLSearchParams({
                'text': text
            })
        })
        .then(response => response.json())
        .then(data => {

            details_value=data.response.response
            details_length=details_value.length

            threshold=299
            let escapedDetails = details_value.replace(/'/g, "\\'").replace(/"/g, '\\"'); // Escape single and double quotes

            if (escapedDetails.length > threshold)
            {
                let shortenedContent = escapedDetails.substr(0, threshold) + '<i>...more</i></br >';

                // Display shortened content with ellipsis
                details.innerHTML = shortenedContent;

                // Add click event listener to ellipsis
                details.addEventListener('click', function() {
                    // Remove ellipsis and show full content in lightbox
                    displayLightbox(escapedDetails);
                });
        }
        else
        {

            details.innerHTML = escapedDetails;
        }



        })
        .catch(error => {
            details.innerHTML = 'Error: ' + error;
        });
    });
});
