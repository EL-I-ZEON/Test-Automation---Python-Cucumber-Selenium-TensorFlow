class GooglePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.google.com"

    def load(self):
        self.driver.get(self.url)

    def search(self, term):
        search_box = self.driver.find_element_by_name("q")
        search_box.clear()
        search_box.send_keys(term)
        search_box.submit()