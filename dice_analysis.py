import decimal
import itertools
import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def find_roll_spread(xaxis, yaxis):
    percentage_chart = create_percentage_chart(xaxis, yaxis)
    print(percentage_chart.to_string())
    create_plot(percentage_chart)

def print_min_mean_max(num_dice, num_sides):
    min = num_dice
    mean = int((num_sides+1)/2 * num_dice)
    max = num_dice * num_sides

    print(f'rolled {num_dice}D{num_sides}')
    print(f'the minimum roll is {min}')
    print(f'the average roll is {mean}')
    print(f'the maximum roll is {max}')

def full_theoretical_distribution(num_dice, num_sides):
    def first_binomial_coff(k):
        return decimal.Decimal(math.factorial(num_dice))/decimal.Decimal((math.factorial((num_dice-k)))*decimal.Decimal(math.factorial(k)))

    def second_binomial_coff(k, total):
        return decimal.Decimal(math.factorial((total-num_sides*k-1)))/(decimal.Decimal(math.factorial((total-num_sides*k-num_dice)))*decimal.Decimal(math.factorial((num_dice-1))))

    def prob_of_each_num(total):
        Probof6thsidedDiceto_n = decimal.Decimal((1/num_sides))**num_dice
        total_prob = decimal.Decimal(0)
        for k in range(0, int(((total-num_dice)/num_sides)+1)):
            num_to_add = ((-1)**k)*first_binomial_coff(k)*second_binomial_coff(k,total)*Probof6thsidedDiceto_n
            total_prob = total_prob + num_to_add

        total_prob = round(total_prob, 4)
        return total_prob

    roll_total_range = range(num_dice, num_dice*num_sides+1)
    distribution = np.zeros(len(roll_total_range)) 
    for index, roll_total in enumerate(range(num_dice,num_dice*num_sides+1)):
        distribution[index] = prob_of_each_num(roll_total)
    return (roll_total_range, distribution)

def add_distributions(distributions):
    lowest = 0
    highest = 0
    for distribution in distributions:
        lowest += distribution[0][0]
        highest += distribution[0][-1]
    
    roll_range = [x for x in range(lowest, highest+1)]
    roll_distribution = [0 for x in range(lowest, highest+1)]

    ranges = [distribution[0] for distribution in distributions]
    all_combos = itertools.product(*ranges)
    for combo in all_combos:
        prod = 1
        total = 0
        for index, num in enumerate(combo):
            lowest_num = distributions[index][0][0]
            prod *= distributions[index][1][num-lowest_num]
            total += num
        roll_distribution[total-lowest] += prod
    
    return (roll_range, roll_distribution)
    
def create_percentage_chart(roll_total_range, distribution):
    
    zero_to_min_roll = range(0, roll_total_range[0])
    distribution_to_min_roll = [0 for x in zero_to_min_roll]
    distribution = [*distribution_to_min_roll, *distribution]
    roll_total_range = [*zero_to_min_roll, *roll_total_range]
    
    percentage = ['' for x in range(0,len(distribution))]
    for index, num in enumerate(distribution):
        percentage[index] = '{:.2%}'.format(num)

    return pd.DataFrame({"total": roll_total_range, "percent":percentage, "probability":distribution})

def create_plot(percentage_chart):
    sns.set_theme()
    sns.lineplot( 
        data=percentage_chart,
        x='total', y='probability',
    )
    plt.show()

def main():
    num_dice = ''
    while True:
        num_dice = input('How many dice (or quit to exit)? ')
        if num_dice == 'quit':
            print('Now Exiting')
            break

        num_sides = input('How many sides per die? ')
        
        try:
            num_dice = int(num_dice)
            num_sides = int(num_sides)
            find_roll_spread(num_dice, num_sides)
        except Exception as e:
            print(e)
        
        print('\n')


decimal.getcontext().prec = 50