

def stringifyUserArguments(args, ex):
    if isinstance(args, list):
        return '[%s]' % ', '.join([stringifyUserArguments(x, ex) for x in args])
    elif isinstance(args, dict):
        return '{%s}' % ', '.join(['%s : %s' % (stringifyUserArguments(k, ex), stringifyUserArguments(v, ex)) for k, v in args.items()])
    elif isinstance(args, int):
        return str(args)
    elif isinstance(args, str):
        return "'%s'" % args
    raise ex('Function accepts only strings, integers, lists and lists thereof.')