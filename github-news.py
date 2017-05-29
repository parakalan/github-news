import dryscrape


def notify(title):
    import os
    notif = 'export DISPLAY=:0.0 && notify-send "%s" ' % (title.text())
    os.system(notif)


def cache_news(load, news=None):
    import pickle
    if load:
        try:
            with open('cached_news') as f:
                news = pickle.load(f)
                return news
        except IOError:
            return []
    else:
        with open('cached_news', 'wb') as f:
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
    login(config['username'], config['password'])
    get_news()
