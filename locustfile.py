from locust import HttpLocust, TaskSet


payload = '{"page":{"path":"inone/konfigurator","language":"en","cfu":"res","charset":"utf-8","viewtype":"classic","template":"Portal Content Page","pagetype":""},"platform":{"platform":"scportal","environment":"prod","context":"online"},"profile":{"loggedIn":"login"},"version":"1.0","timestamp":1492894056,"device":{"deviceType":"classic","os":"windows","applicationType":"browser"}}'


def tealium(l):
    l.client.get("/etc/swisscom/tools/public/tealium.html")

def settopbox(l):
    l.client.get("/content/dam/settopbox/help-links.properties")

def privatkunden(l):
    l.client.get("/de/privatkunden.html")

def portalservices(l):
    l.client.get("/portal-services/occ/ratings/de/000000000011015263")

def fluent(l):
    with l.client.post("/sdc/odl", payload, catch_response=True) as response:
      if response.status_code == 404:
       response.success()

class UserBehavior(TaskSet):
    tasks = [ tealium, settopbox, privatkunden, portalservices, fluent ]


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
