#!/usr/bin/python

import psutil


def is_running(process_type, app_name):
    for process in psutil.process_iter():
        if process.name() == process_type and app_name in ' '.join(process.cmdline()):
            return True
    return False
