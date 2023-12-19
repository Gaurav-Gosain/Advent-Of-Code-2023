# Day 19, FIRST TOP 100!!! 🎅

from collections import namedtuple

fls = {}
flsls, pls = [
    line.split('\n') for line in open(0).read().strip().split('\n\n')
]

for l in flsls:
    name, r = l.split('{')
    r = r[:-1]
    fls[name] = [step.split(':') for step in r.split(',')]

s = 0
pt = namedtuple('part', list('xmas'))
for l in pls:
    p = eval(f'pt({l[1:-1]})')
    fl = 'in'
    while fl not in 'AR':
        for *cond, res in fls[fl]:
            if not cond:
                fl = res
                break
            cond, = cond
            if eval('p.'+cond.replace('=','==')):
                fl = res
                break
    if fl == 'A':
        s += sum(p)
print("Part 1:", s)

for l in flsls:
    name, r = l.split('{')
    r = r[:-1]
    fls[name] = [step.split(':') for step in r.split(',')]

pt = namedtuple('part', list('xmas'))
def solution(fl, mins, maxes):
    if fl == 'R':
        return 0
    if fl == 'A':
        return (1 + maxes.x - mins.x) * (1 + maxes.m - mins.m) * (1 + maxes.a - mins.a) * (1 + maxes.s - mins.s)
    s = 0
    for *cond, res in fls[fl]:
        if not cond:
            s += solution(res, mins, maxes)
        else:
            cond, = cond
            op = cond[1]
            var = cond[0]
            val = int(cond[2:])
            if op == '=':
                s += solution(res,
                            mins._replace(**{var: val}),
                            maxes._replace(**{var: val}))
                s += solution(res,
                            mins._replace(**{var: val + 1}),
                            maxes)
                maxes = maxes._replace(**{var: val - 1})
            elif op == '<':
                s += solution(res,
                            mins,
                            maxes._replace(**{var: val - 1}))
                mins = mins._replace(**{var: val})
            elif op == '>':
                s += solution(res,
                            mins._replace(**{var: val + 1}),
                            maxes)
                maxes = maxes._replace(**{var: val})
            else:
                assert False
    return s

print("Part 2:", solution('in',
                pt(1, 1, 1, 1),
                pt(4000, 4000, 4000, 4000)))
                