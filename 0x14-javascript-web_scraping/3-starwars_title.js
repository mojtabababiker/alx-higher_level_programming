#!/usr/bin/node
/* Script that uses the starWars API and search for
   movie spesified by the id, and prints its title */
const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api/films/';
const moveID = process.argv[2];

request.get(`${API_URL}${moveID}`, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const jsonBody = JSON.parse(body);
  console.log(jsonBody.title);
});
