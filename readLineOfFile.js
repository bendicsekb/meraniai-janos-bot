// source: https://stackoverflow.com/questions/38843016/how-to-remove-one-line-from-a-txt-file

const fs = require('fs');

function readWriteSync(filepath) {
  var data = fs.readFileSync(filepath, 'utf-8');

  var linesExceptFirst = data.split('\n').slice(1).join('\n');
  var firstLine = data.split('\n')[0];

  fs.writeFileSync(filepath, linesExceptFirst, 'utf-8');
  return firstLine
}

module.exports = {
    readWriteSync: readWriteSync
}