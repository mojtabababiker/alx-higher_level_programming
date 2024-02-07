document.addEventListener("DOMContentLoaded", function() {
  $("input#btn_translate").on ("click", function () {
    const lang = $("input#language_code").val();
    $.get(
      "https://hellosalut.stefanbohacek.dev/?lang=" + lang,
      function(content) {
        $("div#hello").text(content.hello);
      },
      "json"
    );
  });
// add event on the Enter key when the text input is in focus
  $("input#language_code").on ("focus", function() {
    // add the kepress event on the etire window
    window.addEventListener("keypress", function(event) {
      // check if the key was the Enter key
      if (event.key === "Enter") {
        const lang = $("input#language_code").val();
        $.get(
          "https://hellosalut.stefanbohacek.dev/?lang=" + lang,
          function(content) {
          $("div#hello").text(content.hello);
          },
          "json"
        );
      }
    })
  })
});