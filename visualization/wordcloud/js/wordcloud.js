var selector = '#wordcloud';
var width = 1024;
var height = 768;

var layout = d3.layout.cloud()
	.timeInterval(10)
	.size([width, height])
	.padding(5)
	.rotate(function() { return ~~(Math.random() * 2) * 90; })
	.font("Impact")
	.fontSize(function(d) { return d.size; })
	.on("word", progress)
	.on("end", draw);

var svg = d3.select(selector).append("svg")
    .attr("width", width)
    .attr("height", height);
// var background = svg.append("g");
var vis = svg.append("g")
	.attr("transform", "translate(" + [width >> 1, height >> 1] + ")");

var filename = 'data/data.csv';
loadFile(filename);


function progress(data) {
    // console.log(data);
}

function draw(data, bounds) {
    var fill = d3.scale.category20();

    vis.selectAll("text")
	.data(data)
	.enter()
	.append("text")
	.style({
	    "font-size": function(d) { return d.size + "px"; },
	    "font-family": "Impact",
	    "fill": function(d, i) { return fill(i); }
	})
	.attr({
	    "text-anchor": "middle",
	    "transform": function(d) { return "translate(" + [d.x, d.y] + ") rotate(" + d.rotate + ")"; }
	})
	.text(function(d) { return d.text; });
}

function loadFile(filename) {
    d3.csv(filename, function(data) {
	data = data.splice(0, 500);
	var words = data.map(function(d) {
	    return {
		text: d.word,
		size: 3*Math.pow(d.count, 1.2)
	    };
	});
	layout.stop().words(words).start();
    });
}