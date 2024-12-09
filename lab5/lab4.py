def field(items, *args):
    if not args:
        return

    for j in items:
        if len(args) == 1:
            if args[0] in j and j[args[0]] is not None:
                yield j[args[0]]
        else:
            ans = {}
            for i in args:
                if i in j and j[i] is not None:
                    ans[i] = j[i]
            if ans:
                yield ans
