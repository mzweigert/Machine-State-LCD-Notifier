class EnvironmentState:
    def __init__(self, server_running=None, job_notifier_running=None, internet_on=None, last_reboot_datetime=None):
        self.server_running = server_running
	self.job_notifier_running = job_notifier_running
        self.internet_on = internet_on
	self.last_reboot_datetime = last_reboot_datetime
