#!/usr/bin/node
//reads and prints the content of a file.

const { argv } = process;
const fs = require('fs');

fs.readFile(argv[2], 'utf8' , (err, data) => {
  if (err) {
      console.error(err);
      return;
  }
    console.log(data);
});
