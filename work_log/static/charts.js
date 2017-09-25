$( document ).ready(function() {
    var data = {
        labels: ['1', '5', '10', '15', '20', '25', '30'],
        datasets: [
            {
                label: "Site Registrations in the Last 30 Days",
                fillColor: "rgba(220,220,220,0.2)",
                strokeColor: "rgba(220,220,220,1)",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: {{ 30_day_registrations }}
            }
        ]
    };
    var ctx = document.getElementById("myChart").getContext("2d");
    var myLineChart = new Chart(ctx).Line(data);
});