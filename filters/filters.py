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
        if option_key == "skip":
            return
        # remove options based on answer
        answer_options = current_question["answer_options"]
        answer_option = answer_options[option_key]
        allowed_questions = answer_option["allowed_questions"]
        question_allowed_options = answer_option["allowed_options"]
        for question_key in dict(self.filter_data):#iterate on copy to allow modifications
            if question_key in allowed_questions[:]:
                if not bool(question_allowed_options) or question_key not in question_allowed_options:
                    continue
                allowed_options = question_allowed_options[question_key]
                question = self.filter_data[question_key]
                for option_key, option_details in dict(question["answer_options"]).items():
                    if option_key not in allowed_options:
                        del question["answer_options"][option_key]
            else:
                del self.filter_data[question_key]

    #return nothing if theres no resulting dataset or (resulting dataset name,colum name)
    def get_resulting_dataset(self):
        for message_key, option_key in self.selected_options:
            resulting_dataset = self.get_resulting_dataset_for_options(message_key,option_key)
            if resulting_dataset:
                return resulting_dataset

    #return nothing if theres no resulting dataset or (resulting dataset name,colum name)
    def get_resulting_dataset_for_options(self, message_key, option_key):
        if not self.initial_filter_data or not self.initial_filter_data["filters"]:
            return
        filters = self.initial_filter_data["filters"]
        if filters[message_key]:
            answer_options = filters[message_key]["answer_options"]
            if answer_options and answer_options[option_key] and answer_options[option_key]["resulting_dataset"]!="None":
                return (answer_options[option_key]["resulting_dataset"],option_key)

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
        return "\"question\":{\"key\"="+self.question_key+", \"text\"= "+self.question_text+", \"options\"="+str([str(option) for option in self.question_options])+"}"
   
class AnswerOption:
    def __init__(self,option_key,option_text):
        self.option_key=option_key
        self.option_text=option_text
    def __str__(self):
        return "AnswerOption(\nkey = "+self.option_key+", \ntext= "+self.option_text+")"   