#!/usr/bin/node
// reads and prints the content of a file.

const { argv } = process;
const fs = require('fs');

fs.readFile(argv[2], 'utf8', (err, data) => {
  if (err) {
    return console.error(err);
  }
  console.log(data);
});
