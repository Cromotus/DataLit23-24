from DataLoader import DataContainer
from filters import Filters
from General_Calculator import ProbPair, calculate_first_accident_prob
import matplotlib.pyplot as plt
from tueplots import bundles
from tueplots.constants.color import rgb
import streamlit as st

# st.set_page_config(layout="wide")
st.title("German Vehicle Accident Probability Calculator")

filters_container = Filters(config_path="../dataset/filter-configuration.json")
data_container = DataContainer()


def func(current_question, counter):
    s = st.selectbox(current_question.question_text, [x.option_key for x in current_question.question_options], None, key=counter)
    return s


def quick_plot(years, data):
    plt.rcParams.update(bundles.icml2022(column="full", usetex=False))
    fig, ax = plt.subplots(figsize=(7, 7))
    fig.suptitle("Probability of first accident")
    ax.plot(years, data, color=rgb.tue_red)
    ax.grid()
    ax.set_ylabel("probability of first accident")
    ax.set_xlabel("Year")
    return fig


counter = 1
current_question = filters_container.get_next_question()
s = func(current_question, counter)
while True:
    if s:
        filters_container.set_question_answer(current_question.question_key, s)
        if filters_container.has_next_question():
            counter += 1
            current_question = filters_container.get_next_question()
            s = func(filters_container.get_next_question(), counter)
        else:
            break


csv_name, column_name = filters_container.get_resulting_dataset()
years, probability = data_container.all_references["Year"], data_container.data[csv_name][column_name]
first_acc = calculate_first_accident_prob(probability)
st.pyplot(quick_plot(years, first_acc))
