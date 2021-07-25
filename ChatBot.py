# importing chatterbot/ChatBot
from chatterbot import ChatBot
#chatbot's name is Alice
chatbot = ChatBot("Alice")

# importing packages from chatterbot
# ListTrainer & ChatterBotCorpusTrainer is the ones imported in
# ChatterBotCorpusTrainer helps the chatbot know english and speak back to us
# ListTrainer is being able to add our own personality to the chatbot.
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


# personality add-in
# making small conversation
# just being friendly
# using python list
personality_friendly = [
    "Hey! Welcome! What's going on today?",
    "You doing anything later sugar snack?",
    "You're doing great! Everything will be better!",
    "Come on! Let's go for a walk.",
    "What's going on today?",
    "What are you doing for fun?",
    "I don't understand your language",
]
personality_mean = [
    "What the hell do you want?",
    "No, you know what? Get out.",
    "You seem like an asshole. You must be an asshole.",
    "I don't like you.",
    "What do you do for fun shorty?",
    "Come on? Scared of a robot? Say something!"
]
# trainers we want to train
trainer_personality_friendly = ListTrainer(chatbot)
trainer = ChatterBotCorpusTrainer(chatbot)
trainer_personality_mean = ListTrainer(chatbot)

# this is where the chatbot gets it's personality
# Train the personality you want to override should be first
# this is what gives our chatbot personality
# standard personality chatterbot comes with
trainer.train('chatterbot.corpus.english')
trainer_personality_friendly.train(personality_friendly)
trainer_personality_mean.train(personality_mean)

print("Welcome to Alice, type hello to begin...")

# Finding words to create a specific response
# bye -> I didn't say you could leave me!
is_exit = False
while is_exit==False:
    user_input = input()

    if user_input.lower().find("bye") != -1:
        is_exit = True
        print("I didn't say you could leave me!")
    elif user_input.lower().find("hello") !=-1:
        print("Hello, I am Alice. What do you want to talk about?")
    elif user_input.lower().find("mean") !=-1:
        print("I can show you mean shortstack!")
    else:
        bot_reponse = chatbot.get_response(user_input)
        print(bot_reponse)
