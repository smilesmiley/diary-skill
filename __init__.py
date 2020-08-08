from mycroft import MycroftSkill, intent_handler
from datetime import datetime
import json
import os
import time


class Diary(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.questions = {1: "What do you think happened to your audio which was captured to evaluate your Mycroft request?",
                          2: "How could the request processing of your smart speaker work?",
                          3: "How would you feel if Mycroft would recorded accidental some conversations without being activated?",
                          4: "Which attacks could happen in the background during your interaction?",
                          5: "Which data could an attacker be interested in?",
                          6: "Have you heard about any security issues in the news and which? If yes does this concern you or if no, why not?",
                          7: "What advantages could an open-source device offer?",
                          8: "What disadvantages could an open-source device offer?",
                          9: "What would you prefer? An open-source device or a market leading device like Amazon's Echo and why?"

                          }

    @intent_handler('diary.intent')
    def handle_diary(self, message):
        self.speak_dialog('diary')
        time.sleep(1)
        self._ask_all_questions()

    def _ask_user(self, number,question, timestamp):
        # asks question
        answer = self.ask_yesno(question)
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
            survey.append(('diary', question, answer, timestamp))
        # saves question,answer, skill instance in a json file
        with open(os.path.join(os.path.abspath('..'), 'study_data', 'diary', 'json', timestamp + 'log_file_ours.json'),
                  'w') as f:
            json.dump(survey, f, indent=4, sort_keys=True)


def create_skill():
    return Diary()

