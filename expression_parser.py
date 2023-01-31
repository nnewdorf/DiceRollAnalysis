import re
import dice_analysis as da

def tokenize_input(inputString):
    tokens = inputString.split('+')
    tokens = list(map(lambda token: token.strip(), tokens))
    return tokens

def parse_dice_roll(inputString):
    result = re.match('(\d+)d(\d+)', inputString)
    if not result:
        raise Exception('Error parsing input string')

    return result.group(1), result.group(2)

def main():
    while True:
        inputString = input('Enter input string (or quit to exit)?')
        if inputString == 'quit':
            print('Now Exiting')
            break

        try:
            tokens = tokenize_input(inputString)
            distributions = []
            ints = []
            for token in tokens:
                if token.isdigit():
                    ints.append(int(token))
                else:
                    num_dice, num_sides = parse_dice_roll(token)    
                    num_dice = int(num_dice)
                    num_sides = int(num_sides)
                    distributions.append(da.full_theoretical_distribution(num_dice, num_sides))
            
            distribution = da.add_distributions(distributions)
            number = sum(ints)
            roll_range = list(map(lambda x : x+number, distribution[0]))
            roll_probability = distribution[1]
            
            da.find_roll_spread(roll_range, roll_probability)
        except Exception as e:
            print(e)

        print('\n')

main()