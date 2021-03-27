arr = [['-', '*', '-', '-', '-', '-', '-', '-', '-'],
       ['*', '-', '-', '-', '*', '-', '*', '-', '-'],
       ['-', '*', '-', '-', '*', '*', '*', '-', '*'],
       ['*', '*', '-', '*', '*', '*', '*', '-', '*']]


def sort(tree):
    start_index = len(tree[0])//2
    stars_count = 1
    for row in tree:
        free_spaces_indices = []
        free_stars_indices = []
        end_index = start_index + stars_count
        for i in range(start_index):
            if row[i] == '*':
                free_stars_indices.append(i)
        for i in range(start_index, end_index):
            if row[i] == '-':
                free_spaces_indices.append(i)
        for i in range(end_index, len(row)):
            if row[i] == '*':
                free_stars_indices.append(i)
        for i in range(len(free_spaces_indices)):
            row[free_stars_indices[i]] = '-'
            row[free_spaces_indices[i]] = '*'
        start_index -= 1
        stars_count += 2


sort(arr)
for item in arr:
    print(item)
