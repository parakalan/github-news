### github-news
#### View Github news feed updates from command line.

A simple Python app to view Github notifications from command line. The script logs into your account, scrapes the news feed from the home page and displays it.


#### Usage
Install dryscrape
```sh
$ pip install dryscrape
```
**Add your credentials in line no. 28** (Sorry :stuck_out_tongue:  Will get credentials from config file in future) . After that,
```sh
$ python github-news.py
```
The top 30 notifications will be printed.


#### To do
- [ ] Get login credentials from config file.
- [ ] Send desktop notifications.
