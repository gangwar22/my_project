// Your JavaScript code here
let searchButton = document.getElementById("search-button");
let searchBar = document.getElementById("search-bar");
let audioPlayer = document.getElementById("audioPlayer");
let image=document.getElementById("imagecircles")// Corrected the ID

searchButton.addEventListener("click", function () {
    let songName = searchBar.value;
    let url = `https://deezerdevs-deezer.p.rapidapi.com/search?q=${songName}`;

    let options = {
        method: 'GET',
        headers: {
            'X-RapidAPI-Key': 'a30104380cmsh9540154b3e422e6p1bbe00jsn7f0be4b7b67a',
            'X-RapidAPI-Host': 'deezerdevs-deezer.p.rapidapi.com'
        }
    };

    fetch(url, options)
        .then(response => response.json())
        .then(value => {
            if (value.data.length !== 0) {
                const obj = value.data[0]; // Assuming you want to display information about the first result
                document.getElementById("title").innerHTML = obj.title;
                document.getElementById("name").innerHTML = obj.artist.name;
                document.getElementById('audiosource').src = obj.preview;
                document.getElementById("imagecircle").src = obj.album.cover_medium;
                // console.log(obj);

            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
});
let audios = document.getElementById("audios")
function playPause() {
    if (audios.paused) {
        audios.load();
        audios.play();
    } else {
        audios.pause();
    }
}



