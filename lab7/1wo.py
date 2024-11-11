from itertools import chain
def unpack(n):
    r = []
    q = [n]
    while len(q) > 0:
        n = q[-1]
        del q[-1]
        match type(n).__name__:
            case 'list' | 'tuple' | 'set': q.extend(n)
            case 'dict':
                q.extend(list(n.keys()))
                q.extend(list(n.values()))
            case _: r.append(n)
    return r[::-1]

print(unpack([None, [1, ({2, 3}, {'foo': 'bar'})]]))
