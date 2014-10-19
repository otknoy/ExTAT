
var dataset = {
    "graphTitle": "test",
    "dataNames": ["test1", "test2", "test3"],
    "attributes": ["hoge", "hige", "hugo", "huge"],
    "matrix": [[1, 3, 5],
	       [3, 3, 2],
	       [4, 1, 0]]
};

$(document).ready(function() {
    var selector = '#barchart';
    createMultiBarChart(selector, dataset);
});


function createMultiBarChart(selector, dataset) {
    var width = 1024;
    var height = 360;
    var barPadding = 1;
    var labelHeight = 24;
    var labelPadding = 2;

    var yScale = d3.scale.linear()
            .domain([0, d3.max(dataset, function(d) { return d.value; })])
            .range([0, height - labelHeight]);

    var svg = d3.select(selector)
	    .append("svg")
	    .attr("width", width)
	    .attr("height", height);

    // text label
    svg.selectAll("text")
	.data(dataset.attributes)
	.enter()
	.append("text")
	.text(function(d) { return d; })
	.attr("fill", "black")
	.attr({
	    "dominant-baseline": "text-after-edge"
	})
	.attr("x", function(d, i) {
	    return i * width/dataset.attributes.length;
	})
	.attr("y", height);

    // bar
    function transpote(matrix) {
	return matrix[0].map(function(col, i) {
	    return matrix.map(function(row) {
		return row[i];
	    });
	});
    }

    var mT = transpote(dataset.matrix);
    var barGroups = svg.selectAll("g")
	    .data(mT)
	    .enter()
	    .append("g")
	    .selectAll("rect")
	    .data(function(d, i) { return d; })
	    .enter()
	    .append("rect")
	    .attr("x", function(d, i) {
		return i * width/mT.length;
	    })
    	    .attr("y", 0)
	    .attr("width", 20)
	    .attr("height", height);
    for (var i = 0; i < barGroups.length; i++) {
	console.log(barGroups[i]);
	barGroups[i].append("rect")
	    .attr("x", function(d, i) {
		return i * 21;
	    })
	    .attr("y", 0)
	    .attr("width", 5)
	    .attr("height", function(d, i) {
		return 10 * d;
	    })
    	    .attr("fill", "teal");
    }
    
    
    svg.selectAll("rect")
    	.data()
    	.enter()
    	.append("rect")
	.attr("x", function(d, i) {
	    return i * width/dataset.matrix.length;
	})
	.attr("y", 0)
	.attr("width", 20)
	.attr("height", function(d, i) {
	    return 10 * d3.sum(d);
	})
    	.attr("fill", "teal");

}