import dryscrape
import pickle
import os
import sys


def check_first_start():
    filepath = os.path.abspath(os.path.join(__file__, "../cached_news"))
    try:
        f = open(filepath)
    except IOError:
        print "Starting for first time."
        setup_cron()


def setup_cron():
    from crontab import CronTab
    cron = CronTab()
    job = cron.new(command=sys.executable + ' ' + os.path.abspath(__file__))
    try:
        job.minute.every(config["interval"])
    except KeyError:
        print "Please check your config file. Interval missing"
        exit()
    import getpass
    cron.write(user=getpass.getuser())


def notify(title):
    notif = 'export DISPLAY=:0.0 && notify-send "%s" ' % (title.text())
    os.system(notif)


def cache_news(load, news=None):
    filepath = os.path.abspath(os.path.join(__file__, "../cached_news"))
    if load:
        try:
            with open(filepath) as f:
                news = pickle.load(f)
                return news
        except IOError:
            return []
    else:
        with open(filepath, 'wb') as f:
            pickle.dump(news, f)


def get_config():
    try:
        import json
        with open('.config') as f:
            config = json.load(f)
        return config
    except IOError:
        print "Please create config file."
        exit()


def get_news():
    sess.visit('/')
    cached_news = cache_news(True)
    news_list = sess.css(".body > .simple")
    for news in news_list:
        title = news.at_css('.title')
        if title.text() in cached_news:
            break
        links = title.css('a')
        if config['preferred_people'] == [] or  \
                links[0].text() in config['preferred_people']:
            notify(title)
            cached_news.append(title.text())
    cache_news(False, cached_news)


def login(username, password):
    sess.visit('/login')
    q = sess.at_xpath('//*[@id="login_field"]')
    q.set(username)
    q = sess.at_xpath('//*[@id="password"]')
    q.set(password)
    login_button = sess.at_xpath('//*[@name="commit"]')
    login_button.click()


if __name__ == '__main__':
    dryscrape.start_xvfb()
    sess = dryscrape.Session(base_url='https://github.com')
    sess.set_attribute('auto_load_images', True)
    config = get_config()
    check_first_start()
    try:
        login(config['username'], config['password'])
    except KeyError:
        print "Please check your config file."
        exit()
    get_news()
