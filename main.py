from optparse import OptionParser
from Population import Population


def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser()
    parser.add_option("-t", "--threshold", type="int", dest="threshold", default=1000,
                      help="number of generation with no change. Default 1000")
    parser.add_option("-s", "--size", type="int", dest="size", default=20,
                      help="number of chromosomes in population. Default 20")
    parser.add_option("-e", "--elitism", type="float", dest="elitism", default=0.2,
                      help="percentage of chromosomes that will survive to next generation. Between 0 and 1. Default 0.2")
    parser.add_option("-w", "--max_weight", type="int", dest="maxWeight", default=1000,
                      help="max weight of knapsack. Default 1000")
    parser.add_option("-m", "--mutation_rate", type="float", dest="mutationRate", default=0.7,
                      help="rate of chromosome mutation. From 0 to 1. Default 0.7")
    parser.add_option("-i", "--interval", type="int", dest="displayInterval", default=10,
                      help="interval between generations to display information. Default 10")

    (options, args) = parser.parse_args()

    if options.threshold <= 0:
        parser.error("-t threshold must greater than zero")
    if options.size <= 0:
        parser.error("-s size must greater than zero")
    if options.elitism <= 0 or options.elitism >= 1:
        parser.error("-e elitism must between 0 and 1")
    if options.maxWeight <= 0:
        parser.error("-w max weight must greater than zero")
    if options.mutationRate < 0 or options.mutationRate > 1:
        parser.error("-m mutation rate must from 0 to 1")
    if options.displayInterval <= 0:
        parser.error("-i display interval must greater than zero")

    population = Population(options.size, options.elitism, options.maxWeight, options.mutationRate)
    population.run(threshold=options.threshold, displayInterval=options.displayInterval)


if __name__ == "__main__":
    main()