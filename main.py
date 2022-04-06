from gtts import gTTS
import random
import time
import playsound
import speech_recognition as sr

def listen_command():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Скажите Вашу команду: ')
        audio = r.listen(source)
    
    # recognize speech using Google Speech Recognition
    try:
        our_speach = r.recognize_google(audio, language='ru')
        print(f'Вы сказали : {our_speach}')
        return our_speach
    except sr.UnknownValueError:
        return "Ошибка!"
    except sr.RequestError as e:
        return "Ошибка!"
        
    # return input('Введите Вашу команду: ')


def say_message(message):
    voice = gTTS(message, lang = 'ru')
    file_voice_name = '_audio_'+'_'+str(time.time())+str(random.randint(0, 100000))+'.mp3'
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    print(f'Говорит голосовой асситент: {message}')



def do_this_command(message):
    message = message.lower()
    if 'привет' in message:
        say_message('Привет Даяна')
    elif 'пока' in message:
        say_message('Пока Даяна')
        exit()
    else:
        say_message('Команда не распознана')







if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)