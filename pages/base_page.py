from configparser import ConfigParser
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
                Basic section:init function, store config data
    """

    def __init__(self, browser=None, url=None):
        self.browser = browser
        self.url = url

    # store data from the config
    config = ConfigParser()
    config.read('config.ini')

    def get_conf_param(self, section, parameter, default_value=None):
        """This function returns config data """
        result = self.config.get(section, parameter)
        return result or default_value

    """
                                 Navigation section. 
    """

    def open(self):
        self.browser.get(self.url)

    """
                        Browser interaction section.
    """

    def browser_set_fullscreen(self, screen_height=1920, screen_width=1080):
        self.browser.set_window_size(screen_height, screen_width)

    """
                        Checking elements section.
    """

    def has_element_appeared(self, how, what, timeout=4):
        """ Check for element with expectation(4 sec by default)"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except NoSuchElementException:
            print("The element hasn't appeared during {} seconds ".format(timeout))
            return False
        return True

    def has_element_disappeared(self, how, what, timeout=4):
        """Check that element has disappeared ...until timeout(4 sec by default) become"""
        try:
            WebDriverWait(self.browser, timeout, 0.25, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            print("The element hasn't disappeared during {} seconds ".format(timeout))
            return False
        return True