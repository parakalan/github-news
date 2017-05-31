## github-news
#### Get Github news feed updates as notifications.

A simple Python app to get Github news feed updates as notifications. The script logs into your account, scrapes the news feed from the home page and sends notifications using `notify-send`.


#### Usage
* Install `dryscrape`
```sh
$ pip install dryscrape
```
* Install `python-crontab`
```sh
$ pip install python-crontab
```
* Create config file from template
```sh
$ cp .config.example .config
```

* Edit .config. Add your details.

* Run script
```sh
$ python github-news.py
```


#### To do
- [x] Get login credentials from config file.
- [x] Send desktop notifications.
- [x] Setup cron from script.
- [ ] Display hyperlink in notifications.
