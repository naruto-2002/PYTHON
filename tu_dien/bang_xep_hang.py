import functools

def cmp(a, b):
    if a['submit_AC'] == b['submit_AC']:
        return a['submitted'] - b['submitted']
    return b['submit_AC'] - a['submit_AC']


t = int(input())
lsv = []
while(t > 0):
    t -= 1
    name = input()
    submit_AC, submitted = map(int, input().split())
    lsv.append({
        'name': name,
        'submit_AC': submit_AC,
        'submitted': submitted
    })
lsv.sort(key=functools.cmp_to_key(cmp))
for sv in lsv:
    print(sv['name'], sv['submit_AC'], sv['submitted'], sep = ' ')
