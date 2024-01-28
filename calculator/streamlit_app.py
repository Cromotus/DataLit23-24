from DataLoader import DataContainer
from filters import Filters
from General_Calculator import ProbPair, calculate_first_accident_prob
from simple_utils import quick_plot
import streamlit as st

# st.set_page_config(layout="wide")
st.title("German Vehicle Accident Probability Calculator")

filters_container = Filters(config_path="../dataset/filter-configuration.json")
data_container = DataContainer()


def func(current_question, counter):
    selection = st.selectbox(current_question.question_text,
                               [x for x in current_question.question_options], None, key=counter,
                               format_func=lambda x: x.option_text)
    return selection


counter = 1
current_question = filters_container.get_next_question()
s = func(current_question, counter)
while True:
    if s:
        filters_container.set_question_answer(current_question.question_key, s.option_key)
        if filters_container.has_next_question():
            counter += 1
            current_question = filters_container.get_next_question()
            s = func(filters_container.get_next_question(), counter)
        else:
            break


csv_name, column_name = filters_container.get_resulting_dataset()
years, yearly_probability = data_container.all_references["Year"], data_container.data[csv_name][column_name]
first_acc = calculate_first_accident_prob(yearly_probability)
st.pyplot(quick_plot(years, first_acc, yearly_probability.return_relative_prob()))
