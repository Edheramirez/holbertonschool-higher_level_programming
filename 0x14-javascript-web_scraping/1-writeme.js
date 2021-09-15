#!/usr/bin/node
// writes a string to a file.

const { argv } = process;
const fs = require('fs');

fs.writeFile(argv[2], argv[3], function (err) {
  if (err) {
    return console.log(err);
  }
  console.log('The file was saved!');
});
