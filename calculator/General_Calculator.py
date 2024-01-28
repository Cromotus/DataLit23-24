import numpy as np


class UiInterface:
    """
    The UiInterface is an Interface to decouple the calculation from the UI.
    With an Object of the UiInterface, you can define what should be done with the probabilities you hand over.
    The interface is recursively defined to support infinite complex combinations.
    """
    def return_value(self):
        pass


class ProbPair(UiInterface):
    """
    The Prob(ability)Pair is the atomic unit. It is the pair of the absolute frequency of an event and the reference
    associated with it.
    """
    def __init__(self, abs_frequency, reference):
        self.abs_frequency = abs_frequency
        self.reference = reference

    def return_value(self):
        return self

    def return_relative_prob(self):
        return self.abs_frequency / self.reference


class PlusCombination(UiInterface):
    """
    A PlusCombination is needed when you want to combine features that are from the same feature category.
    These features are handed over in a List.
    For example: You want the probability of an accident from 18-25 and 25-65. These two Feature are from the category
    age. Hence, they are combined with PlusCombination.
    """
    def __init__(self, freq_list: [UiInterface]):
        self.freq_list = freq_list

    def return_value(self):
        # recursive call of the elements in the Combination so that the actual values are calculated.
        resolved_list = [pair.return_value() for pair in self.freq_list]
        new_abs_freq = 0
        new_reference = 0
        for pair in resolved_list:
            new_abs_freq += pair.abs_frequency
            new_reference += pair.reference

        return ProbPair(new_abs_freq, new_reference)


class AndCombination(UiInterface):
    """
    An AndCombination is needed if you want to combine features that are from different feature categories.
    They are handed over in a list.
    For example: You want the probability of an accident between 18-25 and when you are male. These two features qre not
    from the same category and hence, combined with AndCombination.
    """
    def __init__(self, freq_list: [UiInterface]):
        self.freq_list = freq_list

    def return_value(self):
        # recursive call of the elements in the Combination so that the actual values are calculated.
        resolved_list = [pair.return_value() for pair in self.freq_list]
        new_abs_freq = 1
        new_reference = 1
        # the new combined absolute frequency from all ProbPairs
        for pair in resolved_list:
            new_abs_freq *= pair.abs_frequency
            new_reference *= pair.reference

        return ProbPair(new_abs_freq, new_reference)


def calculate_first_accident_prob(prob_combination: UiInterface, start_year=1991, end_year=2021):
    prob_pair: ProbPair = prob_combination.return_value()
    yearly_prob = prob_pair.return_relative_prob()

    # calculating the probability for the first accident in year year_index
    array_of_probs = yearly_prob[(start_year-1991):20]
    prob_accident = np.array(
        [np.prod(1 - yearly_prob[(start_year-1991+1):year_index]) * yearly_prob[year_index] for year_index in range(end_year - start_year + 1)]
    )

    return prob_accident