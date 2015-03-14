var test = require('components/common/test');
var view = document.querySelector('#views');

var h1 = document.createElement('h1');

h1.textContent = test();

view.appendChild(h1);