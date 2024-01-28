from simple_utils import start_text_ui, quick_plot
from General_Calculator import *
from matplotlib import pyplot as plt


if __name__ == "__main__":
    years, probability = start_text_ui()
    start_year = input("Enter the starting year (default: 1991): ")
    start_year = int(start_year) if start_year else 1991
    end_year = input("Enter the ending year (default: 2021): ")
    end_year = int(end_year) if end_year else 2021
    first_acc = calculate_first_accident_prob(probability, start_year, end_year)
    fig = quick_plot(years[(start_year - 1991) : (end_year - 1991 + 1)], first_acc, probability.return_relative_prob()[(start_year - 1991) : (end_year - 1991 + 1)])
    plt.show()
