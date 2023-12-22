import pandas
import json
import numpy as np
from matplotlib import pyplot as plt
from General_Calculator import *


def get_save_key_selection(question: str, dictionary: dict) -> str:
    """
    Asks the user the question and validates whether the answer is a correct key from the dictionary provided.
    :param question: The Question to ask
    :param dictionary: The dictionary to validate the answer
    """
    selection = input(question)
    while selection not in dictionary:
        print("You made an illegal selection")
        selection = input(question)

    return selection


class DeathCalculator:
    def __init__(self, reference_path: str, deaths_path: str, hierarchy_path: str):
        self.reference = pandas.read_csv(reference_path, sep=';')
        self.deaths = pandas.read_csv(deaths_path, sep=';')
        hierarchy_file = open(hierarchy_path)
        hierarchy = json.load(hierarchy_file)
        self.deaths_hierarchy = hierarchy.get("Deaths -")
        hierarchy_file.close()
        self.num_of_years = self.reference.shape[0]

    def starting_point(self):
        # The questions are made based on the entries in the feature_hierarchy
        question_1 = "What is your age?"
        age_hierarchy: dict = self.deaths_hierarchy.get("age -")
        for key in age_hierarchy.keys():
            question_1 += "\"" + key + "\", "

        age_key = get_save_key_selection(question_1, age_hierarchy)

        question_2 = "What do you drive? \"car\", \"trucks\", \"pedestrians\""
        vehicle_key = input(question_2)
        while vehicle_key != "car" and vehicle_key != "trucks" and vehicle_key != "pedestrians":
            print("You made an illegal selection")
            vehicle_key = input(question_2)


        question_3 = "What is your sex?"
        sex_hierarchy: dict = self.deaths_hierarchy.get("sex -")
        for key in sex_hierarchy.keys():
            question_3 += "\"" + key + "\", "

        sex_key = get_save_key_selection(question_3, sex_hierarchy)

        # Here the probabilities from the dataset are put into UiInterface
        # First into the ProbPair class
        age_probability = ProbPair(self.deaths[age_key], self.reference[self.deaths_hierarchy.get("age -").get(age_key).get("reference")])
        vehicle_probability = ProbPair(self.deaths[vehicle_key], self.reference[self.deaths_hierarchy.get("vehicle -").get(vehicle_key).get("reference")])
        sex_probability = ProbPair(self.deaths[sex_key], self.reference[self.deaths_hierarchy.get("sex -").get(sex_key).get("reference")])

        # And then the probabilities are combined with AndCombined, because they are from different categories.
        combined_prob = AndCombination([age_probability, vehicle_probability, sex_probability])

        first_prob = calculate_first_accident_prob(combined_prob)
        self.visualize_probabilities(first_prob)


    def visualize_probabilities(self, probability: np.ndarray):
        fig, ax = plt.subplots()

        ax.plot(self.reference["Year"], probability, color="green", label="probability of first accident in year x")
        ax.legend(loc="upper right")
        plt.show()



if __name__ == '__main__':
    ref_path = "../dataset/csv/reference_number.csv"
    death_path = "../dataset/csv/Deaths.csv"
    hierarchy_path = "../dataset/csv/reduced_feature_hierarchy.json"
    calc = DeathCalculator(ref_path, death_path, hierarchy_path)

    calc.starting_point()
