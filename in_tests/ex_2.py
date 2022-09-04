from operator import itemgetter
from random import choice
import sys
import time

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print('{0}  {1:2.2f} ms'.format(method.__name__, (te - ts) * 1000))
        return result
    return timed


with open('in_tests/input_4.txt', 'r') as f:
	 data = f.read().splitlines()

fights_num = int(data[0])
ninja_num = int(data[fights_num+1])

fights_list = [data[num] for num in range(1, fights_num+1)]
ninja_list = [data[num] for num in range(fights_num + 2, len(data))]

fights_rules = {fight.split(',')[0]: int(fight.split(',')[1]) for fight in fights_list}

def ninja_digit(rules):
    return {
        'name': rules[0],
        'fight': rules[1],
        'cata': int(rules[2]),
        'forfeit': int(rules[3]),
    }

ninja_rules = [ninja_digit(ninja.split(',')) for ninja in ninja_list]

heroes = []
for fight, num in fights_rules.items():
    ninjas = list(filter(lambda x: x['fight'] == fight, ninja_rules))
    table = sorted(ninjas, key=lambda item: (-item['cata'], item['forfeit']))
    ninjas_names = [ninja['name'] for ninja in table[:num]]
    heroes += ninjas_names

heroes = sorted(heroes)

@timeit
def list_to_file(heroes):
    with open('output.txt', 'w') as outfile:
        outfile.writelines(f'{s}\n' for s in heroes)

@timeit
def list_to_str(heroes):
    ans_str = "\n".join(map(str, heroes))
    print(ans_str)

list_to_file(heroes)
list_to_str(heroes)