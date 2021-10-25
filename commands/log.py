def log_function(func: str,ctx = None):
    if ctx ==None:
        print("\n [!] Command \'" + func + "\' issued\n")
    else:
        print("\n [!] Command \'" + func + "\' issued in "+ctx.guild.name+"\n")
    