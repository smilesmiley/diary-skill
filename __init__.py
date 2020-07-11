from mycroft import MycroftSkill, intent_file_handler


class Diary(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.questions= {1: "What data may have been lost during your interactions with the device?",
                            2: "What do you think happened to your audio which was captured to evaluate your Mycroft request?",
                            3: "How could the processing of your request to the smart speaker work?",
                             4: "Where exactly is the data spoken to the smart speaker processed?",
                             5: "Do you think some conversations could be recorded accidental and why?",
                             6: "Have you ever asked Mycroft a question/command that you wish you could delete due to privacy concerns? What about it was sensitive?",
                             7: "How would you feel if Mycroft would recorded accidental some conversations of you without being activated by you?",
                             8: "Which attacks could happen in the background during your interaction?",
                              9: "What security concerning action could happen during your last interaction?",
                              10: "Which data could an attacker be interested in?",
                              11: "What security concerns do you have about this device?",
                              12: "Have you heard about any security issue in the news and which? If yes does this concern you or if no, why not?",
                              13: "How would you compare your level of security concerns about this device to your level of concerns about your phone or laptop computer?"
                              14: "What advantages could an open-source device offer?",
                              15: "What disadvantages could an open-source device offer?",
                              16: "What would you prefer, an open-source device or a market leading device like Amazon's Echo and why?"

        }

    @intent_file_handler('diary.intent')
    def handle_diary(self, message):
        self.speak_dialog('diary')
        self._ask_all_questions()
     
    def _ask_user(self,question,survey):
        #asks question
        answer = self.ask_yesno(question)
        #saves audio
        src = os.path.join(os.path.abspath(os.path.join('..')), 'study_data','diary','audio','audio_file_user.wav')
        dest = os.path.join(os.path.abspath(os.path.join('..')), 'study_data','diary','audio',timestamp + "_question_" + str(number) + ".wav")
        os.rename(src, dest)
        return answer
    
    def _ask_all_questions(self):
        survey = []
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        for i in len(self.questions):
            question= self.questions[i]
            answer= self.ask_and_save(survey, question, utterance, timestamp)
            survey.append((utterance, question, answer,timestamp))
        #saves question,answer, skill instance in a json file
        with open(os.path.join(os.path.abspath('..'),'study_data','diary', timestamp + 'log_file_ours.json'), 'w') as f:
            json.dump(survey, f, indent=4, sort_keys=True)


def create_skill():
    return Diary()

