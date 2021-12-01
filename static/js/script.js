/*
Katelyn Lindsey
Color Palette App
script.js
*/

/* toggling rgb/hex on palette.html page */
$(function() {
	$("#toggle-rgb-hex").click(function() {

		/* first, get all of the colors of the current palette and what
		type of color value is currently displayed (rgb or hex)*/
		var colors = $("#toggle-rgb-hex").data("colors");
		var currentType = $("#color_1").data("colortype");
		currentType = currentType.toString();


		/* convert the string dictionary to a JSON object - requires some initial reformatting*/
		colors = colors.replace(/'/g, "\"");
		colors = colors.replace(/\(/g, "\"(");
		colors = colors.replace(/\)/g, ")\"");

		colors = JSON.parse(colors);


		/* if the type is currently rgb, switch to hex */
		if(currentType == "rgb") {

			for(var key in colors) {
				$("#" + key).data("colortype", "hex");
				newText = colors[key][1];
				$("#" + key).text("#" + newText);
			}
			console.log("changed to hex");
		} else { /* otherwise, switch to rgb */

			for(var key in colors) {
				$("#" + key).data("colortype", "rgb");
				newText = colors[key][0];
				$("#" + key).text(newText);
			}
			console.log("changed to rgb");
		}

	});
});