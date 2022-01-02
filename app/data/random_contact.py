from urllib.request import Request, urlopen
import json
import urllib


def parseURL(url):
    ''' parseURL() will open, read, and turn the given url into a dictionary '''
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'}
                  )  # establishes a useragent so we don't look like a bot

    page = urlopen(req)
    #dict = page.read()
    dict = json.loads(page.read())
    return dict

def randomContact():
    response = parseURL("https://randomuser.me/api/")['results'][0]
    name = f"{response['name']['title']}. {response['name']['first']} {response['name']['last']}"
    processx = [name, response["dob"]["age"], response["phone"]]
    return processx
if __name__ == "__main__":

    print(randomContact())
