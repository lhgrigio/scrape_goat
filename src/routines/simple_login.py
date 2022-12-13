import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from configreader import getConfig


class SimpleLoginRoutine():

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    def __init__(self, browser, autoRun: bool):
        self.drivenBrowser = browser
        self.routineName = __name__.split('.')[1].replace('_', ' ')

        try:
            self.oidc_routine_config = getConfig()[__package__][__name__.split('.')[
                1]]['routine-config'][browser.browser.name]
        except KeyError:
            self.logger.info("No configuration present for browser '{}' in this routine, please check your configuration".format(
                browser.browser.name))
        if autoRun:
            self.routineInit()

    def routineInit(self):
        self.logger.info(
            'Initiating routine execution for %r routine', self.routineName)
        try:
            self.waitForInitialLoginRedirection()
            self.loginBasic2Fields()
        except Exception as e:
            self.logger.error(
                "Error executing '{}' routine. \n Error: {}".format(self.routineName, e))
        finally:
            self.logger.info(
                "Routine '{}' is done executing!.".format(self.routineName))

    def waitForInitialLoginRedirection(self):
        wait = WebDriverWait(self.drivenBrowser.browser, 10)
        self.drivenBrowser.goToPage(self.oidc_routine_config['initialPage'])
        wait.until(EC.presence_of_element_located(
            (By.ID, self.oidc_routine_config['user_field_id'])))

    def loginBasic2Fields(self):
        try:
            user_field = self.drivenBrowser.browser.find_element(
                By.ID, self.oidc_routine_config['user_field_id'])
            user_field.clear()
            user_field.send_keys(self.oidc_routine_config['user_field_text'])

            pass_field = self.drivenBrowser.browser.find_element(
                By.ID, self.oidc_routine_config['pass_field_id'])
            pass_field.clear()
            pass_field.send_keys(self.oidc_routine_config['pass_field_text'])
        except NoSuchElementException as error:
            self.logger.error(
                "At least one element was not located in the page, please check the id. \n Error: {}".format(error.msg))
