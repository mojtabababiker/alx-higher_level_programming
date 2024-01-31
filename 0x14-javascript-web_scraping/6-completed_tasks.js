#!/usr/bin/node

const request = require('request');
const API_URL = process.argv[2];
const completedTasks = {};

request.get(`${API_URL}/?completed=true`, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const jsonBody = JSON.parse(body);
  jsonBody.forEach((task) => {
    const usrId = task.userId;
    completedTasks[usrId] = completedTasks[usrId] + 1 || 1;
  });
  console.log(completedTasks);
});
