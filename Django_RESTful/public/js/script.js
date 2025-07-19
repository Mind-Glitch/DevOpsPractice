console.log("what?")
const button = document.getElementById("main_button");

button.addEventListener('click', function(event) {
    button.innerText = Number.parseInt(button.innerText) + 1;
})

fetch('/data', {
    "method": 'GET'
}).then(x=>x.text().then(t =>
    document.getElementById('root').innerText = t
))