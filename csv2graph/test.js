// Append a simple d3.js thing to the #graph element

// width and height can get pulled out of the DOM
var width=600,
    height=400,
    margin = {"top": 20, "right": 20, "bottom": 20, "left": 20},
    graph_width = width - (margin.right + margin.left),
    graph_height = height - (margin.top + margin.bottom);

var graph = d3.select("#graph").append("svg")
                .attr("width", graph_width)
                .attr("height", graph_height)
              .append("g")
                .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var data = [
    {"id": 1, "x": 100, "y": 100, "color": "green"},
    {"id": 2, "x": 150, "y": 150, "color": "red"},
    {"id": 3, "x": 200, "y": 200, "color": "purple"}
];

function drawgraph() {

    graph.selectAll(".circle")
        .data(data, (d) => {d.id})
      .enter().append("circle")
        .attr("class", "circle")
        .attr("r", 10)
        .attr("cx", (d, i) => {return d.x})
        .attr("cy", (d, i) => {return d.y})
        .attr("fill", (d, i) => {return d.color});

        // .attr("class", "rect")
        // .attr("x", (d, i) => {return d.y})
        // .attr("y", (d, i) => {return d.y})
        // .attr("height", 10)
        // .attr("width", 10)
        // .attr("fill", (d, i) => {return d.color});
}
