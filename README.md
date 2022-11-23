# Dice Analysis
A python script that determines the likelyhood of any total roll given a number of dice and sides per die.

## Usage

### Input
```
How many dice (or quit to exit)?
How many sides per die?
```
### Output
```
    total percent  decimal
0       0   0.00%   0.0000
1       1   100.00% 1.0000
...
rolled XDX
the minimum roll is X
the minimum roll is X
the minimum roll is X
```

A seaborn plot will also be showed. This plot must be closed before the program will prompt you for the next set of input.

## Aknowlegements
The majority of this code is taken from the following medium article by Tom Leyshon which goes in depth rm into the math used:
https://towardsdatascience.com/modelling-the-probability-distributions-of-dice-b6ecf87b24ea

## Known Issues
Python can only handle certain precisions for floating point numbers. The Decimal package was used to mitigate errors occuring because of this, but if the number of dice or sides get too large, errors might occur. Try increasing the Decimal percision to fix this.

## Future Enhancements
* Add the ability to add constants to dice roll
* Add ability to add 2 different types of dice together
* Create a regex parser for dice roll input (ie. 4d4 + 2 + 5d6)
