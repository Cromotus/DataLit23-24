# Car Accident Calculator DataLiteracy 23/24 Project

## Quickstart
To start the calculator first install the libraries from the requirements.txt file. Then you can start the calculator with `streamlit run streamlit_app.py`.

Then you can choose from the Questions (or filters) and get presented a plot of the probability of the first accident.

## Dataset
The Calculator in developed to be usable for other data.
To adapt the Calculator insert the data as csv files in `./dataset/csv`.
To associate different references for the data, you then add a `reference_association.json` file.
It is structured as followed:
```
{
    "<File-Name>": {
            "<Column-Name>": "<Column-Name of the reference in Reference Numbers.csv>"
    }
    "<next File name>": {
            ...
    }
}
```

Then you have to add the filters for your data. They are structured as followed:
```
{
    "filters":{
        "<filter name>":{
            "display_text": "Text to display in UI",
            "skippable": "<true or false wether the filter is skippable",
            "answer_options":{
                "<Name of option>":{"option_text": "<"Text to display in UI">",
                                    "allowed_questions":[<list of questions that are allowed after anserwing this (some questions might excleude each other>],
                                    "allowed_options":{},
                                    "resulting_dataset":"<file_name or empty if this answer does not immediately shows the answer>"},
                "with damage to people":{"option_text":"damage to people","allowed_questions":[],"allowed_options":{},"resulting_dataset":"Accident Numbers.csv"},
            }
        },
    }
}
```
