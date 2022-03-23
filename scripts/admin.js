$(document).ready(function (e) {
    $('.submit').on('click', function (e) {
        e.preventDefault();

console.log($('input.send').val())

        $.ajax({
            url: '/vancauwenberghe_send',
            type: 'POST',
            data: {"val": $("input.send").val()},
            contentType: 'application/json',
            async: false,
            success: function (msg) {
                alert(msg);
            }
        })
    })
});