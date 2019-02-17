var i, n;
var heading;
$(document).ready(function(){
  /*$(".calendars").click(function(){
    $(this).css("color", "blue");
  });*/
  var time-rows = len($(.cal-row-*));
  console.log(time-rows)
  for (i = 0; i < len($(.cal-row-*)); i++) {
    $("[class^=cal-row-]").click(function(){
      $(".cal-day-sun", this).css("color", "red");
    });
  }
  n = $("tr").length;
  i = $(".cal-column-1").length;
  //alert(i)
});

//heading = document.getElementsByClassName("cal-heading");
//console.log(heading);
//heading.style.color = "red";