#!/usr/bin/python

from checkers import check_internet, check_process
from models import env_model
from drivers import lcddriver
import schedule
import time

env_state = env_model.EnvironmentState()
lcd = lcddriver.lcd()
lcd.clear()


def convert_bool_to_string(_bool):
    return 'Yes' if _bool else 'No '


def refresh_internet_connection_info():
    internet_on = check_internet.is_on()
    if internet_on != env_state.internet_on:
        env_state.internet_on = internet_on
        internet_on_answer = convert_bool_to_string(internet_on)
        lcd.display_string("Internet on:     " + internet_on_answer, 1)
        lcd.display_string("--------------------", 2)


def refresh_server_info():
    server_running = check_process.is_running("java", "mateuszzweigert.pl")
    if server_running != env_state.server_running:
        env_state.server_running = server_running
        server_running_answer = convert_bool_to_string(server_running)
        lcd.display_string("Server running:  " + server_running_answer, 3)
        lcd.display_string("--------------------", 4)


def refresh_lcd():
    refresh_internet_connection_info()
    refresh_server_info()


refresh_lcd()
schedule.every(1).minutes.do(refresh_lcd)

while True:
    schedule.run_pending()
    time.sleep(1)
