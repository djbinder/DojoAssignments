$(function() {
    var pokeapiURL = "http://pokeapi.co/api/v2/generation/1";

    $.getJSON(pokeapiURL).done(function(data) { 
        console.log(data); 
    });
});