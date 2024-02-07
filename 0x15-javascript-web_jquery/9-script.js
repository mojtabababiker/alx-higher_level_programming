document.onload(
  $.get(
  "https://hellosalut.stefanbohacek.dev/?lang=fr",
  function (content) {
    $("div#hello").text(content);
  });
);
