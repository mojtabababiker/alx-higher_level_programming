document.addEventListener('DOMContentLoaded', function () {
  $('input#btn_translate').on('click', function () {
    const lang = $('input#language_code').val();
    $.get(
      'https://hellosalut.stefanbohacek.dev/?lang=' + lang,
      function (content) {
        $('div#hello').text(content.hello);
      },
      'json'
    );
  });
});
