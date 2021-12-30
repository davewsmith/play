function setup() {
    const p = document.createElement('p');
    p.innerHTML = "Watch this space";
    document.body.appendChild(p);
}

document.addEventListener("DOMContentLoaded", function(event) {
    setup();
});

