function make_chart(data){
    var users = $.map(data, function(x){return x.user});
    var comments = $.map(data, function(x){return x.comments});

    var chart_canvas = $("#chart").get(0).getContext("2d");
    var my_chart = new Chart(chart_canvas);

    var grid_color = "#EEE";
    var font_color = "#EEE";
    Chart.defaults.global.responsive = true;
    Chart.defaults.global.scaleFontColor = font_color;
    Chart.defaults.global.scaleLineColor = grid_color;

    var bar_options = {
        barShowStroke: false,
        scaleShowGridLines: false
    }


    var chart_data = {
        labels: users,
        datasets: [{
            label: "Comments",
            data: comments,
            fillColor: "#EEE",
            strokeColor: "#000"
        }],
    }

    my_chart.Bar(chart_data, bar_options);
}

function poll_results_chart(data){
    var choices = $.map(data, function(x){return x.choice});
    var votes = $.map(data, function(x){return x.votes});

    var chart_canvas = $("#chart").get(0).getContext("2d");
    var my_chart = new Chart(chart_canvas);

    var grid_color = "#EEE";
    var font_color = "#EEE";
    Chart.defaults.global.responsive = true;
    Chart.defaults.global.scaleFontColor = font_color;
    Chart.defaults.global.scaleLineColor = grid_color;

    var bar_options = {
        barShowStroke: false,
        scaleShowGridLines: false
    }


    var chart_data = {
        labels: choices,
        datasets: [{
            label: "Comments",
            data: votes,
            fillColor: "#EEE",
            strokeColor: "#000"
        }],
    }

    my_chart.Bar(chart_data, bar_options);
}
$(document).ready(function(){
    $.get("/top_commenters/",
        function(data){
            make_chart(data);
        })
});

