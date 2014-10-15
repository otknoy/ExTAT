var selector = '#wordcloud';
var width = 1024;
var height = 768;

var filename = 'data/data.csv';

d3.csv(filename, function(data){
    data = data.splice(0, 1000);
    var wordcount = data.map(function(d) {
	return {
	    text: d.word,
	    size: d.count
	};
    });

    var fontSizeScale = d3.scale.pow()
	    // .domain([0, d3.max(wordcount, function(d) { return d.size; })])
	    .domain([0, 28])
	    .range([0, 128]);

    var svg = d3.select(selector).append("svg")
	    .attr("width", width)
	    .attr("height", height);
    var vis = svg.append("g")
	    .attr("transform", "translate(" + [width >> 1, height >> 1] + ")");

    var layout = d3.layout.cloud()
	    .size([width, height])
            .words(wordcount)
            .padding(5)
	    .rotate(function() { return 0;})
	    // .rotate(function() { return ~~(Math.random() * 2) * 90; })
            .font("Impact")
            .fontSize(function(d) { return fontSizeScale(d.size); })
	    .on("word", progress)
            .on("end", draw)
	    .start();


    function progress(data) {
	console.log(progress);
    }

    function draw(words) {
	var fill = d3.scale.category20();

        vis.selectAll("text")
            .data(words)
            .enter()
            .append("text")
            .style({
		"font-size": function(d) { return d.size + "px"; },
		"font-family": "Impact",
		"fill": function(d, i) { return fill(i); }
            })
            .attr({
		"text-anchor": "middle",
		"transform": function(d) { return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")"; }
            })
            .text(function(d) { return d.text; });
    }
});

