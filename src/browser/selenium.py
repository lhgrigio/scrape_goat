from selenium import webdriver
from enum import Enum

class SeleniumBrowser:

    def __init__(self, browserType: str):
        self.generateBrowser(browserType)

    def generateBrowser(self, browserType: str):
        if browserType == BrowserOptions.CHROME.value:
            newBrowser = webdriver.Chrome();
        elif browserType == BrowserOptions.FIREFOX.value:
            newBrowser = webdriver.Firefox()
        elif browserType == BrowserOptions.EDGE.value:
            newBrowser = webdriver.Edge()
        elif browserType == BrowserOptions.SAFARI.value:
            newBrowser = webdriver.Safari()
        else:
            newBrowser = webdriver.Chrome()
        
        self.browser = newBrowser

    def getBrowser(self):
        return self.browser
    
    def closeBrowser(self):
        self.browser.close()

    def goToPage(self, page: str):
        self.browser.get(page)

class BrowserOptions(Enum):
    CHROME = 'Chrome'
    FIREFOX = 'Firefox'
    EDGE = 'Edge'
    SAFARI = 'Safari'