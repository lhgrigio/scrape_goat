from loguru import logger

# selenium imports
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# module imports
from configreader import getConfig
from utils.strings import SG_MISSING_BROWSER_CONFIGURATION, SG_EXECUTION_ERRO_ROUTINE_GENERIC, SG_GENERIC_ROUTINE_SUCCESS, SG_GENERIC_ROUTINE_START
from utils.tasks import loginBasic2Fields, waitForInitialElementDetectionByID

class SimpleLoginRoutine():

    def __init__(self, browser, autoRun: bool):
        self.drivenBrowser = browser
        self.routineName = __name__.split('.')[1].replace('_', ' ')

        try:
            self.oidc_routine_config = getConfig()[__package__][__name__.split('.')[
                1]]['routine-config'][browser.browser.name]
        except KeyError:
            logger.info(SG_MISSING_BROWSER_CONFIGURATION(browser.browser.name, self.routineName))
        if autoRun:
            self.routineInit()

    def routineInit(self):
        logger.info(SG_GENERIC_ROUTINE_START(self.routineName))
        try:
            waitForInitialElementDetectionByID(self.drivenBrowser, startPage=self.oidc_routine_config['initialPage'], elementId=self.oidc_routine_config['user_field_id'])
            loginBasic2Fields(sgBrowser=self.drivenBrowser, config=self.oidc_routine_config)
        except Exception as e:
            logger.error(SG_EXECUTION_ERRO_ROUTINE_GENERIC(self.routineName, e))
        finally:
            logger.info(SG_GENERIC_ROUTINE_SUCCESS(self.routineName))