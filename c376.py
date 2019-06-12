'''
Challenge 376
https://www.reddit.com/r/dailyprogrammer/comments/b0nuoh/20190313_challenge_376_intermediate_the_revised/
'''

def num_of_leap_years(year1, year2):
    years = 0
    for year in range(year1, year2):
        if year % 4 == 0 and year % 100 != 0:
            years += 1
        elif year % 900 == 200 or year % 900 == 600:
            years += 1
        else:
            pass
    return years
