var messageBox = document.getElementById("messages");
var close = document.querySelector('.close');

if (close) {
    close.addEventListener('click', function () {
        var toRemove = document.getElementById("message-item");
        toRemove.parentNode.removeChild(toRemove);
        console.log('Closing the message box.');
    });
} else {
    console.log('Nothing to remove yet...');
}

// if (node.parentNode) {
//     node.parentNode.removeChild(node);
// }