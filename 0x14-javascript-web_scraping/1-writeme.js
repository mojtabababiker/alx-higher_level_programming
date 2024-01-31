#!/usr/bin/node
/* script that writesa string to a file using fs/promises module */
const { writeFile } = require('fs/promises');

async function writeContent () {
  try {
    const fileName = process.argv[2];
    const fileContent = process.argv[3];

    await writeFile(fileName, fileContent, { encoding: 'utf-8' });
  } catch (error) {
    console.log(error);
  }
}

writeContent();
