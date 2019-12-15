$(document).ready(function () {
    $("#pretrazi").keyup(function () {
        var value = $("#pretrazi");
        value = value.val().toLowerCase();
        $("#celatabela tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });

    $("a").click(function (e) {
        var value = $(this)
        value = value.text().toLowerCase();
        $("#celatabela tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });

});

