#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = process.argv[2];

request.get(`${API_URL}${movieId}`, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const jsonBody = JSON.parse(body);
  const characters = jsonBody.characters;
  characters.forEach((character) => {
    request.get(character, (err, res, body) => {
      if (err) {
        return console.log(err);
      }
      const charBody = JSON.parse(body);
      console.log(charBody.name);
    });
  });
});
