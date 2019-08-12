import celery
from celery.schedules import crontab
from celery import Celery
app = Celery('birthdays', broker="redis://localhost:6379/0")
app.conf.enable_utc = False

@app.task
def print_seconds():
    print("hellow")

app.conf.beat_schedule = {
    "birthday-task": {
        "task": "birthdays.print_seconds",
        "schedule": crontab(minute="*/1")
    }
}