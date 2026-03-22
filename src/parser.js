// parser.js
const fs = require('fs');
const path = require('path');
const xml2js = require('xml2js');

const parser = {
  parse: (filePath) => {
    const file = fs.readFileSync(filePath, 'utf8');
    const parser = new xml2js.Parser();
    return new Promise((resolve, reject) => {
      parser.parseString(file, (err, result) => {
        if (err) reject(err);
        else resolve(result);
      });
    });
  },
  arrayify: (node) => {
    if (Array.isArray(node)) {
      return node.map((item) => this.arrayify(item));
    } else if (typeof node === 'object') {
      const result = {};
      for (const key in node) {
        if (node.hasOwnProperty(key)) {
          result[key] = this.arrayify(node[key]);
        }
      }
      return result;
    } else {
      return node;
    }
  },
};

module.exports = parser;