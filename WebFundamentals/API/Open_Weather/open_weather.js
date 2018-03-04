$(document).ready(function () {
    $(".submit").click(function() { 
        var api = 'http://api.openweathermap.org/data/2.5/weather?q=';
        var units = '&units=imperial'; 
        var city = $('#city').val(); 
        var api_key = '&appid=96ed06632fd52a70a498d3faa6ddc5bc';
        var url = api + city + api_key + units; 
        console.log(api);
        console.log(units);
        console.log(api_key);
        console.log(city); 
        console.log(api + 'Chicago' + api_key + units); 
        console.log(api + city + api_key + units); 
        console.log(url); 
        $.get(url, gotData); 
    });
    function gotData(data) {
        console.log(data); 
        weather = data; 
        console.log(data); 
        console.log(data.main); 
        console.log(data.main.pressure); 
        $("#weather").append(data.main); 
        $("#weather").append('Pressure: ' + data.main.pressure);  
        $("#weather").append('Rain: ' + data.rain); 
    }
});




// $.get("https://pokeapi.co/api/v2/pokemon/" + image + "/", function (res) {


// function setup() {
//     var button = select('#submit');
//     button.mousePressed(weatherAsk);
//     input = select('#city');
//     console.log("Dan"); 
// }

// function weatherAsk() {
//     var url = api + input.value() + api_key + units;
//     console.log(url); 
//     loadJSON(url, gotData);
//     console.log(url);
// }

// });

   