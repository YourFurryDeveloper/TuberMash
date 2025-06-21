const tuber1 = document.getElementById("tuberContainer1");
const tuber2 = document.getElementById("tuberContainer2");

let oldIndex = 0;
let curTuber1 = 0;
let curTuber2 = 0;

function getRandomFixed(max, exclude) {
    let random;
    do {
        random = Math.floor(Math.random() * (max - 1 + 1)) + 0;
    } while (random === exclude);
    return random;
}

function getNewTuber(tuberNumToChange, tubers) {
    let tubersLen = Object.keys(tubers).length;
    let newIndex = 0;

    if (tuberNumToChange === "1") {
        newIndex = getRandomFixed(tubersLen, curTuber2);
        curTuber1 = newIndex;
    } else if (tuberNumToChange === "2") {
        newIndex = getRandomFixed(tubersLen, curTuber1);
        curTuber2 = newIndex;
    }

    oldIndex = newIndex;

    const newTuberImg = Object.values(tubers)[newIndex];
    const newTuberName = Object.keys(tubers)[newIndex];

    document.getElementById(`tuberContainer${tuberNumToChange}`).style = `background-image: url('${newTuberImg}');`;
    document.getElementById(`tuber${tuberNumToChange}name`).innerHTML = newTuberName;
}

tuber1.addEventListener("click", function() {
    fetch('./channels.json')
    .then(response => response.json())
    .then(data => getNewTuber("2", data))
    .catch(error => console.error('Error fetching JSON:', error));
});

tuber2.addEventListener("click", function() {
    fetch('./channels.json')
    .then(response => response.json())
    .then(data => getNewTuber("1", data))
    .catch(error => console.error('Error fetching JSON:', error));
});

document.addEventListener("keydown", function(event) {
    if (event.key === "ArrowLeft") {
        fetch('./channels.json')
        .then(response => response.json())
        .then(data => getNewTuber("2", data))
        .catch(error => console.error('Error fetching JSON:', error));
    } else if (event.key === "ArrowRight") {
        fetch('./channels.json')
        .then(response => response.json())
        .then(data => getNewTuber("1", data))
        .catch(error => console.error('Error fetching JSON:', error));
    }
});
