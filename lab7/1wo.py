from itertools import chain
def unpack(n):
    r = []
    q = [n]
    while len(q) > 0:
        n = q[-1]
        del q[-1]
        print(r, '|||', n)
        if type(n) == str or type(n) == int:
            r.append(n)
            if len(q) < 1: break
            n = q[-1]
            del q[-1]
            continue
        for x in n:
            match type(x).__name__:
                case 'list' | 'tuple' | 'set':
                    print('lts:', list(x), q)
                    q.extend(list(x))
                case 'dict':
                    q.extend(list(x.keys()))
                    q.extend(list(x.values()))
                case _:
                    r.append(x)
    return r

print(unpack([None, [1, ({2, 3}, {'foo': 'bar'})]]))
