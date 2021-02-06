webgui = Runtime.start('webgui', 'WebGui')
# mouth = Runtime.start('mouth', 'WebkitSpeechSynthesis')
mouth = Runtime.start('mouth', 'MarySpeech')

mouth.speak('testing testing 1 2 3, i have a mouth and it is worky')


def onDepthAi(data):
    print('onDepthAi', data)
    mouth.speak('i see a ' + data)
    
    