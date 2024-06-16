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
    contentDiv.style.maxWidth = '80%'; // Adjust as needed
    contentDiv.style.maxHeight = '80%';
    contentDiv.style.overflowY = 'auto'; // Allow scrolling if content is too long

    // Set content as HTML directly
    contentDiv.innerHTML = content;

    // Create close button
    let closeButton = document.createElement('button');
    closeButton.textContent = 'Close';
    closeButton.onclick = function() {
        lightbox.style.display = 'none';
    };

    // Create expand button
    let expandButton = document.createElement('button');
    expandButton.textContent = 'Expand';
    expandButton.onclick = function() {
        contentDiv.style.width = '100%';
        contentDiv.style.height = '100%';
    };

    // Create minimize button
    let minimizeButton = document.createElement('button');
    minimizeButton.textContent = 'Minimize';
    minimizeButton.onclick = function() {
        contentDiv.style.width = '50%';
        contentDiv.style.height = '50%';
    };

    // Append buttons to content div
    contentDiv.appendChild(closeButton);
    contentDiv.appendChild(expandButton);
    contentDiv.appendChild(minimizeButton);

    // Append content div to lightbox
    lightbox.appendChild(contentDiv);

    // Add lightbox to body
    document.body.appendChild(lightbox);
}
