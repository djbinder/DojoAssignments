$(function pokeSubmit(){
    var param = document.getElementById("pokeInput").value;
    var pokeURL = "http://pokeapi.co/api/v2/pokemon/25" + param;

    $.getJSON(pokeURL, function(data){
        console.log(data);
        console.log(JSON.stringify(data, null, "  "));

    });
});