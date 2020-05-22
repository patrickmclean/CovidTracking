// Scripts for event handling

// Function gets called at the end of page load
$(document).ready(function() {
    // Load default set of countries
    $.get("/loadcountry")
    .done(function(string){
        let countries = Object.values(JSON.parse(string));
        $('#select-countries').empty();
        $.each(countries, function(i, p) {
            $('#select-countries').append($('<option></option>').val(p).html(p));
        });
    }),

    // Set up event handler for clicking on load country
  $("#select-countries").change(function(e) {
    $.post("/loaddata", {"country": $("#select-countries").val()})
     .done(function(string) {
        let input = Array(JSON.parse(string))[0];  // This is a little overwraught with array parsing, but 
        data = input.data;                         // it was what I could get to work
        dates = input.index;
        length = input.index.length;
        myChart.data.labels = dates;
        myChart.data.datasets[0].data = data;
        myChart.update();
        });
    e.preventDefault();
    }),

    $("#y-scale-values").change(function(e) {
        myChart.options.scales.yAxes[0].ticks.max = parseInt(e.currentTarget.value);
        myChart.update();
    })
});
