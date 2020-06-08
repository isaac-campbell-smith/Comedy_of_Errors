let get_inputs = function() {
    let x = $("input#x").val()
    let y = $("input#y").val()
    return {'x': parseInt(x),
            'y': parseInt(y)} 
};

let send_inputs_json = function(inputs) {
    $.ajax({
        url: '/solve',
        contentType: "application/json; charset=utf-8",
        type: 'POST',
        success: function (data) {
            display_solutions(data);
        },
        data: JSON.stringify(inputs)
    });
};

let display_solutions = function(solutions) {
    $("span#solution").html(solutions.lcm)
};


$(document).ready(function() {

    $("button#solve").click(function() {
        let coefficients = get_inputs());
        send_inputs_json(inputs);
    })

})


