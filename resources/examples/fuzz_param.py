# Find more example scripts at https://github.com/PortSwigger/turbo-intruder/blob/master/resources/examples/default.py
import urllib
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False
                           )
    engine.start()

    for i in range(3, 8):
        engine.queue(target.req, randstr(i), learn=1)
        engine.queue(target.req, target.baseInput, learn=2)

    for word in open('/home/hacker/tools/wordlists/params.txt'):

        #word = urllib.quote(word.rstrip()) # URL-encode

        engine.queue(target.req, word.rstrip())


def handleResponse(req, interesting):
    if interesting:
        table.add(req)

