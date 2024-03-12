#!/usr/bin/node

exports.esrever = function (list) {
  const someList = [];
  for (let i = (list.length - 1); i >= 0; i--) {
    someList.push(list[i]);
  }
  return someList;
};
