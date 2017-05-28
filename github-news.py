import dryscrape


def get_news():
    sess.visit('/')
    news_list = sess.css(".body > .simple")
    for news in news_list:
        title = news.at_css('.title')
        print title.text()


def login(username, password):
    sess.visit('/login')
    sess.render('fb.png')
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
    login('<USERNAME_HERE>', '<PASSWORD_HERE>')
    get_news()
