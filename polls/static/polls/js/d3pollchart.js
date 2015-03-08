function wrap(text, width) {
      text.each(function() {
              var text = d3.select(this),
              words = text.text().split(/\s+/).reverse(),
              word,
              line = [],
              lineNumber = 0,
              lineHeight = 1.1, // ems
              y = text.attr("y"),
              dy = parseFloat(text.attr("dy")),
              tspan = text.text(null).append("tspan").attr("x", 0).attr("y", y).attr("dy", dy + "em");
          while (word = words.pop()) {
                    line.push(word);
                          tspan.text(line.join(" "));
                                if (tspan.node().getComputedTextLength() > width) {
                                            line.pop();
                                                    tspan.text(line.join(" "));
                                                            line = [word];
                                                                    tspan = text.append("tspan").attr("x", 0).attr("y", y).attr("dy", ++lineNumber * lineHeight + dy + "em").text(word);
                                                                          }
                                    }
            });
}

function make_chart(data){

    //sort the data
    data.sort(function(a, b){return b.votes - a.votes});
    
    var margin = {top: 20,
                  right: 30,
                  bottom: 30,
                  left: 100}
    var width = 550 - margin.left - margin.right;
    var height = (70 * data.length) - margin.top - margin.bottom;

    var barHeight = height / data.length;
    var vote_max = d3.max(data, function(d){return d.votes;})

    var x = d3.scale.linear()
        .range([0, width])
        .domain([0, vote_max]);

    var y = d3.scale.ordinal()
        .domain($.map(data, function(d){return d.choice}))
        .rangeBands([0, height]);

    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left");

    var chart = d3.select("#chart")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
      .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top +")");


    var bar = chart.selectAll("g")
        .data(data)
        .enter().append("g")
        .attr("class", "poll-bars")
        .attr("transform", 
                function(d){return "translate(0," + y(d.choice)  + ")";});

    bar.append("rect")
        .attr("width", 0)
        .transition().duration(750)
        .attr("width", function(d){return x(d.votes)})
        .attr("height", barHeight - 20);

    bar.append("text")
        .attr("x", 0)
        .transition().duration(750)
        .attr("x", function(d){return x(d.votes) - 3;})
        .attr("y", (barHeight - 20) / 2)
        .attr("dy", ".35em")
        .text(function(d){ return d.votes;});

    chart.append("g")
        .attr("class", "y axis")
        .attr("transform", "translate(0,-10)")
        .call(yAxis)
        .selectAll(".tick text")
        .call(wrap, y.rangeBand())
        .selectAll(".tick tspan")
        .attr("x", "-10");

    //kappa
    kreygasm_width = 21;
    kreygasm_height= 29;

    chart.select(".poll-bars")
        .each(function(d){
            if(d.votes == vote_max){
                d3.select(this).append("image")
                .attr("xlink:href", "/static/polls/imgs/kreygasm.png")
                .attr("height", kreygasm_height)
                .attr("width", kreygasm_width)
                .attr("x", 0)
                .transition().duration(750)
                .attr("x", x(d.votes) - kreygasm_width - 20)
                .attr("y", (barHeight - 20 - kreygasm_height) / 2);
            }
        });
}

$(document).ready(function(){
    var poll_thread_id = $("#thread_id").text();

    var margin = {top: 20,
                  right: 30,
                  bottom: 30,
                  left: 100}
    var width = 550 - margin.left - margin.right;

    var height = (70 * 5) - margin.top - margin.bottom;

    var chart = d3.select("#chart")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom);

    $.get("/poll/" + poll_thread_id + "/results/",
        function(data){
            make_chart(data);
        })
});
