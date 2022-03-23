$(document).ready(function (e) {
    $('.submit').on('click', function (e) {
        e.preventDefault();

console.log($('input.send').val())

        val = $("input.send").val()
        console.log(val)

        $.ajax({
            url: '/vancauwenberghe_send',
            type: 'POST',
            data: JSON.stringify({"val": val}),
            contentType: 'application/json',
            async: false,
            success: function (msg) {
                alert("La mise a bien été envoyée au serveur !");
            }
        })
    })
});