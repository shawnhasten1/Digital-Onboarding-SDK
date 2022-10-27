import json

def formatArgs(locals, json_dump=True):
    args = []
    for param in locals.keys():
        args.append(param)
    payload = {}
    for arg in args:
        #try:
        if arg != 'self' and arg != 'args' and locals.get(arg) != None:
            arg_key = arg
            if 'contact_' in arg:
                arg_key = arg.replace('contact_', 'contact.')
            if 'product_' in arg:
                arg_key = arg.replace('product_', 'product.')
            val = locals.get(arg)
            if type(val) == bool:
                val = '1' if val else '0'
            payload[arg_key] = val
        #except:
        #    pass
    if json_dump:
        return json.dumps(payload)
    return payload