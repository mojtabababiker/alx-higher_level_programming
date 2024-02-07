$.get(
  "https://swapi-api.alx-tools.com/api/filmss/?format=json",
  function (content) {
    content.results.forEach(film => {
      $("ul#list_movies").append("<li>" + (film.title) + "</li>");
    });
  }
);
