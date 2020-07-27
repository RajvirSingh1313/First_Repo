from time import time
from plyer import notification

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch( 'SAPI.SpVoice' )
    speak.Speak( str )


if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 10
    eyessecs = 20
    exsecs = 30

    while True:
        if time() - init_water > watersecs:
            notification.notify(
                title='Drink Water',
                message='Get Up And Drink Some Water!!',
                app_icon='',
                timeout=3
            )
            speak( 'Get Up And Drink Some Water!!' )
            init_water = time()
        if time() - init_eyes > eyessecs:
            notification.notify(
                title='Breathe Fresh Air',
                message='Get Up And Breathe Some Fresh Air',
                app_icon='',
                timeout=3
            )
            speak( 'Get Up And Breathe Some Fresh Air' )
            init_eyes = time()
        if time() - init_exercise > exsecs:
            notification.notify(
                title='Do Exercise',
                message='Get Up And Do Some Exercise!!',
                app_icon='',
                timeout=3
            )
            speak( 'Get Up And Do Some Exercise!!' )
            init_exercise = time()
