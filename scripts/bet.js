$(document).ready(function (e) {
    global = parseInt(document.getElementById('val').textContent)
    val = parseInt(document.getElementById('val').textContent)
    $('input.sync').on('input', function (event) {
        qt = 0;

        origin = $(this);

        $('input.sync').each(function(i, obj) {
            qt += parseInt($(this).val())
        })
        val = global - qt;
        document.getElementById('val').textContent = val;
    });

    $('.submit').on('click', function(e) {
        e.preventDefault();

        $.ajax({
            url: '/send',
            type: 'POST',
            data: JSON.stringify(findJson()),
            contentType: 'application/json',
            dataType: 'json',
            async: false,
            success: function (msg) {
                alert(msg);
            }
        })

        alert("La mise a bien été envoyée !")
    })
});

function findJson() {
    numbers = [];
    $('input.number').each(function(i, obj) {
        numbers[i] = $(this).val();
    })
    colors = [];
    $('input.color').each(function(i, obj) {
        colors[i] = $(this).val();
    })
    return {
        "money": val,
        "numbers": numbers,
        "colors": colors
    }
}