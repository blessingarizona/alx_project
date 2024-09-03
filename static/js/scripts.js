document.addEventListener('DOMContentLoaded', function () {
    fetch('/recommendations')
        .then(response => response.json())
        .then(data => {
            const recommendationsDiv = document.getElementById('recommendations');
            data.forEach(song => {
                const songElement = document.createElement('div');
                songElement.className = 'recommendation-item';

                songElement.innerHTML = `
                    <img src="${song.album_cover}" alt="Album Cover">
                    <div class="info">
                        <div class="name">${song.name}</div>
                        <div class="artist">${song.artist}</div>
                    </div>
                `;

                recommendationsDiv.appendChild(songElement);
            });
        });
});
