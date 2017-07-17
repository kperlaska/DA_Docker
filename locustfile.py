from locust import HttpLocust, TaskSet, task, events
from bs4 import BeautifulSoup
import random

def global_en_home(l):
    urls = set()
    urls.add('/global/en/investment-excellence/research/cio-house-view/')
    urls.add('/global/en/visionary-thinking/fia-formula-e-championship/video-gallery/')
    urls.add('/global/en/menus/footer/rss-feed/')
    urls.add('/group/en/investors/')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
    }


    for testurl in urls:
     response = l.client.request(
        method='GET',
        url=testurl,
        headers=headers,
        verify=False,
     )

     soup = BeautifulSoup(response.text, "html.parser")
     resource_urls = set()
     for res in soup.find_all(src=True):
        url = res['src']
        resource_urls.add(url)
     escurl = testurl.replace('/','%2F')
     resource_urls.add('https://www-uat.juliusbaer.com/piwik.php?action_name=Your%20Private%20Bank&idsite=1&rec=1&r=468510&h=15&m=45&s=51&url=https%3A%2F%2Fwww-uat.juliusbaer.com'+escurl+'&_id=c8427e434e9901e9&_idts=1499179551&_idvc=1&_idn=0&_refts=0&_viewts=1499179551&send_image=1&pdf=0&qt=0&realp=0&wma=0&dir=0&fla=1&java=1&gears=0&ag=0&cookie=1&res=1600x1200&gt_ms=54&pv_id=0AGYad');

     for uri in resource_urls:
        l.client.request(
          method='GET',
          url=uri,
          headers=headers,
          verify=False
          )


class UserBehavior(TaskSet):
    tasks = [ global_en_home ]


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
