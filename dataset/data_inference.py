import pandas as pd

if __name__ == '__main__':
    file_path = "./csv/Reference Numbers.csv"
    reference = pd.read_csv(file_path, sep=';')
    total_pop = reference["total population"]
    reference.insert(11, "male population", 0.5 * total_pop, True)
    reference.insert(12, "female population", 0.5 * total_pop, True)
    reference.to_csv("./csv/reference_number.csv", sep=';')