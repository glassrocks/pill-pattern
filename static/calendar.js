var i;
var heading;
$(document).ready(function(){
  $(".calendars").click(function(){
    $(this).css("color", "blue");
  });
  $(".cal-row-1").click(function(){
    $(".cal-day-sun", this).css("color", "red");
  });
  var n, i;
  n = $("tr").length;
  i = $(".cal-column-1").length;
  //alert(i)
});

//heading = document.getElementsByClassName("cal-heading");
//console.log(heading);
//heading.style.color = "red";