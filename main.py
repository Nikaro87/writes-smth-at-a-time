import random
import time
import pyautogui


interval = (10 , 60) #Chose your time
word = "idk" # chose your word

print(pyautogui.FAILSAFE)
while True:
    delay = random.randint(interval)
    print("Sleep " + str(delay) + "s")
    pyautogui.write(word)
    time.sleep(delay)


