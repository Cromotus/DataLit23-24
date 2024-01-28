from simple_utils import start_text_ui, quick_plot, quick_multi_plot
from General_Calculator import *


def get_multi_plot(title="First Accident Probability", plot_name=None):
    number_of_plots = int(input("How many prompts do you want to combine?"))
    data_name_pair = []
    for _ in range(number_of_plots):
        years, probability, accident_key = start_text_ui()
        first_acc_property = calculate_first_accident_prob(probability)
        data_name_pair.append((first_acc_property, accident_key))

    quick_multi_plot(years, data_name_pair, title=title, file_name=plot_name)


def solo_plot(title="First Accident Probability", plot_name=None):
    years, probability, _ = start_text_ui()
    first_acc_property = calculate_first_accident_prob(probability)
    quick_plot(years, first_acc_property, title=title, file_name=plot_name)


if __name__ == '__main__':
    # solo_plot(title="Cars being the Main Causer", plot_name="cars_main_cause.pdf")
    get_multi_plot(title="Generations Main Causer", plot_name="cars_main_causer.pdf")
