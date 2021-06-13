// https://observablehq.com/@mbostock/hello-cola@68
export default function define(runtime, observer) {
  const main = runtime.module();
  main.variable(observer()).define(["md"], function(md){return(
md`# Hello, CoLa!

This network of character co-occurence in _Les Misérables_ is positioned by constraint-based optimization using [WebCoLa](https://ialab.it.monash.edu/webcola/). Compare to [d3-force](/@mbostock/d3-force-directed-graph).`
)});
  main.variable(observer("chart")).define("chart", ["data","d3","DOM","width","height","cola","color","invalidation"], function(data,d3,DOM,width,height,cola,color,invalidation)
{
  const nodes = data.nodes.map(d => Object.create(d));
  const index = new Map(nodes.map(d => [d.id, d]));
  const links = data.links.map(d => Object.assign(Object.create(d), {
    source: index.get(d.source),
    target: index.get(d.target)
  }));

  const svg = d3.select(DOM.svg(width, height));

  const layout = cola.d3adaptor(d3)
      .size([width, height])
      .nodes(nodes)
      .links(links)
      .jaccardLinkLengths(40, 0.7)
      .start(30);
  
  const link = svg.append("g")
      .attr("stroke", "#999")
      .attr("stroke-opacity", 0.6)
    .selectAll("line")
    .data(links)
    .enter().append("line")
      .attr("stroke-width", d => Math.sqrt(d.value));

  const node = svg.append("g")
      .attr("stroke", "#fff")
      .attr("stroke-width", 1.5)
    .selectAll("circle")
    .data(nodes)
    .enter().append("circle")
      .attr("r", 5)
      .attr("fill", d => color(d.group))
      .call(layout.drag);

  node.append("title")
      .text(d => d.id);

  layout.on("tick", () => {
    link
        .attr("x1", d => d.source.x)
        .attr("y1", d => d.source.y)
        .attr("x2", d => d.target.x)
        .attr("y2", d => d.target.y);

    node
        .attr("cx", d => d.x)
        .attr("cy", d => d.y);
  });

  invalidation.then(() => layout.stop());

  return svg.node();
}
);
  main.variable(observer("color")).define("color", ["d3"], function(d3){return(
d3.scaleOrdinal(d3.schemeCategory10)
)});
  main.variable(observer("height")).define("height", function(){return(
500
)});
  main.variable(observer("data")).define("data", ["d3"], function(d3){return(
d3.json("https://gist.githubusercontent.com/mbostock/4062045/raw/5916d145c8c048a6e3086915a6be464467391c62/miserables.json")
)});
  main.variable(observer("cola")).define("cola", ["require"], function(require){return(
require("webcola@3/WebCola/cola.min.js")
)});
  main.variable(observer("d3")).define("d3", ["require"], function(require){return(
require("d3@5")
)});
  return main;
}
