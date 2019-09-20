(function () {
    if (window.myBookmarklet !== undefined) {
        myBookmarklet();
    }
    else {
        document.body.appendChild(document.createElement('script')).src = 'https://5d325d16.ngrok.io/static/js/bookmarklet.js?r=' + Math.floor(Math.random() * 999999999);
    }
})();