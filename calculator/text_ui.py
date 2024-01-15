from filters import Filters
from DataLoader import DataContainer
from General_Calculator import ProbPair


def start_text_ui():
    filters_container = Filters(config_path="../dataset/csv/filter-configuration.json")
    data_container = DataContainer()

    while filters_container.has_next_question():
        current_question = filters_container.get_next_question()
        answer = input(str(current_question) + "\n")
        filters_container.set_question_answer(current_question.question_key, answer)

    csv_name, column_name = filters_container.get_resulting_dataset()
    return data_container.data[csv_name]["Year"], ProbPair(data_container.data[csv_name][column_name],
                                                           data_container.data["Reference Numbers.csv"]["total registered vehicles"])


if __name__ == '__main__':
    start_text_ui()
