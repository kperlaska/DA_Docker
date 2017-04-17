from locust import HttpLocust, TaskSet

def index(l):
    l.client.get("/")

def test(l):
    l.client.get("/?gws_rd=ssl")

def test1(l):
    l.client.get("/imghp")

def test2(l):
    l.client.get("/iasldkfjal")

class UserBehavior(TaskSet):
    tasks = [ index, test, test1, test2 ]


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
