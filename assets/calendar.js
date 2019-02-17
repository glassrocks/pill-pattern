var i;
var heading;
$(document).ready(function(){
  $("table").click(function(){
    $(this).css("color", "blue");
  });
  $(".cal-column-1").click(function(){
    $(this).css("color", "red");
  });
  var n, i;
  n = $("tr").length;
  i = $("cal-column-1").length;
  //alert(i)
});

//heading = document.getElementsByClassName("cal-heading");
//console.log(heading);
//heading.style.color = "red";