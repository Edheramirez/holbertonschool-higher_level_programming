#!/usr/bin/node
// display the status code of a GET request.

const { argv } = process;
const request = require('request');

request(argv[2], (err, { statusCode }) => {
  if (err) return console.log(err);

    console.log(`code: ${statusCode}`);
});
