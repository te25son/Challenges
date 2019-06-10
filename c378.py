'''
Challenge 378:
https://www.reddit.com/r/dailyprogrammer/comments/bqy1cf/20190520_challenge_378_easy_the_havelhakimi/
'''

def remove_zeros(sequence):
    return [num for num in sequence if num != 0]

def sort_descending(sequence):
    return sorted(sequence, reverse=True)

def number_greater_than_length_of_sequence(num, sequence):
    return num > len(sequence)

def subtract_one_from_first_n_number_of_items(num, sequence):
    return_list = []
    for pos, item in enumerate(sequence):
        if pos in range(0, num):
            return_list.append(item - 1)
        else:
            return_list.append(item)
    return return_list

def havel_hakimi_algorithm(sequence):
    sequence = remove_zeros(sequence)
    if sequence:
        sequence = sort_descending(sequence)
        largest_num = sequence.pop(0)
        if number_greater_than_length_of_sequence(largest_num, sequence):
            return False
        else:
            sequence = subtract_one_from_first_n_number_of_items(largest_num, sequence)
            return havel_hakimi_algorithm(sequence)
    return True
