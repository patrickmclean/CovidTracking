// Scripts for click handling

// Load the covid data
$(document).ready(function() {
  $("#load-data").click(function(e) {
    $.post("/loaddata", {"country": $("input[name='country']").val()})
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
    });
});
  
function changeScale() {
    myChart.options.scales.yAxes[0].ticks.max = parseInt(document.getElementById("y-scale-values").value);
    myChart.update();
}
  