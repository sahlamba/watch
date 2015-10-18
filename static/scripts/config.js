// Config
'use strict';

app.config(['$locationProvider', '$routeProvider', '$interpolateProvider',
  function ($locationProvider, $routeProvider, $interpolateProvider) {

    $routeProvider
      .when('/', {
        templateUrl: '/static/views/home.html',
        controller: 'HomeController'
      })
      .when('/movie/:id/', {
        templateUrl: '/static/views/movie.html',
        controller: 'MovieController'
      })
      .otherwise({
        redirectTo: '/'
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
  cfpLoadingBarProvider.spinnerTemplate = '<div class="la-ball-triangle-path"><div></div><div></div><div></div></div>';
  cfpLoadingBarProvider.parentSelector = '#loading';
}]);
