#!/usr/bin/env python3

permutation = input('Put your permutation string (i.e. \"1 2 3 4\"): ')
permutation = permutation.split()

columns = len(permutation)
num_switches = 0
for num in permutation:
    place = permutation.index(num)
    for other in range(1, columns + 1):
        if (permutation.index(str(other)) < place and int(other) > int(num)) or (permutation.index(str(other)) > place and int(other) < int(num)):
            num_switches += 1
print(num_switches/2, 'switches')

# This version didn't work since it didn't count the correct attribute
# num_switches = 0
# for num in permutation:
#     extra_ahead = permutation.index(num) - int(num) + 1
#     if extra_ahead < 0:
#         extra_ahead = 0  # If it's negative then we've double counted
#     num_switches += extra_ahead
# print(num_switches, 'switches')
