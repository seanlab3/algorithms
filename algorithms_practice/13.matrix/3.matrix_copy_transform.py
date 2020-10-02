from algorithms.matrix.copy_transform import rotate_clockwise,rotate_counterclockwise,top_left_invert,bottom_left_invert

def print_matrix(matrix, name):
    print('{}:\n['.format(name))
    for row in matrix:
        print('  {}'.format(row))
    print(']\n')


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print_matrix(matrix, 'initial')
print_matrix(rotate_clockwise(matrix), 'clockwise')
print_matrix(rotate_counterclockwise(matrix), 'counterclockwise')
print_matrix(top_left_invert(matrix), 'top left invert')
print_matrix(bottom_left_invert(matrix), 'bottom left invert')
