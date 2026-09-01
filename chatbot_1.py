from nltk.chat.util import Chat, reflections

pairs = [
  [r"hello|hi|hey", ["Hello! Welcome to our canteen."]],
  [r"(.*)pizza(.*)", ["Pizza costs rupees120."]],
  [r"(.*)time(.*)", ["The canteen is open 8 AM to 6 PM."]],
  [r"(.*)menu(.*)", ["Today's menu includes Pizza , and Coffee."]],
  # Generic fallback
  [r"(.*)", ["You mentioned: %1"]]

  #[r"(.*)",  ["Sorry, I didnt understand that.Could you rephrase?"."]

 ]

custom_reflections=reflections.copy()
custom_reflections.update({
 
  "we":"you all"

})

chatbot = Chat(pairs,custom_reflections)
chatbot.converse()
