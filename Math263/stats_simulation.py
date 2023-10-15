# Random chance generator for stats
from random import randint
import matplotlib.pyplot as plt


def spinners():
    for i in range(5):  # Number of sets
        set1 = []
        for j in range(200):  # Equivalent to number of simulations ran
            random_choice = randint(1, 200)
            set1.append(random_choice)
            # Counting how many times the number has appeared. So for the range(1, 200), 200 simulations are run where the computer looks for numbers 1 - 199 each time and counts how many times it appears.
            # for k in range(1, 200):
            variable_count = set1.count(j)
            proportion_of_success = variable_count / len(set1)
            #variable_count2 = set1.count(2)
            #variable_count3 = set1.count(3)
            print("\nThe number of times that the number " + str(j) + " has appeared:",
                  variable_count)
            print("Proportion of success:", proportion_of_success)
        #print("\nThe number of times that the number 2 has appeared:", variable_count2)
        #print("\nThe number of times that the number 3 has appeared:", variable_count3)
        # print(set1)
        #print("Length of set"+str(i)+":", len(set1))


def chance_simulation():
    probability = input("Enter a decimal: ")
    sample_size = input("Sample size: ")
    number_of_simulations = input("Number of tries :")
    choice_of_simulations = input(
        "Proportion of success or number count? Enter 'P' or'C': ")


spinners()

# chance_simulation()
