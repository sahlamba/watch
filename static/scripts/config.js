// Config
'use strict';

app.config(['$stateProvider', '$urlRouterProvider', '$interpolateProvider',
  function ($stateProvider, $urlRouterProvider, $interpolateProvider) {

    $urlRouterProvider.otherwise('/');

    $stateProvider
      .state('home', {
        url: '/',
        templateUrl: '/static/views/home.html',
        controller: 'HomeController'
      })
      .state('show', {
        url: '/movie/{name}',
        templateUrl: '/static/views/movie.html',
        controller: 'MovieController'
      });

    $interpolateProvider.startSymbol('{~');
    $interpolateProvider.endSymbol('~}');
  }
]);

app.directive('autofocus', ['$timeout', function ($timeout) {
  return {
    restrict: 'A',
    link: function ($scope, $element) {
      $timeout(function () {
        $element[0].focus();
      });
    }
  }
}]);

app.config(['cfpLoadingBarProvider', function (cfpLoadingBarProvider) {
  cfpLoadingBarProvider.latencyThreshold = 0;
  cfpLoadingBarProvider.includeBar = false;
  cfpLoadingBarProvider.parentSelector = '#ajax-loader';
}]);
