const header = $("header");
$("div#toggle_header").on ("click", function () {
  if (header.hasclass("red")) {
    header.removeclass("red");
    header.addclass("green");
  } else {
    header.removeclass("green");
    header.addclass("red");
  }
});
