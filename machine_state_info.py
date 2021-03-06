#!/usr/bin/python

from checkers import check_internet, check_process
from models import env_model
from drivers import lcddriver
import time
import os

env_state = env_model.EnvironmentState()
lcd = lcddriver.lcd()
lcd.clear()


def convert_bool_to_string(_bool):
    return ' On' if _bool else 'Off'


def refresh_internet_connection_info():
    internet_on = check_internet.is_on()
    if internet_on != env_state.internet_on:
        env_state.internet_on = internet_on
        internet_on_answer = convert_bool_to_string(internet_on)
        lcd.display_string("Internet:        " + internet_on_answer, 1)


def refresh_apps_info():
    server_running = check_process.is_running("java", "mateuszzweigert.pl")
    job_notifier_running = check_process.is_running("java", "job-notifier")
    if server_running != env_state.server_running or job_notifier_running != env_state.job_notifier_running:
        env_state.server_running = server_running
	env_state.job_notifier_running = job_notifier_running
        server_running_answer = convert_bool_to_string(server_running)
	job_notifier_running_answer = convert_bool_to_string(job_notifier_running)
        lcd.display_string("Server:" + server_running_answer + "   J-N:" + job_notifier_running_answer, 2)


def refresh_last_reboot_datetime():
    cmd = os.popen("uptime --since")
    last_reboot_datetime = cmd.read()
    if last_reboot_datetime != env_state.last_reboot_datetime:
        env_state.last_reboot_datetime = last_reboot_datetime
        lcd.display_string("Last reboot datetime", 3)
        date = last_reboot_datetime[:10]
        time = last_reboot_datetime[11:19]
        lcd.display_string(time + "  " + date, 4)

    cmd.close()


def refresh():
    refresh_internet_connection_info()
    refresh_apps_info()
    refresh_last_reboot_datetime()
