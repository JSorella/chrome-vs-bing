
class Browser(object):

    def __init(self):
        self.url = ""

    def __init__(self, driver):
        self.driver = driver

    def access_page(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.close()
