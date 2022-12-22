from random import sample


def generate_list():
    list_len = 10
    rand_list = sorted(sample(range(0, 101, 2), list_len))
    return rand_list


def find_occurrence(list_, target):
    left, right = 0, len(list_) - 1
    while left <= right:
        middle = (left + right) // 2
        if list_[middle] < target:
            left = middle + 1
        elif list_[middle] > target:
            right = middle - 1
        else:
            return middle
    return


def checking_input(target):
    try:
        if int(target) not in range(101):
            raise ValueError
    except ValueError:
        print('Invalid input')
        exit()


def main():
    target_for_search = input('Pick a number between 0-100: ')
    checking_input(target_for_search)

    rand_list = generate_list()
    print(f'List: {rand_list}')

    result_search = find_occurrence(rand_list, int(target_for_search))

    if result_search:
        print(f'Found {target_for_search} in index {result_search}')
    else:
        print(f'Cannot find {target_for_search} in the list')


if __name__ == "__main__":
    main()
