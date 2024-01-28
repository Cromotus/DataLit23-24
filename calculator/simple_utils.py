from filters import Filters
from DataLoader import DataContainer
from General_Calculator import ProbPair
from matplotlib import pyplot as plt
from tueplots import bundles
from tueplots.constants.color import rgb


def start_text_ui():
    """
    simple text based UI to test the system independent of the visual UI
    """
    filters_container = Filters(config_path="../dataset/filter-configuration.json")
    data_container = DataContainer()

    while filters_container.has_next_question():
        current_question = filters_container.get_next_question()
        answer = input(str(current_question) + "\n")
        filters_container.set_question_answer(current_question.question_key, answer)

    csv_name, column_name = filters_container.get_resulting_dataset()
    # returning the years and the ProbPair from the data_container
    return data_container.all_references["Year"], data_container.data[csv_name][column_name]


def quick_plot(years, first_acc_data, yearly_prob):
    plt.rcParams.update(bundles.icml2022(column="full", usetex=False))

    fig, ax = plt.subplots()
    # fig.suptitle("Probability of first accident")
    ax.plot(years, first_acc_data, color=rgb.tue_red, label=f"Probability of first accident starting {years.values[0]}")
    ax.bar(years, yearly_prob, color=(*rgb.tue_blue, 0.3), label="Yearly Probability of accident")
    ax.grid()
    ax.set_ylabel("Probability of accident")
    ax.set_xlabel("Year")
    ax.set_ylim(0, 1.1 * max(max(first_acc_data), max(yearly_prob)))
    ax.set_xlim(years.values[0] - 1, years.values[-1] + 1)
    ax.legend()
    return fig


if __name__ == "__main__":
    start_text_ui()
