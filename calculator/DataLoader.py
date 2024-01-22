import numpy as np
import pandas
import os
import json
from General_Calculator import ProbPair


class DataContainer:
    def __init__(self, dataset_folder_path="../dataset/csv",
                 reference_association_path="../dataset/reference_association.json",
                 start_year=1991, end_year=2021):
        self.data = {}
        # loading the reference association for creating the ProbPairs later
        reference_association = json.load(open(reference_association_path))
        self.all_references = interpolate_gap(pandas.read_csv(os.path.join(dataset_folder_path, "Reference Numbers.csv"),
                                                         sep=';', dtype=np.float64, na_values="-"), start_year, end_year)

        for file_name in os.listdir(dataset_folder_path):
            if file_name == "Reference Numbers.csv":
                # the reference is not loaded as data
                continue
            if os.path.isfile(os.path.join(dataset_folder_path, file_name)) and file_name.endswith("csv"):
                interpolated_data = interpolate_gap(pandas.read_csv(os.path.join(dataset_folder_path, file_name),
                                        sep=';', dtype=np.float64, na_values="-"), start_year, end_year)

                file_reference = reference_association[file_name]
                file_dict = {}

                for column_name, series in interpolated_data.items():
                    if column_name == "Year":
                        # Year is not loaded as Data
                        continue
                    if "COMPLETE_FILE" in file_reference.keys():
                        series_ref_key = file_reference["COMPLETE_FILE"]
                    else:
                        series_ref_key = file_reference[column_name]
                    file_dict[column_name] = ProbPair(series, self.all_references[series_ref_key])
                self.data[file_name] = file_dict


def interpolate_gap(df: pandas.DataFrame, start_year: int, end_year: int):
    years = {"Year": list(range(start_year, end_year + 1))}
    new_df = pandas.DataFrame(years, columns=df.columns)
    for _, row_data in df.iterrows():
        row_year = row_data.iloc[0]
        # the year of the row is in the given range
        if start_year <= row_year <= end_year:
            new_df.iloc[int(row_year - start_year)] = row_data

    lin_interpolated = new_df.infer_objects(copy=False).interpolate()
    lin_interpolate_start_points(lin_interpolated)
    return lin_interpolated


def lin_interpolate_start_points(df: pandas.DataFrame):
    for column_index, column_series in df.items():

        nan_mask = column_series.isna()
        if nan_mask.any():
            for index in range(column_series.size):
                if not nan_mask.iloc[index]:
                    delta = column_series.iloc[index + 1] - column_series.iloc[index]
                    for sub_index in range(index):
                        # linear regression for all values above index
                        df.loc[sub_index, column_index] = column_series.iloc[index] + delta * (sub_index - index)

                    break


if __name__ == '__main__':
    test_container = DataContainer()
