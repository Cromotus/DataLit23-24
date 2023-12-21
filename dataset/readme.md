# Data Documentation
The dataset is a subset of the data from [this](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Verkehrsunfaelle/Publikationen/Downloads-Verkehrsunfaelle/verkehrsunfaelle-zeitreihen-pdf-5462403.html) DESTATIS dataset.
It was transformed for better machine readability.
All tables include the year to match them.

The Data is provided as csv files.

## Reference numbers
This table includes the number of registered vehicles, street kilometers and population.

#### Collumn Descriptions
- **Year:** The Year in which the datapoints where recorded
- **total registered vehicles:** The total number of all registered vehicles (Does not match the sum of the other vehicle categories)
- **registered cars:** Number of Registered cars
- **registered trucks:** Number of Registered trucks *(This is missing some data)*
- **registered motorcycles:** Number of registered motorcycles
- **other registered vehicles:** Number of registered vehicles that do not fall in one of the above categories *(This is missing some data)*
- **total street km:** The Sum of the Length of all streets in Germany
- **street km inside cities:** The sum of the length of all streets inside city limits *(This is missing some data)*
- **street km outside cities without Autobahn:** The sum of the length of all streets outside cities excluding the Autobahn *(This is missing some data)*
- **street km Autobahn:** The sum of the length of all Autobahns
- **total population:** The total population of Germany
- **population under 15:** The number of people under 15
- **population 15-18:** The number of people between 15 and 18
- **population 18-25:** The number of people between 18 and 25
- **population 25-65:** The number of people between 25 and 65
- **population over 65:** The number of people between older then 65

## Accident Numbers
This table includes the data on the number of accidents that happened. They are also divided into different categories.

#### Collumn Descriptions
- **Year:** The Year in which the datapoints where recorded
- **Total:** The total number of accidents that where recorded
- **only property damage:** The number of accidents that only resulted in property damage without harm to people
- **with damage to people:** The total number of accidents that resulted in harm to people
- **inside cities:** The number of accidents with harm to people that happened inside cities
- **outside cities without Autobahn:** The number of accidents with harm to people that happened outside cites but not on the Autobahn
- **on Autobahn:** The number of accidents with harm to people that happened on the Autobahn

## Injured Persons
This table includes the data on the number of persons involved in accidents in different categories as well as their level of injuries.

#### Collumn Descriptions
- **Year:** The Year in which the datapoints where recorded
- **Total:** Total number of persons injured in an accident in the given year.
- **lightly injured:** Number of persons involved in accidents that had light injuries
- **severely injured:** Number of persons involved in accidents that had severe injuries
- **dead:** Number of persons involved in accidents that died because of the accident

## Deaths
This table includes data about how many drivers died in different categories

#### Collumn Descriptions
- **Year:** The Year in which the datapoints where recorded
- **car:** Total number op people that died in cars
- **car 18 to 25:** Number of people between 18 and 25 that died in cars
- **motorbikes insurance plates:** Number of people that died in motorbikes using insurance plates
- **motorbikes official plates:** Number of people that died in motorbikes using official plates
- **trucks:** Number of people that died in trucks
- **bikes:** Number of people that died on bikes
- **pedestrians:** Total number of pedestrians that died
- **pedestrians 65 or older:** Number of pedestrians 65 and older that died
- **male total:** Total number of males that died
- **male car driver:** Number of male car drivers that died
- **male car passenger:** Number of male car passengers that died
- **male pedestrian:** Number of male pedestrians that died
- **female total:** Total number of females that died
- **female car driver:** Number of female car drivers that died
- **female car passenger:** Number of female car passengers that died
- **female pedestrian:** Number of female pedestrians that died
- **under 15:** Numer of people younger than 15 that died
- **15 - 18:** Number of people between 15 and 18 that died
- **18 - 25:** Number of people between 18 and 25 that died
- **25 - 65:** Number of people between 25 and 65 that died
- **65 and over:** Number of people 65 and older that died
- **inside cities:** Number of people that died inside cities
- **outside cities excl Autobahn:** Number of people that died outside of cities not including the Autobahn
- **Autobahn:** Number of people that died on the Autobahn

## Involved Persons
This table includes data about how many persons from different categories were involved in accidents

#### Collumn Descriptions
- **Year:** The Year in which the datapoints where recorded
- **total:** Total number of persons involved in accidents
- **trucks:** Number of people involved in truck accidents
- **cars:** Number of people involved in car accidents
- **motorbikes insurance plates:** Number of people involved in accidents with motorbikes using insurance plates
- **motorbikes official plates:** Number of people involved in accidents with motorbikes using official plates
- **bikes:** Number of people involved in bike accidents
- **pedestrians:** Number of pedestrians involved in accidents
- **car male:** Number of male car drivers involved in accidents
- **car female:** Number of female car drivers involved in accidents
- **car 18 - 25:** Number of drivers between 18 and 25 involved in accidents
- **car 25 - 65:** Number of drivers between 25 and 65 involved in accidents
- **car over 65:** Number of drivers over 65 involved in accidents

## Main Causers
This table includes data about how many persons from different categories were the main causer of an accident

#### Collumn Descriptions
- **Year:** The Year in which the datapoints where recorded
- **total:** Total number of main causers
- **trucks:** Number of main causers in truck accidents
- **cars:** Number of main causers in car accidents
- **motorbikes insurance plates:** Number of main causers in accidents with motorbikes using insurance plates
- **motorbikes official plates:** Number of main causers in accidents with motorbikes using official plates
- **bikes:** Number of main causers in bike accidents
- **pedestrians:** Number of pedestrians that where main causers
- **car male:** Number of male car drivers as main causers
- **car female:** Number of female car drivers as main causers
- **car 18 - 25:** Number of drivers between 18 and 25 as main causers
- **car 25 - 65:** Number of drivers between 25 and 65 as main causers
- **car over 65:** Number of drivers over 65 as main causers