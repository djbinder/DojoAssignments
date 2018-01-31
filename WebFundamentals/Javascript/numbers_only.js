function numbers_only(arr) {
    var new_array = [];
    for (var i=0; i<=arr.length; i++) {
        if(typeof arr[i] == "number") {
            new_array.push(arr[i]);
        }
    }
    console.log(new_array); 
}

var test_array = [2,"fish",6,"bullpen"]; 
numbers_only(test_array); 


var test_array_2 = [2, 9, "night", "day", 6, 200, "blue", "yellow"];
numbers_only(test_array_2);