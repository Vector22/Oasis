(function () {
    if (window.myBookmarklet !== undefined) {
        myBookmarklet();
    }
    else {
        document.body.appendChild(document.createElement('script')).src = 'https://vector-oasis-bucket.s3.amazonaws.com/static/js/bookmarklet.js?r=' + Math.floor(Math.random() * 999999999);
    }
})();