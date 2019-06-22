# weather app

fetch daily accumulated rainfall from wunderground

## deploy to heroku

1.  create the app with the name: `heroku create yt-weather`
2.  add heroku remote: `heroku git:remote --app yt-weather`
3.  add buildpack: `heroku buildpacks:add https://github.com/heroku/heroku-buildpack-chromedriver ; heroku buildpacks:add https://github.com/heroku/heroku-buildpack-google-chrome ; heroku buildpacks:add heroku/python`
4.  set heroku env var: `python heroku_init.py`
5.  run locally with heroku for testing: `heroku local`
6.  deploy: `git add . ; git commit -m 'init' ; git push heroku master`
7.  run remotely on heroku: `heroku run python app.py`

## schedule to run on heroku

1.  add an addon to app: `heroku addons:create scheduler:standard --app yt-weather`
2.  open addon config `heroku addons:open scheduler`
3.  add two jobw in webpage: `python app.py` with Frequency of `Daily at 2:00 PM UTC` and `Daily at 9:00 PM UTC`
