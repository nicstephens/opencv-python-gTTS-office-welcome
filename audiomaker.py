import gtts


tts = gtts.gTTS(tld = 'de', text = "Welcome to the thinktank")
tts1 = gtts.gTTS(tld = 'de', text = "Thank you for visiting the thinktank")

tts1.save(r"file_path_to_farewell.mp3")
tts.save(r"file_path_to_welcome.mp3")