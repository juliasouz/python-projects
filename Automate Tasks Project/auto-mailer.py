import yfinance
import pyautogui
import time 
from time import sleep
import webbrowser
import pyperclip


ticker = input("Enter the stock ticker code:")
start_dt = input("Enter the start date (yyyy-mm-dd): ")
end_dt = input("Enter the end date (yyyy-mm-dd): ")

max_value = round(closing.max(), 2)
min_value = round(closing.min(), 2)
mean_value = round(closing.mean(), 2)

recipient = "your-email@gmail.com"
subject = "Project Analysis"

message = f"""
Good morning,

Here are the stock analyses for {ticker} for the requested period: {start_dt} to {end_dt}:

Highest Price: ${max_value}
Lowest Price: ${min_value}
Mean Value: ${mean_value}

Kind regards,
"""
pyautogui.PAUSE = 4

webbrowser.open("https://mail.google.com/")
sleep(6)

pyautogui.click(x=147,y=201)

pyperclip.copy(recipient)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

pyperclip.copy(subject)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

pyperclip.copy(message)
pyautogui.hotkey("ctrl", "v")

pyautogui.hotkey("ctrl", "enter")
