// Scripts for event handling

// BUG - on first load, nothing loads. need to click something. but when
// i add it at the beginning, the functions have not returned yet and is too early

// Function gets called once page load has succeeded
$(document).ready(function() {
    // Load default set of countries
    $.get("/loadcountries")
    .done(function(string){
        let countries = Object.values(JSON.parse(string));
        $('#select-countries').empty();
        $.each(countries, function(i, p) {
            $('#select-countries').append($('<option></option>').val(p).html(p));
        });
        // Load first dataset
        $.post("/loaddata", 
            {"country": $("#select-countries").val(),
            "state": $("#select-states").val(),
            "datatype": $("#select-metric").val()
            })
        .done(function(string) {
            let input = Array(JSON.parse(string))[0];  
            myChart.data.labels = input.index; //dates
            myChart.data.datasets[0].data = input.data;
            myChart.update();
        });
    }),
    // Load default set of US states
    $.get("/loadusstates")
    .done(function(string){
        let states = Object.values(JSON.parse(string));
        $('#select-states').empty();
        $.each(states, function(i,p) {
            $('#select-states').append($('<option></option>').val(p).html(p));
        });
    }),
    // Hide the states by default
    $('#select-states').hide()
    $('#select-state-label').hide()



    // Set up event handler for clicking on load country
  $("#select-countries").change(function(e) {
    $.post("/loaddata", 
        {"country": $("#select-countries").val(),
        "state": $("#select-states").val(),
        "datatype": $("#select-metric").val()
        })
     .done(function(string) {
        let input = Array(JSON.parse(string))[0];  
        myChart.data.labels = input.index; //dates
        myChart.data.datasets[0].data = input.data;
        myChart.update();
        });
    // if US, show state, else not
    if ($("#select-countries").val() == "US") {
        $('#select-states').show()
        $('#select-state-label').show()
    }
    else {
        $('#select-states').hide()
        $('#select-state-label').hide()
    }

    e.preventDefault();
    }),

    // Same for load state
    $("#select-states").change(function(e) {
        $.post("/loaddata", 
            {"country": $("#select-countries").val(),
            "state": $("#select-states").val(),
            "datatype": $("#select-metric").val()})
         .done(function(string) {
            let input = Array(JSON.parse(string))[0];  
            myChart.data.labels = input.index; //dates
            myChart.data.datasets[0].data = input.data;
            myChart.update();
            });
    e.preventDefault();
    }),

    // Same for change datatype
    $("#select-metric").change(function(e) {
        $.post("/loaddata", 
            {"country": $("#select-countries").val(),
            "state": $("#select-states").val(),
            "datatype": $("#select-metric").val()})
         .done(function(string) {
            let input = Array(JSON.parse(string))[0]; 
            myChart.data.labels = input.index; //dates
            myChart.data.datasets[0].data = input.data;
            myChart.update();
            });
    e.preventDefault();
    }),

    $("#inc-y-scale").click(function(){
        mySession.yScale = mySession.yScale*2;
        myChart.options.scales.yAxes[0].ticks.max = parseInt(mySession.yScale);
        myChart.update();
    });

    $("#dec-y-scale").click(function(){
        mySession.yScale = mySession.yScale/2;
        myChart.options.scales.yAxes[0].ticks.max = parseInt(mySession.yScale);
        myChart.update();
    });


});

class sessionClass {
    constructor(){
        this.resetData();
    }

    resetData(){
        this.yScale = 100; // y axis scale default
    }
}
