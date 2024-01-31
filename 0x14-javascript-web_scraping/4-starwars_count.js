#!/usr/bin/node

const request = require('request');
const API_URL = process.argv[2];
const charId = '18';
let movies = 0;

request.get(API_URL, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const jsonBody = JSON.parse(body);
  jsonBody.results.forEach((result) => {
    result.characters.forEach((character) => {
      if (character.includes(charId)) {
        movies += 1;
      }
    });
  });
  console.log(movies);
});
