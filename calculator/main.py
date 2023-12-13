import pandas
import numpy as np
import matplotlib.pyplot as plt

class Calculator:
    def __init__(self, reference_path: str, accidents_path: str):
        self.reference = pandas.read_csv(reference_path, sep=';')
        self.accidents = pandas.read_csv(accidents_path, sep=';')
        self.num_of_years = self.reference.shape[0]


    def test_dataset(self):
        print(self.reference)
        print(self.accidents)
        print(self.num_of_years)

    def calculate_accident_prob(self):
        years = self.reference['Year'].to_numpy()
        total_registered_cars = self.reference['total registered vehicles'].to_numpy()
        total_accidents = self.accidents['Total'].to_numpy()

        yearly_prob = total_accidents / total_registered_cars
        prob_accident = np.array(
            [np.prod(1 - yearly_prob[:year_index]) * yearly_prob[year_index] for year_index in range(len(years))]
        )
        fig, ax = plt.subplots()

        ax.plot(years, prob_accident, color="green", label="probability of accident in year x")
        ax.plot(years, yearly_prob, color="red", label="yearly probability of accident")
        fig.savefig("test_plot.png")

        return prob_accident



if __name__ == '__main__':
    calc = Calculator("../dataset/csv/Reference Numbers.csv", "../dataset/csv/Accident Numbers.csv")
    prob = calc.calculate_accident_prob()
    print(prob)