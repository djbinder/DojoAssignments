$('form').on('submit', function(e) { 
    e.preventDefault(); 

    var types = $('input[type=text]').val().replace(' ','');
    types = types.split(',');
    console.log(types);
    var trainerTypes = types.map(function(type) {
        return $.ajax({
            url: 'http://pokeapi.co/api/v2/type/' + type,
            dataType: 'json',
            method: 'GET'
        }); 
    });
    $.when.apply(null,trainerTypes)
        .then(function() {
            console.log(arguments); 
            // var pokemonTypes = Array.prototype.slice.call(arguments);
            // console.log(pokemonTypes); 
            // getDoubleDmgTypes(pokemonTypes);
        }); 
});
    
function getDoubleDmgTypes(pokemonTypes) {
    pokemonTypes = pokemonTypes.map(function(types) {
        return types[0].damage_relations.double_damage_from;
    });
    pokemonTypes = flatten(pokemonTypes); 
    
    var damageTypes = pokemonTypes.map(function(type) {
        return $.ajax({ 
            url:type.url,
            dataType: 'json',
            method: 'GET'
        });
    });
    $.when.apply(null,damageTypes)
        .then(function() {
            var pokemon = Array.prototype.slice.call(arguments); 
            buildTeam(pokemon); 
        });
}

function buildTeam(pokemon) {
    pokemon = pokemon.map(function(poke) {
        return poke[0].pokemon; 
    });
    pokemon = flatten(pokemon);
    console.log(pokemon); 
}

function flatten(arrayToFlatten) {
    return arrayToFlatten.reduce(function(a,b) {
        return a.concat(b);
    },[]);
}