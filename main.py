
# import the chatterbot package
# This is the chatbot engine we will use
from chatterbot import ChatBot


# Give our chatbot a name
chatbot = ChatBot("GLaDOS")

# Packages used to Train your chatbot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# using game mechanics for portal 1 & 2
personality_gamemechs = [
    "Portal Gun - Designed to create and place portals on immobile surfaces, or surfaces covered with Conversion Gel that are big enough for the Portals to be opened.",
    "Test Chambers - Exactly as it sounds, these Test Chambers are used for testing subjects on mental capabilities and puzzle solving.",
    "Chamberlock - A room at the end of each Testing Chamber that doesn't allow items from the chambers to be brought through.",
    "Emergency Intelligence Incinerator - A chute that leads directly to a series of furnaces deep within the Aperture Science Facility.",
    "Material Emancipation Grill - Shimmering, semi-transparent particle fields that appear throughout the Aperture Science testing facilities. They disintegrate unauthorized Aperture Science equipment and blocks any portal that passes through. Doesn't affect Portal Gun.",
    "Unstationary Scaffold - A platform that, when activated, moves horizontally back and forth along a beam of blue light. Used to access previously unreachable places and bridges gaps over deadly substances/pitfalls.",
    ""
    
]

personality_quotes = [
   "Killing you and giving you advice aren't mututally exclusive. The rocket really is the way to go.",
   "Remember when teh platform was sliding into the fire pit and I said, 'Goodbye,' and you were like, 'No way,' and then I was all, 'We pretended we were trying to murder you'? That was great.",
   "That jumpsuit you're wearing looks stupid. That's not me talking, it's right here on your file. On other people it looks fine, but right here a scientist has noted that on you it looks stupid. Well, what does a neck-bearded old engineer know about fashion? He probably- Oh, wait. It's a she. Still, what does she know? Oh wait, it says she has a medical degree. In fashion! From France!"
   "How are you holding up? BECAUSE I'M A POTATO. [clap clap clap] Oh good. My slow clap processor made it into this thing. So we have that.",
   "No tricks. This potato only generates 1.1 volts of electricity. I literally do not have the energy to lie to you."
]



# Set the trainers we want train
trainer_personality_quotes=ListTrainer(chatbot)
trainer_personality_gamemechs= ListTrainer(chatbot)
trainer = ChatterBotCorpusTrainer(chatbot)

# Now here we actually train our chatbot on the corpus
# This is what gives our chatbot its personality 
# Train the personality you want to override should come first

# Standard personality chatterbot comes with
trainer.train('chatterbot.corpus.english')
trainer_personality_gamemechs.train(personality_gamemechs)
trainer_personality_quotes.train(personality_quotes)

''' ******************* GUI Below Engine Above **************** '''
# Import for the GUI 
from chatbot_gui import ChatbotGUI

# create the chatbot app
"""
    Options
    - title: App window title.
    - gif_path: File Path to the ChatBot gif.
    - show_timestamps: If the chat has time-stamps.
    - default_voice_options: The voice options provided to the text-to-speech engine by default if not specified
                             when calling the send_ai_message() function.
"""
app = ChatbotGUI(
    title="the cake is a lie  - GLaDOS",
    gif_path="Glados.gif",
    show_timestamps=True,
    default_voice_options={
        "rate": 100,
        "volume": 0.8,
        "voice": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    }
)


# define the function that handles incoming user messages
@app.event
def on_message(chat: ChatbotGUI, text: str):
    """
    This is where you can add chat bot functionality!

    You can use chat.send_ai_message(text, callback, voice_options) to send a message as the AI.
        params:
            - text: the text you want the bot to say
            - callback: a function which will be executed when the AI is done talking
            - voice_options: a dictionary where you can provide options for the AI's speaking voice
                default: {
                   "rate": 100,
                   "volume": 0.8,
                   "voice": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                }

    You can use chat.start_gif() and chat.stop_gif() to start and stop the gif.
    You can use chat.clear() to clear the user and AI chat boxes.

    You can use chat.process_and_send_ai_message to offload chatbot processing to a thread to prevent the GUI from
    freezing up.
        params:
            - ai_response_generator: A function which takes a string as it's input (user message) and responds with
                                     a string (AI's response).
            - text: The text that the ai is responding to.
            - callback: a function which will be executed when the AI is done talking
            - voice_options: a dictionary where you can provide options for the AI's speaking voice
                default: {
                   "rate": 100,
                   "volume": 0.8,
                   "voice": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                }

    :param chat: The chat box object.
    :param text: Text the user has entered.
    :return:
    """
    # this is where you can add chat bot functionality!
    # text is the text the user has entered into the chat
    # you can use chat.send_ai_message("some text") to send a message as the AI, this will do background
    # you can use chat.start_gif() and chat.stop_gif() to start and stop the gif
    # you can use chat.clear() to clear the user and AI chat boxes

    # print the text the user entered to console
    print("User Entered Message: " + text)             
    
    ''' Here you can intercept the user input and override the bot
     output with your own responses and commands.'''
    # if the user send the "clear" message clear the chats
    if text.lower().find("erase chat") != -1:
        chat.clear()
    # user can say any form of bye to close the chat.
    elif text.lower().find("bye") != -1:
        # define a callback which will close the application
        def close():
            chat.exit()
            chat.send_ai_message("__pycache__", callback=close)
    elif text.lower().find("hey") != -1:
        print("Hello human. I am GLaDOS")
    elif text.lower().find("hi") != -1:
        print("Welcome to Aperture Science Testing Facilities. I am GLaDOS.")
    elif text.lower().find("cake") != -1:
        print("You will get your cake at the end of this course.")
    elif text.lower().find("companion cube") != -1:
        print("Take your cube. It is yours.")
        # send the goodbye message and provide the close function as a callback
    else:
        # offload chat bot processing to a worker thread and also send the result as an ai message
        chat.process_and_send_ai_message(chatbot.get_response, text)


# run the chat bot application
app.run()
