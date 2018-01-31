function printRange(start_point, end_point, skip_amount) 
    {
        while (start_point < end_point) {
            console.log(start_point);
            start_point = start_point + skip_amount; 
        }
    }

printRange(2,10,2); 