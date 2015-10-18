// Services and Factories
'use strict';

app.factory('Search', ['$q', '$http', function ($q, $http) {
  function returnEmptyArr() {
    var deferObj = $q.defer();
    var emptyArr = [];
    deferObj.resolve(emptyArr);
    return deferObj.promise;
  }

  return {
    searchMovie: function (query) {
      if (query === undefined) {
        return returnEmptyArr();
      } else {
        query = query.trim();
        if (query === '') {
          return returnEmptyArr();
        } else {
          var deferred = $q.defer();
          $http.get('/movie/api/v1/search/?query=' + query)
            .success(function (data) {
              angular.forEach(data.results, function (item) {
                var parts = item.release_date.split('-');
                item.year = parts[0];
              });
              deferred.resolve(data.results);
            })
            .error(function (error) {
              console.log(error);
            });
          return deferred.promise;
        }
      }
    }
  };
}]);
