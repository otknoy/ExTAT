var selector = '#barchart';

var filename = 'data/data.csv';
loadFile(filename);


function loadFile(filename) {
    d3.csv(filename, function(data) {
	data = data.splice(0, 50).map(function(d) {
	    return {
		label: d.word,
		value: parseInt(d.count)
	    };
	});

	createBarChart(data);
    });
}

function createBarChart(data) {
    var width = 1024;
    var height = 360;
    var barPadding = 1;
    var labelHeight = 24;
    var labelPadding = 2;

    var yScale = d3.scale.linear()
            .domain([0, d3.max(data, function(d) { return d.value; })])
            .range([0, height - labelHeight]);

    var svg = d3.select(selector)
	    .append("svg")
	    .attr("width", width)
	    .attr("height", height);

    // bar
    svg.selectAll("rect")
	.data(data)
	.enter()
	.append("rect")
	.attr("x", function(d, i) {
	    return i * (width / data.length);
	})
	.attr("y", function(d, i) {
	    return height - yScale(d.value);
	})
	.attr("width", width / data.length - barPadding)
	.attr("height", function(d) {
	    return yScale(d.value);
	})
	.attr("fill", "teal");

    // label
    svg.selectAll("text")
	.data(data)
	.enter()
	.append("text")
	.text(function(d) {
	    return d.label;
	})
	.attr("fill", "white")
        .attr({
	    "dominant-baseline": "middle",
	    "transform": function(d, i) {
		var translate = "translate(" + [(i+0.5) * (width / data.length), height-labelPadding] + ")";
		var rotate = "rotate(" + -90 + ")";
		return translate + " " + rotate;
	    }
	});
}