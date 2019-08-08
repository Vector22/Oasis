let messageBox = document.getElementById("messages");
let close = document.querySelector(".close");

close.addEventListener('Click', function (e) {
    e.preventDefault();
    console.log('One click !');
    messageBox.removeChild(document.getElementById('switch'));
});