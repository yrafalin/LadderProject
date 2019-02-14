#!/usr/bin/env python3

permutation = input('Put your permutation string (i.e. \"1 2 3 4\"): ')
permutation = permutation.split()

columns = len(permutation)
new_matrix = []
for num in permutation:
    zeros = ['0' for _ in range(columns)]
    zeros[int(num) - 1] = '1'
    mat_row = '[ ' + ' '.join(zeros) + ' ]\n'
    new_matrix.append(mat_row)
print(''.join(new_matrix))
