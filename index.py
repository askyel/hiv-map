#!/usr/bin/python
print "Content-type: text/html\n"
print """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<script src="http://d3js.org/d3.v3.min.js"></script>
<script src="http://d3js.org/d3.v4.min.js"></script>
<style type="text/css">

h1 {
  color: white;
}

/* On mouse hover, lighten state color */
path:hover {
	/* fill-opacity: 0.7; */
}

/* Style for Custom Tooltip */
div.tooltip {
 	position: absolute;
	text-align: center;
  width:auto;
  padding:4px;
	font: 12px sans-serif;
	background: black;
  color: white;
	border:1px solid grey;
	border-radius: 5px;
	pointer-events: none;
}

/* Legend Font Style */
body {
	font: 11px sans-serif;
  background-color: #222222;
  color: white;
  text-align: center;
  max-width: 1000px;
  margin-left: auto;
  margin-right: auto;
}

#menu {
  position: absolute;
  top: 200px;
  left: 150px;
  height: 50px;
  width: 125px;
}

#menu .option {
  /* float: left; */
  font-size: 12px;
  padding: 10px 20px;
  margin: 0px 10px;
  border: 1px solid white;
  color: white;
  /* background-color: #444; */
}

#menu .option:hover {
  background-color: #888888;
  /* color: #444; */
}

#menu .active {
  background-color: white;
  color: #222222;
}

#filters {
  position: absolute;
  top: 200px;
  right: 25px;
}

#filters table {
  border-collapse: collapse;
}

#filters th {
  padding-right: 10px;
}

#filters td {
  border: 1px solid white;
  padding: 10px;
}

#filters td:hover {
  background-color: #888888;
}

#filters td.active {
  background-color: white;
  color: #222222;
}

/* Legend Position Style */
#legend {
  /* text-align: right; */
}

#legend svg {
  margin-top: 50px;
}

#summary l {
  float: left;
  font-size: 15px;
  /* text-align: left; */
  margin-left: 40px;
}

#summary ol {
  text-align: left;
}

#footer {
  position: absolute;
  right: 20px;
  bottom: 20px;
  text-align: left;
}

#footer a {
  color: #888;
}

</style>
</head>
<body>

<h1>Rates of Adult HIV Infection in the United States</h1>

<div id="menu">
<div class="option" id="percentChangeRate" onClick="updateData('percentChangeRate', [])">% Change</div>
<div class="option" id="adultRate2017" onClick="updateData('adultRate2017', {})">2017</div>
<div class="option" id="adultRate2016" onClick="updateData('adultRate2016', {})">2016</div>
<div class="option" id="adultRate2015" onClick="updateData('adultRate2015', {})">2015</div>
<div class="option" id="adultRate2014" onClick="updateData('adultRate2014', {})">2014</div>
<div class="option" id="adultRate2013" onClick="updateData('adultRate2013', {})">2013</div>
<div class="option" id="adultRate2012" onClick="updateData('adultRate2012', {})">2012</div>
<div class="option" id="adultRate2011" onClick="updateData('adultRate2011', {})">2011</div>
<div class="option" id="adultRate2010" onClick="updateData('adultRate2010', {})">2010</div>
</div>

<div id="filters">
  <table>
    <tr>
      <th>Sex Education Mandated</th>
      <td id="sexEducationMandated:X" onClick="updateDataAddFilter('percentChangeRate', {'name':'sexEducationMandated', 'value':'X'})">True</td>
      <td id="sexEducationMandated:" onClick="updateDataAddFilter('percentChangeRate', {'name':'sexEducationMandated', 'value':''})">False</td>
    </tr>
    <tr>
      <th>HIV Education Mandated</th>
      <td id="hivEducationMandated:X" onClick="updateDataAddFilter('percentChangeRate', {'name':'hivEducationMandated', 'value':'X'})">True</td>
      <td id="hivEducationMandated:" onClick="updateDataAddFilter('percentChangeRate', {'name':'hivEducationMandated', 'value':''})">False</td>
    </tr>
    <tr>
      <th>Medically Accurate</th>
      <td id="educationMedicallyAccurate:X" onClick="updateDataAddFilter('percentChangeRate', {'name':'educationMedicallyAccurate', 'value':'X'})">True</td>
      <td id="educationMedicallyAccurate:" onClick="updateDataAddFilter('percentChangeRate', {'name':'educationMedicallyAccurate', 'value':''})">False</td>
    </tr>
    <tr>
      <th>Culturally Unbiased</th>
      <td id="educationUnbiased:X" onClick="updateDataAddFilter('percentChangeRate', {'name':'educationUnbiased', 'value':'X'})">True</td>
      <td id="educationUnbiased:" onClick="updateDataAddFilter('percentChangeRate', {'name':'educationUnbiased', 'value':''})">False</td>
    </tr>
    <tr>
      <th>Parental Notice</th>
      <td id="parentalNotice:X" onClick="updateDataAddFilter('percentChangeRate', {'name':'parentalNotice', 'value':'X'})">True</td>
      <td id="parentalNotice:" onClick="updateDataAddFilter('percentChangeRate', {'name':'parentalNotice', 'value':''})">False</td>
      <td id="parentalNotice:HIV" onClick="updateDataAddFilter('percentChangeRate', {'name':'parentalNotice', 'value':'HIV'})">HIV Only</td>
    </tr>
    <tr>
      <th>Parental Consent</th>
      <td id="parentalConsent:X" onClick="updateDataAddFilter('percentChangeRate', {'name':'parentalConsent', 'value':'X'})">True</td>
      <td id="parentalConsent:" onClick="updateDataAddFilter('percentChangeRate', {'name':'parentalConsent', 'value':''})">False</td>
      <td id="parentalConsent:Sex" onClick="updateDataAddFilter('percentChangeRate', {'name':'parentalConsent', 'value':'Sex'})">Sex Only</td>
    </tr>
    <tr>
      <th>Parental Opt-Out</th>
      <td id="parentalOptOut:X" onClick="updateDataAddFilter('percentChangeRate', {'name':'parentalOptOut', 'value':'X'})">True</td>
      <td id="parentalOptOut:" onClick="updateDataAddFilter('percentChangeRate', {'name':'parentalOptOut', 'value':''})">False</td>
      <td id="parentalOptOut:HIV" onClick="updateDataAddFilter('percentChangeRate', {'name':'parentalOptOut', 'value':'HIV'})">HIV Only</td>
    </tr>
    <tr>
      <th>Contraceptive</th>
      <td id="sexContraception:X" onClick="updateDataAddFilter('percentChangeRate', {'name':'sexContraception', 'value':'X'})">True</td>
      <td id="sexContraception:" onClick="updateDataAddFilter('percentChangeRate', {'name':'sexContraception', 'value':''})">False</td>
    </tr>
    <tr>
      <th>Abstinence</th>
      <td id="sexAbstinence:Stress" onClick="updateDataAddFilter('percentChangeRate', {'name':'sexAbstinence', 'value':'Stress'})">Stress</td>
      <td id="sexAbstinence:Cover" onClick="updateDataAddFilter('percentChangeRate', {'name':'sexAbstinence', 'value':'Cover'})">Cover</td>
      <td id="sexAbstinence:" onClick="updateDataAddFilter('percentChangeRate', {'name':'sexAbstinence', 'value':''})">None</td>
    </tr>
    <tr>
      <th>Sex Within Marriage</th>
      <td id="sexWithinMarriage:X" onClick="updateDataAddFilter('percentChangeRate', {'name':'sexWithinMarriage', 'value':'X'})">True</td>
      <td id="sexWithinMarriage:" onClick="updateDataAddFilter('percentChangeRate', {'name':'sexWithinMarriage', 'value':''})">False</td>
    </tr>
    <tr>
      <th>Sexual Orientation</th>
      <td id="sexualOrientation:Inclusive" onClick="updateDataAddFilter('percentChangeRate', {'name':'sexualOrientation', 'value':'Inclusive'})">Inclusive</td>
      <td id="sexualOrientation:Negative" onClick="updateDataAddFilter('percentChangeRate', {'name':'sexualOrientation', 'value':'Negative'})">Negative</td>
      <td id="sexualOrientation:HIV Related" onClick="updateDataAddFilter('percentChangeRate', {'name':'sexualOrientation', 'value':'HIV Related'})">HIV Related</td>
      <td id="sexualOrientation:" onClick="updateDataAddFilter('percentChangeRate', {'name':'sexualOrientation', 'value':''})">None</td>
    </tr>
    <tr>
      <th>Healthy Decision Making</th>
      <td id="healthyDecisionMaking:X" onClick="updateDataAddFilter('percentChangeRate', {'name':'healthyDecisionMaking', 'value':'X'})">True</td>
      <td id="healthyDecisionMaking:" onClick="updateDataAddFilter('percentChangeRate', {'name':'healthyDecisionMaking', 'value':''})">False</td>
    </tr>
    <tr>
      <th>HIV: Condoms</th>
      <td id="hivCondoms:X" onClick="updateDataAddFilter('percentChangeRate', {'name':'hivCondoms', 'value':'X'})">True</td>
      <td id="hivCondoms:" onClick="updateDataAddFilter('percentChangeRate', {'name':'hivCondoms', 'value':''})">False</td>
    </tr>
    <tr>
      <th>HIV: Abstinence</th>
      <td id="hivAbstinence:Stress" onClick="updateDataAddFilter('percentChangeRate', {'name':'hivAbstinence', 'value':'Stress'})">Stress</td>
      <td id="hivAbstinence:Cover" onClick="updateDataAddFilter('percentChangeRate', {'name':'hivAbstinence', 'value':'Cover'})">Cover</td>
      <td id="hivAbstinence:" onClick="updateDataAddFilter('percentChangeRate', {'name':'hivAbstinence', 'value':''})">None</td>
    </tr>
  </table>
</div>

<div id="description">
  * Rate is per 10,000 people. Black states do not have data for that year.
</div>

<div id="summary" />

<div id="map" />

<div id="legend" />

<div id="footer">
  <h2>Sources</h2>
  <p><a href="https://www.cdc.gov/hiv/pdf/library/reports/surveillance/cdc-hiv-surveillance-supplemental-report-vol-23-1.pdf">CDC HIV Prevalence Report: 2010 - 2015</a></p>
  <p><a href="https://www.cdc.gov/hiv/pdf/library/reports/surveillance/cdc-hiv-surveillance-report-2017-vol-29.pdf">CDC HIV Prevalence Report: 2016 - 2017</a></p>
  <p><a href="https://www.guttmacher.org/state-policy/explore/sex-and-hiv-education">State Laws and Policies on Sex and HIV Education</a></p>
  <p><a href="https://d3js.org/">D3.js Javascript Library</a></p>
</div>

<script type="text/javascript">

/*  This visualization was made possible by modifying code provided by:

Scott Murray, Choropleth example from "Interactive Data Visualization for the Web"
https://github.com/alignedleft/d3-book/blob/master/chapter_12/05_choropleth.html

Malcolm Maclean, tooltips example tutorial
http://www.d3noob.org/2013/01/adding-tooltips-to-d3js-graph.html

Mike Bostock, Pie Chart Legend
http://bl.ocks.org/mbostock/3888852  */


//Width and height of map
var width = 960;
var height = 500;

// D3 Projection
var projection = d3.geo.albersUsa()
				   .translate([width/2, height/2])    // translate to center of screen
				   .scale([1000]);          // scale things down so see entire US

// Define path generator
var path = d3.geo.path()               // path generator that will convert GeoJSON to SVG paths
		  	 .projection(projection);  // tell path generator to use albersUsa projection

//Create SVG element and append map to the SVG
// var svg = d3.select("body")
// 			.append("svg")
// 			.attr("width", width)
// 			.attr("height", height);

// Append Div for tooltip to SVG
var div = d3.select("body")
		    .append("div")
    		.attr("class", "tooltip")
    		.style("opacity", 0);

var globalFilters = {};

function updateDataAddFilter(feature, filter) {
  globalFilters[filter.name] = filter.value;
  updateData(feature, globalFilters);
}

function updateData(feature, filters) {
  console.log("update data with " + feature);
  globalFilters = filters;

  var current = document.getElementsByClassName("active");
  if (current.length > 0) {
    while (current[0]) {
      current[0].classList.remove("active");
    }
  }
  document.getElementById(feature).classList.add("active");

  for (var key in filters) {
    document.getElementById(key + ":" + filters[key]).classList.add("active");
  }

  // filters.forEach(function(filter) {
  //   document.getElementById(filter.name + ":" + filter.value).classList.add("active");
  // });

  d3.selectAll("svg").remove();
  var svg = d3.select("#map")
  			.append("svg")
  			.attr("width", width)
  			.attr("height", height);

  d3.select("#summary").selectAll("l").remove();
  var summary = d3.select("#summary");
  var topStates = summary.append("l").text("Lowest States").append("ol");
  var bottomStates = summary.append("l").text("Highest States").append("ol");

  // Load in my states data
  d3.csv("/hiv-infection-and-education.csv", function(data) {
    data.forEach(function(d) {
      d[feature] = +d[feature]
      d.oldestYear = d.oldestYear

      for (var key in filters) {
        d[key] = d[key]
      }
    })

    var sorted = d3.entries(data)
      .filter(function(d) { return d.value[feature]; })
      .filter(function(d) {
        var filterOut = false;
        for (var key in filters) {
          if (d.value[key] !== filters[key]) {
            filterOut = true;
          }
        }
        return !filterOut;
      })
      // sort by value descending
      .sort(function(a, b) { return d3.ascending(a.value[feature], b.value[feature]); });

    var positiveCount = sorted
      .filter(function(d) { return d.value[feature] > 0; })
      .length;

    var negativeCount = sorted
      .filter(function(d) { return d.value[feature] < 0; })
      .length;

    summary.append("l").text("Negative: " + negativeCount);
    summary.append("l").text("Positive: " + positiveCount);
    summary.append("l").text("Ratio -/+: " + (negativeCount/positiveCount).toFixed(2));

    for (var i = 0; i < sorted.length && i < 5; i++) {
      topStates
        .append("li")
        .text(sorted[i].value.state +" ("+ sorted[i].value[feature].toFixed(1) +")");

      bottomStates
        .append("li")
        .text(sorted[sorted.length - i - 1].value.state +" ("+ sorted[sorted.length - i - 1].value[feature].toFixed(1) +")");
    }

    // Load GeoJSON data and merge with states data
    d3.json("us-states.json", function(json) {

    for (var i = 0; i < data.length; i++) {
    	var dataState = data[i].state;
      var dataValue = data[i][feature];
      var oldestYear = data[i].oldestYear;

    	// Find the corresponding state inside the GeoJSON
    	for (var j = 0; j < json.features.length; j++)  {
    		var jsonState = json.features[j].properties.name;
    		if (dataState == jsonState) {
    		    // Copy the data value into the JSON
    		    json.features[j].properties.value = dataValue;
            json.features[j].properties.oldestYear = oldestYear;
            for (var key in filters) {
              json.features[j].properties[key] = data[i][key];
            }
            // Stop looking through the JSON
            break;
    		}
    	}
    }

    var avr;
    if (feature === 'percentChangeRate') {
      avr = Math.abs(data[51][feature]);
    } else {
      // avr = data[51][feature];
      avr = 16.3;
    }

    if (feature === 'percentChangeRate') {
      var leftMax = d3.interpolate("#ffffff", "#50d0ff")(2*avr);
      var rightMax = d3.interpolate("#ffffff", "#ff7f50")(2*avr);
      updateLegend([leftMax, "#ffffff", rightMax], [4*avr, -4*avr], 5);
    } else {
      updateLegend(["#ffffff", "#800080"], [2*avr, 0], 5);
    }

    // Bind the data to the SVG and create one path per GeoJSON feature
    svg.selectAll("path")
    	.data(json.features)
    	.enter()
    	.append("path")
    	.attr("d", path)
    	.style("stroke", "#fff")
    	.style("stroke-width", "1")
    	.style("fill", function(d) {
        return fillColor(d, avr, feature, filters);
      })

      .on("mouseover", function(d) {
        var label = d.properties.name;
        if (feature === 'percentChangeRate') {
          label += " (" + d.properties.oldestYear + " - 2017): ";
        } else {
          label += ": ";
        }

        div.transition()
          .duration(200)
          .style("opacity", .9);
        div.text(label + d.properties.value.toFixed(1))
          .style("left", (d3.event.pageX) + "px")
          .style("top", (d3.event.pageY - 28) + "px");
      })

      // fade out tooltip on mouse out
      .on("mouseout", function(d) {
        div.transition()
          .duration(500)
          .style("opacity", 0);
      });

  	});

  });

}

function updateLegend(colorStops, domain, ticks) {
  var w = 300, h = 50;

    var key = d3.select("#legend")
      .append("svg")
      .attr("width", w)
      .attr("height", h);

    var legend = key.append("defs")
      .append("svg:linearGradient")
      .attr("id", "gradient")
      .attr("x1", "0%")
      .attr("y1", "100%")
      .attr("x2", "100%")
      .attr("y2", "100%")
      .attr("spreadMethod", "pad");

    for (var i = 0; i < colorStops.length; i++) {
      var offset = Math.round(i * 100 / (colorStops.length - 1));
      legend.append("stop")
        .attr("offset", offset+"%")
        .attr("stop-color", colorStops[i])
        .attr("stop-opacity", 1);
    }

    key.append("rect")
      .attr("width", w)
      .attr("height", h - 30)
      .style("fill", "url(#gradient)")
      .attr("transform", "translate(0,10)");

    var y = d3.scaleLinear()
      .range([300, 0])
      .domain(domain);

    var yAxis = d3.axisBottom()
      .scale(y)
      .ticks(ticks);

    function customYAxis(g) {
      g.call(yAxis)
      g.selectAll(".tick line").attr("stroke", "#fff")
      g.selectAll(".tick text").attr("fill", "#fff")
    }

    var g = key.append("g")
      .attr("class", "y axis")
      .attr("transform", "translate(0,30)")
      .call(customYAxis)
      .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("axis title");

}

function filterOut(d, filters) {
  var filterOut = false;
  for (var key in filters) {
    if (d.properties[key] !== filters[key]) {
      filterOut = true;
    }
  }
  return filterOut;
}

function fillColor(d, avr, feature, filters) {
  var value = d.properties.value;

  if (filterOut(d, filters)) {
    return "#888888";
  }

  var c;
  if (feature === 'percentChangeRate') {
    if (value < 0) {
      c = d3.interpolate("#ffffff", "#50d0ff")(Math.abs(value)/(2*avr));
    } else {
      c = d3.interpolate("#ffffff", "#ff7f50")(value/(2*avr));
    }
  } else {
    if (value) {
      c = d3.interpolate("#ffffff", "#800080")(value/(2*avr));
    } else {
      c = "#000000"
    }
  }

  return c;
}

updateData("percentChangeRate", {});
// updateData("percentChangeRate", [{'name':'hivAbstinence', 'value':'Stress'}]);

</script>

</body>
</html>
"""
