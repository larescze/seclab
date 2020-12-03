$(document).ready(function () {
  $("#launch").click(function () {
    let valid = true;
    $("[required]").each(function () {
      if ($(this).is(":invalid") || !$(this).val()) {
        valid = false;
      }
    });
    if (valid) {
      $("#searchIcon").replaceWith($("#searchGif"));
    }
  });

  function sepNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
  }

  $("#total").text(sepNumber($("#total").text()));
  $("#totalVuln").text(sepNumber($("#totalVuln").text()));

  $(".checked").each(function () {
    $(this).children(".form-check-input").prop("checked", true);
  });

  $(".selected").prop("selected", true);

  var chartColors = ["#2382bc", "#b7ceeb", "#ff8b0a", "#a2e395", "#32aa32"];

  $(".btn-chart").on("click", function () {
    var title = "Chart " + $(this).siblings().find(".host").text();
    $("#chartTitle").text(title);

    var charType = $("#chartType").text();

    var isLegend = true;
    if (charType === "bar") {
      isLegend = false;
    }

    var ctx = document.getElementById("summaryChart");

    if (window.chart instanceof Chart) {
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
      type: charType,
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
      options: {
        legend: {
          display: isLegend,
        },
      },
    });
  });

  $("#attack_type").on("change", function () {
    if (this.value == "custom") {
      $("#custom_code").prop("readonly", false);
      $("#custom_code").prop("required", true);
    } else {
      $("#custom_code").prop("readonly", true);
      $("#custom_code").val();
    }
  });
});
