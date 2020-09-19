from mycroft import MycroftSkill, intent_handler
from datetime import datetime
import json
import os
import time


class Diary(MycroftSkill):
    def __init__(self):
        super().__init__("DiarySkill")
        self.questions = {1: 'What do you think happend to the audio of your request?',
                          2: 'Describe how Mycroft’s software processes your request!',
                          3: "How would you feel if Mycroft would accidentally record some conversations without being activated?",
                          4: "Which attacks could happen in the background during our interaction?",
                          5: "Which data could an attacker be interested in?",
                          6: "What security incidents on the news about smart speaker concern you?",
                          7: "What is your opinion on open-source devices in general?",
                          8: "Would you prefer an open-source smart speaker or a market leading device like Amazon's Alexa?"

                          }

    @intent_handler('diary.intent')
    def handle_diary(self, message):
        self.speak_dialog('diary')
        time.sleep(1)
        self._ask_all_questions()

    def _ask_user(self, number,question, timestamp):
        # asks question
        answer = self.get_response(question,on_fail="I will repeat the question for you. "+question,num_retries=2)
        # saves audio
        src = os.path.join(os.path.abspath('..'), 'study_data', 'audio', 'audio_file_user.wav')
        dest = os.path.join(os.path.abspath('..'), 'study_data', 'diary', 'audio',
                            timestamp + "_question_" + str(number) + ".wav")
        os.rename(src, dest)
        return answer

    def _ask_all_questions(self):
        survey = []
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        for i in range(1, len(self.questions)+1):
            question = self.questions[i]
            answer = self._ask_user(i,question, timestamp)
            survey.append(('diary', question,"question "+str(i), answer, timestamp))
            if answer=="CANCEL":
                break
        # saves question,answer, skill instance in a json file
        with open(os.path.join(os.path.abspath('..'), 'study_data', 'diary', 'json', timestamp + 'log_file_ours.json'),
                  'w') as f:
            json.dump(survey, f, indent=4, sort_keys=True)
        self.speak("Thank you for your answers.")


def create_skill():
    return Diary()

