SG_MISSING_BROWSER_CONFIGURATION = lambda browser, routine: "No configuration present for browser '{}' in this routine, please check your configuration".format(browser, routine)
SG_MISSING_ELEMENT_GENERIC_ROUTINE_ERROR =  lambda error: "At least one element was not located in the page, please check the id. \n Error: {}".format(error.msg)
SG_EXECUTION_ERRO_ROUTINE_GENERIC = lambda routineName, err: "Error executing '{}' routine. \n Error: {}".format(routineName, err)
SG_GENERIC_ROUTINE_SUCCESS = lambda routineName: "Routine '{}' is done executing!.".format(routineName)
SG_GENERIC_ROUTINE_START = lambda routineName: "Initiating routine execution for {} routine".format(routineName)