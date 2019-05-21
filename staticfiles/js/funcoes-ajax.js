function utilizouHoraExtra(id) {
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/hora-extra/utilizar_hora_extra/' + id,
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result) {
            console.log(result)
            $("#mensagem").text(result.mensagem);
            $("#total_horas").text(result.total_horas);
        }
    });
}

function desmarcaUtilizouHoraExtra(id) {
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/hora-extra/desmarca_utilizar_hora_extra/' + id,
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result) {
            console.log(result)
            $("#mensagem").text(result.mensagem);
            $("#total_horas").text(result.total_horas);
        }
    });
}