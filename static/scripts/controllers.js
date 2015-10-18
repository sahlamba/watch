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

app.controller('MovieController', ['$scope', '$http', '$routeParams', '$sce',
  function ($scope, $http, $routeParams, $sce) {
    $scope.getMovieData = function () {
      $scope.done = false;
      $http.get('/movie/api/v1/show/?query=' + $routeParams.id)
        .success(function (data) {
          $scope.movie = data;
          $scope.done = true;
          $scope.movie.trailer = $sce.trustAsResourceUrl($scope.movie.trailer);
          var iframe = angular.element('<iframe width="560" height="315" src="' + $scope.movie.trailer + '" frameborder="0" allowfullscreen></iframe>');
          angular.element('#wrapper').append(iframe);
          console.log(data);
        });
    };
  }
]);
