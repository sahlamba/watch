// Config
'use strict';

app.config(['$stateProvider', '$urlRouterProvider', '$interpolateProvider',
  function ($stateProvider, $urlRouterProvider, $interpolateProvider) {

    $urlRouterProvider.otherwise('/');

    $stateProvider
      .state('home', {
        url: '/',
        templateUrl: '../../templates/views/home.html',
        controller: 'HomeController'
      });

    $interpolateProvider.startSymbol('{~');
    $interpolateProvider.endSymbol('~}');
  }
]);
