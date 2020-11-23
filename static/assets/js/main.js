$(document).ready(function () {
  $("#searchBtn").click(function () {
    $("#searchIcon").replaceWith($("#searchGif"));
  });

  $(".checked").each(function () {
    $(this).children(".form-check-input").prop("checked", true);
  });

  var chartColors = ["#2382bc", "#b7ceeb", "#ff8b0a", "#a2e395", "#32aa32"];

  $(".btn-chart").on("click", function () {
    $("#chartTitle").text($(this).siblings().find(".host").text());
    var ctx = document.getElementById("summaryChart");
    if (window.chart != undefined) {
      window.chart.destroy();
    }
    var label = [];
    $(this)
      .siblings()
      .find(".chart-label")
      .each(function () {
        label.push($(this).text());
      });
    var count = [];
    $(this)
      .siblings()
      .find(".chart-value")
      .each(function () {
        count.push($(this).text());
      });
    window.chart = new Chart(ctx, {
      type: "pie",
      data: {
        labels: label,
        datasets: [
          {
            data: count,
            backgroundColor: chartColors,
            borderWidth: 1,
          },
        ],
      },
    });
  });
});
