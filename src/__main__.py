from configreader import getConfig
from browser.selenium import SeleniumBrowser

from routines.simple_login import SimpleLoginRoutine

customBrowser = SeleniumBrowser('Firefox');

SimpleLoginRoutine(customBrowser, True)