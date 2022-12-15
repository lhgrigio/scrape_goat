from loguru import logger

# selenium imports
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# module imports
from utils.strings import SG_MISSING_BROWSER_CONFIGURATION, SG_MISSING_ELEMENT_GENERIC_ROUTINE_ERROR

def loginBasic2Fields(sgBrowser, config):
    try:
        user_field = sgBrowser.browser.find_element(
            By.ID, config['user_field_id'])
        user_field.clear()
        user_field.send_keys(config['user_field_text'])

        pass_field = sgBrowser.browser.find_element(
            By.ID, config['pass_field_id'])
        pass_field.clear()
        pass_field.send_keys(config['pass_field_text'])
    except NoSuchElementException as error:
        logger.error(SG_MISSING_ELEMENT_GENERIC_ROUTINE_ERROR(error))

def waitForInitialElementDetectionByID(sgBrowser, startPage: str, elementId: str, timeout: int = None):
    wait = WebDriverWait(sgBrowser.browser, timeout or 10)
    sgBrowser.goToPage(startPage)
    wait.until(EC.presence_of_element_located((By.ID, elementId)))
