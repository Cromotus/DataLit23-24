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
    fig.suptitle("Probability of first accident")
    ax.plot(years, first_acc_data, color=rgb.tue_red)
    ax2 = ax.twinx()
    ax2.bar(years, yearly_prob, color=(*rgb.tue_blue, 0.3))
    ax2.set_ylabel("probability of accident in that year")
    ax.grid()
    ax.set_ylabel("probability of first accident")
    ax.set_xlabel("Year")

    return fig
    # plt.show()

    #plt.savefig("test.pdf")


if __name__ == '__main__':
    start_text_ui()
