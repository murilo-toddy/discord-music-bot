def log_function(func: str):
    print("\n [!] Command \'" + func + "\' issued\n")

def log_error(func: str, error_msg: str):
    print(f" [!!] Error in \'{func}\'\n      * {error_msg}")