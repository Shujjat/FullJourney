function displayLightbox(content) {
    // Create lightbox div
    let lightbox = document.createElement('div');
    lightbox.id = 'lightbox';
    lightbox.style.display = 'flex';
    lightbox.style.justifyContent = 'center';
    lightbox.style.alignItems = 'center';
    lightbox.style.position = 'fixed';
    lightbox.style.top = '0';
    lightbox.style.bottom = '0';
    lightbox.style.left = '0';
    lightbox.style.right = '0';
    lightbox.style.backgroundColor = 'rgba(0, 0, 0, 0.7)';
    lightbox.style.zIndex = '9999';

    // Create content div
    let contentDiv = document.createElement('div');
    contentDiv.style.backgroundColor = '#fff';
    contentDiv.style.padding = '20px';
    contentDiv.style.borderRadius = '15px';

    // Check if content is a URL
    if (content.startsWith('http')) {
        // Create video element
        let video = document.createElement('video');
        video.src = content;
        video.controls = true;
        video.style.width = '100%';
        video.style.height = 'auto';

        // Add video to content
        contentDiv.appendChild(video);

        // Calculate video duration
        video.onloadedmetadata = function() {
            let duration = video.duration;
            let minutes = Math.floor(duration / 60);
            let seconds = Math.floor(duration % 60);
            let durationText = document.createTextNode(minutes + ' min ' + seconds + ' sec');
            contentDiv.appendChild(durationText);
        };
    } else {
        // Add HTML content
        contentDiv.innerHTML = content;
    }

    // Create buttons
    let closeButton = document.createElement('button');
    closeButton.textContent = 'Close';
    closeButton.onclick = function() {
        lightbox.style.display = 'none';
    };

    let expandButton = document.createElement('button');
    expandButton.textContent = 'Expand';
    expandButton.onclick = function() {
        contentDiv.style.width = '100%';
        contentDiv.style.height = '100%';
    };

    let minimizeButton = document.createElement('button');
    minimizeButton.textContent = 'Minimize';
    minimizeButton.onclick = function() {
        contentDiv.style.width = '50%';
        contentDiv.style.height = '50%';
    };

    // Add buttons to content
    contentDiv.appendChild(closeButton);
    contentDiv.appendChild(expandButton);
    contentDiv.appendChild(minimizeButton);

    // Add content to lightbox
    lightbox.appendChild(contentDiv);

    // Add lightbox to body
    document.body.appendChild(lightbox);
}