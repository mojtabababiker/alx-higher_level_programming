$.getJSON(
  "https://swapi-api.alx-tools.com/api/people/5/?format=json"
  function (content) {
    $("div#character").append(content.name);
  });
