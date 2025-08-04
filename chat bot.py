import random
import re
class RuleBot:
    negative_res = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
    random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? "
    )
    def __init__(self):
        self.alienbabble = {
            'describe_planet_intent': r'.*\s*your planet.*',
            'answer_why_intent': r'why\sare.*',
            'about_intellipaat': r'.*\s*intellipaat.*'
        }
    def greet(self):
        self.name = input("what is your name?\n")
        will_help = input(f"Hi {self.name}, I am a bot. Will you help me learn about your planet?\n").lower()
        if will_help in self.negative_res:
            print("Have a nice Earth day!")
            return
        self.chat()
    def make_exit(self, reply):
        for command in self.exit_commands:
            if command in reply.lower():
                print("Have a nice day!")
                return True
        return False
    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))
    def match_reply(self, reply):
        for intent, regex_pattern in self.alienbabble.items():
            found_match = re.match(regex_pattern, reply, re.IGNORECASE)
            if found_match:
                if intent == 'describe_planet_intent':
                    return self.describe_planet_intent()
                elif intent == 'answer_why_intent':
                    return self.answer_why_intent()
                elif intent == 'about_intellipaat':
                    return self.about_intellipaat()
        return self.no_match_intent()
    def describe_planet_intent(self):
        responses = (
            "My planet is a utopia of diverse organisms.\n",
            "I heard the coffee is good.\n"
        )
        return random.choice(responses)
    def answer_why_intent(self):
        responses = (
            "I come in peace.\n",
            "I am here to collect data on your planet and its inhabitants.\n",
            "I heard the coffee is good.\n"
        )
        return random.choice(responses)
    def about_intellipaat(self):
        responses = (
            "python is a powerful programming language.\n",
            "Intellipaat helps you learn concepts like never before.\n",
            "Intellipaat is where your career and skills grow.\n"
        )
        return random.choice(responses)
    def no_match_intent(self):
        responses = (
            "Please tell me more.\n",
            "Tell me more!\n",
            "I see. Can you elaborate?\n",
            "Interesting. Can you tell me more?\n",
            "I see. How do you think?\n",
            "Why?\n",
            "How do you think I feel when you say that? Why?\n"
        )
        return random.choice(responses)
if __name__ == "__main__":
    bot = RuleBot()
    bot.greet()
