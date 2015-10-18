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
          $http.get('http://api.themoviedb.org/3/search/movie?api_key=' + API_KEY + '&query=' + query)
            .success(function (data) {
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
