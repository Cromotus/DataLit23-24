from calculator.General_Calculator import calculate_first_accident_prob
from calculator.DataLoader import DataContainer
from matplotlib import pyplot as plt
from tueplots import bundles

def quick_multi_plot(years, data_name_pair, title="First Accident Probability", file_name=None):
    plt.rcParams.update(bundles.icml2022(column="half", usetex=False))

    fig, ax = plt.subplots()
    fig.suptitle(title)
    for data, name in data_name_pair:
        ax.plot(years, data, label=name)

    ax.grid()
    ax.set_ylabel("probability of first accident")
    ax.set_xlabel("Year")
    ax.legend()
    if file_name:
        plt.savefig(file_name)
    else:
        plt.show()

if __name__ == '__main__':
    # Plots for the section 4.1 General Results
    data_container = DataContainer()
    years = data_container.all_references["Year"]

    # Plot "Fender bender and injuries on german roads"
    probs_property_damage = data_container.data["Accident Numbers.csv"]["only property damage"]
    probs_human_injury = data_container.data["Accident Numbers.csv"]["with damage to people"]

    first_acc_property = calculate_first_accident_prob(probs_property_damage)
    first_acc_injury = calculate_first_accident_prob(probs_human_injury)

    quick_multi_plot(years, [(first_acc_property, "only property damage"),
                             (first_acc_injury, "with damage to people")],
                     title="Fender bender and injuries on german roads", file_name="fender_bender.pdf")

    # Plot "Deadly Car Accidents"
    probs_car_death = data_container.data["Deaths.csv"]["car"]

    first_acc_car_death = calculate_first_accident_prob(probs_car_death)

    quick_multi_plot(years, [(first_acc_car_death, "deadly car accidents")],
                     title="Deadly Car Accidents", file_name="deadly_car_acc.pdf")

    # Plot "Generations Main Causerds"
    probs_cause_18_25 = data_container.data["Main Causer.csv"]["car 18 - 25"]
    probs_cause_25_65 = data_container.data["Main Causer.csv"]["car 25 - 65"]
    probs_cause_over_65 = data_container.data["Main Causer.csv"]["car over 65"]

    first_cause_18_25 = calculate_first_accident_prob(probs_cause_18_25)
    first_cause_25_65 = calculate_first_accident_prob(probs_cause_25_65)
    first_cause_over_65 = calculate_first_accident_prob(probs_cause_over_65)

    quick_multi_plot(years, [(first_cause_18_25, "car drivers 18-25"),
                             (first_cause_25_65, "car drivers 25-65"),
                             (first_cause_over_65, "car drivers over 65")],
                     title="Generations Main Causer", file_name="main_causer_generations.pdf")
