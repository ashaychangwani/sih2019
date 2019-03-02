from background_task import background
from logging import getLogger

from django.contrib.auth.models import User
from django.http import request


@background(schedule=1)
def SchedulingAlgo(user_id):
    # lookup user by id and send them a message
    print("this is a background task")

