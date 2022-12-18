import os
import importlib
from loguru import logger
from simple_term_menu import TerminalMenu
from sortedcontainers import SortedDict
from browser.selenium import ScrapeGoatBrowser, BrowserOptions
from configreader import saveConfig, getConfig

global selectedBrowser
global selectedBrowserName
global selectedRoutines

def configMock():
    global selectedBrowser
    global selectedRoutines
    if 'selectedBrowser' not in globals():
        selectedBrowser = 'None'
    if 'selectedRoutines' not in globals():
        selectedRoutines = 'None'

def loadCliSettings():
    cli_config = getConfig()['cli']
    global selectedBrowser
    global selectedBrowserName
    global selectedRoutines

    if 'selectedRoutines' not in globals():
        selectedRoutines = cli_config['selected_routines']
    if 'selectedBrowserName' not in globals():
        selectedBrowserName = cli_config['selected_browser']
        if selectedBrowserName not in BrowserOptions.list():
            selectedBrowserName = BrowserOptions.CHROME.value
    if 'selectedBrowser' not in globals():
        selectedBrowser = ScrapeGoatBrowser(browserType=selectedBrowserName)

def saveCliSettings():
    global selectedBrowser
    global selectedRoutines
    config = getConfig()
    config['cli']['selected_browser'] = selectedBrowser.browser.name.capitalize()
    config['cli']['selected_routines'] = selectedRoutines
    saveConfig(config)

def checkExtensions(items_list):
    result_list = []
    for i, browser in enumerate(items_list):
        base, ext = os.path.splitext(browser)
        if ext is None or '__' in browser:
            continue
        else:
            result_list.append(base)
    return result_list

browserList = checkExtensions(os.listdir('./src/browser'))
routineList = checkExtensions(os.listdir('./src/routines'))

def listBrowser():
    global selectedBrowser
    global selectedBrowserName
    
    menuItems = prepareShortcuts(BrowserOptions.list())

    driver_menu = TerminalMenu(menuItems)
    driver_menu.show()

    selectedBrowser.closeBrowser()
    selectedBrowser = ScrapeGoatBrowser(
        browserType=driver_menu.chosen_menu_entry)
    selectedBrowserName = driver_menu.chosen_menu_entry
    saveCliSettings()
    logger.info('New browser selected: {} !'.format(selectedBrowserName))
    mainMenu()

def listRoutines():
    global selectedRoutines
    driver_menu = TerminalMenu(routineList, multi_select=True, preselected_entries=selectedRoutines, show_multi_select_hint=True, multi_select_select_on_accept=False, multi_select_empty_ok=True)
    driver_menu.show()

    selectedRoutines = driver_menu.chosen_menu_entries
    saveCliSettings()
    logger.info('New routines selected: {}!'.format(selectedRoutines))
    mainMenu()

def prepareShortcuts(items):
    menu_list = []
    for item in items:
        string = "[{}] {}".format(item[0].lower(), item)
        menu_list.append(string)
    return menu_list


def convert_class(class_name):
    parts = [part.title() for part in class_name.split("_")]
    return "".join(parts) + "Routine"


def execRoutines():
    logger.info('Initating routines...')

    try:
        class_names = ['simple_login']
        for routine_class_name in class_names:
            module = importlib.import_module('routines' + '.' + routine_class_name)
            module = getattr(module, convert_class(routine_class_name))
            module(browser=selectedBrowser, autoRun=True)
    except Exception as e:
        logger.error('Exception while executing routines: ', e)
        exit_cli()
    finally:
        logger.info('Done with routines!')
        mainMenu()

def exit_cli():
    global selectedBrowser
    selectedBrowser.closeBrowser()
    quit()

def mainMenu():
    global selectedBrowser
    global selectedRoutines

    loadCliSettings()
    mm_options = SortedDict()
    mm_options[0] = "[d] Driver selection"
    mm_options[1] = "[e] Execute routines"
    mm_options[2] = "[r] Select routines"
    mm_options[3] = "[q] Quit"

    try:
        current_config = "\n Current Driver: {}, selected routines: {}".format(
            selectedBrowserName, selectedRoutines)
    except KeyError:
        print('Missing configuration')

    menu = TerminalMenu(mm_options.values(), title="Main Menu \n", accept_keys=[
                        "d", "e", "r", "enter"], status_bar=current_config)
    menu.show()

    if menu.chosen_menu_index == 0:
        listBrowser()
    elif menu.chosen_menu_index == 1:
        execRoutines()
    elif menu.chosen_menu_index == 2:
        listRoutines()
    elif menu.chosen_accept_key == 'q' or menu.chosen_menu_index == 3:
        exit_cli()
