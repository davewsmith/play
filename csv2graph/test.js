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
    {"key": 1, "x": 100, "y": 100, "color": "green"},
    {"key": 2, "x": 150, "y": 150, "color": "red"},
    {"key": 3, "x": 200, "y": 200, "color": "purple"}
];

function drawgraph() {

    var circles = graph.selectAll(".circle")
        .data(data, (d) => {return d.key.toString()});

    console.log("update: " + circles.size());
    console.log("exit  : " + circles.exit().size());

    circles.exit().each((d) => {console.log("exiting key " + d.key)});

    circles
      .exit().transition()
        .attr("r", 0)
        .remove();

    console.log("enter : " + circles.enter().size());
    // console.log("to merge: " + circles.merge().size());

    circles
      .enter().append("circle")
        .attr("class", "circle")
        .attr("r", 0)
        .attr("cx", (d, i) => {return d.x})
        .attr("cy", (d, i) => {return d.y})
        .attr("fill", (d, i) => {return d.color})
      .transition()
        .attr("r", 10)
        .attr("fill", "gray");
}

var interval;

function animategraph() {
    drawgraph();

    interval = setInterval(() => {
        // console.log("data pre: " + data[0].key + " to " + data[data.length -1].key);
        data.shift();
        data.push({
            "key": data[data.length - 1].key + 1,
            "x": d3.randomInt(graph_width)(),
            "y": d3.randomInt(graph_height)(),
            "color": "red"
        });
        // console.log("data post: " + data[0].key + " to " + data[data.length -1].key);
        drawgraph();
    }, 5 * 1000);
}
