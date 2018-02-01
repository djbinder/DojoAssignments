$(document).ready(function(){ 
    $(".add_user").click(function(){
        var firstname = $("#firstname").val();
        var lastname = $("#lastname").val();
        var emailaddress = $("#emailaddress").val();
        var contactnumber = $("#contactnumber").val(); 
        var markup = "<tr><td>" + firstname + "</td><td>" + lastname + "</td><td>" + emailaddress + "</td><td>" + contactnumber + "</td></tr>";
        $("table tbody").append(markup); 
        $("form")[0].reset(); 
    });
});