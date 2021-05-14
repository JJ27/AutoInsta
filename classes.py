from instapy import InstaPy

session = InstaPy(username="inactiveoldfanacc", password="tester").login()

session.unfollow_users(amount=100, nonFollowers=True, style="RANDOM", unfollow_after=10, sleep_delay=655)
