import json
from configreader import getConfig
from browser.selenium import ScrapeGoatBrowser

from routines.simple_login import SimpleLoginRoutine

config = getConfig()

customBrowser = ScrapeGoatBrowser('Chrome');

SimpleLoginRoutine(customBrowser, True)
input()