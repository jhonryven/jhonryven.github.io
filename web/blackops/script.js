$(document).ready(function() {
    $(".btn").click(function() {
      var filter = $(this).attr("data-filter");
      if (filter == "all") {
        $(".item").show();
      } else {
        $(".item").hide();
        $(".item[data-filter='" + filter + "']").show();
      }
      $(".btn").removeClass("active1");
      $(this).addClass("active1");
    });
  });