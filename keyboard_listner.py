from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed '.format(key.char))
        if key.char == 'A':
            print('here....got A')
        elif key.char == '@':
            print('@ here')
    except:
        print('special key {0} pressed '.format(key))

def on_release(key):
    print('{0} released '.format(key))
    if key == keyboard.Key.shift: # handles if key release is shift
        print('success motive')
        return True
    elif key == keyboard.Key.esc:
        return False

def get_current_key_input():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

get_current_key_input()
