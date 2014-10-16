var selector = '#barchart';
var width = 1024;
var height = 768;

var filename = 'data/data.csv';
loadFile(filename);


function loadFile(filename) {
    d3.csv(filename, function(data) {
	data = data.splice(0, 100).map(function(d) {
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

    var yScale = d3.scale.linear()
            .domain([0, d3.max(data, function(d) { return d.value; })])
            .range([0, height]);

    var svg = d3.select(selector)
	    .append("svg")
	    .attr("width", width)
	    .attr("height", height);

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
	});
    
}