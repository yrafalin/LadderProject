#!/usr/bin/env python3

def fix_rung(rung): return int(rung) - 1

num_inputs = input('How many inputs are there: ')
rung_order = input('Put your permutation string (i.e. \"3 2\" is a rung between 3 and 4 and then a rung under that between 2 and 3: ')
rung_order = rung_order.split()
rung_order = list(map(fix_rung, rung_order))

in_to_out = [x for x in range(1, int(num_inputs)+1)]
for switch in rung_order:
    prior = in_to_out[switch]
    in_to_out[switch] = in_to_out[switch + 1]
    in_to_out[switch + 1] = prior
print('The output would be', ''.join(list(map(str, in_to_out))))
