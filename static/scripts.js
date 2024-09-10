document.addEventListener('DOMContentLoaded', () => {
    const recommendationsBtn = document.getElementById('get-recommendations');
    const recommendationsList = document.getElementById('recommendations-list');

    recommendationsBtn.addEventListener('click', () => {
        fetch('/recommendations')
            .then(response => response.json())
            .then(data => {
                recommendationsList.innerHTML = '';
                if (data.error) {
                    recommendationsList.innerHTML = `<p>${data.error}</p>`;
                } else {
                    data.forEach(track => {
                        const card = document.createElement('div');
                        card.classList.add('recommendation-card');
                        card.innerHTML = `
                            <img src="${track.album_cover}" alt="${track.name}">
                            <strong>${track.name}</strong>
                            <p>by ${track.artist}</p>
                        `;
                        recommendationsList.appendChild(card);
                    });
                }
            })
            .catch(error => {
                recommendationsList.innerHTML = `<p>Failed to load recommendations. Please try again later.</p>`;
                console.error('Error fetching recommendations:', error);
            });
    });
});
