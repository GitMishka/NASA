document.addEventListener('DOMContentLoaded', function() {
    fetch('http://127.0.0.1:5000/apod')
        .then(response => response.json())
        .then(data => {
            document.getElementById('apod-image').src = data.hdurl;
            document.getElementById('apod-title').innerText = data.title;
            document.getElementById('apod-description').innerText = data.explanation;
        })
        .catch(error => console.error('Error:', error));
});
