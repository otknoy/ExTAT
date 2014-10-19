var selector = '#barchart';

var filename = 'data/hiki_tf.csv';
loadFile(filename);


function loadFile(filename) {
    d3.csv(filename, function(data) {
	data = data.splice(0, 100).map(function(d) {
	    return {
		label: d.word,
		value: parseInt(d.count)
	    };
	});

	createBarChart('#barchart', data);
	createBarChart('#test', data);
    });
}

function createBarChart(selector, data) {
    var width = 300;
    var height = 1024;
    var barHeight = 20;
    var barPadding = 1;
    var labelHeight = 24;
    var labelPadding = 2;

    var xScale = d3.scale.sqrt()
            .domain([0, d3.max(data, function(d) { return d.value; })])
            .range([0, width]);

    var svg = d3.select(selector)
	    .append("svg")
	    .attr("width", width)
	    .attr("height", height);

    // bar
    svg.selectAll("rect")
	.data(data)
	.enter()
	.append("rect")
	.attr("x", 0)
	.attr("y", function(d, i) {
	    return i * (barHeight + barPadding);
	})
	.attr("width", function(d) {
	    return xScale(d.value);
	})
	.attr("height", barHeight)
	.attr("fill", "teal");

    // text label
    svg.selectAll("text.label")
	.data(data)
	.enter()
	.append("text")
	.attr("class", "label")
	.text(function(d) { return d.label; })
	.attr("font-size", barHeight*0.75)
	.attr("fill", "white")
	.attr("x", labelPadding)
	.attr("y", function(d, i) {
	    return i * (barHeight + barPadding) + (barHeight / 2);
	}).
	attr({
	    "text-anchor": "text-before-edge",
	    "dominant-baseline": "middle"
	});

    // value label
    svg.selectAll("text.value")
	.data(data)
	.enter()
	.append("text")
	.attr("class", "value")
	.text(function(d) { return d.value; })
	.attr("fill", "white")
	.attr({
	    "text-anchor": "text-before-edge",
	    "dominant-baseline": "text-before-edge"
	})
	.attr("x", function(d, i) {
	    return height - xScale(d.value);
	})
	.attr("y", function(d, i) {
	    return i * (width / data.length);

	});

}