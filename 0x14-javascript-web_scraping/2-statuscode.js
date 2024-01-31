#!/usr/bin/node
/* Script that use the request module to
   send GET resquet and print its status cose */
const request = require('request');
const url = process.argv[2];

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  console.log(`code: ${res.statusCode}`);
});
