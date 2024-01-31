#!/usr/bin/node
/* Script that reads and print file contents using the fs/promises module */
const { readFile } = require('node:fs/promises');

async function readContents () {
  try {
    const fileName = process.argv[2];
    const fileContent = await readFile(fileName, { encoding: 'utf-8' });
    console.log(fileContent);
  } catch (error) {
    console.log(error);
  }
}

readContents();
