import json

class filters:
    def __init__(self):
        #Load from json
        configuartion_file_path="./filters/filter-configuration.json"
        with open(configuartion_file_path) as filter_data_json_file:
            #keep initial data for reset
            self.initial_filter_data = json.load(filter_data_json_file)
            self.reset()
        
    def reset(self):
        self.filter_data=dict(self.initial_filter_data["filters"])
        self.selected_options=[]

    def hasNextQuestion(self): 
        return bool(self.filter_data)

    #getNextQuestion(): {question_key, message_text, message_options[]}
    def getNextQuestion(self):
        if(not self.hasNextQuestion()):
            return {}
        for key, value in self.filter_data.items():
            answer_options = []
            for option_key, option_attributes in value["answer_options"].items():
                option = answer_option(option_key,option_attributes["option_text"])
                answer_options.append(option)
            return question(key, value["display_text"], answer_option)
            
    #setQuestionAnswer(message_key, option_key): void
    def setQuestionAnswer(self, message_key, option_key):
        self.selected_options.append((message_key,option_key))
        #remove options based on answer
        if(option_key != "skip"):
            currentQuestion = self.filter_data[message_key]
            answer_options = currentQuestion["answer_options"]
            answer_option = answer_options[option_key]
            for restricts_question in answer_option["restricts_questions"]:
                if restricts_question in self.filter_data:
                    del self.filter_data[restricts_question]
            #TODO delete single options
        del self.filter_data[message_key]

            

class question:
    def __init__(self,question_key,question_text,question_options):
        self.question_key=question_key
        self.question_text=question_text
        self.question_options=question_options

class answer_option:
    def __init__(self,option_key,option_text):
        self.option_key=option_key
        self.option_text=option_text