from simple_term_menu import TerminalMenu
import os

def checkExtensions(list):
    for i, browser in enumerate(list):
        base, ext = os.path.splitext(browser)
        if ext is None:
                list.remove(browser)
                break
        list[i] = base
        print(base)


browserList = checkExtensions(os.listdir('./src/browser'))
routineList = checkExtensions(os.listdir('./src/routines'))

print(checkExtensions(browserList))
print(checkExtensions(routineList))

menu = TerminalMenu(browserList)
menu = TerminalMenu(routineList)
a = menu.show()

