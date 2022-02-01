import random

def even_or_odd(sample_list: list) -> None:
    '''Determines if each item in a given list is even or odd and prints that to the terminal'''
    for num in sample_list:
        if num%2 == 0:
            print(f'{num} is even')
        else:
            print(f'{num} is odd')

if __name__ == '__main__':
    my_list = []
    for _ in range(10):
        my_list.append(int(random.random()*100))
    even_or_odd(my_list)
