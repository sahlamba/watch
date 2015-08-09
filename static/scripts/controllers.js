// Controllers
'use strict';

app.controller('MainController', ['$scope', 'Search',
  function ($scope, Search) {
    $scope.title = 'Popcorn';

    $scope.search = {
      query: '',
      results: [],
      search: function () {
        if (this.query === undefined || this.query === '') {
          $scope.search.results = [];
          return;
        } else {
          Search.searchMovie(this.query)
          .then(function (data) {
            $scope.search.results = data;
            console.log($scope.search.results);
          });
        }
      }
    };
  }
]);

app.controller('HomeController', ['$scope',
  function ($scope) {
    $scope.title = 'Popcorn';
  }
]);
