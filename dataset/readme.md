# Data Documentation
The dataset is a subset of the data from [this](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Verkehrsunfaelle/Publikationen/Downloads-Verkehrsunfaelle/verkehrsunfaelle-zeitreihen-pdf-5462403.html) DESTATIS dataset.
It was transformed for better machine readability.
All tables include the year to match them.

The Data is provided as csv files or as a .hdf5.

## Reference numbers
This table includes the number of registered vehicles, street kilometers and population.

HDF5 Key: "reference"

#### Collumn Descriptions
- **Year:** The Year in which the datapoints where recorded
- **total registered vehicles:** The total number of all registered vehicles (Does not match the sum of the other vecicle categories)
- **registered cars:** Number of Registered cars
- **registered trucks:** Number of Registerd trucks *(This is missing some data)*
- **registered motorcycles:** Number of registerd motorcycles
- **other registered vehicles:** Number of registered vehicles that do not fall in one of the above categories *(This is missing some data)*
- **total street km:** The Sum of the Length of all streets in Germany
- **street km inside cities:** The sum of the length of all streets inside of city limits *(This is missing some data)*
- **street km outside cities without Autobahn:** The sum of the length of all streets outside cities excluding the Autobahn *(This is missing some data)*
- **street km Autobahn:** The sum of the lenth of all Autobahns
- **total population:** The total population of Germany
- **population under 15:** The number of people under 15
- **population 15-18:** The number of people between 15 and 18
- **population 18-25:** The number of people between 18 and 25
- **population 25-65:** The number of people between 25 and 65
- **population over 65:** The number of people between older then 65

## Accident Numbers
This table includes the data on the number of accidents that happened. They are also divided into different categories.

HDF5 Key: "accidents"

#### Collumn Descriptions
- **Year:** The Year in which the datapoints where recorded
- **Total:** The total number of accidents that where recorded
- **only property damage:** The number of accidents that only resulted in property damage without harm to people
- **with damage to people:** The number of accidents that resulted in harm to people
- **inside cities:** The number of accidents that happened inside cities
- **outside cities without Autobahn:** The number of accidents that happend outside cites but not on the Autobahn
- **on Autobah:** The number of accidents that happened on the Autobahn
