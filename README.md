# watch
One place to view all necessary details and links related to any movie on the web. A collection of ratings, reviews, download links and subtitles.

> Written using the [Django](https://www.djangoproject.com/) framework and [AngularJS](https://angularjs.org/)  
> Hosted on [Heroku](http://popcorns.herokuapp.com/)

## Setup local development environment
#### Clone the repository
```bash
git clone https://github.com/thedrumsknight/watch.git
cd watch
```

#### Setup Postgres DB
```bash
createuser -s -d -l -P aman
```
When prompted to enter password enter ```cg.9```
```bash
createdb -O aman watch
```

#### Install dependencies
```bash
pip install -r requirements.txt
```
#### Run migrations to sync DB
```bash
python manage.py syncdb
```

#### Start server
```bash
python manage.py runserver
```
Server will start on [http://localhost:8000/](http://localhost:8000/)

## Credits
>Developed and maintained by [Sahil Lamba](https://github.com/thedrumsknight), [Aman Shrivastava](https://github.com/amanthedorkknight) and [Mihir Rana](https://github.com/thedespicableknight)
