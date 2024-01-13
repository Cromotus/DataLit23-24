import json

class Filters:
    def __init__(self):
        # Load from json
        configuartion_file_path="./filters/filter-configuration.json"
        with open(configuartion_file_path) as filter_data_json_file:
            # keep initial data for reset
            self.initial_filter_data = json.load(filter_data_json_file)
            self.reset()
        
    def reset(self):
        self.filter_data=dict(self.initial_filter_data["filters"])
        self.selected_options=[]

    def has_next_question(self): 
        return bool(self.filter_data)

    # getNextQuestion(): {question_key, message_text, message_options[]}
    def get_next_question(self):
        if(not self.has_next_question()):
            return {}
        for key, value in self.filter_data.items():
            answer_options = []
            for option_key, option_attributes in value["answer_options"].items():
                option = AnswerOption(option_key,option_attributes["option_text"])
                answer_options.append(option)
            return Question(key, value["display_text"], answer_options)
            
    # setQuestionAnswer(message_key, option_key): void
    def set_question_answer(self, message_key, option_key):
        self.selected_options.append((message_key,option_key))
        current_question = self.filter_data[message_key]
        del self.filter_data[message_key]
        if(option_key == "skip"):
            return
        

        # remove options based on answer
        answer_options = current_question["answer_options"]
        answer_option = answer_options[option_key]
        allowed_questions = answer_option["allowed_questions"]
        for question in dict(self.filter_data):#iterate on copy to allow modifications
            if question in allowed_questions[:]:
                question_allowed_options = answer_option["allowed_options"]
                if bool(question_allowed_options) or question not in question_allowed_options:
                    continue
                allowed_options = question_allowed_options[question]
                for option_key, option_details in question["answer_options"].items():
                    if option_key not in allowed_options:
                        del question[answer_options][option_key]
            else:
                del self.filter_data[question]

    def get_all_filters(self):
        return (self.selected_options,self.filter_data)
    
    def __str__(self):
        return "\"filter\":{\"selected_options\"="+str(self.selected_options)+",\"filter_data="+str(self.filter_data)+",\"initial_filter_data\"="+str(self.initial_filter_data)+"}"
            

class Question:
    def __init__(self,question_key,question_text,question_options):
        self.question_key=question_key
        self.question_text=question_text
        self.question_options=question_options
    def __str__(self):
        return "\"question\":{\"key\"="+self.question_key+", \"text\"= "+self.question_text+", \"options\"="+str(self.question_options)+"}"
   
class AnswerOption:
    def __init__(self,option_key,option_text):
        self.option_key=option_key
        self.option_text=option_text
    def __str__(self):
        return "AnswerOption(\nkey = "+self.option_key+", \ntext= "+self.option_text+")"