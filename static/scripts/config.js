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
