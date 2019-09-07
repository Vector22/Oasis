(function () {
    if (window.myBookmarklet !== undefined) {
        myBookmarklet();
    }
    else {
        document.body.appendChild(document.createElement('script')).src = 'https://d7182ac6.ngrok.io/static/js/bookmarklet.js?r=' + Math.floor(Math.random() * 999999999);
    }
})();