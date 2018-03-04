$(document).ready(function () {
    for (var i = 1; i <= 151; i++) { // as long as i less than 151, run the function; starts at 1
        $(".pokemon").append("<img id='" + i + "'src='http://pokeapi.co/media/img/" + i + ".png'>");
    }       // this is what happens when the function is run  |  append the Pokemon div with  |  set image i with a source from the Pokemon api  |  the source is a PNG file  

    $(document).on("click", "img", function () {   // runs when the image is clicked

        var image = $(this).attr("id");  // set variable image to whatever is clicked with the current i
        $.get("https://pokeapi.co/api/v2/pokemon/" + image + "/", function (res) {  //get an image from the pokemon api and return the result 

            var html_str = "<h1>" + res.name + "</h1>";  // set variable html_str to be a header 1 that has the name of the response
            html_str += "<img id='" + i + "'src='http://pokeapi.co/media/img/" + image + ".png'>";  // resets the variable to now be a png. 
            html_str += "<h4>Types</h4><ul>"; // again resets the variable to types

            for (var i = 0; i < res.types.length; i++) {
                html_str += "<li>" + res.types[i].name + "</li>";
                console.log(res.height); 
            }

            html_str += "</ul><h4>Height</h4><p>" + res.height + "</p><h4>Weight</h4><p>" + res.weight + "</p>";

            $(".pokedex").html(html_str);
        }, "json");
    });
});
