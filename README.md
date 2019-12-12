# advent of code 2019
This is a collection of my solutions (and try-outs) for the [Advent of Code 2019](https://adventofcode.com) challenges in Python. 

## What is Advent of Code?
[Advent of Code](http://adventofcode.com) is a yearly advent calender of small programming puzzles for a variety of skill sets and skill levels that can be solved in any liked language, created by [Eric Wastl](https://twitter.com/ericwastl).

## Progress

| Day  | Part One | Part Two | 
|---|:---:|:---:|
|**Day 1**: [The Tyranny of the Rocket Equation](https://adventofcode.com/2019/day/1)|[⭐️](https://github.com/Paulinovich/advent-of-code-2019/blob/master/day1/part1/adventOfCode_day1.1.py)|[⭐️](https://github.com/Paulinovich/advent-of-code-2019/blob/master/day1/part2/adventOfCode_day1.2.py)|
|**1**:   To determine the required amount of fuel to bring Santa back to earth, we need to calculate the fuel needed for the mass of each module (mass divided by three, round down, and 2 subtracted) and add them together.
**2**:   Fuel itself requires fuel just like a module and needs to be added to the calculation for each module. Any mass that would require negative fuel should instead be treated as if it requires zero fuel.|||
|**Day 2**: [2: 1202 Program Alarm](https://adventofcode.com/2019/day/2)|[⭐️](https://github.com/Paulinovich/advent-of-code-2019/blob/master/day2/part1/adventOfCode_day2.1.py)|[⭐️](https://github.com/Paulinovich/advent-of-code-2019/blob/master/day2/part2/adventOfCode_day2.2.py)|
|**1**: After our computer got fire, we have to write a program to read an Intcode program after it's restored to the '1202 program' state. The program consists of intervals of 4 integers: the operator(1 = +, 2 = \*), the index of the first value, index of the second value, index where to store the result. Returned should be the number at the first position of the program after being run.
**2**: We need to determine what pair of inputs at index 1 and 2 produces the output 19690720 and return the result of a calculation with these 2 numbers. Each of the two input values will be between 0 and 99, inclusive.|||
|**Day 3**: [Crossed Wires](https://adventofcode.com/2019/day/3)|[💫](https://github.com/Paulinovich/advent-of-code-2019/blob/master/day3/part1/adventOfCode_day3.1.py)||
|**1**: To fix the electricity circuit, we need to find the intersection point of two wires closest to the central port following the Manhattan Distance calculation. The wires' path is given as a list of commands containing a direction and the steps (e.g. U365 for up 365 steps. We should return the distance of the closest path crossing.|||
|**Day 4**: [Secure Container](https://adventofcode.com/2019/day/4)|[⭐️](https://github.com/Paulinovich/advent-of-code-2019/blob/master/day4/part1/adventOfCode_day4.1.py)|[💫](https://github.com/Paulinovich/advent-of-code-2019/blob/master/day4/part2/adventOfCode_day4.2.py)|
|**1**: The password of the fuel depot is forgotten, we only remember a few facts about the passwort: The number is between 197487 and 673251, contains a pair of equal adjacent digits, and the digits do not decrease from left to right. We should find the amount of possibilities.
**2**: An Elf just remembered one more important detail: one pair of two adjacent matching digits is not part of a larger group of matching digits. We have to update the possibilities.|||
