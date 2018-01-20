# Knapsack Generic Algorithm
Solve the knapsack problem by genetic algorithm written in python 2.7

## Usage
```
Usage: main.py [options]

Options:
  -h, --help                                      show this help message and exit
  -t THRESHOLD, --threshold=THRESHOLD             number of generation with no change. Default 1000
  -s SIZE, --size=SIZE                            number of chromosomes in population. Default 20
  -e ELITISM, --elitism=ELITISM                   percentage of chromosomes that will survive to next
                                                  generation. Between 0 and 1. Default 0.2
  -w MAXWEIGHT, --max_weight=MAXWEIGHT            max weight of knapsack. Default 1000
  -m MUTATIONRATE, --mutation_rate=MUTATIONRATE   rate of chromosome mutation. From 0 to 1. Default 0.7
  -i DISPLAYINTERVAL, --interval=DISPLAYINTERVAL  interval between generations to display information. Default 10
```

