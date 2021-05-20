from instapy import InstaPy
from time import sleep
import random

session = InstaPy(username="inactiveoldfanacc", password="tester").login()

for i in range(100):
    current = random.randint(0,45)
    session.unfollow_users(amount=1, nonFollowers=True, style="RANDOM", unfollow_after=0, sleep_delay=0)
    print(current);
    sleep(current)

session.close()
