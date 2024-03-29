import pandas as pd

accidents = pd.read_csv("csv/Accident Numbers.csv", sep=";")
referenceNumbers = pd.read_csv("csv/Reference Numbers.csv", sep=";")
injuredPersons = pd.read_csv("csv/Injured Persons.csv", sep=";")
injuredPersons2 = pd.read_csv("csv/Injured Persons 2.csv", sep=";")
involvedPersons = pd.read_csv("csv/Involved Persons.csv", sep=";")
deaths = pd.read_csv("csv/Deaths.csv", sep=";")
mainCauser = pd.read_csv("csv/Main Causer.csv", sep=";")
accidentsByState = pd.read_csv("csv/Accidents by State.csv", sep=";")
accidentCauses = pd.read_csv("csv/Accident Causes.csv", sep=";")
registeredVehiclesByState = pd.read_csv("csv/Registered Vehicles by State.csv", sep=";")