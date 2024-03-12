#!/usr/bin/node

exports.converter = function (base) {
  return function (num) {
    if (num === 0) {
      return '0';
    }
    let result = '';
    while (num !== 0) {
      const rem = num % base;
      num = Math.floor(num / base);
      result = (rem < 10) ? String.fromCharCode(rem + 48) + result : String.fromCharCode(rem + 55) + result;
    }
    return result;
  }
}
