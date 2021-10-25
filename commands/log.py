def log_function(func: str, ctx):
    print("\n [!] Command \'" + func + "\' issued in "+ ctx.guild.name+"\n")

def log_error(func: str, error_msg: str):
    print(f" [!!] Error in \'{func}\'\n      * {error_msg}")
