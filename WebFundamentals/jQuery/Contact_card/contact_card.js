$(document).ready(function(){ 
    $(".add_user").click(function() {   

        var firstname = $("#firstname").val();
        var lastname = $("#lastname").val();
        var description = $("#text_description").val();
        var full_name = firstname+" "+lastname; 
        var contact_card = "<div><h1>" + full_name + "</h1><p>" + description + "</p></div>"; 
        
        $("#contact_cards_section").append("<div class='new_info'><h1>"+full_name+"</h1>"+"<p>"+description+"</p></div>"); 
    }); 
        $(document).on('click','.new_info',function() {
            $(this).children('p').toggle('slow'); 
            $("form")[0].reset(); 
        });   
}); 

// 

// $("div #card_full_name").append(full_name); 
// $("div #card_description").append(description); 


// $("input[type=submit]").click(function(){
//     $("<li />").html("item").appendTo("ul");
// })


// $("input[type=submit").click(function() {
//     $("div #card_full_name").append(full_name); 
//     $("div #card_description").append(description); 
//     $("div #contact_cards_section").append(contact_card); 



// $(".add_user").click(function(){


// $(document).ready(function(){ 
//     $(".add_user").click(function(){
//         var firstname = $("#firstname").val();
//         var lastname = $("#lastname").val();
//         var emailaddress = $("#emailaddress").val();
//         var contactnumber = $("#contactnumber").val(); 
//         var markup = "<tr><td>" + firstname + "</td><td>" + lastname + "</td><td>" + emailaddress + "</td><td>" + contactnumber + "</td></tr>";
//         $("table tbody").append(markup); 
//         $("form")[0].reset(); 
//     });
// });

// $(document).on('click',".add_user",function(){
//     // $(".add_user").click(function(){
//         $("div #contact_cards_section").append(contact_card); 
//         // $("div #card_description").append(description); 
//         $("form")[0].reset(); 
//     }); 
// });