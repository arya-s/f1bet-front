(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({"/Users/andrei/dev/f1bet-front/js/components/common/test/index.js":[function(require,module,exports){
module.exports = function() {

    return 'This is a browserify test.';

};
},{}],"/Users/andrei/dev/f1bet-front/js/index.js":[function(require,module,exports){
var test = require('components/common/test');
var view = document.querySelector('#views');

var h1 = document.createElement('h1');

h1.textContent = test();

view.appendChild(h1);
},{"components/common/test":"/Users/andrei/dev/f1bet-front/js/components/common/test/index.js"}]},{},["/Users/andrei/dev/f1bet-front/js/index.js"]);
