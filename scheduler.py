"""
scheduler.py
Example scheduler using schedule to run simulations periodically.
"""
import time
import os
from mother_core import MotherCore

try:
    import schedule
except Exception:
    schedule = None


def job():
    mc = MotherCore()
    mc.run_all()


if __name__ == '__main__':
    if schedule is None:
        print('schedule package not installed; see requirements.txt')
    else:
        schedule.every(24).hours.do(job)
        while True:
            schedule.run_pending()
            time.sleep(60)
