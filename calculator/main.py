from simple_utils import start_text_ui, quick_plot
from General_Calculator import *


if __name__ == '__main__':
    years, probability = start_text_ui()
    first_acc = calculate_first_accident_prob(probability)
    quick_plot(years, first_acc)
