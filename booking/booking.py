import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        super(Booking, self).__init__()
        self.teardown = teardown

    def __quit__(self):
        if self.teardown:
            self.quit()

    def close_login(self):
        close = self.find_element(By.CLASS_NAME, 'loginCloseBtn')
        close.click()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def sel_source(self, source_detail):
        source = self.find_element(By.XPATH, '//*[@id="origin"]/span/input')
        source.click()
        source.send_keys(source_detail)
        source.send_keys(Keys.ARROW_DOWN)
        source.send_keys(Keys.ARROW_DOWN)
        source.send_keys(Keys.ENTER)

    def sel_destination(self, destination_detail):
        destination = self.find_element(By.XPATH, '//*[@id="destination"]/span/input')
        destination.click()
        destination.send_keys(destination_detail)
        destination.send_keys(Keys.ARROW_DOWN)
        destination.send_keys(Keys.ARROW_DOWN)
        destination.send_keys(Keys.ENTER)

    def journey_date(self, journey_date):
        date = self.find_element(By.XPATH, '//*[@id="jDate"]/span/input')
        date.click()
        ActionChains(self).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(
            Keys.BACKSPACE).send_keys(journey_date).perform()

    def search_btn(self):
        search = self.find_element(By.XPATH,
                                   '//*[@id="divMain"]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[5]/div[1]/button')
        search.click()
