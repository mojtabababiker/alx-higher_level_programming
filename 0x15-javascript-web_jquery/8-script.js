$.getJSON(
  "https://swapi-api.alx-tools.com/api/films/?format=json",
  function (content) {
    $.each( film, function (key, val) {
      if (key === "title") {
	$("ul#list_movies").append("<li>" + val + "</li>");
      };
    });
  });
