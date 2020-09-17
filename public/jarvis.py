def assistant_speaks(output):
    global num
     # with different name to remove ambiguity
                    num += 1
                    print("Jarvis : ", output)
                
                    toSpeak = gTTS(text=output, lang='en-IN', slow=False)
                    # saving the audio file given by google text to speech
                    file = str(num)+".mp3"