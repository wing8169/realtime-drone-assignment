# # import keyboard

# # keyboard.press_and_release('shift+s, space')

# # keyboard.write('The quick brown fox jumps over the lazy dog.')

# # # keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))

# # # Press PAGE UP then PAGE DOWN to type "foobar".
# # keyboard.add_hotkey('page up, page down', lambda: keyboard.write('foobar'))

# # # Blocks until you press esc.
# # keyboard.wait('esc')

# # # Record events until 'esc' is pressed.
# # recorded = keyboard.record(until='esc')
# # # Then replay back at three times the speed.
# # keyboard.play(recorded, speed_factor=3)

# # # Type @@ then press space to replace with abbreviation.
# # keyboard.add_abbreviation('@@', 'my.long.email@example.com')

# # # Block forever, like `while True`.
# # keyboard.wait()

# from pymouse import PyMouse
# from pykeyboard import PyKeyboard

# m = PyMouse()
# k = PyKeyboard()

# # x_dim, y_dim = m.screen_size()
# # m.click(x_dim/2, y_dim/2, 1)
# # k.type_string('Hello, World!')

# # pressing a key
# k.press_key('H')
# # which you then follow with a release of the key
# k.release_key('H')
# # or you can 'tap' a key which does both
# k.tap_key('e')
# # note that that tap_key does support a way of repeating keystrokes with a interval time between each
# k.tap_key('l', n=2, interval=5)
# # and you can send a string if needed too
# k.type_string('o World!')


from threading import Thread
import serial
from pykeyboard import PyKeyboard
import time

k = PyKeyboard()

# pressing a key
# which you then follow with a release of the key
# k.release_key('w')

# ser = serial.Serial('/dev/pts/3', 9600, timeout=0)


def worker():
    # f = open('test.txt', 'r')
    # txt = f.readlines()
    # for i in txt:
    while True:
        msg = i
        # msg = ser.readline()
        if len(msg) > 0:
            if 'w' in msg:
                k.press_key('w')
            else:
                k.release_key('w')
            if 's' in msg:
                k.press_key('s')
            else:
                k.release_key('s')
            if 'a' in msg:
                k.press_key('a')
            else:
                k.release_key('a')
            if 'd' in msg:
                k.press_key('d')
            else:
                k.release_key('d')
            if 'j' in msg:
                k.press_key('j')
            else:
                k.release_key('j')
            if 'k' in msg:
                k.press_key('k')
            else:
                k.release_key('k')
            # time.sleep(1)
            # print("Message Received: %s" % msg)


t = Thread(target=worker)
t.daemon = True
t.start()

while True:
    pass
