import pandas
import numpy as np
from matplotlib import pyplot as plt


class Calculator:
    def __init__(self, reference_path: str, accidents_path: str):
        self.reference = pandas.read_csv(reference_path, sep=';')
        self.accidents = pandas.read_csv(accidents_path, sep=';')
        self.num_of_years = self.reference.shape[0]

    def test_dataset(self):
        print(self.reference)
        print(self.accidents)
        print(self.num_of_years)

    def start_point(self):
        question1 = "What accident do you want to analayze? Type the number\n["
        for key_index in range(1, len(self.accidents.columns)):
            question1 += self.accidents.columns[key_index] + " (" + str(key_index) + "), "

        question1 += "]\n"
        accident_class_index = input(question1)
        self.calculate_first_accident_prob(self.accidents.columns[int(accident_class_index)])

    def calculate_first_accident_prob(self, accident_class: str):
        years = self.reference['Year'].to_numpy()
        total_registered_cars = self.reference['total registered vehicles'].to_numpy()
        accidents = self.accidents[accident_class].to_numpy()

        yearly_prob = accidents / total_registered_cars
        prob_accident = np.array(
            [np.prod(1 - yearly_prob[:year_index]) * yearly_prob[year_index] for year_index in range(len(years))]
        )
        fig, ax = plt.subplots()

        ax.plot(years, prob_accident, color="green", label="probability of first accident in year x")
        ax.plot(years, yearly_prob, color="red", label="yearly probability of accident")
        ax.legend(loc="upper right")
        plt.show()

    def show_all_accidents(self):
        years = self.reference['Year'].to_numpy()
        total_registered_cars = self.reference['total registered vehicles'].to_numpy()
        fig, ax = plt.subplots()
        for key in self.accidents.keys():
            if key == "Year":
                continue
            accidents = self.accidents[key].to_numpy()

            yearly_prob = accidents / total_registered_cars
            prob_accident = np.array(
                [np.prod(1 - yearly_prob[:year_index]) * yearly_prob[year_index] for year_index in range(len(years))]
            )

            ax.plot(years, prob_accident, label=f"First {key} accident")

        ax.legend(loc="upper right")
        ax.set_ylabel("probability of first accident")
        ax.set_xlabel("Year")
        plt.show()


if __name__ == '__main__':
    calc = Calculator("../dataset/csv/Reference Numbers.csv", "../dataset/csv/Accident Numbers.csv")
    calc.show_all_accidents()