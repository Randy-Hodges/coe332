import copy

def column_printer(*args):
    '''prints out the values of the given items in columns'''
    column_width = 4
    for lst in args:
        for num in lst:
            space_buffer = column_width - len(str(num))
            if (space_buffer < 0):
                space_buffer = 0
            space_buffer = space_buffer*' '
            print(f'|{num}{space_buffer}', end='')
        print('|')

def three_list_generator() -> None:
    '''Generates three lists: list1 with values 1-10, and 2 others which are the squares and cubes of list1. The values are printed.'''
    list1 = []
    for i in range(1, 11):
        list1.append(i)

    list2 = copy.deepcopy(list1)
    list3 = copy.deepcopy(list1)

    for idx, value in enumerate(list2):
        list2[idx] = value**2

    for idx, value in enumerate(list3):
        list3[idx] = value**3

    column_printer(list1, list2, list3)

if __name__ == '__main__':
   three_list_generator()
