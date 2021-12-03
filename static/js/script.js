/*
Katelyn Lindsey
Color Palette App
script.js
*/

/* function for toggling rgb/hex values on palette.html page */
$(function() {

	$("#toggle-rgb-hex").click(function() {

		/* 
		get all of the colors of the current palette and what type of
		color value is currently displayed (rgb or hex)
		*/
		var colors = $("#toggle-rgb-hex").data("colors");
		var currentType = $("#color_1").data("colortype");
		currentType = currentType.toString();


		/* 
		convert the string dictionary to a JSON object - 
		requires some initial reformatting 
		*/
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

		} else { /* otherwise, switch to rgb */

			for(var key in colors) {
				$("#" + key).data("colortype", "rgb");
				newText = colors[key][0];
				$("#" + key).text(newText);
			}

		}

	});
});


/* 
start over button and confirmatino that goes back to the home page - 
used in images.html 
*/
function startOver(form) {

	var answer = confirm("You may not see these images again. Are you sure?")

	if(answer == true) { /* only go to home page if the user confirms their choice */
		form.method = "get";
		form.action = "/";
		return true;
	} else {
		return false;
	}
}