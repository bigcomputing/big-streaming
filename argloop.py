def processArgs(args):
    options=[]
    for arg in args:
        if arg[:1] == '-':
            options.append(arg)
    return options
