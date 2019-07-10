# Weather App

This app fetches daily accumulated rainfall from wunderground at scheduled time.

## setup

Create a new `.env` file at the root folder of this project following this example:

    TIMEZONE=America/New_York
    CRONTAB="0 8,17 * * *"
    WEATHER_STATION=us/nc/morrisville/KRDU
    DAYS=7
    PAGE_LOADING_DELAY=30
    PUSHBULLET_API=<your_pushbullet_api_key>

## run

This app can run in two mode: python application and dockerized application.

### python application mode

1.  install packages: `pip install -r requirements.txt`
2.  run app: `python -u app.py`

### dockerized application mode

1.  install `docker` and `docker-compose`
2.  run app: `docker-compose down -v; docker-compose rm -f; docker-compose build --no-cache; docker-compose up --remove-orphans --force-recreate`

## deploy to heroku

Currently heroku supports python application on heroku-18 stack and dockerized application mode on container stack.

### deploy with git

1.  on localhost, log in heroku: `heroku login`
2.  create the app with the name: `heroku create yt-weather`
3.  set stack: `heroku stack:set heroku-18`
4.  add heroku remote: `heroku git:remote --app yt-weather`
5.  add buildpack: `heroku buildpacks:add https://github.com/heroku/heroku-buildpack-chromedriver ; heroku buildpacks:add https://github.com/heroku/heroku-buildpack-google-chrome ; heroku buildpacks:add heroku/python`
6.  set heroku env var: `python heroku_init.py`
7.  run locally with heroku for testing: `heroku local`
8.  deploy: `git add . ; git commit -m 'init' ; git push heroku master`
9.  run remotely on heroku: `heroku run python -u app.py`

### deploy with docker

1.  on localhost, log in heroku: `heroku container:login`
2.  create the app with the name: `heroku create yt-weather`
3.  set stack: `heroku stack:set container`
4.  add heroku remote: `heroku git:remote --app yt-weather`
5.  set heroku env var: `python heroku_init.py`
6.  deploy: `git add . ; git commit -m 'init' ; git push heroku master`
7.  bring up app: `heroku ps:scale worker=1` (if needs to bring down first, run `heroku ps:scale worker=0`)
