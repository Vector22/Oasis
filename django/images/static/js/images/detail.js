$(document).ready(function () {
    $('a.like').click(function (e) {
        e.preventDefault();
        $.post('/images/like/', {
            id: $(this).data('id'),
            action: $(this).data('action')
        },
            function (data) {
                if (data['status'] == 'ok') {
                    let previous_action = $('a.like').data('action');
                    // toggle data-action
                    $('a.like').data('action', previous_action == 'like' ?
                        'unlike' : 'like');
                    // toggle link text
                    $('a.like').text(previous_action == 'like' ? 'Unlike' :
                        'Like');
                    // update total likes
                    let previous_likes = parseInt($('button.count .total').text());
                    $('button.count .total').text(previous_action == 'like' ?
                        previous_likes + 1 : previous_likes - 1);
                }
            }
        );
    });
});