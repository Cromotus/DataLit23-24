# DataLit23-24
To start the simple text UI start the main file.

A question (or filter) is then presented you can choose from the presented answer options:

```
"question":{"key"=damage, "text"= Result of the accident, "options"=['AnswerOption(\nkey = only property damage, \ntext= only property damage)', 'AnswerOption(\nkey = damage to people, ....
```

The options to choose from can be selected by typing in the key of the answer, for example 
`only property damage`. This way you maneuver through the filters. If you have chosen all filters, the plot should appear.
At this point the plot is normalized by the number of registered vehicles, but this will change later.