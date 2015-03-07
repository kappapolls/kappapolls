function make_map(data){
    var width = 768;
    var height = 500;

    var img_small = {
        'x': 10,
        'y': 15
    }

    var img_large = {
        'x': 21,
        'y': 29
    }
    
    //we dont need antarctica
    data.features = $.grep(data.features, function(x, i){
        return x.properties.continent != 'Antarctica' &&
               x.properties.continent != 'Seven seas (open ocean)';});

    //color by continent
    continents = $.unique($.map(data.features, function(x, i){
        return x.properties.continent}));

    var continent_colors = d3.scale.ordinal()
        .domain(['Asia', 'Africa', 'Europe', 'South America', 'Oceania', 'North America'])
        .range(['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#bcbd22']);

    var projection = d3.geo.equirectangular().scale(1).translate([0, 0]);
    var path = d3.geo.path().projection(projection);

    var mymap = d3.select("#map")
        .attr("width", width)
        .attr("height", height)

    var bounds = path.bounds(data)
    var s = 0.95 / Math.max( (bounds[1][0] - bounds[0][0]) / width, 
                             (bounds[1][1] - bounds[0][1]) / height)

    var t = [(width - s * (bounds[1][0] + bounds[0][0])) / 2,
             (height - s * (bounds[1][1] + bounds[0][1])) / 2]

    //s = 500;
    //t = [400, 400];


    projection
        .scale(s)
        .translate(t)

    mymap.append("g")
        .attr("class", "tracts").attr("fill", "#202020")
        .selectAll("path")
        .data(data.features)
        .enter().append("path")
        .attr("d", path)
        //.attr("fill-opacity", 0.5)
        .attr("fill", function(d){return continent_colors(d.properties.continent)})
        .attr("stroke", function(d){return continent_colors(d.properties.continent)}); 

    var div = d3.select("body").append("div")
        .attr("class", "tooltip")
        .style("opacity", 1e-6)
        .style("z-index", 10000);

    function mouseoverfunction(d, elem){
        //move g to the top
        elem.parentNode.appendChild(elem);

        div.style("left", (d3.event.pageX + 10) + "px")
            .style("top", (d3.event.pageY + 10) + "px")
            .style("border", "1px solid white")
            .transition()
            .duration(500)
            .style("opacity", 1);

        var div_text = '';
        for(var i=0; i<d.sponsorships.length; i++){
            sponsorship = d.sponsorships[i]

            div_text += "<b>Player: </b>" + sponsorship.player + "<br/>";
            div_text += "<b>Event: </b>" + sponsorship["event"] + "<br/>";
            div_text += "<b>Result: </b>" + 
                        (sponsorship.result==0? "TBD": sponsorship.result) + 
                        "<br/>";

            if(d.sponsorships.length > 1){
                div_text += "<br/>";
            }
        }

        div.html(div_text);
        
    }

    function mouseout(){
        div.transition()
            .duration(500)
            .style("opacity", 1e-6);
    }

    //plot evo
    mymap.selectAll("g .kreygasm")
        .data(all_locations)
        .enter().append("g")
        .attr("transform", function(d){
            return "translate(" + 
                projection(d.coords) + 
                ")"}
                )
        .attr("class", "kreygasm")
        .append("image")
            .attr("width", img_large.x)
            .attr("height", img_large.y)
            .attr("xlink:href", "/static/polls/imgs/kreygasm.png")
            .attr("x", -10)
            .attr("y", -15)
            .on("mouseover", function(d){return mouseoverfunction(d, this.parentNode)})
            .on("mouseout", mouseout);

}



$(document).ready(function(){
    $.get("/static/polls/worldmap.json",
        function(data){
            make_map(data);
        });
});
