var i, n;
var heading;
$(document).ready(function(){
  /*$(".calendars").click(function(){
    $(this).css("color", "blue");
  });*/
  var timeRows;
  timeRows = $("[class^=cal-row-]").length;
  for (i = 0; i < timeRows; i++) {
    $("[class^=cal-day-]").click(function(){
      $(this).css("background-color", "#80bfff");
    });
  }
  n = $("tr").length;
  i = $(".cal-column-1").length;
  //alert(i)
});

//heading = document.getElementsByClassName("cal-heading");
//console.log(heading);
//heading.style.color = "red";